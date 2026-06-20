# Excalibur BLOG — Legis24

Язык работы: русский.

## Главное правило

Для полной SEO/GEO статьи **нельзя** выполнять весь пайплайн одним Cloud Agent.

Cloud Agent обязан оркестрировать через **Директора** и запускать субагентов:

```text
python3 scripts/excalibur_blog_today.py
  → excalibur-blog-research (research-notes-gate.json PASS)
  → excalibur-blog-writer (human article from research brief)
  → excalibur-blog-geo-qa (human-voice-report.json PASS)
  → excalibur-blog-cover || excalibur-blog-schema
  → excalibur-blog-indexer
  → excalibur-blog-publish
```

## Cloud Task fallback

Если Cloud API не принимает `excalibur-blog-*` как Task types:

- **отдельный `Task(generalPurpose)` на каждую роль**;
- передай путь `.cursor/agents/<role>.md` и `.cursor/skills/<skill>/SKILL.md`;
- один Task = одна роль;
- параллель `cover || schema` — два отдельных Task в одном сообщении.

## Субагенты

| name | skill | что делает |
|------|-------|-----------|
| excalibur-blog-research | excalibur-research | web research, Wordstat, SERP, sources, pain_solution_map |
| excalibur-blog-writer | writer-excalibur-blog | пишет HTML-статью по research brief |
| excalibur-blog-geo-qa | excalibur-geo-qa | E-E-A-T, human voice gate, anti-slop |
| excalibur-blog-cover | cover-excalibur-blog | генерация обложки через MCP (gpt-image-2) |
| excalibur-blog-schema | schema-excalibur-blog | structured data (FAQ, Article) |
| excalibur-blog-indexer | indexer-excalibur-blog | внутренние ссылки, cannibalization guard |
| excalibur-blog-publish | excalibur-wp-publish | публикация через wordpress_create_post MCP |

## Канонические пути

| Артефакт | Путь |
|----------|------|
| Site brief | `memory/brief/site-brief.md` |
| Conversion map | `memory/brief/conversion-map.md` |
| Topics | `memory/topics/blog-topics.md` |
| Cover concept | `memory/cover/cover-concept.md` |
| Published ledger | `shared/published-articles.md` |
| Article artifacts | `memory/blog/articles/<topic_id>-<slug>/` |
| Agents | `.cursor/agents/` |
| Skills | `.cursor/skills/` |

## Правила для статей Legis24

1. **Ссылки на advokat-vsem.ru** — минимум 2 CTA в каждой статье (см. conversion-map.md)
2. **Картинки на русском** — все надписи на обложках только кириллицей
3. **Без дублирования картинок** — обложка только через `featured_media`, НЕ вставлять `<figure>` в контент
4. **Формат cover:** 16:9, фотореалистичный, тёмно-синий + белый
5. **Стиль текста:** деловой, без воды, со ссылками на НК РФ/ст./п.

## Секреты (Cursor Dashboard)

- `PUBLIC_SITE_URL` = https://advokat-vsem.online
- `EXCALIBUR_BLOG_ALLOW_PUBLISH` = yes (для боевой публикации)
- WordPress API credentials — через MCP Kovcheg (уже подключён)

## Cursor Cloud specific instructions

- MCP Kovcheg содержит все необходимые инструменты: `wordpress_create_post`, `wordpress_update_post`, `wordpress_upload_image_from_url`, `gpt-image-2`, `wordstat_get_top_requests`
- Тема сайта: Divi 4.27.5.1
- Главная страница: page ID 146
- Категория «Налоги и суды»: ID 5
- Для исследования: `WebSearch` + MCP `wordstat_get_top_requests`
- Для обложек: MCP `gpt-image-2` (prompt на русском, 16:9)
- Для публикации: MCP `wordpress_create_post` + `wordpress_upload_image_from_url`
