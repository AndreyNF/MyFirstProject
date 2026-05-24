=== МАКС (QA) ===
Статус: ✅

**URL:** https://advokat-vsem.online/otvet-na-pretensiyu-po-intellektualnoj-sobstvennosti/  
**Дата проверки:** 2026-05-24

## Проверки

| # | Критерий | Результат | Детали |
|---|----------|-----------|--------|
| 1 | HTTP 200 | ✅ | `HTTP/2 200`, `content-type: text/html; charset=UTF-8` |
| 2 | `main#primary` | ✅ | `<main id="primary" class="site-main otvet-na-pretensiyu-po-intellektualnoj-sobstvennosti-page" role="main">` |
| 3 | Hero section | ✅ | `<section id="l24-hero-ip-pret-otvet" class="hero-ip-pret-otvet">` — H1, дедлайны, CTA |
| 4 | Блок Бориса | ✅ | `<section id="l24-boris-ip-pret-sroki-track" class="l24-boris-ip-pret-sroki">` — календарь, три режима сроков |
| 5 | Нет breadcrumbs | ✅ | В DOM нет видимых `.breadcrumb` / `.breadcrumbs`; CSS `display: none !important` для breadcrumb-классов; только JSON-LD BreadcrumbList в `<script>` |
| 6 | CTA → advokat-vsem.ru | ✅ | 5 CTA в `main#primary`: hero + 4× `ym-cta__btn`, все `href="https://advokat-vsem.ru/"` |
| 7 | alt у img/svg | ✅ | `<img>` в контенте: 0 (нет без alt). SVG: 3 шт. — 2 с `role="img"` + `aria-label`, 1 декоративный с `aria-hidden="true"` |
| 8 | Mobile-friendly CSS | ✅ | `<meta name="viewport" content="width=device-width, initial-scale=1.0">`; `@media (max-width: 900px)` в hero, блоке Бориса и page-level; `clamp()`, grid→1 col на мобиле |

## Итог

Все 8 проверок пройдены. Страница готова к публикации.
