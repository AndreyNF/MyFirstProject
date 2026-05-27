# Skill: visual-avito-images

Визуальный блок пайплайна Avito (MCP Kovcheg).

## Вход

`=== ПЕТРОВИЧ (КАРТОЧКА AVITO) ===` + ниша из ввода.

## Цепочка (канон)

```
I1: gpt-image-2 (text-to-image, 1:1, 1K)
  → при таймауте MCP: z-image
  → wordpress_upload_media (стабильный HTTPS на advokat-vsem.online)
```

Опционально (если нужна галерея 5–8 фото):

- дополнительные вызовы `gpt-image-2` с разными промптами;
- legacy: `flux2-pro-text-to-image` → `recraft_remove_background` → `seedream-4_5-edit`.

### I1 — gpt-image-2

- `aspect_ratio`: `1:1` (главное для фида), при галерее также `4:3`
- `resolution`: `1K`
- Промпт-шаблон: «Professional legal services, tax documents on clean desk, soft daylight, corporate navy blue accents, no text overlay, no faces, photorealistic»

Подстрой промпт под нишу SKU (акт ФНС, требование, иск, СК…).

### Хостинг

**Обязательно** `wordpress_upload_media` после генерации — временные URL Kie.ai Avito не подхватит надёжно.

## Итого в пакете

Минимум **1** URL на SKU в XML; для галереи — **5–8** URL.

## Выход

```markdown
=== ВИЗУАЛ-AVITO (ФОТО) ===
Статус: ✅ ГОТОВО

| # | URL | Модель | Назначение |
| 1 | https://advokat-vsem.online/wp-content/uploads/... | gpt-image-2 | Главное |

## Промпты (архив)
...
```

## Запреты

- Не использовать лица реальных людей
- Не копировать чужие скрины Avito
- Не отправлять в Telegram
