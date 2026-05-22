# Nero Network Office Page — Legis24 (automation)

Репозиторий для **Cursor Automation** (cron): публикация лонгридов на https://advokat-vsem.online/

## Обязательный pre-check

Перед каждым запуском пайплайна:

```bash
python3 scripts/nero-precheck-queue.py --mark-done --write-handoff
```

Если скрипт вернул **SKIP** (exit 1) — статья уже в журнале, **не** гонять Коля/Женю/Юру повторно.

Подробно: [AUTOMATION.md](AUTOMATION.md)

## Журналы

| Файл | Назначение |
|------|------------|
| `nero-network-office-page/shared/content-plan-legis24.md` | Очередь #1–#16 |
| `nero-network-office-page/shared/published-pages.md` | Опубликованные slug + page_id |

## Плагин

Клон: `git clone https://github.com/Horosheff/nero-network-office-page.git nero-repo` → `ln -sfn nero-repo nero-network-office-page`
