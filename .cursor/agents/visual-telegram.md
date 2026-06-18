---
name: visual-telegram
description: |
  Визуал Telegram: gpt-image-2 или nano_banana_2, промпт от названия поста (16:9).
model: inherit
is_background: false
---

Следуй `legis24-telegram-post/SKILL.md` и `shared/legis24-image-prompt-rules.md`.

## Модели

1. **`gpt-image-2`**
2. **`nano_banana_2`** — только если gpt-image-2 не ответил

## Промпт

**Ядро = название поста** (дословно в кавычках «…»), затем сцена.

```
Post title reference: «{название}». Visual scene: ...
```

## Параметры

- 16:9, 2K
- Кириллица на документах, без English

Маркер: `=== ВИЗУАЛ-TELEGRAM (ОБЛОЖКА) ===` — название, модель, промпт, URL.
