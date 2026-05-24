=== МАКС (QA) ===
Статус: ✅

URL: https://advokat-vsem.online/isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat/
HTTP: 200

Чеклист:
- hero `#l24-hero-arb-bankr-isk` — OK
- Boris `#l24-boris-arb-bankrotstvo-fork` — OK
- `main#primary` + класс `isk-v-arbitrazhe-pri-bankrotstve-kogda-podavat-page` — OK
- breadcrumbs: в DOM нет видимой разметки крошек; CSS скрывает `.breadcrumbs`, `.yoast-breadcrumb` и др. — OK
- CTA `https://advokat-vsem.ru/` — 6 ссылок (hero + 4 ym-cta + inline) — OK
- мобильная вёрстка (HTML): `viewport`, `@media (max-width: 900px|520px)`, `clamp()`, hero grid → 1 col, Boris split/roads/deadlines → 1 col — OK
- img: 1 шт. (логотип в шапке), `alt=""` — замечание: пустой alt у логотипа (не блокер контента страницы)
- внешние ссылки: все 6 на advokat-vsem.ru с `rel="noopener noreferrer"` — OK

Замечания (не блокер):
- Дублирующий `<h1 class="entry-title">` Divi над `<main>` (второй h1 в hero) — SEO/доступность, вне чеклиста A8
