=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Тема:** A14 (ARB) — мировое соглашение в арбитраже  
**SLUG:** mirovoe-soglashenie-v-arbitrazhe-plyusy-riski  
**code:** A14  
**Режим:** контраст к hero Алины — тёмная редакционная сетка в теле лонгрида (не полноэкран, не canvas)  
**Якорь для Наташи:** `#ym-matrix-ms-arb`  
**Section id:** `#l24-boris-arb-ms-matrix`  
**Размещение:** после H2 «Когда мировое соглашение выгодно бизнесу» (2-я секция лонгрида), перед H2 «Плюсы мирового соглашения в арбитраже»  
**TOC-пункт для Наташи:** «Матрица мир vs суд · этапы утверждения» → `#ym-matrix-ms-arb`

## Чеклист отличий от hero (Алина)

- [x] Не hero — блок в теле статьи, `margin: 48px 0`, без `min-height: 88vh`
- [x] Свой section id: `l24-boris-arb-ms-matrix` (не пересекается с hero)
- [x] Только static SVG + inline CSS — **без** `<canvas>`, **без** `<script>`
- [x] Сплит/сетка: матрица «мир vs суд» + чек-лист этапов утверждения МС
- [x] Цвета бренда: `#1e3a8a`, `#a31830`
- [x] Якорь `#ym-matrix-ms-arb` на заголовке h3 внутри секции

## HTML (вставка для Наташи)

