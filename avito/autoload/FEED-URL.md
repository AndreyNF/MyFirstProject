# Avito автозагрузка по URL — Legis24

В кабинете включена **загрузка по ссылке**. Фид обновляется после `git push` (GitHub raw).

## Как работаем (с пользователем)

Вы пишете в чат, что нужно (новое объявление, освежить все, поменять цену/текст).  
Агент (Петрович / Cloud):

1. Правит `avito/autoload/legis24-new-ads.xml` (или единый `legis24-feed.xml`) по `shared/legis24-avito-xml-rules.md`
2. `python3 scripts/avito-generate-autoload-xml.py` при необходимости
3. Проверка xmlcheck (логика полей)
4. `git commit` + `git push` → Avito подтягивает **ту же ссылку** по расписанию в кабинете
5. Краткий ответ: что изменено, ссылка на фид, когда смотреть отчёт (~1 ч)

Ручная загрузка в кабинете и Telegram **не используются**.

## URL фида (GitHub raw)

**Ветка пайплайна (текущая):**

```
https://raw.githubusercontent.com/AndreyNF/MyFirstProject/cursor/legis24-avito-pipeline-81c8/avito/autoload/legis24-new-ads.xml
```

**После слияния в `main` (стабильная ссылка для кабинета):**

```
https://raw.githubusercontent.com/AndreyNF/MyFirstProject/main/avito/autoload/legis24-new-ads.xml
```

Проверка в браузере: ссылка должна открывать XML, не HTML-страницу 404.

## Обновление фида

```bash
python3 scripts/avito-generate-autoload-xml.py
git add avito/autoload/legis24-new-ads.xml
git commit -m "Update Avito autoload feed"
git push origin <ветка>
```

Avito подтянет изменения **по расписанию** из кабинета (не мгновенно). Отчёт — раздел «Автозагрузка» → «Посмотреть отчёты».

## Настройка в кабинете Avito

1. https://www.avito.ru/professionals/autoload → **Настройки**
2. **Загрузка по ссылке** (не ручная)
3. Вставить URL фида → **Сохранить**
4. Расписание: сколько объявлений / дни / время (по лимиту тарифа)
5. Почта для отчётов — по желанию

До сохранения: https://autoload.avito.ru/format/xmlcheck/

## Альтернатива — свой домен

Если выложить `legis24-new-ads.xml` на https://advokat-vsem.ru/... (статический файл), указать этот URL в Avito — обновление без привязки к GitHub.

## Правила XML

`shared/legis24-avito-xml-rules.md` — обязательные поля (проверено xmlcheck).
