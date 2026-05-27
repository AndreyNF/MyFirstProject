=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Тема:** Precheck A15 (IP) — регистрация товарного знака: этапы, отказ Роспатента, обжалование  
**Slug:** registraciya-tovarnogo-znaka-etapy-otkaz  
**Режим:** продолжение метафоры «трёх писем Роспатента» из лонгрида (контраст hero: процедура регистрации, не защита в суде)  
**Якорь для Наташи:** `#l24-boris-tz-route`  
**Техника:** inline `<style>` + static SVG; без `<canvas>` и `<script>`

```html
<section id="l24-boris-tz-route" class="l24-boris-tz-route" aria-label="Три письма Роспатента: запрос, уведомление, отказ — сроки и последствия">
<style>
.l24-boris-tz-route {
  --tzr-navy: #0f2744;
  --tzr-navy-soft: #1a365d;
  --tzr-blue: #3182ce;
  --tzr-gold: #ecc94b;
  --tzr-amber: #d69e2e;
  --tzr-accent: #c53030;
  --tzr-mint: #68d391;
  --tzr-ink: #e2e8f0;
  --tzr-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-tz-route__shell {
  background: linear-gradient(148deg, var(--tzr-navy) 0%, #152a45 52%, var(--tzr-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--tzr-ink);
}
.l24-boris-tz-route__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--tzr-gold);
}
.l24-boris-tz-route__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-tz-route__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--tzr-muted);
  max-width: 66ch;
}
.l24-boris-tz-route__lead strong { color: #fff; }
.l24-boris-tz-route__split {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 0.98fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-tz-route__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-tz-route__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--tzr-gold);
}
.l24-boris-tz-route__map-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 200px;
  margin-bottom: 14px;
}
.l24-boris-tz-route__letters {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-tz-route__letter {
  margin: 0;
  padding: 12px 10px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-top: 3px solid var(--tzr-blue);
  font-size: 0.76rem;
  line-height: 1.42;
}
.l24-boris-tz-route__letter:nth-child(2) { border-top-color: var(--tzr-amber); }
.l24-boris-tz-route__letter:nth-child(3) { border-top-color: var(--tzr-accent); }
.l24-boris-tz-route__letter strong {
  display: block;
  color: #fff;
  font-size: 0.82rem;
  margin-bottom: 4px;
}
.l24-boris-tz-route__matrix {
  display: grid;
  grid-template-columns: 1fr;
  gap: 10px;
  margin: 0 0 12px;
}
.l24-boris-tz-route__row {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(72px, 0.7fr) minmax(0, 1fr);
  gap: 8px 10px;
  align-items: center;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.35;
}
.l24-boris-tz-route__row--req { border-left: 3px solid var(--tzr-blue); }
.l24-boris-tz-route__row--notif { border-left: 3px solid var(--tzr-amber); }
.l24-boris-tz-route__row--ref { border-left: 3px solid var(--tzr-accent); }
.l24-boris-tz-route__row-name {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-tz-route__row-term {
  font-weight: 800;
  color: var(--tzr-gold);
  text-align: center;
  font-size: 0.8rem;
}
.l24-boris-tz-route__row-fail {
  color: #fed7d7;
  font-size: 0.72rem;
}
.l24-boris-tz-route__row-fail em {
  font-style: normal;
  color: var(--tzr-mint);
  font-weight: 600;
}
.l24-boris-tz-route__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--tzr-muted);
}
.l24-boris-tz-route__note em {
  font-style: normal;
  color: var(--tzr-mint);
  font-weight: 600;
}
.l24-boris-tz-route__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-tz-route__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--tzr-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-tz-route__tag--pps { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
.l24-boris-tz-route__tag--warn { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-tz-route__caption {
  margin: 12px 0 0;
  font-size: 0.72rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
  letter-spacing: 0.02em;
}
@media (max-width: 900px) {
  .l24-boris-tz-route__split { grid-template-columns: 1fr; }
  .l24-boris-tz-route__letters { grid-template-columns: 1fr; }
  .l24-boris-tz-route__row {
    grid-template-columns: 1fr;
    gap: 4px;
  }
  .l24-boris-tz-route__row-term { text-align: left; }
}
</style>

  <div class="l24-boris-tz-route__shell">
    <p class="l24-boris-tz-route__eyebrow">ГК РФ ст. 1499 п.3 · 1500 · 1501 · АР ТЗ № 483</p>
    <h3 class="l24-boris-tz-route__title">Три письма Роспатента: не путать запрос, уведомление и отказ</h3>
    <p class="l24-boris-tz-route__lead">Слева — <strong>маршрут корреспонденции</strong> на пути к свидетельству. Справа — <strong>сроки и цена пропуска</strong>: только у запроса есть продление; уведомление даёт жёсткие <strong>6 месяцев</strong> с даты <strong>направления</strong>; после финального отказа — <strong>4 месяца</strong> в ППС и затем СИП.</p>

    <div class="l24-boris-tz-route__split">
      <div class="l24-boris-tz-route__panel">
        <p class="l24-boris-tz-route__panel-title">Карта трёх писем</p>
        <svg class="l24-boris-tz-route__map-svg" viewBox="0 0 540 172" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="tzr-letters-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#3182ce"/>
              <stop offset="50%" stop-color="#d69e2e"/>
              <stop offset="100%" stop-color="#c53030"/>
            </linearGradient>
          </defs>
          <line x1="44" y1="82" x2="496" y2="82" stroke="url(#tzr-letters-line)" stroke-width="4" stroke-linecap="round"/>
          <rect x="28" y="52" width="88" height="58" rx="6" fill="rgba(49,130,206,0.22)" stroke="#63b3ed" stroke-width="1.4"/>
          <text x="72" y="72" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="700">Запрос</text>
          <text x="72" y="88" text-anchor="middle" fill="#e2e8f0" font-size="8">п.102 АР ТЗ</text>
          <text x="72" y="102" text-anchor="middle" fill="#90cdf4" font-size="7.5">+ продление</text>
          <rect x="206" y="48" width="128" height="66" rx="6" fill="rgba(214,158,46,0.2)" stroke="#ecc94b" stroke-width="1.6"/>
          <text x="270" y="70" text-anchor="middle" fill="#faf089" font-size="9" font-weight="700">Уведомление</text>
          <text x="270" y="86" text-anchor="middle" fill="#e2e8f0" font-size="8">ст. 1499 п.3</text>
          <text x="270" y="102" text-anchor="middle" fill="#fbd38d" font-size="7.5" font-weight="600">6 мес. · без продления</text>
          <rect x="424" y="52" width="88" height="58" rx="6" fill="rgba(197,48,48,0.22)" stroke="#fc8181" stroke-width="1.4"/>
          <text x="468" y="72" text-anchor="middle" fill="#fed7d7" font-size="9" font-weight="700">Отказ</text>
          <text x="468" y="88" text-anchor="middle" fill="#e2e8f0" font-size="8">решение</text>
          <text x="468" y="102" text-anchor="middle" fill="#feb2b2" font-size="7.5">→ ППС 4 мес.</text>
          <circle cx="72" cy="82" r="10" fill="#3182ce" stroke="#fff" stroke-width="1.5"/>
          <circle cx="270" cy="82" r="10" fill="#d69e2e" stroke="#fff" stroke-width="1.5"/>
          <circle cx="468" cy="82" r="10" fill="#c53030" stroke="#fff" stroke-width="1.5"/>
          <path d="M 120 82 L 198 82" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
          <path d="M 338 82 L 412 82" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4 3"/>
          <rect x="32" y="128" width="148" height="32" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="106" y="148" text-anchor="middle" fill="#e2e8f0" font-size="8">не ответили → отзыв заявки</text>
          <rect x="196" y="128" width="148" height="32" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="270" y="148" text-anchor="middle" fill="#e2e8f0" font-size="8">молчание → финальный отказ</text>
          <rect x="360" y="128" width="148" height="32" rx="5" fill="rgba(39,103,73,0.4)" stroke="rgba(104,211,145,0.35)" stroke-width="1"/>
          <text x="434" y="148" text-anchor="middle" fill="#c6f6d5" font-size="8" font-weight="600">возражение 9 000 ₽ · ППС</text>
        </svg>
        <ul class="l24-boris-tz-route__letters">
          <li class="l24-boris-tz-route__letter">
            <strong>1. Запрос экспертизы</strong>
            Уточнение документов, МКТУ, изображения. Срок в запросе; можно продлить ходатайством и пошлиной. Пропуск — отзыв заявки (п.105 АР ТЗ), не «отказ по 1483».
          </li>
          <li class="l24-boris-tz-route__letter">
            <strong>2. Уведомление (предварительный отказ)</strong>
            Доводы заявителя — 6 месяцев со дня направления (1499 п.3). Срок не продлевается. Игнор — решение без учёта аргументов.
          </li>
          <li class="l24-boris-tz-route__letter">
            <strong>3. Решение об отказе</strong>
            Возражение в ППС — 4 месяца (1500); копии противопоставлений — запрос в 2 месяца. Далее СИП по ст. 1248 после досудебки.
          </li>
        </ul>
      </div>

      <div class="l24-boris-tz-route__panel">
        <p class="l24-boris-tz-route__panel-title">Сроки и последствия</p>
        <div class="l24-boris-tz-route__matrix" role="table" aria-label="Сравнение запроса, уведомления и отказа">
          <div class="l24-boris-tz-route__row l24-boris-tz-route__row--req" role="row">
            <span class="l24-boris-tz-route__row-name" role="cell">Запрос</span>
            <span class="l24-boris-tz-route__row-term" role="cell">до 6 мес.</span>
            <span class="l24-boris-tz-route__row-fail" role="cell">Продление <em>да</em> · пропуск → <em>отзыв заявки</em></span>
          </div>
          <div class="l24-boris-tz-route__row l24-boris-tz-route__row--notif" role="row">
            <span class="l24-boris-tz-route__row-name" role="cell">Уведомление</span>
            <span class="l24-boris-tz-route__row-term" role="cell">6 мес.</span>
            <span class="l24-boris-tz-route__row-fail" role="cell">Продление <em>нет</em> · отсчёт с <em>направления</em>, не получения</span>
          </div>
          <div class="l24-boris-tz-route__row l24-boris-tz-route__row--ref" role="row">
            <span class="l24-boris-tz-route__row-name" role="cell">Отказ</span>
            <span class="l24-boris-tz-route__row-term" role="cell">4 мес.</span>
            <span class="l24-boris-tz-route__row-fail" role="cell">ППС 9 000 ₽ · восстановление по <em>1501</em> — 6 мес., причины</span>
          </div>
        </div>
        <p class="l24-boris-tz-route__note"><em>Частичный отказ</em> — регистрация по одним классам МКТУ и спор по отказной части в ППС. <em>Копии противопоставлений</em> в 2 месяца продлевают подготовку возражения (1500 п.1).</p>
      </div>
    </div>

    <div class="l24-boris-tz-route__foot" aria-label="Следующие шаги после отказа">
      <span class="l24-boris-tz-route__tag l24-boris-tz-route__tag--pps">ППС: первое заседание ≤ 1 мес. с принятия</span>
      <span class="l24-boris-tz-route__tag">СИП: досудебный порядок обязателен (ст. 1248)</span>
      <span class="l24-boris-tz-route__tag l24-boris-tz-route__tag--warn">Не путать «отказ 1483» и отзыв заявки</span>
      <span class="l24-boris-tz-route__tag">Письмо-согласие · сужение МКТУ (1500 п.2)</span>
    </div>
    <p class="l24-boris-tz-route__caption">Подпись блока: карта корреспонденции Роспатента — три типа писем, три режима сроков, одна заявка.</p>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| Anchor id | `l24-boris-tz-route` |
| Класс секции | `l24-boris-tz-route` |
| Размещение | после H2 «Этапы регистрации…» / рядом с таблицей «трёх писем» в лонгриде |
| Композиция | split: SVG-карта + 3 карточки слева; матрица сроков справа |
| Метафора | продолжение «трёх писем» (запрос → уведомление → отказ → ППС) |

**Чеклист отличий от hero Алины**

- [x] Не hero: нет полноэкранной сцены, нет H1 страницы
- [x] Без `<canvas>` и `<script>` — только static SVG
- [x] Свой `id` секции: `l24-boris-tz-route` (не совпадает с hero)
- [x] Тёмная редакционная оболочка (split/grid), не узкий центрированный «квадратик»
- [x] Тема процедуры регистрации и корреспонденции Роспатента, не маркетплейс/иск
