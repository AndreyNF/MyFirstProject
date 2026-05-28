# Legis24 — правила XML автозагрузки Avito (проверено)

**Статус:** файл `avito/autoload/legis24-new-ads.xml` прошёл проверку на https://autoload.avito.ru/format/xmlcheck/  
**Эталон:** опубликованное объявление №8159283806 (Legis24)  
**Генератор:** `python3 scripts/avito-generate-autoload-xml.py`

Любое новое объявление в XML **обязано** повторять эту структуру полей. Не выдумывать значения — брать из этого файла или из скачанного шаблона кабинета Avito.

## Иерархия категории

| Тег | Значение |
|-----|----------|
| `Category` | Предложение услуг |
| `ServiceType` | Деловые услуги |
| `ServiceSubtype` | Юридические услуги |
| `ServiceSubspecies` | Составление договоров, доверенностей, исков |

## Обязательные параметры услуги (как на живом объявлении)

| Тег | Значение |
|-----|----------|
| `Prepayment` | Нужна |
| `WorkWithContract` | Да |
| `Consultations` | Нет |
| `Place` | Удалённо |
| `WorkExperience` | 4–7 лет |

## Общие поля карточки

| Тег | Значение |
|-----|----------|
| `ListingFee` | Package |
| `AdStatus` | Free |
| `Address` | Россия |
| `ContactPhone` | 79126994560 |
| `ContactMethod` | **В сообщениях** (без звонков) |
| `CompanyName` | Legis24 |
| `DateBegin` | YYYY-MM-DD (дата публикации) |

## Что меняется per SKU

- `Id` — уникальный slug (`legis24-...`)
- `Title` — ≤50 символов
- `Description` — текст объявления + order@advokat-vsem.ru + https://advokat-vsem.ru
- `Price` — фикс с advokat-vsem.ru
- `Images` / `Image[@url]` — одно главное фото на SKU (публичный HTTPS, JPG/PNG; хостинг: `advokat-vsem.online` после `wordpress_upload_media`)

Пример:

```xml
<Images>
  <Image url="https://advokat-vsem.online/wp-content/uploads/2026/05/example-1.png"/>
  <Image url="https://advokat-vsem.online/wp-content/uploads/2026/05/example-2.png"/>
  <Image url="https://advokat-vsem.online/wp-content/uploads/2026/05/example-3.png"/>
</Images>
```

Рекомендуется **3 фото** на SKU (разные ракурсы, кириллица на документах). Поле в генераторе: `image_urls` (список).

Генерация: MCP `gpt-image-2` (при таймауте — `z-image`), промпт с **русским текстом на документах** (`legis24-image-prompt-rules.md`), затем WP media.

## Запреты

- Не публиковать XML без блока полей из таблицы «Обязательные параметры».
- Не менять `ServiceSubtype` / `Prepayment` / `Place` без нового объявления-эталона в кабинете.
- Не отправлять превью в Telegram (отдельный канал).
- Публикация: **автозагрузка по URL** (`avito/autoload/FEED-URL.md`) после `git push`; API `POST` — только если появится scope.

## Порядок тегов в `<Ad>` (рекомендуемый)

```
Id, DateBegin, ListingFee, AdStatus, Category,
ServiceType, ServiceSubtype, ServiceSubspecies,
WorkExperience, Prepayment, WorkWithContract, Consultations, Place,
Title, Description, Images, Price, Address, ContactPhone, ContactMethod, CompanyName
```
