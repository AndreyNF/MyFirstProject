=== ЛЁНЯ (SEO-АУДИТ) ===
## Аудит Лёни
Статус: ❌ НУЖНА ПЕРЕСБОРКА
URL: https://advokat-vsem.online/vs-kreditor-dobrosovestnost-neosnovatelnoe-obogaschenie-bankrotstvo-2026/
Дата проверки: 2026-08-26
Метод: curl + парсинг HTML (IndexLift в окружении недоступен)

### Сводка по чеклисту

| Проверка | Статус | Комментарий |
|---|---|---|
| Title | ⚠️ | 104 символов без бренда — переполнение SERP; отличается от SEO-ядра Коли |
| Meta description | ❌ | `<meta name="description">` отсутствует; только `og:description` (191 симв.) |
| H1 | ⚠️ | Hero H1 ✅ совпадает с ядром; в DOM второй скрытый H1 WP (`entry-title`, `display:none`) |
| Структура H2/H3 | ✅ | 8 секций H2 + FAQ; 15 H3; якоря `l24-h2-*` / `l24-h3-*`; TOC 9 пунктов |
| FAQ schema | ❌ | JSON-LD FAQPage в `<div hidden>` + `<pre aria-hidden>` — не в `<script type="application/ld+json">` |
| Внутренние ссылки | ❌ | 4 ссылки в теле; 1 битая (404); нет ключевых ARB-хабов из ядра |
| CTA | ⚠️ | 4 CTA на `advokat-vsem.ru/` — ок по QA, но без deep-link на ARB-лендинги |
| Mobile-friendly | ⚠️ | Responsive CSS ✅; `viewport` с `user-scalable=0` — минус доступность |
| ARB-углы | ✅ | К1–К7 закрыты в тексте; hero badge ARB; блок Бориса в TOC |

---

### Title

**Факт:** `ВС РФ: кредитор в банкротстве должен доказать добросовестность при взыскании неосновательного обогащения - Legis24` (114 симв. с брендом, 104 без).

**Ядро Коли:** `ВС РФ: добросовестность кредитора при взыскании неосновательного обогащения 2026` (~70 симв.).

**Проблемы:**
- Длина > 60–70 симв. — обрезка в Google/Яндекс.
- Нет года `2026` в конце (инфоповод).
- Другая формулировка vs SEO-ядро.

---

### Meta description

**Факт:** тег `<meta name="description">` **не найден** в `<head>`.

**Доступно:** `og:description` — «Определение ВС 18.08.2026 по делу № А65-968/2025: отменено взыскание 56,8 млн ₽ с банкрота. Кредитор должен доказать пользование недвижимостью и добросовестность — защита в арбитражном споре.» (191 симв.).

**Проблема:** Yoast не вывел description; поисковики могут сниппетить случайный текст. Текст og совпадает с ядром — нужно продублировать в `meta description` (≤ 155–160 симв.).

---

### H1

| Элемент | Статус |
|---|---|
| Hero `h1.l24-hero-vs-kreditor-dobrosovestnost__h1` | ✅ Текст = ядро Коли |
| WP `h1.entry-title.main_title` | ⚠️ Дубль в DOM, скрыт CSS (`display:none !important`) |

Рекомендация: убрать WP H1 из шаблона страницы или не генерировать `entry-title` для L24-лонгридов.

---

### Структура H2/H3

✅ **Соответствует SEO-ядру (8+ секций ARB):**

1. `l24-h2-1` — Определение ВС 18.08.2026… (+ H3 1.1, 1.2)
2. `l24-h2-2` — Дело № А65-968/2025… (+ H3 2.1, 2.2)
3. `l24-h2-3` — Спор с кредитором в арбитраже… (+ H3 3.1, 3.2)
4. `l24-boris-kreditor-timeline-matrix` — таймлайн Бориса (в TOC)
5. `l24-h2-4` — Неосновательное обогащение… (+ H3 4.1–4.3)
6. `l24-h2-5` — Добросовестность кредитора… (+ H3 5.1, 5.2)
7. `l24-h2-6` — Банкротный контекст… (+ H3 6.1, 6.2)
8. `l24-h2-7` — Защита должника… (+ H3 7.1, 7.2)
9. `#faq` — Частые вопросы (FAQ)

TOC `ym-toc` — 9 якорей, все id существуют.

---

### FAQ schema

