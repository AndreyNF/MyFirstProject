=== МАКС (QA) ===
Статус: ✅

**URL:** https://advokat-vsem.online/rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026/
**Дата проверки:** 2026-08-26

## Чеклист

| Проверка | Результат |
|---|---|
| HTTP 200 | ✅ 200 |
| `main#primary` | ✅ `<main id="primary" class="site-main rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026-page">` |
| Hero `l24-hero-rospatent-maugli` | ✅ секция `#l24-hero-rospatent-maugli-rot-front-annulirovanie-tovarnyj-znak-2026`, H1, факты, SVG-иллюстрация, CTA |
| Boris `#boris-maugli-tz-flow` | ✅ секция на месте, маршрут ППС → СИП, inline CSS + SVG |
| CTA href `advokat-vsem.ru` | ✅ 4 CTA → `https://advokat-vsem.ru/` |
| HTML без явных поломок | ✅ парсер: 0 ошибок вложенности тегов |
| Breadcrumbs hidden | ✅ CSS `display: none !important` на `.breadcrumbs`, `.breadcrumb`, `.yoast-breadcrumb`; видимых крошек в DOM нет |

## Детали

- **Hero:** H1 «Роспатент аннулировал товарный знак «Маугли»…», факты (№ 162034, приоритет 30.01.1996, п. 9 ст. 1483 / ст. 1512 ГК, «Рот Фронт» vs «Союзмультфильм», аннулирование 24.08.2026), CTA «Консультация по защите бренда».
- **Boris:** тёмный блок `#boris-maugli-tz-flow` после §2, маршрут возражения → ППС → СИП.
- **CTA (все 4):** hero `__cta` + 3× `ym-cta__btn` — только `advokat-vsem.ru`.
- **Примечание:** WP/Divi подключают `<script>` в футере темы (jQuery, gtag) — вне L24-контента, не блокер.

**Проблемы:** нет.
