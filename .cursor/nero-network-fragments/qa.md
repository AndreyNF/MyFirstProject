=== МАКС (QA) ===
Статус: ✅

URL: https://advokat-vsem.online/dosudebnaya-zashchita-po-ugolovnomu-delu/

- HTTP: 200 (страница и CTA-цель advokat-vsem.ru — 200)
- Проверено: curl HTML + Playwright (Chromium headless, mobile 390px + desktop 1280px), 2026-05-28
- Консоль / pageerror: без ошибок

### Чеклист
| Проверка | Результат |
| --- | --- |
| `main#primary` | ✅ 1×, `class="site-main dosudebnaya-zashchita-po-ugolovnomu-delu-page"`, visible |
| Hero `l24-hero-dosudeb` | ✅ секция `#l24-hero-dosudeb-zashchita` (префикс `l24-hero-dosudeb`), класс `hero-ug-dosudeb`, SVG + CTA, visible mobile/desktop |
| Блок Бориса / матрица `#ym-matrix-dosudeb` | ✅ секция `#l24-boris-ug-dosudeb-matrix`, якорь `#ym-matrix-dosudeb` на h3, сетка 3×3 + легенда, visible |
| CTA → `advokat-vsem.ru` | ✅ 4 ссылки, все `target="_blank"` + `rel="noopener noreferrer"` |
| FAQ | ✅ `#ym-dosudeb-faq`, h2 «FAQ: короткие ответы», 4 вопроса, `FAQPage` schema |
| Вёрстка | ✅ без horizontal overflow (mobile/desktop); inline CSS с `@media (max-width: 900px/520px)` |
| Mobile-friendly (HTML) | ✅ `<meta name="viewport" content="width=device-width, initial-scale=1.0…">`, `et_mobile_nav_menu`, responsive `@media`, `prefers-reduced-motion` |

### Замечания (не блокеры)
- ID hero в DOM: `l24-hero-dosudeb-zashchita` (не ровно `l24-hero-dosudeb`) — якорь и контент на месте.
- В теле статьи есть дополнительные блоки `.l24-faq-a13__item` вне секции `#ym-dosudeb-faq` — ожидаемая структура longread.
