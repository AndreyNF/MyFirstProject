# Типичные сложности пайплайна Nero Network Office Page

## 0. Pre-check: «статья уже была» (ОБЯЗАТЕЛЬНО до handoff)

| Симптом | Причина | Что делать |
|--------|---------|------------|
| Cron снова гоняет A3/A4, хотя страница на проде | Пустой `published-pages.md` в git или агент не читал журнал **до** Task | **Шаг 0:** `python3 scripts/nero-precheck-queue.py --mark-done --write-handoff`. Exit **1** = SKIP |
| Slug в плане ≠ slug на проде | Алиас (напр. `…-30-dnej-…` vs `…-30-vs-…`) | Скрипт знает оба варианта; канон — slug из журнала |
| В очереди нет ✅, в журнале есть строка | План не синхронизирован | `--mark-done` обновит `content-plan-legis24.md` |

**Порядок каждого cron-запуска:**

1. `python3 scripts/nero-precheck-queue.py --mark-done --write-handoff`
2. Exit **1** → только URL + page_id, **стоп**
3. Exit **0** + `PROCEED` → сброс handoff → пайплайн
4. Exit **0** + `KIRILL` → все 16 ✅
5. Exit **2** → блокер

См. `AUTOMATION.md` и `=== PRECHECK (ГЕЙТ) ===` в handoff.
