# Cursor Automation — Legis24 (Nero Network Office Page)

**Репозиторий:** `AndreyNF/MyFirstProject`  
**Ветка разработки:** `cursor/a3-a2ec` (base: `main`)  
**Сайт:** https://advokat-vsem.online/  
**Расписание cron (настроить в Cursor Automation):** `0 3,9,15 * * *` → **3 статьи в сутки**, интервал **6 часов** (03:00 / 09:00 / 15:00 UTC = 06:00 / 12:00 / 18:00 МСК).

---

## Полный промпт для Cursor Automation

Скопируйте **целиком** файл [`cursor-automation-prompt.txt`](cursor-automation-prompt.txt) в Instructions automation.

**Cron в настройках automation (обязательно):** `0 3,9,15 * * *`

---

## Шаг 0 — справка (дубль для README)

```bash
python3 scripts/nero-precheck-queue.py --mark-done --write-handoff
```

| Код выхода | Действие | Пайплайн |
|------------|----------|----------|
| **1** SKIP | Тема уже в `published-pages.md` | **Не запускать.** Финальный ответ: URL + page_id |
| **0** PROCEED | Новая строка очереди | Полный пайплайн (Director → …) |
| **0** KIRILL | Все 16 строк ✅ | Только Кирилл → далее как обычно |
| **2** BLOCKER | Нет плана/темы (TBD) | Остановка с причиной |

---

## Расписание публикаций (3 слота / сутки)

| Слот | Cron UTC | МСК | Тип | Первая тема в очереди |
|------|----------|-----|-----|------------------------|
| 1 | **03:00** | 06:00 | **ARB** — арбитраж | A5 |
| 2 | **09:00** | 12:00 | **IP** — ИС, товарный знак, ответ на иск | A6 |
| 3 | **15:00** | 18:00 | **UG** — уголовное право | A7 |

**Cron в Cursor Automation:** `0 3,9,15 * * *`

Подробные углы: `nero-network-office-page/shared/article-types-legis24.md`

### Масштаб: 300 статей в день?

Полный пайплайн Nero (субагенты, лонгрид 8k+, hero, QA) — **не рассчитан на сотни статей/сутки**. Реалистично **3 качественных лонгрида/день** при текущем cron. Для десятков/сотен нужен отдельный «лёгкий» шаблон без hero/canvas и много параллельных automation — это отдельная задача.

Ручной прогон вне окна слота: `python3 scripts/nero-precheck-queue.py --slot 1|2|3 --mark-done --write-handoff`

---

## Режим Cloud MCP-only

- Публикация: `commands/nero-publish-mcp.md`, Kovcheg `wordpress_*_from_blob`
- Без Aura, FTP, `page-{slug}.php`, canvas/script в hero/Борисе
- CTA: только https://advokat-vsem.ru/ в `href`; в **тексте** кнопки/ссылки — без домена и названия сайта

## Клон плагина (если пустой workspace)

```bash
git clone --depth 1 https://github.com/Horosheff/nero-network-office-page.git nero-repo
ln -sfn nero-repo nero-network-office-page
cp -r nero-repo/agents .cursor/
```

Скиллы и агенты — из `nero-repo` / `.cursor/agents/`.

## Связанные файлы

| Файл | Назначение |
|------|------------|
| `commands/nero-precheck.md` | Команда pre-check |
| `commands/nero-publish-mcp.md` | MCP-публикация |
| `.cursor/agents/director.md` | Цепочка субагентов + шаг 0 |
| `scripts/nero-precheck-queue.py` | Скрипт гейта |
| `.github/workflows/nero-precheck.yml` | CI-проверка скрипта |
