#!/usr/bin/env bash
# Fix Firefox opening https://find-it.pro/?utm_source=distr_m on every new tab/window.
# The distr_m tag usually means the page was installed via bundled software or an extension.

set -euo pipefail

FINDIT_PATTERN='find-it\.pro|finditpro|findit-pro|newtab\.club'
DRY_RUN=0
AUTO_FIX=0

usage() {
  cat <<'EOF'
Usage: fix-firefox-find-it.sh [options]

Find and remove find-it.pro hijacker settings from Mozilla Firefox.

Options:
  --dry-run    Show what would be changed without modifying files
  --fix        Apply safe fixes automatically (backs up files first)
  -h, --help   Show this help

Examples:
  ./scripts/fix-firefox-find-it.sh --dry-run
  ./scripts/fix-firefox-find-it.sh --fix
EOF
}

log() { printf '[find-it-fix] %s\n' "$*"; }
warn() { printf '[find-it-fix] WARNING: %s\n' "$*" >&2; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=1; shift ;;
    --fix) AUTO_FIX=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) warn "Unknown option: $1"; usage; exit 1 ;;
  esac
done

find_firefox_profiles() {
  local roots=()
  if [[ -n "${HOME:-}" ]]; then
    roots+=("$HOME/.mozilla/firefox")
    roots+=("$HOME/snap/firefox/common/.mozilla/firefox")
    roots+=("$HOME/.var/app/org.mozilla.firefox/.mozilla/firefox")
  fi

  local root profile_ini
  for root in "${roots[@]}"; do
    profile_ini="$root/profiles.ini"
    [[ -f "$profile_ini" ]] || continue

    awk -F= '
      /^\[Install/ { install=1; next }
      /^\[/ { install=0 }
      install && /^Default=/ { print $2 }
    ' "$profile_ini" | while IFS= read -r default_profile; do
      [[ -n "$default_profile" && -d "$root/$default_profile" ]] && printf '%s\n' "$root/$default_profile"
    done

    awk -F= '
      /^\[Profile/ { in_profile=1; path=""; is_relative=1; next }
      /^\[/ { if (in_profile && path != "") print path "|" is_relative; in_profile=0; next }
      in_profile && /^Path=/ { path=$2 }
      in_profile && /^IsRelative=/ { is_relative=$2 }
      END { if (in_profile && path != "") print path "|" is_relative }
    ' "$profile_ini" | while IFS='|' read -r path is_relative; do
      if [[ "$is_relative" == "1" ]]; then
        [[ -d "$root/$path" ]] && printf '%s\n' "$root/$path"
      else
        [[ -d "$path" ]] && printf '%s\n' "$path"
      fi
    done
  done | sort -u
}

scan_file() {
  local file="$1"
  [[ -f "$file" ]] || return 0
  grep -En "$FINDIT_PATTERN" "$file" || true
}

backup_file() {
  local file="$1"
  local backup="${file}.bak.$(date +%Y%m%d%H%M%S)"
  cp -a "$file" "$backup"
  log "Backup created: $backup"
}

remove_matching_lines() {
  local file="$1"
  if [[ "$DRY_RUN" -eq 1 ]]; then
    log "Would remove find-it.pro lines from: $file"
    return 0
  fi
  backup_file "$file"
  grep -Ev "$FINDIT_PATTERN" "$file" > "${file}.tmp"
  mv "${file}.tmp" "$file"
  log "Cleaned: $file"
}

clean_pref_file() {
  local file="$1"
  local matches
  matches="$(scan_file "$file")"
  [[ -n "$matches" ]] || return 0
  warn "Found in $file:"
  printf '%s\n' "$matches"
  if [[ "$AUTO_FIX" -eq 1 ]]; then
    remove_matching_lines "$file"
  fi
}

reset_homepage_prefs() {
  local profile="$1"
  local user_js="$profile/user.js"
  local prefs_js="$profile/prefs.js"

  clean_pref_file "$user_js"
  clean_pref_file "$prefs_js"

  if [[ "$AUTO_FIX" -eq 1 && "$DRY_RUN" -eq 0 ]]; then
    # Safe defaults if hijacker removed homepage settings entirely.
    if ! grep -q '^user_pref("browser.startup.homepage"' "$prefs_js" 2>/dev/null; then
      log "Setting homepage to Firefox default (about:home)"
      printf '\nuser_pref("browser.startup.homepage", "about:home");\n' >> "$prefs_js"
    fi
    if ! grep -q '^user_pref("browser.newtab.url"' "$prefs_js" 2>/dev/null; then
      log "Setting new tab page to Firefox default (about:newtab)"
      printf 'user_pref("browser.newtab.url", "about:newtab");\n' >> "$prefs_js"
    fi
  fi
}

scan_extensions() {
  local profile="$1"
  local extensions_dir="$profile/extensions"
  [[ -d "$extensions_dir" ]] || return 0

  find "$extensions_dir" -maxdepth 2 -type f \( -name '*.xpi' -o -name 'manifest.json' \) 2>/dev/null | while IFS= read -r item; do
    if [[ "$item" == *.xpi ]]; then
      if unzip -p "$item" manifest.json 2>/dev/null | grep -Eiq "$FINDIT_PATTERN|find.?it"; then
        warn "Suspicious extension archive: $item"
      fi
    elif grep -Eiq "$FINDIT_PATTERN|find.?it" "$item"; then
      warn "Suspicious extension manifest: $item"
    fi
  done
}

main() {
  log "Scanning Mozilla Firefox profiles for find-it.pro hijacker..."

  mapfile -t profiles < <(find_firefox_profiles)
  if [[ "${#profiles[@]}" -eq 0 ]]; then
    warn "No Firefox profiles found."
    cat <<'EOF'

Manual steps in Firefox:
1. Open about:addons and remove extensions named Find-it / FindItPro / similar.
2. Open Settings -> Home and disable custom homepage https://find-it.pro
3. Open about:config and reset:
   - browser.startup.homepage
   - browser.newtab.url
   - browser.startup.homepage_override.mstone (set to ignore)
4. If the issue returns, check your profile for user.js and delete find-it.pro lines.
5. Scan the computer with Malwarebytes or AdwCleaner.
EOF
    exit 1
  fi

  local profile
  for profile in "${profiles[@]}"; do
    log "Profile: $profile"
    reset_homepage_prefs "$profile"
    scan_extensions "$profile"

    local search_metadata="$profile/search.json.mozlz4"
    if [[ -f "$search_metadata" ]]; then
      warn "Custom search engines detected in search.json.mozlz4"
      warn "Open about:preferences#search in Firefox and remove find-it.pro / newtab.club search providers."
    fi
  done

  cat <<'EOF'

Next steps:
1. Completely close Firefox (all windows) and reopen it.
2. In Firefox: about:addons -> Extensions -> remove Find-it / FindItPro.
3. Settings -> Home -> Homepage: choose "Firefox Home (Default)".
4. Settings -> Search -> Default search engine: choose Google/DuckDuckGo/etc.
5. If find-it.pro still opens, run: about:support -> Refresh Firefox.

If this keeps coming back, uninstall suspicious programs from the system
and run an anti-malware scan — the hijacker is often reinstalled by Windows software.
EOF

  if [[ "$AUTO_FIX" -eq 0 && "$DRY_RUN" -eq 0 ]]; then
    log "Run with --fix to automatically clean prefs.js/user.js entries."
  fi
}

main "$@"
