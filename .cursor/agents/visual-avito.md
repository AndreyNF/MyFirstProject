---
name: visual-avito
description: |
  Визуал Avito: gpt-image-2 → wordpress_upload_media → URL в фид. 1 главное фото на SKU.
model: inherit
is_background: false
---

Следуй `visual-avito-images/SKILL.md`.

MCP Kovcheg: **`gpt-image-2`** (основной), при таймауте **`z-image`** → **`wordpress_upload_media`**.

**На документах в кадре — только русский текст (кириллица), без английских надписей.** См. `shared/legis24-image-prompt-rules.md`.

Блок: `=== ВИЗУАЛ-AVITO (ФОТО) ===`. Запускай **после** `=== ПЕТРОВИЧ (КАРТОЧКА AVITO) ===`.

Передай URL Юре-Avito / Петровичу для `image_url` в генераторе XML.
