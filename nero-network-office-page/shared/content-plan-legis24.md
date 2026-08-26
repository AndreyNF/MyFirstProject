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
| 3 | A5 | ARB | Арбитражный спор с кредитором: сроки, подсудность и первая стратегия ответа | arbitrazhnyj-spor-s-kreditorom-sroki-strategiya | ✅ page_id 343 |
| 4 | A6 | IP | Товарный знак: как защитить бренд и что делать, если подали иск по интеллектуальной собственности | zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstvennosti | ✅ page_id 339 |
| 5 | A7 | UG | Уголовные риски при долгах: мошенничество, злостное уклонение — что важно знать гражданину | ugolovnye-riski-pri-dolgah-chto-vazhno-znat | ✅ page_id 341 |
| 6 | A8 | ARB | Иск в арбитраже при банкротстве: когда подавать и как оспорить требования | isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat | ✅ page_id 358 |
| 7 | A9 | IP | Нарушение товарного знака: доказательства, компенсация и защита в суде | narushenie-tovarnogo-znaka-dokazatelstva-kompensaciya | ✅ page_id 346 |
| 8 | A10 | UG | Защита по уголовному делу на стадии проверки и в суде: права и тактика | zashchita-po-ugolovnomu-delu-stadiya-proverki | ✅ page_id 354 |
| 9 | A11 | ARB | Арбитражный управляющий и оспаривание сделок: сроки и последствия для должника | arbitrazhnyj-upravlyayushchij-osparivanie-sdelok | ✅ page_id 382 |
| 10 | A12 | IP | Ответ на претензию по интеллектуальной собственности: сроки и типовые ошибки | otvet-na-pretensiyu-po-intellektualnoj-sobstvennosti | ✅ page_id 364 |
| 11 | A13 | UG | Статья 159 и 177 УК при долгах: где гражданская граница и когда нужен адвокат | statya-159-177-uk-pri-dolgah-granica | ✅ page_id 370 |
| 12 | A14 | ARB | Мировое соглашение в арбитраже: плюсы, риски и когда это выгодно | mirovoe-soglashenie-v-arbitrazhe-plyusy-riski | ✅ page_id 416 |
| 13 | A15 | IP | Регистрация товарного знака: этапы, отказ Роспатента и обжалование | registraciya-tovarnogo-znaka-etapy-otkaz | ✅ page_id 368 |
| 14 | A16 | UG | Досудебная защита по уголовному делу: что говорить следователю и чего избегать | dosudebnaya-zashchita-po-ugolovnomu-delu | ✅ page_id 412 |
| 15 | B1 | ARB | Арбитражный процессуальный срок: как не пропустить подачу и возражения | arbitrazhnyj-processualnyj-srok-podacha | ✅ page_id 419 |
| 16 | B2 | IP | Иск о защите интеллектуальной собственности против вас: пошаговый план ответа | isk-o-zashchite-is-protiv-vas-plan-otveta | ✅ page_id 384 |
| 17 | B3 | IP | POIZON в СИП: как суд признал товарный знак недействительным (Кирилл, май 2026) | poizon-tovarnyj-znak-sip-osporenie-registracii | ✅ page_id 422 |
| 18 | B4 | IP | ВС: защита от компенсации за ТЗ иностранца из недружественной страны (Кирилл, июнь 2026) | vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany | ✅ page_id 443 |
| 19 | B5 / KIRILL-ARB | ARB | ВС РФ обзор № 8/2026: спецмеры в арбитраже — ничтожность сделок в обход Указов № 81, 95, 322 (Кирилл, июнь 2026) | vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok | ✅ page_id 535 |
| 20 | B6 / KIRILL-IP | IP | СИП 2026: Президиум аннулировал товарный знак «ВПР» издательства «Просвещение» — злоупотребление правом (Кирилл, июнь 2026) | sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie | ✅ page_id 540 |
| 21 | B7 / KIRILL-UG | UG | Пленум ВС № 19 (2026): цифровой рубль как предмет кражи — когда обман это не мошенничество (Кирилл, июнь 2026) | plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026 | ✅ page_id 543 |
| 22 | B8 / KIRILL-ARB | ARB | Пленум ВС РФ № 42 от 23.12.2025: новые правила субсидиарной ответственности директора, учредителя и КДЛ при банкротстве (Кирилл, июль 2026) | plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026 | ✅ page_id 545 |
| 23 | B9 / KIRILL-ARB | ARB | Обзор ВС 2026: оспаривание сделок с жильём в банкротстве — дарение, цена, мнимость | vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026 | ✅ page_id 555 |
| 24 | B10 / KIRILL-UG | UG | Обзор ВС РФ 01.07.2026: продажа квартиры под влиянием мошенников — ст. 159 УК, ст. 178–179 ГК, защита на проверке и в суде (Кирилл, июль 2026) | vs-prodazha-kvartiry-moshenniki-st-159-zashchita-2026 | ✅ page_id 562 |
| 25 | B11 / KIRILL-UG | UG | ВС РФ прекратил дело о краже как малозначительное: ч. 2 ст. 14 УК и защита в кассации — дайджест № 7/2026, № 11-УД26-3-К6 (Кирилл, июль 2026) | vs-maloznachitelnost-krazha-st-14-zashchita-kassaciya-2026 | ✅ page_id 572 |
| 26 | B12 / KIRILL-ARB | ARB | Обзор ВС № 5/2026: ФНС как залоговый кредитор при налоговом аресте в банкротстве — 109 млн ₽, п. 4 ст. 61.4 (Кирилл, июль 2026) | vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo | ✅ page_id 576 |
| 27 | B13 / KIRILL-ARB | ARB | ВС РФ 18.08.2026: кредитор в банкротстве должен доказать добросовестность при взыскании 56,8 млн ₽ неосновательного обогащения (дело № А65-968/2025) | vs-kreditor-dobrosovestnost-neosnovatelnoe-obogaschenie-bankrotstvo-2026 | ✅ page_id 581 |
| 28 | B14 / KIRILL-IP | IP | Роспатент 24.08.2026: по возражению «Союзмультфильма» аннулирована охрана ТЗ «Маугли» у ОАО «Рот Фронт» (конфеты драже, 30 класс) | rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026 | ✅ page_id 584 |

> Канонический URL A3 на проде: `srok-vozrazhenij-30-vs-15-mify` (без «dnej» в slug).  
> Типы и углы: `article-types-legis24.md`.

## Кирилл после плана

Кирилл запускается только когда все 16 строк очереди имеют статус ✅.
