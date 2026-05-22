# Cursor Automation — Legis24 (Nero Network Office Page)

## Шаг 0 — обязательный pre-check (до Director и handoff)

```bash
python3 scripts/nero-precheck-queue.py --mark-done --write-handoff
```

| Код выхода | Действие | Пайплайн |
|------------|----------|----------|
| **1** SKIP | Тема уже в `published-pages.md` | **Не запускать.** Финальный ответ: URL + page_id из вывода |
| **0** PROCEED | Новая строка очереди | Полный пайплайн (Director → …) |
| **0** KIRILL | Все 16 строк ✅ | Только Кирилл → далее как обычно |
| **2** BLOCKER | Нет плана/темы | Остановка с причиной |

Журналы (канон):

- `nero-network-office-page/shared/content-plan-legis24.md`
- `nero-network-office-page/shared/published-pages.md`

## Фрагмент для промпта automation (вставить в начало)

```text
0. PRE-CHECK (обязательно первым):
   - Выполни: python3 scripts/nero-precheck-queue.py --mark-done --write-handoff
   - Если exit code 1 (SKIP): НЕ сбрасывай handoff на «новая сессия», НЕ запускай Task(subagents).
     Ответ пользователю: «Уже опубликовано» + URL + page_id из JSON/вывода скрипта.
   - Если exit code 2: блокер, стоп.
   - Если exit code 0 и action=PROCEED: только тогда Write handoff «# Nero Network — новая сессия» и полный пайплайн.
   - Перед публикацией сверь slug с published-pages; после Юры — допиши строку в журнал.
```

## Режим Cloud MCP-only

- Публикация: `commands/nero-publish-mcp.md`, Kovcheg `wordpress_*_from_blob`
- Без Aura, FTP, `page-{slug}.php`, canvas/script в hero/Борисе
- CTA: только https://advokat-vsem.ru/

## Клон плагина (если пустой workspace)

```bash
git clone --depth 1 https://github.com/Horosheff/nero-network-office-page.git nero-repo
ln -sfn nero-repo nero-network-office-page
cp -r nero-repo/agents .cursor/
```

Скиллы и агенты — из `nero-repo` / `.cursor/agents/`.
