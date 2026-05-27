=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Тема:** A13 UG — ст. 159/177 УК при долгах, гражданская граница  
**Slug:** `statya-159-177-uk-pri-dolgah-granica`  
**Режим:** контраст hero «весы / граница» — практическая **матрица событие → плоскость ответственности** (углубление, не дубль A7-таймлайна)  
**Якорь для Наташи:** `#boris-ug-matrix-a13`  
**Техника:** inline `<style>` + static SVG; без `<canvas>` и `<script>`

```html
<section id="boris-ug-matrix-a13" class="l24-boris-ug-matrix-a13" aria-label="Схема: событие при долге — гражданская ответственность, ст. 159, 159.1, 177 или налоги">
<style>
.l24-boris-ug-matrix-a13 {
  --ugm-navy: #0f2744;
  --ugm-navy-soft: #1a365d;
  --ugm-civil: #63b3ed;
  --ugm-159: #fc8181;
  --ugm-1591: #f6ad55;
  --ugm-177: #68d391;
  --ugm-tax: #b794f4;
  --ugm-warn: #ecc94b;
  --ugm-ink: #e2e8f0;
  --ugm-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ug-matrix-a13__shell {
  background: linear-gradient(148deg, var(--ugm-navy) 0%, #152a45 52%, var(--ugm-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--ugm-ink);
}
.l24-boris-ug-matrix-a13__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ugm-warn);
}
.l24-boris-ug-matrix-a13__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ug-matrix-a13__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ugm-muted);
  max-width: 66ch;
}
.l24-boris-ug-matrix-a13__lead strong { color: #fff; }
.l24-boris-ug-matrix-a13__split {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 0.98fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ug-matrix-a13__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ug-matrix-a13__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ugm-warn);
}
.l24-boris-ug-matrix-a13__tree-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 320px;
}
.l24-boris-ug-matrix-a13__routes {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 14px 0 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ug-matrix-a13__route {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-top: 3px solid var(--ugm-civil);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-ug-matrix-a13__route--159 { border-top-color: var(--ugm-159); }
.l24-boris-ug-matrix-a13__route--1591 { border-top-color: var(--ugm-1591); }
.l24-boris-ug-matrix-a13__route--177 { border-top-color: var(--ugm-177); }
.l24-boris-ug-matrix-a13__route--tax {
  grid-column: 1 / -1;
  border-top-color: var(--ugm-tax);
}
.l24-boris-ug-matrix-a13__route strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 3px;
}
.l24-boris-ug-matrix-a13__matrix {
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.l24-boris-ug-matrix-a13__row {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
  gap: 10px;
  align-items: start;
  padding: 11px 12px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border-left: 3px solid var(--ugm-civil);
  font-size: 0.76rem;
  line-height: 1.42;
}
.l24-boris-ug-matrix-a13__row--159 { border-left-color: var(--ugm-159); }
.l24-boris-ug-matrix-a13__row--1591 { border-left-color: var(--ugm-1591); }
.l24-boris-ug-matrix-a13__row--177 { border-left-color: var(--ugm-177); }
.l24-boris-ug-matrix-a13__row--tax { border-left-color: var(--ugm-tax); }
.l24-boris-ug-matrix-a13__row-event {
  color: #fff;
  font-weight: 600;
}
.l24-boris-ug-matrix-a13__row-plane {
  color: var(--ugm-muted);
}
.l24-boris-ug-matrix-a13__row-plane em {
  font-style: normal;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ug-matrix-a13__thresh {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 12px 0 0;
}
.l24-boris-ug-matrix-a13__thresh-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-ug-matrix-a13__thresh-card--177 { border-color: rgba(104, 211, 145, 0.45); }
.l24-boris-ug-matrix-a13__thresh-card--159 { border-color: rgba(252, 129, 129, 0.45); }
.l24-boris-ug-matrix-a13__thresh-label {
  display: block;
  font-size: 0.66rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ugm-muted);
  margin-bottom: 3px;
}
.l24-boris-ug-matrix-a13__thresh-value {
  font-size: 0.95rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-ug-matrix-a13__note {
  margin: 12px 0 0;
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--ugm-muted);
}
.l24-boris-ug-matrix-a13__note em {
  font-style: normal;
  color: var(--ugm-warn);
  font-weight: 600;
}
.l24-boris-ug-matrix-a13__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ug-matrix-a13__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: var(--ugm-ink);
}
.l24-boris-ug-matrix-a13__tag--civil { border: 1px solid var(--ugm-civil); color: #bee3f8; }
.l24-boris-ug-matrix-a13__tag--159 { border: 1px solid var(--ugm-159); color: #fed7d7; }
.l24-boris-ug-matrix-a13__tag--177 { border: 1px solid var(--ugm-177); color: #c6f6d5; }
.l24-boris-ug-matrix-a13__tag--warn { border: 1px solid var(--ugm-warn); color: #faf089; }
.l24-boris-ug-matrix-a13__caption {
  margin: 12px 0 0;
  font-size: 0.7rem;
  color: var(--ugm-muted);
  line-height: 1.4;
}
@media (max-width: 900px) {
  .l24-boris-ug-matrix-a13__split { grid-template-columns: 1fr; }
  .l24-boris-ug-matrix-a13__row { grid-template-columns: 1fr; }
  .l24-boris-ug-matrix-a13__thresh { grid-template-columns: 1fr; }
}
@media (max-width: 520px) {
  .l24-boris-ug-matrix-a13__routes { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-ug-matrix-a13__shell">
    <p class="l24-boris-ug-matrix-a13__eyebrow">УК РФ · Пленум ВС № 48 · ФЗ № 79‑ФЗ с 17.04.2024</p>
    <h3 class="l24-boris-ug-matrix-a13__title">Событие при долге → гражданка, ст. 159, 159.1 или 177</h3>
    <p class="l24-boris-ug-matrix-a13__lead">Просрочка сама по себе — <strong>не уголовка</strong>. Слева — развилка по факту: был ли обман <strong>до</strong> получения денег, есть ли судебный акт и злостное уклонение. Справа — та же логика строками: куда уходит спор и какие пороги действуют в <strong>2026</strong> (для ст. 177 — <strong>3,5 млн ₽</strong>, не устаревшие 2,25 млн).</p>

    <div class="l24-boris-ug-matrix-a13__split">
      <div class="l24-boris-ug-matrix-a13__panel">
        <p class="l24-boris-ug-matrix-a13__panel-title">Схема: событие → плоскость</p>
        <svg class="l24-boris-ug-matrix-a13__tree-svg" viewBox="0 0 560 268" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="a13-ugm-hub" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#d69e2e"/>
            </linearGradient>
          </defs>
          <!-- hub -->
          <rect x="200" y="8" width="160" height="44" rx="10" fill="url(#a13-ugm-hub)" stroke="#fff" stroke-width="1.5"/>
          <text x="280" y="28" text-anchor="middle" fill="#1a202c" font-size="10" font-weight="800">СОБЫТИЕ</text>
          <text x="280" y="42" text-anchor="middle" fill="#2d3748" font-size="8" font-weight="600">долг · займ · кредит · ИП</text>
          <!-- stems -->
          <line x1="280" y1="52" x2="280" y2="68" stroke="#a0aec0" stroke-width="2"/>
          <line x1="80" y1="68" x2="480" y2="68" stroke="#a0aec0" stroke-width="2"/>
          <line x1="80" y1="68" x2="80" y2="88" stroke="#63b3ed" stroke-width="2"/>
          <line x1="200" y1="68" x2="200" y2="88" stroke="#fc8181" stroke-width="2"/>
          <line x1="360" y1="68" x2="360" y2="88" stroke="#f6ad55" stroke-width="2"/>
          <line x1="480" y1="68" x2="480" y2="88" stroke="#68d391" stroke-width="2"/>
          <!-- civil -->
          <rect x="12" y="88" width="136" height="72" rx="8" fill="rgba(99,179,237,0.18)" stroke="#63b3ed" stroke-width="1.4"/>
          <text x="80" y="108" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="800">ГРАЖДАНКА</text>
          <text x="80" y="124" text-anchor="middle" fill="#e2e8f0" font-size="7.5" font-weight="600">не обманывал при выдаче</text>
          <text x="80" y="138" text-anchor="middle" fill="#a0aec0" font-size="7">иск · пристав · ст. 807 ГК</text>
          <text x="80" y="152" text-anchor="middle" fill="#a0aec0" font-size="7">просрочка ≠ ст. 159</text>
          <!-- 159 -->
          <rect x="132" y="88" width="136" height="72" rx="8" fill="rgba(252,129,129,0.16)" stroke="#fc8181" stroke-width="1.4"/>
          <text x="200" y="108" text-anchor="middle" fill="#fed7d7" font-size="9" font-weight="800">ст. 159</text>
          <text x="200" y="124" text-anchor="middle" fill="#e2e8f0" font-size="7.5" font-weight="600">обман / злоупотребление</text>
          <text x="200" y="138" text-anchor="middle" fill="#a0aec0" font-size="7">доверием ДО получения</text>
          <text x="200" y="152" text-anchor="middle" fill="#a0aec0" font-size="7">займ · расписка · схема</text>
          <!-- 159.1 -->
          <rect x="292" y="88" width="136" height="72" rx="8" fill="rgba(246,173,85,0.16)" stroke="#f6ad55" stroke-width="1.4"/>
          <text x="360" y="108" text-anchor="middle" fill="#fbd38d" font-size="9" font-weight="800">ст. 159.1</text>
          <text x="360" y="124" text-anchor="middle" fill="#e2e8f0" font-size="7.5" font-weight="600">кредит: ложные сведения</text>
          <text x="360" y="138" text-anchor="middle" fill="#a0aec0" font-size="7">без намерения возвращать</text>
          <text x="360" y="152" text-anchor="middle" fill="#a0aec0" font-size="7">не просрочка платежа</text>
          <!-- 177 -->
          <rect x="412" y="88" width="136" height="72" rx="8" fill="rgba(104,211,145,0.16)" stroke="#68d391" stroke-width="1.4"/>
          <text x="480" y="108" text-anchor="middle" fill="#c6f6d5" font-size="9" font-weight="800">ст. 177</text>
          <text x="480" y="124" text-anchor="middle" fill="#e2e8f0" font-size="7.5" font-weight="600">суд в силе + ИП</text>
          <text x="480" y="138" text-anchor="middle" fill="#a0aec0" font-size="7">злостное уклонение</text>
          <text x="480" y="152" text-anchor="middle" fill="#a0aec0" font-size="7">может платить · &gt; 3,5 млн</text>
          <!-- tax branch -->
          <line x1="280" y1="168" x2="280" y2="186" stroke="#b794f4" stroke-width="2" stroke-dasharray="4 3"/>
          <rect x="190" y="186" width="180" height="52" rx="8" fill="rgba(183,148,244,0.14)" stroke="#b794f4" stroke-width="1.2"/>
          <text x="280" y="206" text-anchor="middle" fill="#e9d8fd" font-size="8" font-weight="700">Недоимка бюджету → ст. 198–199</text>
          <text x="280" y="222" text-anchor="middle" fill="#a0aec0" font-size="7">не путать со ст. 177 · прямой умысел</text>
          <!-- legend -->
          <text x="280" y="258" text-anchor="middle" fill="#718096" font-size="7">Пленум 30.11.2017 № 48, п. 3–4 · умысел до передачи имущества</text>
        </svg>
        <ul class="l24-boris-ug-matrix-a13__routes">
          <li class="l24-boris-ug-matrix-a13__route">
            <strong>Гражданка</strong>
            Взял в долг, не вернул — без обмана при выдаче: ГПК, иск, пристав.
          </li>
          <li class="l24-boris-ug-matrix-a13__route l24-boris-ug-matrix-a13__route--159">
            <strong>ст. 159</strong>
            «Не собирался возвращать» до получения; крупный от 250&nbsp;001&nbsp;₽ (ч. 1–4).
          </li>
          <li class="l24-boris-ug-matrix-a13__route l24-boris-ug-matrix-a13__route--1591">
            <strong>ст. 159.1</strong>
            Кредит с ложными данными без намерения платить; иначе — ст. 176, не 159.1.
          </li>
          <li class="l24-boris-ug-matrix-a13__route l24-boris-ug-matrix-a13__route--177">
            <strong>ст. 177</strong>
            Акт суда + злостность + возможность платить; дознание ФССП.
          </li>
          <li class="l24-boris-ug-matrix-a13__route l24-boris-ug-matrix-a13__route--tax">
            <strong>198–199</strong>
            Налоговая недоимка с умыслом — отдельные пороги, не «долг по решению суда».
          </li>
        </ul>
      </div>

      <div class="l24-boris-ug-matrix-a13__panel">
        <p class="l24-boris-ug-matrix-a13__panel-title">Матрица ситуаций</p>
        <div class="l24-boris-ug-matrix-a13__matrix" role="table" aria-label="Событие и плоскость ответственности">
          <div class="l24-boris-ug-matrix-a13__row" role="row">
            <span class="l24-boris-ug-matrix-a13__row-event" role="cell">Взял в долг, не вернул без обмана</span>
            <span class="l24-boris-ug-matrix-a13__row-plane" role="cell"><em>ГПК</em> · иск · пристав · ст. 807 ГК</span>
          </div>
          <div class="l24-boris-ug-matrix-a13__row l24-boris-ug-matrix-a13__row--159" role="row">
            <span class="l24-boris-ug-matrix-a13__row-event" role="cell">Обман / не планировал возвращать до выдачи</span>
            <span class="l24-boris-ug-matrix-a13__row-plane" role="cell"><em>ст. 159</em> · полиция / СК</span>
          </div>
          <div class="l24-boris-ug-matrix-a13__row l24-boris-ug-matrix-a13__row--1591" role="row">
            <span class="l24-boris-ug-matrix-a13__row-event" role="cell">Кредит: ложь в анкете, не намерен возвращать</span>
            <span class="l24-boris-ug-matrix-a13__row-plane" role="cell"><em>ст. 159.1</em> · не просрочка</span>
          </div>
          <div class="l24-boris-ug-matrix-a13__row l24-boris-ug-matrix-a13__row--177" role="row">
            <span class="l24-boris-ug-matrix-a13__row-event" role="cell">Суд в силе, ИП, уклонение, может платить</span>
            <span class="l24-boris-ug-matrix-a13__row-plane" role="cell"><em>ст. 177</em> · долг &gt; 3,5 млн ₽</span>
          </div>
          <div class="l24-boris-ug-matrix-a13__row l24-boris-ug-matrix-a13__row--tax" role="row">
            <span class="l24-boris-ug-matrix-a13__row-event" role="cell">Недоимка перед бюджетом</span>
            <span class="l24-boris-ug-matrix-a13__row-plane" role="cell"><em>ст. 198–199</em> · не ст. 177</span>
          </div>
        </div>
        <div class="l24-boris-ug-matrix-a13__thresh">
          <div class="l24-boris-ug-matrix-a13__thresh-card l24-boris-ug-matrix-a13__thresh-card--159">
            <span class="l24-boris-ug-matrix-a13__thresh-label">ст. 159 ч. 1–4 · крупный / особо крупный</span>
            <span class="l24-boris-ug-matrix-a13__thresh-value">250 001 / 1 млн ₽</span>
          </div>
          <div class="l24-boris-ug-matrix-a13__thresh-card l24-boris-ug-matrix-a13__thresh-card--177">
            <span class="l24-boris-ug-matrix-a13__thresh-label">ст. 177 · крупный (79‑ФЗ)</span>
            <span class="l24-boris-ug-matrix-a13__thresh-value">&gt; 3,5 млн ₽</span>
          </div>
        </div>
        <p class="l24-boris-ug-matrix-a13__note"><em>3,5 млн ровно</em> — ещё не крупный размер по гл. 22. Ч. 5–7 ст. 159 (ИП/юрлица) — другие пороги: 250 тыс. / 4,5 / 18 млн. «Списание долгов» из СМС — не защита, а риск нового 159 (Пленум № 48, п. 21–22).</p>
      </div>
    </div>

    <div class="l24-boris-ug-matrix-a13__foot" aria-label="Ключевые различия статей">
      <span class="l24-boris-ug-matrix-a13__tag l24-boris-ug-matrix-a13__tag--civil">Гражданка — спор о долге</span>
      <span class="l24-boris-ug-matrix-a13__tag l24-boris-ug-matrix-a13__tag--159">159 / 159.1 — умысел до получения</span>
      <span class="l24-boris-ug-matrix-a13__tag l24-boris-ug-matrix-a13__tag--177">177 — после суда и ФССП</span>
      <span class="l24-boris-ug-matrix-a13__tag l24-boris-ug-matrix-a13__tag--warn">Не дублировать матрицу A7 — угол 159+177</span>
    </div>
    <p class="l24-boris-ug-matrix-a13__caption">Подпись блока: практическая карта «событие → ответственность» для лонгрида A13 — без калькулятора, с актуальными порогами 2026.</p>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| Anchor id | `boris-ug-matrix-a13` |
| Класс секции | `l24-boris-ug-matrix-a13` |
| Размещение | после H2 «Где проходит граница: гражданское взыскание или уголовное дело» (перед CTA / блоком «Возбуждение дела…») |
| Композиция | split: SVG-дерево «событие → 4 ветки» + карточки слева; матрица строк + пороги справа |
| Метафора | контраст hero «весы»: не абстрактная граница, а **развилка по факту** из research Артёма |

**Чеклист отличий от hero Алины**

- [x] Не hero: нет `min-height: 85vh`, нет H1 страницы и CTA-кнопки в блоке
- [x] Без `<canvas>` и `<script>` — только static SVG + inline CSS
- [x] Свой `id`: `boris-ug-matrix-a13` (не совпадает с hero; у A7 Boris был `l24-boris-ug-risk-track`)
- [x] Тёмная редакционная оболочка split/grid, не полноэкранная светлая сцена «весов»
- [x] Фокус A13: матрица **событие → гражданка / 159 / 159.1 / 177** (+ 198–199), порог 177 **3,5 млн** (79‑ФЗ), не таймлайн «просрочка → ФССП» как в A7
- [x] Узкий угол статьи: углубление 159/177, не полная «карта рисков» A7
