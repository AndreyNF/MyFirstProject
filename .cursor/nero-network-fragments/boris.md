=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Тема:** B1 (ARB) — Арбитражный процессуальный срок: как не пропустить подачу и возражения  
**SLUG:** `arbitrazhnyj-processualnyj-srok-podacha`  
**code:** B1  
**Режим:** контраст к hero — тёмная редакционная сетка «календарь сроков» в теле лонгрида (не полноэкран, не canvas)  
**Якорь для Наташи:** `#ym-matrix-srok-arb`  
**Section id:** `#l24-boris-arb-srok-matrix`  
**Размещение:** после H2 «Сроки подачи иска, отзыва и процессуальных документов в первой инстанции», перед H2 «Сроки обжалования и возражений»  
**TOC-пункт для Наташи:** «Матрица сроков: претензия → отзыв → обжалование» → `#ym-matrix-srok-arb`

## Чеклист отличий от hero (Алина)

- [x] Не hero — блок в теле статьи, `margin: 48px 0`, без `min-height: 88vh`
- [x] Свой section id: `l24-boris-arb-srok-matrix` (не пересекается с hero)
- [x] Только static SVG + inline CSS — **без** `<canvas>`, **без** `<script>`
- [x] Сплит/сетка: горизонтальный таймлайн + матрица этапов + линия +6 мес восстановления
- [x] Цвета бренда: `#1e3a8a`, `#a31830`
- [x] Якорь `#ym-matrix-srok-arb` на заголовке h3 внутри секции

## HTML (вставка для Наташи)

