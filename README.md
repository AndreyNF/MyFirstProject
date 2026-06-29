# MyFirstProject

## Firefox: ошибка при открытии find-it.pro

Если Mozilla Firefox постоянно открывает `https://find-it.pro/?utm_source=distr_m` при каждой новой вкладке или окне, это браузерный перехватчик (hijacker), а не ошибка самого сайта.

### Быстрое исправление

```bash
./scripts/fix-firefox-find-it.sh --dry-run   # показать, что найдено
./scripts/fix-firefox-find-it.sh --fix       # очистить настройки Firefox
```

После скрипта:

1. Полностью закройте Firefox и откройте снова.
2. `about:addons` → удалите расширения Find-it / FindItPro.
3. Настройки → Домашняя страница → «Firefox Home (Default)».
4. Настройки → Поиск → выберите обычную поисковую систему.
5. Если проблема возвращается: `about:support` → «Обновить Firefox».

### Патч для владельцев find-it.pro

Если вы поддерживаете сайт и видите сбои навигации в Firefox, примените патч:

```bash
./scripts/patch-find-it-main-js.sh
```

Файл `patches/find-it-pro/main.patched.js` заменяет устаревший `setTopWindowLocation()` на прямую навигацию, совместимую с Firefox.
