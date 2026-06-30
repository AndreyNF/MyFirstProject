---
description: Публикация страницы Legis24 через MCP Kovcheg (blob flow), без FTP/Aura
---

Режим **Cloud MCP-only**. Скилл: **publisher-yura** (адаптация под MCP).

## Алгоритм

1. `wordpress_create_page` — черновик, slug, title, status=draft
2. HTML от Наташи: обернуть в `<!-- wp:html -->`; **удалить все `<script>`** перед blob (WP ломает body)
3. `wordpress_content_blob_append` — чанки ≤20000, последний с `finalize=true`
4. `wordpress_update_page_from_blob` — page_id + blob_id
5. `wordpress_update_page` — status=publish, excerpt=Description из SEO
6. Записать в `nero-network-office-page/shared/published-pages.md` и `content-plan-legis24.md` (✅ + page_id)

## Запреты
- FTP, SSH, `page-{slug}.php`
- canvas/script в hero и блоке Бориса (static SVG/CSS only)
- CTA только https://advokat-vsem.ru/