```html
<section id="l24-boris-arb-srok-matrix" class="l24-boris-arb-b1" aria-label="Матрица и таймлайн арбитражных процессуальных сроков по АПК">
<style>
.l24-boris-arb-b1 {
  --b1-navy: #1e3a8a;
  --b1-navy-soft: #1e40af;
  --b1-accent: #a31830;
  --b1-accent-soft: #c53030;
  --b1-ink: #e2e8f0;
  --b1-muted: #94a3b8;
  --b1-warn: #fbbf24;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-arb-b1__shell {
  background: linear-gradient(152deg, #0f172a 0%, #1e293b 48%, #172554 100%);
  border: 1px solid rgba(30, 58, 138, 0.45);
  border-radius: 14px;
  padding: 32px 28px 28px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(15, 23, 42, 0.38);
  color: var(--b1-ink);
}
.l24-boris-arb-b1__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #93c5fd;
}
.l24-boris-arb-b1__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-arb-b1__lead {
  margin: 0 0 20px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--b1-muted);
  max-width: 72ch;
}
.l24-boris-arb-b1__lead strong { color: #fff; }
.l24-boris-arb-b1__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  margin: 0 0 22px;
  padding: 0;
  list-style: none;
  font-size: 0.78rem;
  color: var(--b1-muted);
}
.l24-boris-arb-b1__legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  margin: 0;
}
.l24-boris-arb-b1__legend-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}
.l24-boris-arb-b1__legend-dot--flow { background: var(--b1-navy-soft); box-shadow: 0 0 0 2px #93c5fd; }
.l24-boris-arb-b1__legend-dot--branch { background: #6366f1; box-shadow: 0 0 0 2px #c7d2fe; }
.l24-boris-arb-b1__legend-dot--restore {
  width: 18px;
  height: 0;
  border-radius: 0;
  border-top: 2px dashed var(--b1-warn);
  background: transparent;
  box-shadow: none;
}
.l24-boris-arb-b1__timeline-wrap {
  margin-bottom: 22px;
  padding: 18px 16px 14px;
  border-radius: 10px;
  background: rgba(0, 0, 0, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-arb-b1__timeline-label {
  margin: 0 0 10px;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #93c5fd;
}
.l24-boris-arb-b1__timeline-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 132px;
}
.l24-boris-arb-b1__split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-arb-b1__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-arb-b1__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: #93c5fd;
}
.l24-boris-arb-b1__confusion {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
  margin: 0 0 14px;
  padding: 0;
  list-style: none;
}
.l24-boris-arb-b1__conf-item {
  margin: 0;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(251, 191, 36, 0.08);
  border-left: 3px solid var(--b1-warn);
  font-size: 0.72rem;
  line-height: 1.42;
}
.l24-boris-arb-b1__conf-item strong {
  display: block;
  color: #fde68a;
  font-size: 0.76rem;
  margin-bottom: 3px;
}
.l24-boris-arb-b1__matrix {
  display: grid;
  grid-template-columns: minmax(88px, 0.9fr) minmax(0, 0.75fr) minmax(0, 1fr) minmax(0, 0.85fr);
  gap: 5px;
  font-size: 0.7rem;
  line-height: 1.36;
}
.l24-boris-arb-b1__mhead {
  padding: 7px 8px;
  font-size: 0.64rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--b1-muted);
  background: rgba(0, 0, 0, 0.25);
  border-radius: 6px;
}
.l24-boris-arb-b1__mrow {
  display: contents;
}
.l24-boris-arb-b1__mcell {
  padding: 9px 8px;
  border-radius: 6px;
  background: rgba(0, 0, 0, 0.18);
  align-self: stretch;
}
.l24-boris-arb-b1__mcell--stage {
  font-weight: 700;
  color: #fff;
  border-left: 3px solid var(--b1-navy-soft);
}
.l24-boris-arb-b1__mrow:nth-child(3) .l24-boris-arb-b1__mcell--stage { border-left-color: #3b82f6; }
.l24-boris-arb-b1__mrow:nth-child(4) .l24-boris-arb-b1__mcell--stage { border-left-color: #6366f1; }
.l24-boris-arb-b1__mrow:nth-child(5) .l24-boris-arb-b1__mcell--stage { border-left-color: #818cf8; }
.l24-boris-arb-b1__mrow:nth-child(6) .l24-boris-arb-b1__mcell--stage { border-left-color: var(--b1-accent-soft); }
.l24-boris-arb-b1__mrow:nth-child(7) .l24-boris-arb-b1__mcell--stage { border-left-color: var(--b1-accent); }
.l24-boris-arb-b1__mcell--term strong {
  display: block;
  color: #fff;
  font-size: 0.82rem;
  font-weight: 800;
}
.l24-boris-arb-b1__mcell--term span {
  font-size: 0.64rem;
  color: #93c5fd;
}
.l24-boris-arb-b1__mcell--restore {
  color: #fde68a;
  font-size: 0.66rem;
}
.l24-boris-arb-b1__restore-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 56px;
  margin-top: 12px;
}
.l24-boris-arb-b1__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}
.l24-boris-arb-b1__tag {
  font-size: 0.68rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(0, 0, 0, 0.25);
  color: var(--b1-muted);
}
.l24-boris-arb-b1__tag--4 { border: 1px solid var(--b1-navy-soft); color: #bfdbfe; }
.l24-boris-arb-b1__tag--131 { border: 1px solid #3b82f6; color: #bfdbfe; }
.l24-boris-arb-b1__tag--228 { border: 1px solid #6366f1; color: #c7d2fe; }
.l24-boris-arb-b1__tag--259 { border: 1px solid var(--b1-accent-soft); color: #fecaca; }
.l24-boris-arb-b1__tag--117 { border: 1px solid var(--b1-warn); color: #fde68a; }
.l24-boris-arb-b1__caption {
  margin: 14px 0 0;
  font-size: 0.72rem;
  line-height: 1.45;
  color: var(--b1-muted);
}
@media (max-width: 820px) {
  .l24-boris-arb-b1__split { grid-template-columns: 1fr; }
  .l24-boris-arb-b1__matrix {
    grid-template-columns: 1fr 1fr;
  }
  .l24-boris-arb-b1__mhead:nth-child(3),
  .l24-boris-arb-b1__mhead:nth-child(4) { display: none; }
  .l24-boris-arb-b1__mrow .l24-boris-arb-b1__mcell:nth-child(3)::before {
    content: "Начало: ";
    color: var(--b1-muted);
    font-weight: 600;
  }
  .l24-boris-arb-b1__mrow .l24-boris-arb-b1__mcell:nth-child(4)::before {
    content: "Восстановление: ";
    color: var(--b1-muted);
    font-weight: 600;
  }
}
</style>

  <div class="l24-boris-arb-b1__shell">
    <p class="l24-boris-arb-b1__eyebrow">АПК РФ · ст. 4 · 131 · 228 · 259 · 276 · 117 · Пленум ВАС № 99</p>
    <h3 class="l24-boris-arb-b1__title" id="ym-matrix-srok-arb">Матрица сроков: от претензии до кассации и предел +6 месяцев</h3>
    <p class="l24-boris-arb-b1__lead">Горизонтальный <strong>таймлайн</strong> — типовая цепочка для бизнеса: досудебная претензия → отзыв в суде → апелляция → кассация. Справа — <strong>матрица</strong> с началом течения и лимитом восстановления; пунктир — «окно» до <strong>6 месяцев</strong> по ст. 117, 259, 276 АПК.</p>

    <ul class="l24-boris-arb-b1__legend" aria-label="Легенда схемы">
      <li class="l24-boris-arb-b1__legend-item"><span class="l24-boris-arb-b1__legend-dot l24-boris-arb-b1__legend-dot--flow" aria-hidden="true"></span> Основной процессуальный срок</li>
      <li class="l24-boris-arb-b1__legend-item"><span class="l24-boris-arb-b1__legend-dot l24-boris-arb-b1__legend-dot--branch" aria-hidden="true"></span> Ветка УП: 15 / 30 дней (ст. 228)</li>
      <li class="l24-boris-arb-b1__legend-item"><span class="l24-boris-arb-b1__legend-dot l24-boris-arb-b1__legend-dot--restore" aria-hidden="true"></span> Предел восстановления (≤ 6 мес.)</li>
    </ul>

    <div class="l24-boris-arb-b1__timeline-wrap">
      <p class="l24-boris-arb-b1__timeline-label">Таймлайн этапов</p>
      <svg class="l24-boris-arb-b1__timeline-svg" viewBox="0 0 720 128" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="b1-tl-title b1-tl-desc">
        <title id="b1-tl-title">Цепочка арбитражных процессуальных сроков</title>
        <desc id="b1-tl-desc">Претензия 30 календарных дней, отзыв 15 или 30 дней, апелляция 1 месяц, кассация 2 месяца, линия восстановления до 6 месяцев</desc>
        <defs>
          <linearGradient id="b1-flow" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="35%" stop-color="#3b82f6"/>
            <stop offset="65%" stop-color="#6366f1"/>
            <stop offset="100%" stop-color="#a31830"/>
          </linearGradient>
        </defs>
        <!-- базовая ось -->
        <line x1="48" y1="52" x2="672" y2="52" stroke="url(#b1-flow)" stroke-width="4" stroke-linecap="round"/>
        <!-- линия +6 мес восстановления -->
        <line x1="380" y1="98" x2="672" y2="98" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6 5" opacity="0.9"/>
        <text x="382" y="118" fill="#fde68a" font-size="7.5" font-weight="600">+6 мес. — предел восстановления (ст. 117, 259, 276)</text>
        <!-- узел 1: претензия -->
        <circle cx="56" cy="52" r="14" fill="#1e3a8a" stroke="#fff" stroke-width="2"/>
        <text x="56" y="56" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">1</text>
        <rect x="12" y="8" width="88" height="34" rx="6" fill="rgba(30,58,138,0.45)" stroke="#3b82f6"/>
        <text x="56" y="22" text-anchor="middle" fill="#bfdbfe" font-size="7" font-weight="700">Претензия</text>
        <text x="56" y="34" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">30 к.д.</text>
        <text x="56" y="78" text-anchor="middle" fill="#94a3b8" font-size="6.5">ч. 5 ст. 4</text>
        <!-- узел 2: отзыв 15/30 -->
        <circle cx="208" cy="52" r="14" fill="#3b82f6" stroke="#fff" stroke-width="2"/>
        <text x="208" y="56" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">2</text>
        <rect x="148" y="8" width="120" height="34" rx="6" fill="rgba(59,130,246,0.28)" stroke="#6366f1"/>
        <text x="208" y="22" text-anchor="middle" fill="#c7d2fe" font-size="7" font-weight="700">Отзыв</text>
        <text x="208" y="34" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">15 / 30</text>
        <text x="208" y="78" text-anchor="middle" fill="#94a3b8" font-size="6.5">131 · 228</text>
        <!-- ветка УП -->
        <path d="M 208 66 L 208 82 L 168 82" fill="none" stroke="#818cf8" stroke-width="1.5"/>
        <text x="132" y="86" text-anchor="end" fill="#a5b4fc" font-size="6">УП ≥15</text>
        <path d="M 208 66 L 248 82" fill="none" stroke="#818cf8" stroke-width="1.5"/>
        <text x="252" y="86" fill="#a5b4fc" font-size="6">доп. ≥30</text>
        <!-- узел 3: апелляция -->
        <circle cx="380" cy="52" r="14" fill="#6366f1" stroke="#fff" stroke-width="2"/>
        <text x="380" y="56" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">3</text>
        <rect x="318" y="8" width="124" height="34" rx="6" fill="rgba(99,102,241,0.3)" stroke="#818cf8"/>
        <text x="380" y="22" text-anchor="middle" fill="#e0e7ff" font-size="7" font-weight="700">Апелляция</text>
        <text x="380" y="34" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">1 мес.</text>
        <text x="380" y="78" text-anchor="middle" fill="#94a3b8" font-size="6.5">ст. 259</text>
        <!-- маркер начала +6 от апелляции -->
        <circle cx="380" cy="98" r="4" fill="#fbbf24"/>
        <!-- узел 4: кассация -->
        <circle cx="552" cy="52" r="14" fill="#a31830" stroke="#fff" stroke-width="2"/>
        <text x="552" y="56" text-anchor="middle" fill="#fff" font-size="7" font-weight="700">4</text>
        <rect x="490" y="8" width="124" height="34" rx="6" fill="rgba(163,24,48,0.35)" stroke="#fca5a5"/>
        <text x="552" y="22" text-anchor="middle" fill="#fecaca" font-size="7" font-weight="700">Кассация</text>
        <text x="552" y="34" text-anchor="middle" fill="#fff" font-size="9" font-weight="800">2 мес.</text>
        <text x="552" y="78" text-anchor="middle" fill="#94a3b8" font-size="6.5">ст. 276</text>
        <circle cx="552" cy="98" r="4" fill="#fbbf24"/>
        <!-- финиш: безвозврат -->
        <circle cx="672" cy="98" r="5" fill="none" stroke="#fca5a5" stroke-width="2"/>
        <text x="684" y="101" fill="#fca5a5" font-size="7" font-weight="700">далее — нет</text>
        <!-- стрелка к суду -->
        <polygon points="120,52 132,46 132,58" fill="#3b82f6"/>
        <text x="124" y="44" text-anchor="middle" fill="#64748b" font-size="6">иск</text>
      </svg>
    </div>

    <div class="l24-boris-arb-b1__split">
      <div class="l24-boris-arb-b1__panel">
        <p class="l24-boris-arb-b1__panel-title">Типовая ошибка: 30 vs 15</p>
        <ul class="l24-boris-arb-b1__confusion" aria-label="Различие 30 и 15 дней">
          <li class="l24-boris-arb-b1__conf-item">
            <strong>30 календарных дней</strong>
            Ответ на <em>претензию</em> до суда (досудебный порядок), не срок отзыва в арбитраже. ч. 5 ст. 4 АПК.
          </li>
          <li class="l24-boris-arb-b1__conf-item">
            <strong>15 дней (минимум)</strong>
            Отзыв и доказательства в <em>упрощённом</em> производстве — с определения о принятии. ч. 2 ст. 228 АПК.
          </li>
          <li class="l24-boris-arb-b1__conf-item">
            <strong>30 дней (минимум)</strong>
            Второй этап УП — дополнительные документы; опоздание → возврат без рассмотрения. ч. 3–4 ст. 228 АПК.
          </li>
        </ul>
        <svg class="l24-boris-arb-b1__restore-svg" viewBox="0 0 360 48" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <rect x="0" y="14" width="360" height="20" rx="8" fill="rgba(251,191,36,0.12)" stroke="#fbbf24" stroke-dasharray="4 3"/>
          <text x="12" y="28" fill="#fde68a" font-size="8" font-weight="700">Окно восстановления: уважительные причины + ходатайство одновременно с действием</text>
          <text x="12" y="40" fill="#94a3b8" font-size="7">ст. 117 АПК · рассмотрение ходатайства — 5 дней</text>
        </svg>
      </div>

      <div class="l24-boris-arb-b1__panel">
        <p class="l24-boris-arb-b1__panel-title">Матрица: срок · начало · восстановление</p>
        <div class="l24-boris-arb-b1__matrix" role="table" aria-label="Матрица арбитражных процессуальных сроков">
          <div class="l24-boris-arb-b1__mhead" role="columnheader">Этап</div>
          <div class="l24-boris-arb-b1__mhead" role="columnheader">Срок</div>
          <div class="l24-boris-arb-b1__mhead" role="columnheader">Начало течения</div>
          <div class="l24-boris-arb-b1__mhead" role="columnheader">Предел восстановления</div>

          <div class="l24-boris-arb-b1__mrow" role="row">
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--stage" role="rowheader">Претензия</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--term" role="cell"><strong>30</strong><span>календ. дней</span></div>
            <div class="l24-boris-arb-b1__mcell" role="cell">Вручение / получение претензии; иное в договоре</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--restore" role="cell">—</div>
          </div>
          <div class="l24-boris-arb-b1__mrow" role="row">
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--stage" role="rowheader">Отзыв (обычное)</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--term" role="cell"><strong>15–30</strong><span>в определении</span></div>
            <div class="l24-boris-arb-b1__mcell" role="cell">Определение о принятии иска (ст. 127, 131)</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--restore" role="cell">Продление судом (ст. 118); пропуск → риск без отзыва</div>
          </div>
          <div class="l24-boris-arb-b1__mrow" role="row">
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--stage" role="rowheader">Отзыв (УП)</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--term" role="cell"><strong>≥15</strong><span>и ≥30 доп.</span></div>
            <div class="l24-boris-arb-b1__mcell" role="cell">Определение о принятии (ст. 228)</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--restore" role="cell">Жёстко: опоздание → возврат (ч. 4)</div>
          </div>
          <div class="l24-boris-arb-b1__mrow" role="row">
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--stage" role="rowheader">Апелляция</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--term" role="cell"><strong>1 мес.</strong><span>рабочие дни</span></div>
            <div class="l24-boris-arb-b1__mcell" role="cell">Со дня принятия решения 1 инстанции (ст. 259)</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--restore" role="cell">≤ 6 мес. с принятия решения (ч. 2 ст. 259)</div>
          </div>
          <div class="l24-boris-arb-b1__mrow" role="row">
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--stage" role="rowheader">Кассация</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--term" role="cell"><strong>2 мес.</strong><span>округ / ВС</span></div>
            <div class="l24-boris-arb-b1__mcell" role="cell">Вступление акта в законную силу (ст. 276, 291.2)</div>
            <div class="l24-boris-arb-b1__mcell l24-boris-arb-b1__mcell--restore" role="cell">≤ 6 мес. (ч. 2 ст. 276, 291.2)</div>
          </div>
        </div>
      </div>
    </div>

    <div class="l24-boris-arb-b1__foot" aria-label="Нормы АПК">
      <span class="l24-boris-arb-b1__tag l24-boris-arb-b1__tag--4">ст. 4: претензия 30 к.д.</span>
      <span class="l24-boris-arb-b1__tag l24-boris-arb-b1__tag--131">131: отзыв — срок в определении</span>
      <span class="l24-boris-arb-b1__tag l24-boris-arb-b1__tag--228">228: УП 15 / 30</span>
      <span class="l24-boris-arb-b1__tag l24-boris-arb-b1__tag--259">259 · 276: 1 мес. · 2 мес.</span>
      <span class="l24-boris-arb-b1__tag l24-boris-arb-b1__tag--117">117: восстановление + действие</span>
      <span class="l24-boris-arb-b1__tag">«Мой арбитр» до 24:00 МСК</span>
    </div>
    <p class="l24-boris-arb-b1__caption">Схема к разделам о подаче, отзыве и обжаловании — не заменяет сверку сроков по определению суда и КАД по конкретному делу.</p>
  </div>
</section>
```

## Передача Наташе

- Вставить секцию **после** H2 «Сроки подачи иска, отзыва и процессуальных документов в первой инстанции», **перед** H2 «Сроки обжалования и возражений».
- В TOC добавить: `<li><a href="#ym-matrix-srok-arb">Матрица сроков: претензия → отзыв → обжалование</a></li>`
- Класс страницы: `arbitrazhnyj-processualnyj-srok-podacha-page` (или `{slug}-page` по шаблону B1).
- Canvas/script **не требуются** — только этот HTML-блок.