```html
<section id="l24-boris-arb-ms-matrix" class="l24-boris-arb-a14" aria-label="Мировое соглашение в арбитраже: матрица мир vs суд и этапы утверждения">
<style>
.l24-boris-arb-a14 {
  --a14-navy: #1e3a8a;
  --a14-navy-soft: #1e40af;
  --a14-accent: #a31830;
  --a14-accent-soft: #c53030;
  --a14-ink: #e2e8f0;
  --a14-muted: #94a3b8;
  --a14-say: #93c5fd;
  --a14-quiet: #fca5a5;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-arb-a14__shell {
  background: linear-gradient(152deg, #0f172a 0%, #1e293b 48%, #172554 100%);
  border: 1px solid rgba(30, 58, 138, 0.45);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(15, 23, 42, 0.38);
  color: var(--a14-ink);
}
.l24-boris-arb-a14__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #93c5fd;
}
.l24-boris-arb-a14__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-arb-a14__lead {
  margin: 0 0 20px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--a14-muted);
  max-width: 72ch;
}
.l24-boris-arb-a14__lead strong { color: #fff; }
.l24-boris-arb-a14__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  margin: 0 0 22px;
  padding: 0;
  list-style: none;
  font-size: 0.78rem;
  color: var(--a14-muted);
}
.l24-boris-arb-a14__legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0;
}
.l24-boris-arb-a14__legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}
.l24-boris-arb-a14__legend-dot--peace { background: var(--a14-navy-soft); box-shadow: 0 0 0 2px #93c5fd; }
.l24-boris-arb-a14__legend-dot--court { background: var(--a14-accent); box-shadow: 0 0 0 2px #fca5a5; }
.l24-boris-arb-a14__split {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 0.92fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-arb-a14__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-arb-a14__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #93c5fd;
}
.l24-boris-arb-a14__matrix-svg,
.l24-boris-arb-a14__steps-svg {
  display: block;
  width: 100%;
  height: auto;
}
.l24-boris-arb-a14__matrix-svg { max-height: 118px; margin-bottom: 14px; }
.l24-boris-arb-a14__steps-svg { max-height: 200px; margin-bottom: 14px; }
.l24-boris-arb-a14__matrix {
  display: grid;
  grid-template-columns: minmax(72px, 0.85fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 6px;
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-arb-a14__corner {
  padding: 8px 6px;
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--a14-muted);
  align-self: end;
}
.l24-boris-arb-a14__colhead {
  padding: 8px 10px;
  border-radius: 8px;
  font-size: 0.74rem;
  font-weight: 700;
  text-align: center;
}
.l24-boris-arb-a14__colhead--peace {
  background: rgba(30, 58, 138, 0.35);
  border: 1px solid rgba(147, 197, 253, 0.35);
  color: #bfdbfe;
}
.l24-boris-arb-a14__colhead--court {
  background: rgba(163, 24, 48, 0.28);
  border: 1px solid rgba(252, 165, 165, 0.35);
  color: #fecaca;
}
.l24-boris-arb-a14__rowhead {
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  font-weight: 700;
  color: #fff;
  font-size: 0.72rem;
  align-self: stretch;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
.l24-boris-arb-a14__rowhead span {
  display: block;
  margin-top: 3px;
  font-weight: 500;
  font-size: 0.64rem;
  color: var(--a14-muted);
}
.l24-boris-arb-a14__cell {
  padding: 10px 9px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.18);
  border-top: 3px solid var(--a14-navy-soft);
}
.l24-boris-arb-a14__cell--court { border-top-color: var(--a14-accent); }
.l24-boris-arb-a14__cell strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 3px;
}
.l24-boris-arb-a14__badge {
  display: inline-block;
  margin-bottom: 4px;
  padding: 2px 7px;
  border-radius: 999px;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}
.l24-boris-arb-a14__badge--plus {
  background: rgba(30, 58, 138, 0.45);
  color: #bfdbfe;
  border: 1px solid rgba(147, 197, 253, 0.4);
}
.l24-boris-arb-a14__badge--minus {
  background: rgba(163, 24, 48, 0.35);
  color: #fecaca;
  border: 1px solid rgba(252, 165, 165, 0.35);
}
.l24-boris-arb-a14__steps {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.l24-boris-arb-a14__step {
  display: grid;
  grid-template-columns: 28px minmax(0, 1fr);
  gap: 10px;
  align-items: start;
  margin: 0;
  padding: 10px 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border-left: 3px solid var(--a14-navy);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-arb-a14__step:nth-child(2) { border-left-color: #3b82f6; }
.l24-boris-arb-a14__step:nth-child(3) { border-left-color: #6366f1; }
.l24-boris-arb-a14__step:nth-child(4) { border-left-color: var(--a14-accent-soft); }
.l24-boris-arb-a14__step:nth-child(5) { border-left-color: var(--a14-accent); }
.l24-boris-arb-a14__step-num {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--a14-navy);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 700;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.l24-boris-arb-a14__step:nth-child(4) .l24-boris-arb-a14__step-num,
.l24-boris-arb-a14__step:nth-child(5) .l24-boris-arb-a14__step-num {
  background: var(--a14-accent);
}
.l24-boris-arb-a14__step strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 3px;
}
.l24-boris-arb-a14__step em {
  font-style: normal;
  color: #93c5fd;
  font-size: 0.66rem;
}
.l24-boris-arb-a14__nums {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin-top: 14px;
}
.l24-boris-arb-a14__num {
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(30, 58, 138, 0.22);
  border: 1px solid rgba(147, 197, 253, 0.2);
  text-align: center;
}
.l24-boris-arb-a14__num-label {
  display: block;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: var(--a14-muted);
  margin-bottom: 4px;
}
.l24-boris-arb-a14__num-value {
  display: block;
  font-size: 1.05rem;
  font-weight: 800;
  color: #fff;
}
.l24-boris-arb-a14__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-arb-a14__tag {
  font-size: 0.68rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(0, 0, 0, 0.25);
  color: var(--a14-muted);
}
.l24-boris-arb-a14__tag--139 { border: 1px solid var(--a14-navy-soft); color: #bfdbfe; }
.l24-boris-arb-a14__tag--141 { border: 1px solid #6366f1; color: #c7d2fe; }
.l24-boris-arb-a14__tag--142 { border: 1px solid var(--a14-accent); color: #fecaca; }
.l24-boris-arb-a14__caption {
  margin: 14px 0 0;
  font-size: 0.72rem;
  line-height: 1.45;
  color: var(--a14-muted);
}
@media (max-width: 760px) {
  .l24-boris-arb-a14__split { grid-template-columns: 1fr; }
  .l24-boris-arb-a14__matrix { grid-template-columns: 1fr; }
  .l24-boris-arb-a14__corner { display: none; }
  .l24-boris-arb-a14__colhead { text-align: left; }
  .l24-boris-arb-a14__rowhead { margin-top: 4px; }
  .l24-boris-arb-a14__nums { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-arb-a14__shell">
    <p class="l24-boris-arb-a14__eyebrow">АПК РФ · гл. 15 · ст. 139–142 · НК 333.40 · 2024–2026</p>
    <h3 class="l24-boris-arb-a14__title" id="ym-matrix-ms-arb">Матрица «мир vs суд» и пять шагов до утверждённого мирового</h3>
    <p class="l24-boris-arb-a14__lead">Слева — <strong>стратегический выбор</strong>: когда **мировое соглашение в арбитраже** выигрывает у решения суда по срокам, сумме и пошлине, а когда риски отказа в утверждении перевешивают компромисс. Справа — <strong>чек-лист процедуры</strong> по ст. 139–141 АПК: от проекта до исполнительного листа и возврата госпошлины.</p>

    <ul class="l24-boris-arb-a14__legend" aria-label="Легенда матрицы">
      <li class="l24-boris-arb-a14__legend-item"><span class="l24-boris-arb-a14__legend-dot l24-boris-arb-a14__legend-dot--peace" aria-hidden="true"></span> Мир — утверждённое МС (ст. 141–142 АПК)</li>
      <li class="l24-boris-arb-a14__legend-item"><span class="l24-boris-arb-a14__legend-dot l24-boris-arb-a14__legend-dot--court" aria-hidden="true"></span> Суд — решение / апелляция / кассация</li>
    </ul>

    <div class="l24-boris-arb-a14__split">
      <div class="l24-boris-arb-a14__panel">
        <p class="l24-boris-arb-a14__panel-title">Матрица: мир vs суд</p>
        <svg class="l24-boris-arb-a14__matrix-svg" viewBox="0 0 520 96" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="a14-peace-bar" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#1e3a8a"/>
              <stop offset="100%" stop-color="#3b82f6"/>
            </linearGradient>
            <linearGradient id="a14-court-bar" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#a31830"/>
              <stop offset="100%" stop-color="#e53e3e"/>
            </linearGradient>
          </defs>
          <rect x="0" y="8" width="520" height="28" rx="6" fill="rgba(255,255,255,0.06)"/>
          <rect x="0" y="8" width="340" height="28" rx="6" fill="url(#a14-peace-bar)" opacity="0.85"/>
          <text x="12" y="26" fill="#fff" font-size="9" font-weight="700">Мир: быстрее · гибче · возврат пошлины</text>
          <rect x="0" y="52" width="520" height="28" rx="6" fill="rgba(255,255,255,0.06)"/>
          <rect x="0" y="52" width="420" height="28" rx="6" fill="url(#a14-court-bar)" opacity="0.75"/>
          <text x="12" y="70" fill="#fff" font-size="9" font-weight="700">Суд: дольше · исход неопределён · полная пошлина</text>
          <text x="350" y="26" fill="#93c5fd" font-size="8" font-weight="600">~65%</text>
          <text x="430" y="70" fill="#fca5a5" font-size="8" font-weight="600">~80%</text>
        </svg>

        <div class="l24-boris-arb-a14__matrix" role="table" aria-label="Сравнение мирового соглашения и судебного решения">
          <div class="l24-boris-arb-a14__corner" role="columnheader">Критерий ↓</div>
          <div class="l24-boris-arb-a14__colhead l24-boris-arb-a14__colhead--peace" role="columnheader">Мир (МС)</div>
          <div class="l24-boris-arb-a14__colhead l24-boris-arb-a14__colhead--court" role="columnheader">Суд</div>

          <div class="l24-boris-arb-a14__rowhead" role="rowheader">Срок<span>до итога спора</span></div>
          <div class="l24-boris-arb-a14__cell" role="cell">
            <span class="l24-boris-arb-a14__badge l24-boris-arb-a14__badge--plus">Плюс</span>
            <strong>Недели–месяцы.</strong> Прекращение производства сразу после утверждения (ч. 13 ст. 141).
          </div>
          <div class="l24-boris-arb-a14__cell l24-boris-arb-a14__cell--court" role="cell">
            <span class="l24-boris-arb-a14__badge l24-boris-arb-a14__badge--minus">Минус</span>
            <strong>Месяцы–годы.</strong> Заседания, экспертизы, апелляция, кассация.
          </div>

          <div class="l24-boris-arb-a14__rowhead" role="rowheader">Сумма<span>и условия</span></div>
          <div class="l24-boris-arb-a14__cell" role="cell">
            <span class="l24-boris-arb-a14__badge l24-boris-arb-a14__badge--plus">Плюс</span>
            <strong>Компромисс.</strong> Рассрочка, прощение пени, распределение расходов (ст. 140).
          </div>
          <div class="l24-boris-arb-a14__cell l24-boris-arb-a14__cell--court" role="cell">
            <strong>«Всё или ничего».</strong> Суд в рамках иска и норм права; преюдиция по итогу.
          </div>

          <div class="l24-boris-arb-a14__rowhead" role="rowheader">Госпошлина<span>333.40 НК</span></div>
          <div class="l24-boris-arb-a14__cell" role="cell">
            <span class="l24-boris-arb-a14__badge l24-boris-arb-a14__badge--plus">Плюс</span>
            <strong>Возврат 70 / 50 / 30%</strong> — 1-я / апелляция / кассация.
          </div>
          <div class="l24-boris-arb-a14__cell l24-boris-arb-a14__cell--court" role="cell">
            <span class="l24-boris-arb-a14__badge l24-boris-arb-a14__badge--minus">Минус</span>
            <strong>Без возврата</strong> при решении в пользу истца; расходы на процесс.
          </div>

          <div class="l24-boris-arb-a14__rowhead" role="rowheader">Риски<span>до фиксации</span></div>
          <div class="l24-boris-arb-a14__cell" role="cell">
            <span class="l24-boris-arb-a14__badge l24-boris-arb-a14__badge--minus">Минус</span>
            <strong>Отказ в утверждении</strong> (ч. 6 ст. 141) — дело продолжается; ошибки в тексте → res judicata.
          </div>
          <div class="l24-boris-arb-a14__cell l24-boris-arb-a14__cell--court" role="cell">
            <strong>Неопределённый исход.</strong> Проигрыш, обеспечительные меры, публичность решения.
          </div>
        </div>
      </div>

      <div class="l24-boris-arb-a14__panel">
        <p class="l24-boris-arb-a14__panel-title">Чек-лист: утверждение МС</p>
        <svg class="l24-boris-arb-a14__steps-svg" viewBox="0 0 520 168" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="a14-step-line" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#1e3a8a"/>
              <stop offset="55%" stop-color="#6366f1"/>
              <stop offset="100%" stop-color="#a31830"/>
            </linearGradient>
          </defs>
          <line x1="32" y1="20" x2="32" y2="148" stroke="url(#a14-step-line)" stroke-width="3" stroke-linecap="round"/>
          <circle cx="32" cy="24" r="12" fill="#1e3a8a" stroke="#fff" stroke-width="2"/>
          <text x="32" y="28" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">1</text>
          <rect x="54" y="10" width="450" height="28" rx="6" fill="rgba(30,58,138,0.35)" stroke="#3b82f6"/>
          <text x="66" y="28" fill="#bfdbfe" font-size="8" font-weight="700">Проект МС + подписи (ст. 140 АПК)</text>
          <circle cx="32" cy="58" r="12" fill="#3b82f6" stroke="#fff" stroke-width="2"/>
          <text x="32" y="62" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">2</text>
          <rect x="54" y="44" width="450" height="28" rx="6" fill="rgba(59,130,246,0.2)" stroke="#6366f1"/>
          <text x="66" y="62" fill="#c7d2fe" font-size="8" font-weight="700">Ходатайство об утверждении (ч. 3 ст. 141)</text>
          <circle cx="32" cy="92" r="12" fill="#6366f1" stroke="#fff" stroke-width="2"/>
          <text x="32" y="96" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">3</text>
          <rect x="54" y="78" width="450" height="28" rx="6" fill="rgba(99,102,241,0.18)" stroke="#818cf8"/>
          <text x="66" y="96" fill="#e0e7ff" font-size="8" font-weight="700">Заседание · проверка законности (ч. 6–8)</text>
          <circle cx="32" cy="126" r="12" fill="#a31830" stroke="#fff" stroke-width="2"/>
          <text x="32" y="130" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">4</text>
          <rect x="54" y="112" width="218" height="28" rx="6" fill="rgba(30,58,138,0.4)" stroke="#93c5fd"/>
          <text x="66" y="130" fill="#bfdbfe" font-size="8" font-weight="700">Утверждение ✓</text>
          <rect x="286" y="112" width="218" height="28" rx="6" fill="rgba(163,24,48,0.35)" stroke="#fca5a5"/>
          <text x="298" y="130" fill="#fecaca" font-size="8" font-weight="700">Отказ → спор продолжается</text>
          <circle cx="32" cy="154" r="10" fill="#a31830" stroke="#fff" stroke-width="2"/>
          <text x="32" y="157" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">5</text>
          <rect x="54" y="146" width="450" height="18" rx="5" fill="rgba(163,24,48,0.22)" stroke="#a31830"/>
          <text x="66" y="158" fill="#fecaca" font-size="7.5" font-weight="600">ИЛ по заявлению (ст. 142) · возврат пошлины в ФНС</text>
        </svg>

        <ol class="l24-boris-arb-a14__steps" aria-label="Этапы утверждения мирового соглашения">
          <li class="l24-boris-arb-a14__step">
            <span class="l24-boris-arb-a14__step-num" aria-hidden="true">1</span>
            <div><strong>Проект и полномочия.</strong> Письменный текст, сумма и сроки; представитель — с полномочием на мировое. <em>ст. 140 АПК</em></div>
          </li>
          <li class="l24-boris-arb-a14__step">
            <span class="l24-boris-arb-a14__step-num" aria-hidden="true">2</span>
            <div><strong>Ходатайство в суд.</strong> Совместная подача; можно просить рассмотрение в отсутствие. <em>ч. 3 ст. 141</em></div>
          </li>
          <li class="l24-boris-arb-a14__step">
            <span class="l24-boris-arb-a14__step-num" aria-hidden="true">3</span>
            <div><strong>Заседание.</strong> Суд проверяет законность, не «справедливость»; незаконные условия — предложение убрать. <em>ч. 7–8 ст. 141</em></div>
          </li>
          <li class="l24-boris-arb-a14__step">
            <span class="l24-boris-arb-a14__step-num" aria-hidden="true">4</span>
            <div><strong>Определение.</strong> Утверждение → прекращение дела; отказ (нарушение прав третьих лиц, противоречие закону) → обжалование. <em>ч. 6, 12 ст. 141</em></div>
          </li>
          <li class="l24-boris-arb-a14__step">
            <span class="l24-boris-arb-a14__step-num" aria-hidden="true">5</span>
            <div><strong>После утверждения.</strong> Исполнительный лист при просрочке; заявление на возврат госпошлины. <em>ст. 142 АПК · п. 3 ст. 333.40 НК</em></div>
          </li>
        </ol>

        <div class="l24-boris-arb-a14__nums" aria-label="Возврат госпошлины по стадиям">
          <div class="l24-boris-arb-a14__num">
            <span class="l24-boris-arb-a14__num-label">1-я инстанция</span>
            <span class="l24-boris-arb-a14__num-value">70%</span>
          </div>
          <div class="l24-boris-arb-a14__num">
            <span class="l24-boris-arb-a14__num-label">Апелляция</span>
            <span class="l24-boris-arb-a14__num-value">50%</span>
          </div>
          <div class="l24-boris-arb-a14__num">
            <span class="l24-boris-arb-a14__num-label">Кассация</span>
            <span class="l24-boris-arb-a14__num-value">30%</span>
          </div>
        </div>
      </div>
    </div>

    <div class="l24-boris-arb-a14__foot" aria-label="Нормы и риски">
      <span class="l24-boris-arb-a14__tag l24-boris-arb-a14__tag--139">ст. 139: на любой стадии + при исполнении</span>
      <span class="l24-boris-arb-a14__tag l24-boris-arb-a14__tag--141">141: суд не редактирует условия</span>
      <span class="l24-boris-arb-a14__tag l24-boris-arb-a14__tag--142">142: ИЛ только после утверждения</span>
      <span class="l24-boris-arb-a14__tag">151 АПК: res judicata после мира</span>
    </div>
    <p class="l24-boris-arb-a14__caption">Схема к разделам о выгоде и порядке утверждения — не заменяет проверку проекта мирового и расчёт сценария «мир или суд» по конкретному арбитражному спору.</p>
  </div>
</section>
```

## Передача Наташе

- Вставить секцию **после** закрытия H2 «Когда мировое соглашение выгодно бизнесу», **перед** H2 «Плюсы мирового соглашения в арбитраже».
- В TOC добавить: `<li><a href="#ym-matrix-ms-arb">Матрица мир vs суд · этапы утверждения</a></li>`
- Класс страницы: `mirovoe-soglashenie-v-arbitrazhe-plyusy-riski-page` (или `{slug}-page` по шаблону A14).
- Canvas/script **не требуются** — только этот HTML-блок.
