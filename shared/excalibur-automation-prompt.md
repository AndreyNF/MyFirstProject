# Экскалибур — промпты для автоматизации блога (2× в день)

Сайт: **https://advokat-vsem.ru**  
Агент: **@excalibur**  
Skill: `excalibur-blog-automation`

---

## Утро (09:00 МСК) — 1 статья

Скопируйте в Cloud Agent / расписание:

```
@excalibur

Слот: morning

Опубликуй одну новую статью в блог Legis24 по полному пайплайну:
Кирилл (тема) → Коля‖Артём (параллельно) → Женя (лонгрид HTML) → Юра (WordPress publish).

Перед стартом:
- прочитай shared/legis24-published-pages.md и shared/legis24-topics-ledger.md;
- если сегодня слот morning уже published в shared/excalibur-run-log.md — SKIP с отчётом.

Требования:
- тема: налоги, ФНС, арбитраж или уголовка бизнеса; без дублей за 90 дней;
- Wordstat 8–15 вызовов;
- лонгрид 6000–12000 знаков, HTML, CTA order@advokat-vsem.ru;
- обложка: gpt-image-2 или nano_banana_2, промпт от заголовка статьи, кириллица на документах;
- статус WP: publish;
- обнови legis24-published-pages.md и excalibur-run-log.md.

В конце выдай блок === ЭКСКАЛИБУР (ОТЧЁТ) === с URL и WP ID.
```

---

## Вечер (18:00 МСК) — 1 статья

```
@excalibur

Слот: evening

Опубликуй одну новую статью в блог Legis24 по полному пайплайну:
Кирилл → Коля‖Артём → Женя → Юра (WordPress publish).

Перед стартом:
- проверь дубли и excalibur-run-log.md (слот evening сегодня);
- если уже published — SKIP.

Требования — как в утреннем промпте.

В конце: === ЭКСКАЛИБУР (ОТЧЁТ) === с URL и WP ID.
```

---

## Оба слота одним запуском (если пропустили расписание)

```
@excalibur

Режим: catch-up

Опубликуй до 2 статей за сегодня: сначала morning (если не было), затем evening (если не было).
Между статьями — полный сброс handoff. Не больше 2 статей за запуск.
```

---

## Проверка без публикации (dry-run)

```
@excalibur

Режим: dry-run
Слот: morning

Только Кирилл + Коля: тема и SEO-ядро. Без Жени и Юры. Без publish.
```

---

## Настройка расписания (Cursor Cloud Agent)

1. Создайте **2 scheduled tasks** на ветке `main` (или рабочей).
2. Утро: cron `0 9 * * *` Europe/Moscow + промпт «Утро» выше.
3. Вечер: cron `0 18 * * *` Europe/Moscow + промпт «Вечер» выше.
4. Убедитесь, что MCP Kovcheg (WordPress, Wordstat) доступен в Cloud.

---

## Связанные файлы

| Файл | Роль |
|------|------|
| `.cursor/agents/excalibur.md` | Агент |
| `.cursor/agents/director.md` | Пайплайн статей |
| `shared/legis24-site-context.md` | Цены, оффер |
| `shared/excalibur-run-log.md` | Журнал слотов |
