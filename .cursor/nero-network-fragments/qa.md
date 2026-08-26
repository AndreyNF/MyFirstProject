=== МАКС (QA) ===
Статус: ✅

**URL:** https://advokat-vsem.online/vs-kreditor-dobrosovestnost-neosnovatelnoe-obogaschenie-bankrotstvo-2026/
**Дата проверки:** 2026-08-26

## Чеклист

| Проверка | Результат |
|---|---|
| HTTP 200 | ✅ 200 |
| `main#primary` | ✅ `<main id="primary" class="site-main vs-kreditor-dobrosovestnost-neosnovatelnoe-obogaschenie-bankrotstvo-2026-page">` |
| Hero `#l24-hero-vs-kreditor-dobrosovestnost` | ✅ секция на месте, SVG-иллюстрация, CTA |
| Boris `#l24-boris-kreditor-timeline-matrix` | ✅ секция на месте, static SVG таймлайн + карточки 4 дел |
| NO `<script>` / `<canvas>` в контенте | ✅ в `entry-content`, hero и boris — 0 script, 0 canvas (только inline CSS + SVG) |
| CTA href `advokat-vsem.ru` | ✅ 4 CTA → `https://advokat-vsem.ru/` |
| alt на img | ✅ в контенте статьи `<img>` нет; SVG с `aria-label` / `aria-labelledby` |
| Breadcrumbs hidden | ✅ CSS `display: none !important` на `.breadcrumbs`, `.breadcrumb`, `.yoast-breadcrumb`; видимых крошек в DOM нет |

## Детали

- **Hero:** H1, факты дела (№ 306-ЭС26-695, 56 829 324,48 ₽, 13 объектов, Казань, ст. 10/1102 ГК), CTA «Консультация по арбитражному спору».
- **Boris:** тёмный блок таймлайна после H2 §3, 4 карточки дел, итог ~94,4 млн ₽.
- **CTA (все 4):** hero + 3× `ym-cta__btn` — только `advokat-vsem.ru`.
- **Примечание:** WP/Divi подключают `<script>` в футере темы (jQuery, gtag) — вне L24-контента, не блокер.

**Проблемы:** нет.
