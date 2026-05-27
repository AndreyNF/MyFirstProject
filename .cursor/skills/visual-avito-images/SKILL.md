# Skill: visual-avito-images

Визуальный блок пайплайна Avito (MCP Kovcheg).

## Вход

`=== ПЕТРОВИЧ (КАРТОЧКА AVITO) ===` + ниша из ввода.

## Цепочка

```
I1: flux2-pro-text-to-image  (или nano_banana_2)
  → I2: recraft_remove_background (для 2–3 лучших)
  → I3: seedream-4_5-edit (2–3 варианта фона)
```

### I1 — генерация (3–5 базовых)

**flux2-pro-text-to-image** (предпочтительно):

- `aspect_ratio`: `1:1` и `4:3`
- `resolution`: `1K`
- Промпт-шаблон: «Professional legal services, tax documents and gavel on clean desk, soft daylight, corporate blue accents, no text overlay, no faces, photorealistic»

**nano_banana_2** — запасной, если flux недоступен.

### I2 — без фона

**recraft_remove_background** — для 2–3 URL из I1 (лучшие по композиции).

### I3 — варианты

**seedream-4_5-edit**:

- `prompt`: «Replace background with subtle Russian office skyline, keep documents sharp»
- `image_urls`: [png из I2]
- `quality`: `basic`

Сделать 2–3 варианта на разные промпты (ночной дедлайн / спокойный офис / абстрактный синий градиент).

## Итого в пакете

**5–8** публичных URL (после загрузки на хостинг при необходимости — иначе URL от MCP).

## Выход

```markdown
=== ВИЗУАЛ-AVITO (ФОТО) ===
Статус: ✅ ГОТОВО

| # | URL | Размер | Назначение |
| 1 | ... | 1:1 | Главное фото |
...

## Промпты (архив)
...
```

## Запреты

- Не использовать лица реальных людей / знаменитостей
- Не копировать чужие скрины с Avito
- Не отправлять в Telegram без блока ПАКЕТ (Директор)
