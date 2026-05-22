---
description: Обязательный pre-check очереди Legis24 перед пайплайном (уже опубликовано → SKIP)
---

Полный текст для Cursor Automation: `cursor-automation-prompt.txt` или `AUTOMATION.md`.

**Первый шаг каждого cron-запуска.** Русский ответ.

```bash
python3 scripts/nero-precheck-queue.py --mark-done --write-handoff
```

| Exit | Значение |
|------|----------|
| 1 | SKIP — не запускать субагентов, вернуть URL + page_id |
| 0 | PROCEED или KIRILL — продолжить по `AUTOMATION.md` |
| 2 | BLOCKER |

Журналы: `nero-network-office-page/shared/content-plan-legis24.md`, `published-pages.md`.
