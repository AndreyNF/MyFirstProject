=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Режим:** контраст к светлому hero Алины (витрина 159/177) → плотная тёмная карта риска в теле лонгрида.  
**Якорь для Наташи:** вставить сразу после абзаца с *«Сквозная шкала риска»* (конец H2 «Уголовная ответственность за долги: когда долг перестаёт быть только гражданским»), перед H2 «Мошенничество и статья 159 УК»; альтернатива — после вводного абзаца H2 «Статья 177 УК: злостное уклонение…».  
**ID секции:** `l24-boris-ug-risk-track` (не пересекается с hero Алины).

### Чеклист отличий от hero
- [x] Не первый экран, не fullscreen
- [x] Без `<canvas>` и `<script>` — только static SVG + CSS (образец A6)
- [x] Свой `id`: `l24-boris-ug-risk-track`
- [x] Контраст: тёмный inset (#0f2744) vs светлый hero
- [x] Сплит: таймлайн «Просрочка → суд → ФССП → ст. 177» + мини-сетка порогов 159 vs 177
- [x] `aria-label` и семантика `<section>`

---

```html
<section id="l24-boris-ug-risk-track" class="l24-boris-ug-risk" aria-label="Уголовные риски при долгах: путь к ст. 177 и пороги статей 159 и 177">
<style>
.l24-boris-ug-risk {
  --ug-navy: #0f2744;
  --ug-navy-soft: #1a365d;
  --ug-accent: #c53030;
  --ug-warn: #ecc94b;
  --ug-safe: #68d391;
  --ug-ink: #e2e8f0;
  --ug-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ug-risk__shell {
  background: linear-gradient(145deg, var(--ug-navy) 0%, #152a45 55%, var(--ug-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.22);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--ug-ink);
}
.l24-boris-ug-risk__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ug-warn);
}
.l24-boris-ug-risk__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.4rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ug-risk__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ug-muted);
  max-width: 62ch;
}
.l24-boris-ug-risk__lead strong { color: #fff; }
.l24-boris-ug-risk__split {
  display: grid;
  grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.95fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ug-risk__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ug-risk__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ug-warn);
}
.l24-boris-ug-risk__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 220px;
}
.l24-boris-ug-risk__steps {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin: 16px 0 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ug-risk__step {
  margin: 0;
  padding: 11px 8px;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  border-left: 3px solid var(--ug-accent);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-ug-risk__step:nth-child(2) { border-left-color: #ed8936; }
.l24-boris-ug-risk__step:nth-child(3) { border-left-color: var(--ug-warn); }
.l24-boris-ug-risk__step:nth-child(4) { border-left-color: var(--ug-safe); }
.l24-boris-ug-risk__step strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 4px;
}
.l24-boris-ug-risk__thresh-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin: 0 0 12px;
}
.l24-boris-ug-risk__thresh-card {
  padding: 12px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-ug-risk__thresh-card--177 {
  border-color: rgba(104, 211, 145, 0.4);
}
.l24-boris-ug-risk__thresh-card--159 {
  border-color: rgba(197, 48, 48, 0.45);
}
.l24-boris-ug-risk__thresh-card--vs {
  grid-column: 1 / -1;
  background: rgba(197, 48, 48, 0.12);
  border-color: rgba(236, 201, 75, 0.35);
}
.l24-boris-ug-risk__thresh-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ug-muted);
  margin-bottom: 4px;
}
.l24-boris-ug-risk__thresh-value {
  font-size: 1.02rem;
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}
.l24-boris-ug-risk__thresh-note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ug-muted);
}
.l24-boris-ug-risk__thresh-note em {
  font-style: normal;
  color: var(--ug-safe);
  font-weight: 600;
}
.l24-boris-ug-risk__vs-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin-top: 8px;
  font-size: 0.74rem;
  line-height: 1.4;
}
.l24-boris-ug-risk__vs-col {
  padding: 10px;
  border-radius: 6px;
  background: rgba(0, 0, 0, 0.25);
}
.l24-boris-ug-risk__vs-col--159 { border-top: 2px solid var(--ug-accent); }
.l24-boris-ug-risk__vs-col--177 { border-top: 2px solid var(--ug-safe); }
.l24-boris-ug-risk__vs-col strong {
  display: block;
  color: #fff;
  font-size: 0.8rem;
  margin-bottom: 4px;
}
.l24-boris-ug-risk__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ug-risk__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: var(--ug-ink);
}
.l24-boris-ug-risk__tag--159 { border: 1px solid var(--ug-accent); color: #feb2b2; }
.l24-boris-ug-risk__tag--177 { border: 1px solid var(--ug-safe); color: #9ae6b4; }
@media (max-width: 900px) {
  .l24-boris-ug-risk__split { grid-template-columns: 1fr; }
  .l24-boris-ug-risk__steps { grid-template-columns: 1fr 1fr; }
  .l24-boris-ug-risk__thresh-grid { grid-template-columns: 1fr; }
  .l24-boris-ug-risk__vs-row { grid-template-columns: 1fr; }
}
@media (max-width: 520px) {
  .l24-boris-ug-risk__steps { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-ug-risk__shell">
    <p class="l24-boris-ug-risk__eyebrow">УК РФ · ст. 159 / 159.1 / 177 · 2025–2026</p>
    <h3 class="l24-boris-ug-risk__title">Просрочка → суд → ФССП → ст. 177: где включается уголовка</h3>
    <p class="l24-boris-ug-risk__lead">Обычная <strong>просрочка</strong> остаётся гражданкой. Цепочка к <strong>ст. 177</strong> — только после <strong>решения суда</strong>, исполнительного производства у приставов и <strong>злостного</strong> уклонения при сумме <strong>свыше 2&nbsp;250&nbsp;000&nbsp;₽</strong>. Слева — маршрут; справа — пороги и отличие от <strong>ст. 159</strong> (обман до получения денег).</p>

    <div class="l24-boris-ug-risk__split">
      <div class="l24-boris-ug-risk__panel">
        <p class="l24-boris-ug-risk__panel-title">Маршрут должника</p>
        <svg class="l24-boris-ug-risk__timeline-svg" viewBox="0 0 560 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="ug-risk-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#a0aec0"/>
              <stop offset="35%" stop-color="#ed8936"/>
              <stop offset="65%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
          </defs>
          <line x1="40" y1="72" x2="520" y2="72" stroke="url(#ug-risk-line)" stroke-width="4" stroke-linecap="round"/>
          <circle cx="64" cy="72" r="20" fill="#4a5568" stroke="#fff" stroke-width="2"/>
          <text x="64" y="77" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">0</text>
          <circle cx="200" cy="72" r="20" fill="#c05621" stroke="#fff" stroke-width="2"/>
          <text x="200" y="77" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">⚖</text>
          <circle cx="336" cy="72" r="20" fill="#d69e2e" stroke="#fff" stroke-width="2"/>
          <text x="336" y="76" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="700">ФССП</text>
          <circle cx="496" cy="72" r="22" fill="#c53030" stroke="#ecc94b" stroke-width="2"/>
          <text x="496" y="77" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">177</text>
          <text x="64" y="38" text-anchor="middle" fill="#cbd5e0" font-size="9" font-weight="600">Просрочка</text>
          <text x="200" y="38" text-anchor="middle" fill="#fbd38d" font-size="9" font-weight="600">Суд / приказ</text>
          <text x="336" y="38" text-anchor="middle" fill="#faf089" font-size="9" font-weight="600">ИП</text>
          <text x="496" y="38" text-anchor="middle" fill="#feb2b2" font-size="9" font-weight="600">ст. 177 УК</text>
          <rect x="12" y="108" width="118" height="28" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="71" y="126" text-anchor="middle" fill="#e2e8f0" font-size="8">гражданка</text>
          <rect x="148" y="108" width="118" height="28" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="207" y="126" text-anchor="middle" fill="#e2e8f0" font-size="8">10 дн. отмена приказа</text>
          <rect x="284" y="108" width="118" height="28" rx="5" fill="rgba(0,0,0,0.35)"/>
          <text x="343" y="126" text-anchor="middle" fill="#e2e8f0" font-size="8">предупреждение</text>
          <rect x="420" y="108" width="130" height="28" rx="5" fill="rgba(197,48,48,0.35)"/>
          <text x="485" y="126" text-anchor="middle" fill="#fed7d7" font-size="8">&gt; 2,25 млн + злость</text>
        </svg>
        <ol class="l24-boris-ug-risk__steps">
          <li class="l24-boris-ug-risk__step">
            <strong>Просрочка</strong>
            Кредит, расписка, МФО — взыскание по договору, без ст. 177.
          </li>
          <li class="l24-boris-ug-risk__step">
            <strong>Суд</strong>
            Иск, судебный приказ; игнор суда — мост к ИП и рискам формулировок.
          </li>
          <li class="l24-boris-ug-risk__step">
            <strong>ФССП</strong>
            Исполнительное производство: арест, запрет выезда; рапорт / заявление кредитора.
          </li>
          <li class="l24-boris-ug-risk__step">
            <strong>ст. 177</strong>
            После акта в силу — злостное уклонение при возможности платить.
          </li>
        </ol>
      </div>

      <div class="l24-boris-ug-risk__panel">
        <p class="l24-boris-ug-risk__panel-title">Пороги: 2,25 млн и 159 vs 177</p>
        <div class="l24-boris-ug-risk__thresh-grid">
          <div class="l24-boris-ug-risk__thresh-card l24-boris-ug-risk__thresh-card--177">
            <span class="l24-boris-ug-risk__thresh-label">ст. 177 · крупный размер</span>
            <span class="l24-boris-ug-risk__thresh-value">&gt; 2,25 млн ₽</span>
          </div>
          <div class="l24-boris-ug-risk__thresh-card l24-boris-ug-risk__thresh-card--159">
            <span class="l24-boris-ug-risk__thresh-label">ст. 159 · крупный / особо крупный</span>
            <span class="l24-boris-ug-risk__thresh-value">250 001 / 1 млн ₽</span>
          </div>
          <div class="l24-boris-ug-risk__thresh-card l24-boris-ug-risk__thresh-card--vs">
            <span class="l24-boris-ug-risk__thresh-label">159 vs 177 — не путать</span>
            <div class="l24-boris-ug-risk__vs-row">
              <div class="l24-boris-ug-risk__vs-col l24-boris-ug-risk__vs-col--159">
                <strong>ст. 159 / 159.1</strong>
                Обман или злоупотребление доверием <em>до</em> получения денег; ложный кредит без намерения вернуть (ППВС № 48, п. 13).
              </div>
              <div class="l24-boris-ug-risk__vs-col l24-boris-ug-risk__vs-col--177">
                <strong>ст. 177</strong>
                Решение суда в силе + злостность + сумма по исп. документу <em>свыше</em> 2,25 млн; дознаватели ФССП.
              </div>
            </div>
          </div>
        </div>
        <p class="l24-boris-ug-risk__thresh-note"><em>2,25 млн ровно</em> — ещё не крупный размер по гл. 22 УК. Налоги — <strong>ст. 198–199</strong>, не 177. Просрочка кредита без суда — не «посадка за неплатёж».</p>
      </div>
    </div>

    <div class="l24-boris-ug-risk__foot" aria-label="Ключевые статьи материала">
      <span class="l24-boris-ug-risk__tag l24-boris-ug-risk__tag--159">159 / 159.1 — умысел при получении</span>
      <span class="l24-boris-ug-risk__tag l24-boris-ug-risk__tag--177">177 — после суда и ФССП</span>
      <span class="l24-boris-ug-risk__tag">198–199 — долг бюджету, другие пороги</span>
    </div>
  </div>
</section>
```

**Паспорт блока (для Наташи):** slug `ugolovnye-riski-pri-dolgah-chto-vazhno-znat`; тип UG / A7; визуализирует сквозную шкалу из лонгрида Жени и матрицу Артёма; цифры: **&gt; 2&nbsp;250&nbsp;000 ₽** (177), **250&nbsp;001 / 1&nbsp;000&nbsp;001 ₽** (159), **10 дней** на отмену приказа, предупреждение пристава (ФССП 03.10.2016); без canvas/script.
