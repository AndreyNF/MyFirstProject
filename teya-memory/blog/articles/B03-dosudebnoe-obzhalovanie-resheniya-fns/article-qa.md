# Article QA — B03 dosudebnoe-obzhalovanie-resheniya-fns

**Дата:** 2026-09-15  
**verdict:** PASS

## Сводка

| Gate | Status |
|---|---|
| research-notes-gate | PASS |
| html-linter | PASS |
| slop-detector | PASS |
| fact-checker | PASS |
| link-verify | PASS |
| utility-gate | PASS |
| human-voice-gate | PASS |
| cannibalization | PASS |

## Beginner-fit

- **Боль новичка:** страх пропустить пресекательный срок апелляции и потерять досудебный этап перед судом.
- **Где показано решение:** таблица «апелляция vs жалоба», пошаговый `<ol>` из 7 пунктов, схема маршрута через ИФНС.
- **Первый результат:** читатель определяет тип жалобы, адресата и успевает подать документ через свою инспекцию.
- **Термины «на пальцах»:** апелляция vs жалоба в общем порядке, УФНС как вышестоящий орган, вступление решения в силу через 1 месяц.

## CORE-EEAT (lite)

| Критерий | Оценка | Комментарий |
|---|---|---|
| Experience | 4/5 | Сценарий директора, типичные ошибки |
| Expertise | 4/5 | Нормы D01-D15 из fact-bank |
| Authoritativeness | 4/5 | ФНС, Consultant, Fact Check Box |
| Trustworthiness | 4/5 | Без гарантий отмены доначислений |
| **Итого** | **16/20** | PASS |

## Объём и структура

- **char_count:** 8683 (диапазон 8500-9500)
- **article_mode:** B (guide)
- **FAQ:** 7 пар
- **CTA advokat-vsem.ru:** 3 упоминания (≤3)
- **Факты:** только D01-D15 + L05/L12 для CTA

## Reader grounding

- **reader_story:** директор, доначисление, три недели, месячный срок
- **surprising_fact:** жалоба не приостанавливает исполнение решения
- **success_criteria:** регистрация в ИФНС с пересылкой в УФНС

## Cover

- **Путь:** `cover/cover.png`
- **Alt:** Обложка: досудебное обжалование решения ФНС - жалоба в УФНС
- **Примечание:** MCP `gpt-image-2` вернул -32001 Request timed out (5 попыток). Создана локальная обложка по палитре AURA (#FAFAF7, #E85D4C, #1A1A2E); Директору рекомендуется перегенерировать через MCP при доступности Kie.

## WP handoff

- **wp_status:** publish (в meta)
- **Публикация в WP:** не выполнялась (handoff Директору)
