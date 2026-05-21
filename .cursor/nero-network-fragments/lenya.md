=== ЛЁНЯ (SEO-АУДИТ) ===
## Аудит Лёни — цикл 2
Статус: ❌ НУЖНА ПЕРЕСБОРКА
URL: https://advokat-vsem.online/srok-vozrazhenij-30-vs-15-mify/
Дата: 2026-05-21
Артефакты:
- Markdown: nero-repo/skills/indexlift-seo-auditor/deliverables/seo-audit-advokat-vsem-online-2026-05-21/seo-audit-advokat-vsem-online-2026-05-21.md
- JSON: nero-repo/skills/indexlift-seo-auditor/deliverables/seo-audit-advokat-vsem-online-2026-05-21/seo-audit-advokat-vsem-online-2026-05-21.json
- Ручная проверка: curl HTML (URL **со slash**), WebFetch контент — 2026-05-21
- IndexLift: low confidence (redirect loop **без** trailing slash; page_snapshot = null)

### Сверка элементов (цикл 2)

| Элемент | Ожидание (handoff) | Факт live | Статус |
|---|---|---|---|
| Meta description (Yoast) | «Сроки подачи возражений… 30 и 15 дней… 127-ФЗ на 2025–2026» | `<meta name="description">` **отсутствует**; `og:description` = placeholder `Description` | ❌ |
| Title | «Срок возражений при банкротстве: 30 или 15 дней — мифы» | `Срок возражений при банкрotстве: 30 или 15 дней — мифы - Legis 24` (65 симв.) | ⚠️ суффикс « - Legis 24» |
| H1 | один (hero): «30 или 15 дней? Разбираем мифы о сроке возражений» | **2× H1**: Divi `entry-title` + hero | ❌ |
| Canonical | self, со slash | `https://advokat-vsem.online/srok-vozrazhenij-30-vs-15-mify/` | ✅ |
| Чек-лист `#chek-list` | секция опубликована | H2 + 7 пунктов, `id="chek-list"` | ✅ |
| FAQ `#faq` | секция опубликована | H2 + 7 вопросов (H3), `id="faq"` | ✅ |
| Итог `#itog` | секция опубликована | H2 + абзац, `id="itog"` | ✅ |
| Полнота контента | 10 H2, без обрезки | 10 H2, ~3470 слов, `#propusk-sroka` полный, сырой JSON в `<p>` **нет** | ✅ |
| JSON-LD FAQPage | FAQPage в head | только Yoast `@graph` (WebPage, BreadcrumbList, WebSite); FAQPage **нет** | ⚠️ |
| OG image | featured | `og:image` **отсутствует** | ⚠️ |

### Детали ручного аудита (curl HTML, canonical URL)

**Yoast SEO v27.6** — плагин активен, но meta description **не рендерится** в `<head>`.

**Title:** `Срок возражений при банкротстве: 30 или 15 дней — мифы - Legis 24`

**Meta description:** NOT FOUND — критично для сниппета Яндекс/Google.

**og:description:** `Description` — placeholder (совпадает с WP excerpt из handoff цикла 2), не handoff-текст про 30/15 и 127-ФЗ.

**Canonical:** `https://advokat-vsem.online/srok-vozrazhenij-30-vs-15-mify/` ✅

**H1 (2 шт. — дубль):**
1. `Срок возражений при банкротстве: 30 или 15 дней — мифы` (Divi `.entry-title`)
2. `30 или 15 дней? Разбираем мифы о сроке возражений` (hero `.ym-hero`)

**H2 (10 шт. — полная структура):**
1. Что такое возражения…
2. Срок возражений… 30 дней
3. «15 дней» — откуда миф
4. Возражения в реструктуризации
5. Возражения при реализации
6. Возражение на банкротство…
7. Что будет, если пропустить срок
8. **Чек-лист** (`#chek-list`)
9. **Частые вопросы (FAQ)** (`#faq`, 7× H3)
10. **Итог** (`#itog`)

**Оглавление:** якоря `#chek-list`, `#faq`, `#itog`, `#propusk-sroka` — все резолвятся ✅

**JSON-LD:** 1 блок Yoast schema graph; FAQPage отсутствует. Битого JSON в body нет (исправлено vs цикл 1).

**Redirect:** URL без `/` → 301 на канонический с `/`. IndexLift без slash — «Too many redirects»; для аудита использовать URL со slash.

### Прогресс vs цикл 1

| Проблема цикла 1 | Цикл 2 |
|---|---|
| Обрезанный контент / нет chek-list, faq, itog | ✅ исправлено |
| Сырой JSON FAQ в `<p>` | ✅ исправлено |
| Meta description отсутствует | ❌ не исправлено |
| Дубль H1 | ❌ не исправлено |
| og:description placeholder | ❌ не исправлено (excerpt = «Description») |

### Что исправить Юре

1. **Critical:** Заполнить Yoast meta description handoff-текстом и убедиться, что в `<head>` появляется `<meta name="description" content="…">`. Сейчас `_yoast_wpseo_metadesc` заявлен «обновлён», но в HTML тега нет; `og:description` = `Description`.
2. **High:** Оставить один H1 — скрыть Divi `.entry-title` на hero-first шаблоне или понизить hero до `<p>` / `role="heading" aria-level="2"`.
3. **Medium:** Убрать суффикс « - Legis 24» из title/og:title (Yoast title template) или согласовать шаблон.
4. **Medium:** Добавить FAQPage JSON-LD (7 вопросов из секции FAQ) — отдельный валидный `<script type="application/ld+json">`.
5. **Medium:** Добавить `og:image` (featured image).

### Приоритет
- Critical: meta description (Yoast не выводит в HTML)
- High: дубль H1
- Medium: title suffix, og:description/og:image, FAQPage JSON-LD

### Итоговая таблица ✅/❌

| Проверка | |
|---|---|
| Meta description (Yoast) | ❌ |
| Title | ⚠️ |
| H1 | ❌ |
| Canonical | ✅ |
| Чек-лист | ✅ |
| FAQ | ✅ |
| Итог | ✅ |
| Полнота статьи | ✅ |
