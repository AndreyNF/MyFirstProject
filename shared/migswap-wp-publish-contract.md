# MigSwap BLOG — WordPress publish contract

## Prerequisites

- `article.html`, `article.meta.json`
- QA: `validate_article.py` → OK
- `MIGSWAP_BLOG_ALLOW_PUBLISH=yes` (или publish: yes в промте)
- `PUBLIC_SITE_URL` совпадает с доменом WordPress MCP

## Порядок

```bash
python3 scripts/migswap_blog_flatten_lists.py \
  memory/blog/articles/<topic_id>-<slug>/article.html \
  -o memory/blog/articles/<topic_id>-<slug>/article.wp.html
```

Длинный HTML: `wordpress_content_blob_append` (чанки ≤20000, finalize=true) → `wordpress_create_post_from_blob`.

Короткий: `wordpress_create_post` / `wordpress_create_article`.

title и excerpt из `article.meta.json`. Только HTML, не Markdown.

## Статус

`MIGSWAP_WP_STATUS` (по умолчанию `draft`).

## Артефакты

- `wp-publish-result.json`
- строка в `shared/published-articles.md`
- строка в `memory/blog/wp-publish-log.md`

## Blockers

- QA FAIL
- `PUBLIC_SITE_URL` не совпадает с WP
- `MIGSWAP_BLOG_ALLOW_PUBLISH` не yes
