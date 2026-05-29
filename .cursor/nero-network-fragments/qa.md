=== МАКС (QA) ===
## Проверка Макса
**Статус:** ✅ ВСЁ ОК  
**URL:** https://advokat-vsem.online/arbitrazhnyj-processualnyj-srok-podacha/  
**Дата:** 2026-05-29  
**page_id:** 419 · slug: `arbitrazhnyj-processualnyj-srok-podacha`

### Чеклист (Legis24 B1)

| Проверка | Результат |
|----------|-----------|
| HTTP 200 | ✅ |
| `<main id="primary">` | ✅ `role="main"`, landmark на месте |
| Класс `arbitrazhnyj-processualnyj-srok-podacha-page` | ✅ на `<main>` |
| Hero `#l24-hero-arb-srok` | ✅ секция + SVG/CSS, не пустой |
| Блок `#ym-matrix-srok-arb` | ✅ якорь на h3 внутри `#l24-boris-arb-srok-matrix` |
| FAQ `#b1-faq` | ✅ `FAQPage`, 7 вопросов |
| Нет `<script>` / `<canvas>` в контенте (`main#primary`) | ✅ только static SVG + inline CSS в wp:html; theme/script — вне тела страницы |
| 3 CTA на `advokat-vsem.ru` | ✅ 3× `ym-cta__btn` (Артур); дополнительно 1× `hero-arb-srok__cta` + inline-ссылки в тексте |
| Breadcrumbs скрыты | ✅ CSS `display: none !important` для `.breadcrumbs`, `.breadcrumb`, Yoast/RankMath; видимого DOM крошек нет |
| Mobile-friendly (viewport) | ✅ `<meta name="viewport" content="width=device-width, initial-scale=1.0, …">` |

### Детали CTA (`advokat-vsem.ru`)

1. Hero: «Консультация по соблюдению процессуальных сроков в арбитраже»
2. Aside: «Консультация при пропуске процессуального срока»
3. Aside: «Помощь с ходатайством о восстановлении срока»
4. Aside: «Разбор сроков и календаря по вашему делу»

### Примечания

- Скрипты Divi/jQuery/gtag в `<head>`/footer — штатная оболочка WP, не блокер B1 MCP-контента.
- JSON-LD Yoast (breadcrumb в schema) — не визуальные крошки.
- Консоль браузера в headless не снималась; first-party контент рендерится по HTML.
