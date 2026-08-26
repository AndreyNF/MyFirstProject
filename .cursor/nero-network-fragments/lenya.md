=== ЛЁНЯ (SEO-АУДИТ) ===
## Аудит Лёни
Статус: ❌ НУЖНА ПЕРЕСБОРКА
URL: https://advokat-vsem.online/rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026/
Дата проверки: 2026-08-26
Метод: curl + парсинг live HTML

### Сводка по чеклисту

| Проверка | Статус | Комментарий |
|---|---|---|
| Title | ⚠️ | Текст = ядро Коли ✅; 73 симв. без бренда, 83 с « - Legis24» — на грани SERP |
| Meta description | ❌ | `<meta name="description">` отсутствует; только `og:description` (162 симв., текст = ядро Коли) |
| H1 | ⚠️ | Hero H1 ✅ = ядро Коли; второй H1 WP `entry-title` в DOM (не скрыт CSS — скрыт только `.entry-header`) |
| Структура H2/H3 | ✅ | 10 H2 (8 контент + FAQ + Источники), 23 H3; якоря `s1-sut-h`…`s8-sip-h`; TOC 8 пунктов |
| FAQ schema | ⚠️ | Microdata `FAQPage` в `#faq` ✅; Article JSON-LD в `<div class="l24-jsonld-maugli" hidden>` — не в `<script>` |
| Внутренние ссылки | ❌ | 5 ссылок в теле; **2 битые (404)** — опечатка `sobstavennosti` вместо `sobstvennosti`; нет `sip-vpr-prosveshchenie` |
| CTA | ✅ | 4 CTA → `https://advokat-vsem.ru/` (`target="_blank"`, `rel="noopener noreferrer"`) |
| Slug | ✅ | `rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026` — соответствует теме |
| Mobile-friendly | ⚠️ | Responsive CSS ✅; `viewport` с `user-scalable=0` — минус a11y |

---

### Title

**Факт:** `Аннулирование товарного знака «Маугли»: возражение «Союзмультфильма» 2026 - Legis24` (83 симв., 73 без бренда).

**Ядро Коли:** `Аннулирование товарного знака «Маугли»: возражение «Союзмультфильма» 2026` — **совпадает**.

**Замечание:** длина на верхней границе 60–70; бренд в хвосте может обрезаться.

---

### Meta description

**Факт:** тег `<meta name="description">` **не найден** в `<head>`.

**Доступно:** `og:description` — «Роспатент аннулировал ТЗ «Маугли» у «Рот Фронта» по возражению «Союзмультфильма». Как оспорить регистрацию знака с персонажем мультфильма и ответить на иск по ИС.» (162 симв.) — **= ядро Коли**.

**Проблема:** Yoast не вывел description; сниппет может собираться случайно.

---

### H1

| Элемент | Статус |
|---|---|
| Hero `h1.l24-hero-rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026__h1` | ✅ Текст = ядро Коли |
| WP `h1.entry-title.main_title` | ⚠️ Дубль в DOM, **не скрыт** (текст = Title, не Hero H1) |

Рекомендация: скрыть `.entry-title` или убрать из шаблона L24-лонгридов.

---

### Структура H2/H3

✅ **Соответствует SEO-ядру Коли (8 секций + FAQ):**

1. `s1-sut-h` — Роспатент аннулировал… (+ H3 1.1, 1.2)
2. `s2-fabula-h` — Дело «Маугли» и «Рот Фронт»… (+ H3 2.1, 2.2)
3. `boris-maugli-tz-flow` — таймлайн Бориса (в TOC)
4. `s3-vozrazhenie-h` — Возражение против товарного знака… (+ H3 3.1, 3.2)
5. `s4-1483-h` — Ст. 1483 и 1512 ГК РФ… (+ H3 4.1, 4.2)
6. `s5-personazh-h` — Товарный знак и персонаж мультфильма… (+ H3 5.1, 5.2)
7. `s6-kompensaciya-h` — Нарушение товарного знака и компенсация… (+ H3 6.1, 6.2)
8. `s7-zashchita-h` — Защита бренда и ответ на иск… (+ H3 7.1, 7.2)
9. `s8-sip-h` — Обжалование решения Роспатента в СИП… (+ H3 8.1, 8.2)
10. `#faq` — FAQ (+ H3 8.3 внутри)
11. `istochniki-h` — Источники и выводы

---

### FAQ schema

| Компонент | Статус |
|---|---|
| FAQ в HTML | ✅ 6 вопросов в `#faq` |
| FAQPage microdata | ✅ `itemscope itemtype="https://schema.org/FAQPage"` |
| Article JSON-LD | ❌ В `<div class="l24-jsonld-maugli" style="display:none">` — не в `<script type="application/ld+json">` |
| Yoast schema | ⚠️ Только WebPage + BreadcrumbList в head; Article не индексируется |

---

### Внутренние ссылки

**В теле статьи (5 уникальных):**

| Ссылка | Статус |
|---|---|
| `/isk-o-zashchite-is-protiv-vas-plan-otveta/` | ✅ 200 |
| `/narushenie-tovarnogo-znaka-dokazatelstva-kompensaciya/` | ✅ 200 |
| `/registraciya-tovarnogo-znaka-etapy-otkaz/` | ✅ 200 |
| `/otvet-na-pretensiyu-po-intellektualnoj-sobstavennosti/` | ❌ **404** (опечатка: `sobstavennosti`) |
| `/zashchita-tovarnogo-znaka-isk-po-intellektualnoj-sobstavennosti/` | ❌ **404** (опечатка: `sobstavennosti`) |

**Корректные slug (200):** `…sobstvennosti` (без лишней «n»).

**Не линкованы (из ядра Коли):**
- `sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie`

---

### CTA

| Блок | href | Текст |
|---|---|---|
| Hero `__cta` | `https://advokat-vsem.ru/` | Консультация по защите бренда |
| ym-cta--primary | `https://advokat-vsem.ru/` | Консультация по защите бренда |
| ym-cta--legis24 | `https://advokat-vsem.ru/` | Помощь с ответом на претензию по ИС |
| ym-cta--bottom | `https://advokat-vsem.ru/` | Обсудить ситуацию с юристом по ИС |

✅ Все 4 CTA на `advokat-vsem.ru/`.

---

### Slug

✅ `rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026` — Роспатент + Маугли + Рот Фронт + аннулирование + товарный знак + 2026.

---

### Что исправить Юре

1. **Critical:** Добавить `<meta name="description">` в Yoast (текст из og:description).
2. **Critical:** Исправить опечатки в 2 внутренних ссылках: `sobstavennosti` → `sobstvennosti`.
3. **Critical:** Перенести Article JSON-LD из hidden div в `<script type="application/ld+json">`.
4. **High:** Убрать/скрыть дублирующий WP H1 `entry-title`.
5. **Medium:** Добавить ссылку на `sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie`.
6. **Medium:** Убрать `user-scalable=0` из viewport.

### Приоритет

- **Critical:** meta description, 2 битые внутренние ссылки (404), Article schema в script
- **High:** dual H1 в DOM
- **Medium:** перелинковка sip-vpr, viewport zoom