| Компонент | Статус |
|---|---|
| FAQ в HTML | ✅ 6 вопросов в `#faq` |
| FAQPage JSON-LD | ❌ В `<div class="l24-jsonld-arb" hidden>` → `<pre aria-hidden="true">` |
| Article JSON-LD | ❌ Та же проблема — не в `<script type="application/ld+json">` |
| Yoast schema | ⚠️ Только WebPage + BreadcrumbList; Article/FAQPage не в head |

Google/Yandex **не индексируют** schema из hidden `<pre>`. Rich results FAQ недоступны.

---

### Внутренние ссылки

**В теле статьи (4 уникальные):**

| Ссылка | Статус |
|---|---|
| `/vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo-vs/` | ❌ **HTTP 404** |
| `/plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026/` | ✅ 200 (но ≠ slug из ядра) |
| `/vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026/` | ✅ 200 |
| `/vs-obzor-5-2026-subsidiarnaya-otvetstvennost-kreditora/` | ❌ **не линкован** (ядро Коли) |

**Не найдены в контенте (из ядра Коли для Жени):**
- `isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat`
- `arbitrazhnyj-spor-s-kreditorom-sroki-strategiya`
- `konsultaciya-po-arbitrazhnomu-sporu`
- `predstavitel-v-arbitrazhe`
- `vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo` (канонический slug)

---

### CTA

| Блок | href | Текст |
|---|---|---|
| Hero | `https://advokat-vsem.ru/` | Консультация по арбитражному спору |
| ym-cta--primary | `https://advokat-vsem.ru/` | Консультация по арбитражному спору |
| ym-cta--legis24 | `https://advokat-vsem.ru/` | Помощь со стратегией в арбитражном суде |
| ym-cta--bottom | `https://advokat-vsem.ru/` | Обсудить ситуацию с юристом |

✅ CTA присутствуют, `target="_blank"`, `rel="noopener noreferrer"`.
⚠️ Все ведут на главную `.ru`, без deep-link на ARB-услуги (`konsultaciya-po-arbitrazhnomu-sporu`, `predstavitel-v-arbitrazhe`).

---

### Mobile-friendly markup

✅ `viewport` width=device-width  
✅ `clamp()`, CSS Grid, `@media (max-width: 900px)` — hero, intro, boris  
✅ SVG `width="100%"`, `max-width:520px`  
✅ `aria-label` на hero, FAQ, boris, TOC  
⚠️ `maximum-scale=1.0, user-scalable=0` — блокирует зум (минус mobile UX/a11y)  
⚠️ Yoast `twitter:data1` = «1 минута» при ~3900 слов в main

---

### ARB-углы (покрытие кластеров Коли)

| Кластер | Покрытие |
|---|---|
| К1 Арбитражный спор | ✅ H2 §1, §3, §7 |
| К2 Неосновательное обогащение | ✅ H2 §4, hero, FAQ |
| К3 Спор с кредитором / добросовестность | ✅ H2 §3, §5, hero facts |
| К4 Доказывание / преюдиция | ✅ H2 §4, boris timeline |
| К5 Защита / представитель | ⚠️ H2 §7 без внутр. ссылки на лендинг |
| К6 Кейс ВС 2026 | ✅ hero facts, H2 §2 |
| К7 Банкротный контекст | ✅ H2 §6 |
| К8 Обзор ВС 2022 | ✅ упоминание в §6 |

---

### Что исправить Юре

1. **Critical:** Добавить `<meta name="description">` в Yoast (текст из og:description, ≤ 160 симв.).
2. **Critical:** Перенести Article + FAQPage JSON-LD в `<script type="application/ld+json">` в `<head>` или перед `</body>`; убрать hidden `<pre>`.
3. **Critical:** Исправить битую ссылку `/vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo-vs/` → `/vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo/`.
4. **High:** Сократить title до ~60–70 симв., добавить `2026` (по ядру Коли).
5. **High:** Добавить 3–5 внутренних ссылок в текст: `vs-obzor-5-2026-subsidiarnaya-otvetstvennost-kreditora`, `isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat`, `arbitrazhnyj-spor-s-kreditorom-sroki-strategiya`.
6. **High:** Убрать дублирующий WP H1 (`entry-title`) из DOM.
7. **Medium:** Убрать `user-scalable=0` из viewport.
8. **Medium:** CTA deep-link на ARB-лендинги (не только главная `.ru`).
9. **Medium:** Скорректировать Yoast reading time / `dateModified`.

### Приоритет

- **Critical:** meta description, FAQ/Article schema в script, битая внутренняя ссылка 404
- **High:** title length, внутренняя перелинковка ARB-хабов, dual H1
- **Medium:** viewport zoom, CTA deep-links, reading time
