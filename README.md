# MyFirstProject

## Firefox: ошибка при открытии find-it.pro

Если Mozilla Firefox постоянно открывает `https://find-it.pro/?utm_source=distr_m` при каждой новой вкладке или окне, это браузерный перехватчик (hijacker), а не ошибка самого сайта.

### Windows (рекомендуется)

Откройте **PowerShell** в папке проекта и выполните:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\fix-firefox-find-it.ps1 -DryRun
powershell -ExecutionPolicy Bypass -File .\scripts\fix-firefox-find-it.ps1 -Fix
```

Профили Firefox на Windows обычно находятся здесь:

```text
%APPDATA%\Mozilla\Firefox\Profiles\
```

### Linux / macOS / Git Bash

```bash
./scripts/fix-firefox-find-it.sh --dry-run
./scripts/fix-firefox-find-it.sh --fix
```

### После скрипта

1. Полностью закройте Firefox (в диспетчере задач не должно быть `firefox.exe`).
2. `about:addons` → удалите расширения Find-it / FindItPro.
3. **Настройки → Home (Домашняя страница)** → «Firefox Home (Default)».
4. **Настройки → Поиск** → выберите обычную поисковую систему.
5. Если проблема возвращается: `about:support` → «Обновить Firefox...».
6. Удалите подозрительные программы в Windows и запустите Malwarebytes или AdwCleaner.

### Патч для владельцев find-it.pro

```bash
./scripts/patch-find-it-main-js.sh
```

Файл `patches/find-it-pro/main.patched.js` заменяет устаревший `setTopWindowLocation()` на прямую навигацию, совместимую с Firefox.
