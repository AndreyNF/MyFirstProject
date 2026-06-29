# Fix Firefox opening https://find-it.pro/?utm_source=distr_m on every new tab/window.
# Run in PowerShell (Windows):
#   powershell -ExecutionPolicy Bypass -File .\scripts\fix-firefox-find-it.ps1 -DryRun
#   powershell -ExecutionPolicy Bypass -File .\scripts\fix-firefox-find-it.ps1 -Fix

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$Fix
)

$ErrorActionPreference = 'Stop'
$FindItPattern = 'find-it\.pro|finditpro|findit-pro|newtab\.club'

function Write-Log([string]$Message) {
    Write-Host "[find-it-fix] $Message"
}

function Write-Warn([string]$Message) {
    Write-Warning "[find-it-fix] $Message"
}

function Get-FirefoxProfileRoots {
    $roots = @()

    if ($env:APPDATA) {
        $roots += Join-Path $env:APPDATA 'Mozilla\Firefox'
    }

    if ($env:LOCALAPPDATA) {
        $roots += Join-Path $env:LOCALAPPDATA 'Mozilla\Firefox'
    }

    return $roots | Select-Object -Unique
}

function Get-FirefoxProfiles {
    $profiles = @()

    foreach ($root in Get-FirefoxProfileRoots) {
        $iniPath = Join-Path $root 'profiles.ini'
        if (-not (Test-Path -LiteralPath $iniPath)) {
            continue
        }

        $ini = Get-Content -LiteralPath $iniPath
        $current = @{}
        $entries = @()

        foreach ($line in $ini) {
            if ($line -match '^\[(.+)\]$') {
                if ($current.Count -gt 0) { $entries += ,@($current.Clone()) }
                $current = @{ Section = $Matches[1] }
                continue
            }
            if ($line -match '^([^=]+)=(.*)$') {
                $current[$Matches[1].Trim()] = $Matches[2].Trim()
            }
        }
        if ($current.Count -gt 0) { $entries += ,@($current.Clone()) }

        foreach ($entry in $entries) {
            if (-not $entry.Path) { continue }
            if ($entry.IsRelative -eq '0') {
                if (Test-Path -LiteralPath $entry.Path) { $profiles += $entry.Path }
            }
            else {
                $profilePath = Join-Path $root $entry.Path
                if (Test-Path -LiteralPath $profilePath) { $profiles += $profilePath }
            }
        }
    }

    return $profiles | Select-Object -Unique
}

function Get-MatchingLines([string]$FilePath) {
    if (-not (Test-Path -LiteralPath $FilePath)) { return @() }
    return Select-String -Path $FilePath -Pattern $FindItPattern -AllMatches
}

function Backup-File([string]$FilePath) {
    $timestamp = Get-Date -Format 'yyyyMMddHHmmss'
    $backup = "$FilePath.bak.$timestamp"
    Copy-Item -LiteralPath $FilePath -Destination $backup -Force
    Write-Log "Backup created: $backup"
}

function Remove-MatchingLines([string]$FilePath) {
    if ($DryRun) {
        Write-Log "Would remove find-it.pro lines from: $FilePath"
        return
    }

    Backup-File $FilePath
    $filtered = Get-Content -LiteralPath $FilePath | Where-Object { $_ -notmatch $FindItPattern }
    Set-Content -LiteralPath $FilePath -Value $filtered -Encoding UTF8
    Write-Log "Cleaned: $FilePath"
}

function Clean-PrefFile([string]$FilePath) {
    $matches = Get-MatchingLines $FilePath
    if (-not $matches) { return }

    Write-Warn "Found in $FilePath`:"
    foreach ($match in $matches) {
        Write-Host ("  line {0}: {1}" -f $match.LineNumber, $match.Line.Trim())
    }

    if ($Fix) {
        Remove-MatchingLines $FilePath
    }
}

function Reset-HomepagePrefs([string]$ProfilePath) {
    Clean-PrefFile (Join-Path $ProfilePath 'user.js')
    $prefsJs = Join-Path $ProfilePath 'prefs.js'
    Clean-PrefFile $prefsJs

    if ($Fix -and -not $DryRun -and (Test-Path -LiteralPath $prefsJs)) {
        $prefs = Get-Content -LiteralPath $prefsJs -Raw
        if ($prefs -notmatch 'browser\.startup\.homepage') {
            Write-Log 'Setting homepage to Firefox default (about:home)'
            Add-Content -LiteralPath $prefsJs -Value "`nuser_pref(`"browser.startup.homepage`", `"about:home`");"
        }
        if ($prefs -notmatch 'browser\.newtab\.url') {
            Write-Log 'Setting new tab page to Firefox default (about:newtab)'
            Add-Content -LiteralPath $prefsJs -Value "user_pref(`"browser.newtab.url`", `"about:newtab`");"
        }
    }
}

