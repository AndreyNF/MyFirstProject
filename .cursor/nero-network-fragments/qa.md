=== МАКС (QA) ===
## Проверка Макса
Статус: ✅ ВСЁ ОК
URL: https://advokat-vsem.online/isk-o-zashchite-is-protiv-vas-plan-otveta/

- HTTP: 200
- Hero `#l24-hero-ip-isk-otvet`: отображается (mobile 390px + desktop), контент и CTA на месте
- Canvas: N/A — по ТЗ hero static SVG + inline CSS, без canvas (ожидаемо)
- Script: теги в норме (22/22), hero без escaped `<script>`
- Консоль: без first-party ошибок (Playwright, headless)
- Контент: секции, Boris, FAQ, CTA рендерятся

### Чеклист задачи
| Проверка | Результат |
| --- | --- |
| `#l24-hero-ip-isk-otvet` | ✅ 1×, visible |
| `#l24-boris-ip-plan-b2` | ✅ 1×, visible |
| `main#primary` | ✅ `class="site-main isk-o-zashchite-is-protiv-vas-plan-otveta-page"` |
| Breadcrumbs не видны | ✅ CSS `display:none` для `.breadcrumb*`; в DOM нет видимого nav; Yoast JSON-LD только |
| `#b2-faq` | ✅ 1×, visible, `FAQPage` schema |
| CTA → `advokat-vsem.ru` | ✅ 6 ссылок, все `target="_blank"` + `rel="noopener noreferrer"` |
| Layout | ✅ без horizontal overflow на mobile; padding-top сброшен под header |
| `img` alt | ⚠️ 1 img (логотип шапки): `alt=""` — атрибут есть, текст пустой (не блокер) |

Проверено: curl HTML + Playwright (Chromium headless), 2026-05-28.
