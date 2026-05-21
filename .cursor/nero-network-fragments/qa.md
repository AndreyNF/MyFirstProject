=== МАКС (QA) === цикл 2. Итог ✅

URL: https://advokat-vsem.online/srok-vozrazhenij-30-vs-15-mify/
Проверка: curl (HTML/CSS), 2026-05-21

## Чеклист

| # | Пункт | Статус | Детали |
|---|-------|--------|--------|
| 1 | Hero `.hero-bankrot-sroki` | ✅ | `<section id="hero" class="hero-bankrot-sroki">` — badge, H1 «30 или 15 дней?», шаги 1–3, SVG-визуал, hero-CTA на advokat-vsem.ru |
| 2 | Блок Бориса `#srok-vozrazhenij-boris-block` | ✅ | Секция с chips 15/30, таблицей «Миф vs факт», caption и footnote |
| 3 | TOC `.ym-toc` | ✅ | `<nav class="ym-toc reveal">` — 10 якорей (#chto-takoe-vozrazheniya … #itog), incl. #chek-list, #faq, #itog |
| 4 | 3× CTA `.ym-btn-primary` → advokat-vsem.ru | ✅ | «Консультация по банкротству», «Обсудить ваш случай», «Получить консультацию» — все `href="https://advokat-vsem.ru/"` |
| 5 | CTA `.ym-btn-primary` — красные | ✅ | `--ym-primary: #ff0000`; `.ym-btn-primary { background: var(--ym-primary) }` |
| 6 | `#chek-list` / `#faq` / `#itog` | ✅ | Секции на месте: чек-лист (7 шагов), FAQ (7 вопросов + sidebar), итог + финальный CTA |
| 7 | Нет JSON-мусора в `<p>` | ✅ | В `<main#primary>` — 0 параграфов с JSON/`{"`/`"@context` |
| 8 | `main#primary` | ✅ | `<main id="primary" class="site-main srok-vozrazhenij-30-vs-15-mify-page">` |
| 9 | Padding reset | ✅ | `#primary, .site-main { padding-top: 0 !important; margin-top: 0 !important; }` |
| 10 | Hero — SVG (не canvas) | ✅ | `<svg class="hero-bankrot-sroki__svg" role="img">`; `<canvas>` отсутствует |

## Замечания (не блокеры)

- Логотип в шапке темы: `<img … alt="">` (пустой alt) — правится в Divi/теме, не в контенте статьи.
- Hero-CTA использует `.hero-bankrot-sroki__cta` (синий), не `.ym-btn-primary`; ссылка advokat-vsem.ru корректна.

## Итог

**✅** — все обязательные пункты цикла 2 пройдены; единственное замечание — пустой `alt` у логотипа в шапке (тема, не блокер).