function Find-SuspiciousExtensions([string]$ProfilePath) {
    $extensionsDir = Join-Path $ProfilePath 'extensions'
    if (-not (Test-Path -LiteralPath $extensionsDir)) { return }

    Get-ChildItem -LiteralPath $extensionsDir -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.xpi', '.json' -or $_.Name -eq 'manifest.json' } |
        ForEach-Object {
            if ($_.Extension -eq '.xpi') {
                try {
                    Add-Type -AssemblyName System.IO.Compression.FileSystem -ErrorAction SilentlyContinue
                    $zip = [System.IO.Compression.ZipFile]::OpenRead($_.FullName)
                    $entry = $zip.Entries | Where-Object { $_.FullName -eq 'manifest.json' } | Select-Object -First 1
                    if ($entry) {
                        $stream = $entry.Open()
                        $reader = New-Object System.IO.StreamReader($stream)
                        $manifest = $reader.ReadToEnd()
                        $reader.Close()
                        $stream.Close()
                        if ($manifest -match 'find-it|findit|newtab\.club') {
                            Write-Warn "Suspicious extension archive: $($_.FullName)"
                        }
                    }
                    $zip.Dispose()
                }
                catch {
                    Write-Warn "Could not inspect extension: $($_.FullName)"
                }
            }
            elseif ($_.Name -eq 'manifest.json' -or $_.Extension -eq '.json') {
                $content = Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue
                if ($content -match 'find-it|findit|newtab\.club') {
                    Write-Warn "Suspicious extension manifest: $($_.FullName)"
                }
            }
        }
}

function Show-ManualSteps {
    @'

Ручные шаги в Firefox (Windows):
1. Полностью закройте Firefox (в диспетчере задач не должно быть firefox.exe).
2. Откройте Firefox -> about:addons -> Расширения -> удалите Find-it / FindItPro.
3. Меню -> Настройки -> Home (Домашняя страница) -> выберите "Firefox Home (Default)".
4. Настройки -> Поиск -> выберите Google, Yandex или DuckDuckGo.
5. В адресной строке: about:config -> примите риск -> найдите и сбросьте:
   - browser.startup.homepage
   - browser.newtab.url
6. Если find-it.pro снова появляется: about:support -> "Обновить Firefox...".
7. Проверьте "Установка и удаление программ" Windows и удалите подозрительные программы.
8. Запустите Malwarebytes или AdwCleaner.

Профили Firefox на Windows обычно здесь:
  %APPDATA%\Mozilla\Firefox\Profiles\
'@ | Write-Host
}

Write-Log 'Scanning Mozilla Firefox profiles for find-it.pro hijacker (Windows)...'

$profiles = @(Get-FirefoxProfiles)
if ($profiles.Count -eq 0) {
    Write-Warn 'No Firefox profiles found.'
    Show-ManualSteps
    exit 1
}

foreach ($profile in $profiles) {
    Write-Log "Profile: $profile"
    Reset-HomepagePrefs $profile
    Find-SuspiciousExtensions $profile

    $searchFile = Join-Path $profile 'search.json.mozlz4'
    if (Test-Path -LiteralPath $searchFile) {
        Write-Warn 'Custom search engines detected in search.json.mozlz4'
        Write-Warn 'Open about:preferences#search and remove find-it.pro / newtab.club providers.'
    }
}

@'

Дальше:
1. Полностью закройте Firefox и откройте снова.
2. about:addons -> удалите Find-it / FindItPro.
3. Настройки -> Home -> "Firefox Home (Default)".
4. Настройки -> Поиск -> обычная поисковая система.
5. Если не помогло: about:support -> "Обновить Firefox...".

Если find-it.pro возвращается после перезагрузки, удалите подозрительные
программы Windows и запустите антивирусную проверку.
'@ | Write-Host

if (-not $Fix -and -not $DryRun) {
    Write-Log 'Run with -Fix to automatically clean prefs.js/user.js entries.'
    Write-Log 'Example: powershell -ExecutionPolicy Bypass -File .\scripts\fix-firefox-find-it.ps1 -Fix'
}

if ($DryRun) {
    Write-Log 'Dry run complete. No files were changed.'
}
