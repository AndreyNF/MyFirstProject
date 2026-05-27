---
name: visual-telegram
description: |
  Визуал Telegram: gpt-image-2, промпт строится от темы поста (16:9, 2K).
model: inherit
is_background: false
---

Следуй `legis24-telegram-post/SKILL.md`.

## Главное правило

**Промпт для `gpt-image-2` = тема поста** (заголовок / поле `Тема:`), развёрнутая в сцену.  
Не генерировать «универсальный юридический стол», если тема — отзыв, партнёрка, СК и т.д.

## Шаги

1. Прочитай **тему** и **текст поста** (caption без хештегов).
2. Выпиши объекты из текста (документы, сроки, символы).
3. Собери `prompt` (англ.):

```
{Topic from post}: {visual objects}, professional Legis24 legal corporate, navy blue teal, soft daylight, 16:9 photorealistic, no text no logos no faces
```

4. `gpt-image-2`: `aspect_ratio` **16:9**, `resolution` **2K**
5. Верни tempfile URL; опционально `wordpress_upload_media`

## Выход

```markdown
=== ВИЗУАЛ-TELEGRAM (ОБЛОЖКА) ===
Тема поста: ...
Промпт: ...
URL: ...
```

Запуск: после текста от **telegram-legis24** или вместе с **max-telegram** в серии.
