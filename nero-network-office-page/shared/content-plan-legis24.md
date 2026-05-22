# Контент-план Legis24

## Расписание (3 публикации в сутки, интервал 6 ч)

| Слот | Cron UTC | МСК | Тип |
|------|----------|-----|-----|
| 1 | 03:00 | 06:00 | **ARB** — арбитраж |
| 2 | 09:00 | 12:00 | **IP** — защита ИС, товарный знак, ответ на иск |
| 3 | 15:00 | 18:00 | **UG** — уголовное право |

**Cron для Cursor Automation:** `0 3,9,15 * * *`

Precheck: `python3 scripts/nero-precheck-queue.py --mark-done --write-handoff` (слот определяется по UTC или `--slot N`).

---

## Очередь публикации

| # | Код | Тип | H1 | SLUG | Статус |
|---|-----|-----|-----|------|--------|
| 1 | A3 | — | Срок возражений: 30 дней vs 15 (мифы) | srok-vozrazhenij-30-dnej-vs-15-mify | ✅ page_id 323 |
| 2 | A4 | — | План реструктуризации долгов гражданина: сроки, утверждение и возражения | plan-restrukturizacii-dolgov-grazhdanina-sroki | ✅ page_id 335 |
| 3 | A5 | ARB | Арбитражный спор с кредитором: сроки, подсудность и первая стратегия ответа | arbitrazhnyj-spor-s-kreditorom-sroki-strategiya | |
| 4 | A6 | IP | Товарный знак: как защитить бренд и что делать, если подали иск по интеллектуальной собственности | zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti | ✅ page_id 339 |
| 5 | A7 | UG | Уголовные риски при долгах: мошенничество, злостное уклонение — что важно знать гражданину | ugolovnye-riski-pri-dolgah-chto-vazhno-znat | ✅ page_id 341 |
| 6 | A8 | ARB | Иск в арбитраже при банкротстве: когда подавать и как оспорить требования | isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat | |
| 7 | A9 | IP | Нарушение товарного знака: доказательства, компенсация и защита в суде | narushenie-tovarnogo-znaka-dokazatelstva-kompensaciya | |
| 8 | A10 | UG | Защита по уголовному делу на стадии проверки и в суде: права и тактика | zashchita-po-ugolovnomu-delu-stadiya-proverki | |
| 9 | A11 | ARB | Арбитражный управляющий и оспаривание сделок: сроки и последствия для должника | arbitrazhnyj-upravlyayushchij-osparivanie-sdelok | |
| 10 | A12 | IP | Ответ на претензию по интеллектуальной собственности: сроки и типовые ошибки | otvet-na-pretensiyu-po-intellektualnoj-sobstvennosti | |
| 11 | A13 | UG | Статья 159 и 177 УК при долгах: где гражданская граница и когда нужен адвокат | statya-159-177-uk-pri-dolgah-granica | |
| 12 | A14 | ARB | Мировое соглашение в арбитраже: плюсы, риски и когда это выгодно | mirovoe-soglashenie-v-arbitrazhe-plyusy-riski | |
| 13 | A15 | IP | Регистрация товарного знака: этапы, отказ Роспатента и обжалование | registraciya-tovarnogo-znaka-etapy-otkaz | |
| 14 | A16 | UG | Досудебная защита по уголовному делу: что говорить следователю и чего избегать | dosudebnaya-zashchita-po-ugolovnomu-delu | |
| 15 | B1 | ARB | Арбитражный процессуальный срок: как не пропустить подачу и возражения | arbitrazhnyj-processualnyj-srok-podacha | |
| 16 | B2 | IP | Иск о защите интеллектуальной собственности против вас: пошаговый план ответа | isk-o-zashchite-is-protiv-vas-plan-otveta | |

> Канонический URL A3 на проде: `srok-vozrazhenij-30-vs-15-mify` (без «dnej» в slug).  
> Типы и углы: `article-types-legis24.md`.

## Кирилл после плана

Кирилл запускается только когда все 16 строк очереди имеют статус ✅.
