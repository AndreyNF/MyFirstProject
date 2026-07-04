=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

### Параметры
- **SLUG:** `vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo`
- **Якорь для Наташи:** `l24-boris-fns-zalogovyy-kreditor-role-matrix`
- **Размещение:** после H2-4 «Налоговый арест и залог в силу закона: ст. 73, 77 и 101 НК РФ» (перед H2-5)
- **Режим:** Legis24 MCP-only — static SVG + inline CSS, без `<canvas>` и `<script>`
- **Композиция:** сплит-сетка — слева SVG «арест → залог → банкротство», справа матрица ролей (директор / КУ / кредиторы vs ФНС); контраст к hero Алины (масштаб процедуры, не дубль сцены)

```html
<section id="l24-boris-fns-zalogovyy-kreditor-role-matrix" class="l24-boris-fns-zalogovyy-kreditor" aria-label="Матрица ролей при налоговом аресте и залоге ФНС в банкротстве — обзор ВС № 5/2026, дело А72-19547/2022">
<style>
.l24-boris-fns-zalogovyy-kreditor {
  --fz-navy: #0f2744;
  --fz-navy-soft: #1a365d;
  --fz-gold: #ecc94b;
  --fz-amber: #f6ad55;
  --fz-mint: #5eead4;
  --fz-blue: #63b3ed;
  --fz-rose: #fc8181;
  --fz-violet: #b794f4;
  --fz-muted: #a0aec0;
  --fz-ink: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-fns-zalogovyy-kreditor__shell {
  background: linear-gradient(148deg, var(--fz-navy) 0%, #152a45 52%, var(--fz-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 26px;
  color: var(--fz-ink);
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
}
.l24-boris-fns-zalogovyy-kreditor__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--fz-gold);
}
.l24-boris-fns-zalogovyy-kreditor__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-fns-zalogovyy-kreditor__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--fz-muted);
  max-width: 72ch;
}
.l24-boris-fns-zalogovyy-kreditor__lead strong { color: #fff; }
.l24-boris-fns-zalogovyy-kreditor__split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr);
  gap: 20px;
  margin-bottom: 20px;
}
.l24-boris-fns-zalogovyy-kreditor__panel {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 12px;
  padding: 18px 16px 16px;
}
.l24-boris-fns-zalogovyy-kreditor__panel-title {
  margin: 0 0 12px;
  font-size: 0.76rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--fz-gold);
}
.l24-boris-fns-zalogovyy-kreditor__chain-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 14px;
}
.l24-boris-fns-zalogovyy-kreditor__chain-note {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.1);
  border: 1px solid rgba(236, 201, 75, 0.28);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--fz-muted);
}
.l24-boris-fns-zalogovyy-kreditor__chain-note strong { color: var(--fz-gold); }
.l24-boris-fns-zalogovyy-kreditor__matrix {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr) minmax(0, 0.95fr) minmax(0, 0.95fr) minmax(0, 1.05fr);
  gap: 0;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.12);
  margin-bottom: 14px;
}
.l24-boris-fns-zalogovyy-kreditor__matrix-h {
  padding: 9px 10px;
  font-size: 0.64rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  text-align: center;
}
.l24-boris-fns-zalogovyy-kreditor__matrix-h--sit { text-align: left; }
.l24-boris-fns-zalogovyy-kreditor__matrix-h--dir { color: #bee3f8; }
.l24-boris-fns-zalogovyy-kreditor__matrix-h--ku { color: #b2f5ea; }
.l24-boris-fns-zalogovyy-kreditor__matrix-h--cred { color: #fed7d7; }
.l24-boris-fns-zalogovyy-kreditor__matrix-h--fns { color: #fbd38d; background: rgba(246, 173, 85, 0.12); }
.l24-boris-fns-zalogovyy-kreditor__matrix-row { display: contents; }
.l24-boris-fns-zalogovyy-kreditor__matrix-cell {
  padding: 9px 10px;
  font-size: 0.72rem;
  line-height: 1.38;
  color: #cbd5e1;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  background: rgba(255, 255, 255, 0.03);
}
.l24-boris-fns-zalogovyy-kreditor__matrix-cell--sit {
  font-weight: 600;
  color: #e2e8f0;
  background: rgba(255, 255, 255, 0.05);
}
.l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir { color: #bee3f8; }
.l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku { color: #b2f5ea; }
.l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred { color: #fed7d7; }
.l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns {
  color: #fbd38d;
  background: rgba(246, 173, 85, 0.06);
  font-weight: 600;
}
.l24-boris-fns-zalogovyy-kreditor__matrix-row:last-child .l24-boris-fns-zalogovyy-kreditor__matrix-cell { border-bottom: none; }
.l24-boris-fns-zalogovyy-kreditor__badge {
  display: inline-block;
  margin-top: 4px;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}
.l24-boris-fns-zalogovyy-kreditor__badge--low { background: rgba(252, 129, 129, 0.22); color: #fed7d7; }
.l24-boris-fns-zalogovyy-kreditor__badge--mid { background: rgba(236, 201, 75, 0.18); color: #faf089; }
.l24-boris-fns-zalogovyy-kreditor__badge--high { background: rgba(104, 211, 145, 0.18); color: #c6f6d5; }
.l24-boris-fns-zalogovyy-kreditor__badge--win { background: rgba(246, 173, 85, 0.22); color: #fbd38d; }
.l24-boris-fns-zalogovyy-kreditor__verdict {
  margin: 0 0 12px;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(99, 179, 237, 0.1);
  border: 1px solid rgba(99, 179, 237, 0.28);
  font-size: 0.8rem;
  line-height: 1.48;
  color: var(--fz-muted);
}
.l24-boris-fns-zalogovyy-kreditor__verdict strong { color: #bee3f8; }
.l24-boris-fns-zalogovyy-kreditor__caption {
  margin: 0;
  font-size: 0.72rem;
  line-height: 1.4;
  color: #718096;
}
.l24-boris-fns-zalogovyy-kreditor__caption strong { color: #a0aec0; font-weight: 600; }
.l24-boris-fns-zalogovyy-kreditor__roles {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-fns-zalogovyy-kreditor__role {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.14);
  color: var(--fz-ink);
}
.l24-boris-fns-zalogovyy-kreditor__role--dir { border-color: rgba(99, 179, 237, 0.45); color: #bee3f8; }
.l24-boris-fns-zalogovyy-kreditor__role--ku { border-color: rgba(94, 234, 212, 0.45); color: #b2f5ea; }
.l24-boris-fns-zalogovyy-kreditor__role--cred { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-fns-zalogovyy-kreditor__role--fns { border-color: rgba(246, 173, 85, 0.55); color: #fbd38d; }
@media (max-width: 900px) {
  .l24-boris-fns-zalogovyy-kreditor__split { grid-template-columns: 1fr; }
  .l24-boris-fns-zalogovyy-kreditor__matrix { grid-template-columns: 1fr; }
  .l24-boris-fns-zalogovyy-kreditor__matrix-h:not(:first-child) { display: none; }
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir::before,
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku::before,
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred::before,
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns::before {
    display: block;
    font-size: 0.62rem;
    font-weight: 800;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 4px;
    opacity: 0.85;
  }
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir::before { content: "Директор"; color: #bee3f8; }
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku::before { content: "КУ"; color: #b2f5ea; }
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred::before { content: "Кредиторы"; color: #fed7d7; }
  .l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns::before { content: "ФНС"; color: #fbd38d; }
}
</style>

  <div class="l24-boris-fns-zalogovyy-kreditor__shell">
    <p class="l24-boris-fns-zalogovyy-kreditor__eyebrow">п. 1 обзора № 5/2026 · п. 2.1 ст. 73 · п. 4 ст. 61.4 · дело № А72-19547/2022</p>
    <h3 class="l24-boris-fns-zalogovyy-kreditor__title">Налоговый арест → залог в силу закона: матрица ролей против ФНС</h3>
    <p class="l24-boris-fns-zalogovyy-kreditor__lead">После ареста по <strong>ст. 77 / 101 НК РФ</strong> ФНС получает статус <strong>залогового кредитора</strong> и до <strong>70% выручки</strong> с арестованного имущества (ст. 138). Директор, конкурсный управляющий и незалоговые кредиторы действуют в разных плоскостях — оспаривание по ст. 61.2/61.3 после обзора ВС не работает.</p>

    <div class="l24-boris-fns-zalogovyy-kreditor__split">
      <div class="l24-boris-fns-zalogovyy-kreditor__panel">
        <p class="l24-boris-fns-zalogovyy-kreditor__panel-title">Цепочка: арест → залог → банкротство (кейс 109 млн ₽)</p>
        <svg class="l24-boris-fns-zalogovyy-kreditor__chain-svg" viewBox="0 0 520 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="fz-boris-chain-title fz-boris-chain-desc">
          <title id="fz-boris-chain-title">Схема налогового ареста, залога в силу закона и банкротства — роли участников</title>
          <desc id="fz-boris-chain-desc">Выездная проверка, арест 4 объектов недвижимости и 153 единиц движимого имущества, залог по п. 2.1 ст. 73 НК РФ, банкротство 09.01.2023; ФНС в центре как залоговый кредитор, вокруг — директор, конкурсный управляющий и кредиторы</desc>
          <defs>
            <linearGradient id="fz-boris-flow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#63b3ed"/>
              <stop offset="50%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#f6ad55"/>
            </linearGradient>
            <marker id="fz-boris-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
          </defs>

          <!-- Timeline chain top -->
          <text x="260" y="18" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="700" letter-spacing="0.05em">АРЕСТ ДО БАНКРОТСТВА · ИНЗЕНСКИЙ ЗАВОД</text>
          <rect x="24" y="28" width="130" height="44" rx="8" fill="rgba(99,179,237,0.15)" stroke="#63b3ed" stroke-width="1.4"/>
          <text x="89" y="46" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">Проверка</text>
          <text x="89" y="60" text-anchor="middle" fill="#a0aec0" font-size="7">ст. 77 / 101 НК</text>
          <path d="M154 50 H186" stroke="url(#fz-boris-flow)" stroke-width="2" marker-end="url(#fz-boris-arr)"/>
          <rect x="186" y="28" width="148" height="44" rx="8" fill="rgba(236,201,75,0.15)" stroke="#ecc94b" stroke-width="1.4"/>
          <text x="260" y="46" text-anchor="middle" fill="#faf089" font-size="8" font-weight="700">Арест + ЕГРН</text>
          <text x="260" y="60" text-anchor="middle" fill="#a0aec0" font-size="7">4 НО + 153 движимых</text>
          <path d="M334 50 H366" stroke="url(#fz-boris-flow)" stroke-width="2" marker-end="url(#fz-boris-arr)"/>
          <rect x="366" y="28" width="130" height="44" rx="8" fill="rgba(246,173,85,0.18)" stroke="#f6ad55" stroke-width="1.4"/>
          <text x="431" y="46" text-anchor="middle" fill="#fbd38d" font-size="8" font-weight="700">п. 2.1 ст. 73</text>
          <text x="431" y="60" text-anchor="middle" fill="#a0aec0" font-size="7">залог в силу закона</text>
          <path d="M431 72 V92" stroke="#f6ad55" stroke-width="2" marker-end="url(#fz-boris-arr)"/>
          <rect x="366" y="92" width="130" height="40" rx="8" fill="rgba(252,129,129,0.12)" stroke="#fc8181" stroke-width="1.2"/>
          <text x="431" y="110" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="700">Банкротство</text>
          <text x="431" y="124" text-anchor="middle" fill="#a0aec0" font-size="7">09.01.2023</text>

          <!-- Central FNS -->
          <circle cx="260" cy="210" r="52" fill="rgba(246,173,85,0.2)" stroke="#f6ad55" stroke-width="2"/>
          <text x="260" y="198" text-anchor="middle" fill="#fbd38d" font-size="10" font-weight="800">ФНС</text>
          <text x="260" y="212" text-anchor="middle" fill="#fff" font-size="7.5" font-weight="700">залоговый кредитор</text>
          <text x="260" y="224" text-anchor="middle" fill="#ecc94b" font-size="7">109 млн ₽</text>
          <text x="260" y="236" text-anchor="middle" fill="#a0aec0" font-size="6.5">70% выручки · ст. 138</text>
          <text x="260" y="248" text-anchor="middle" fill="#a0aec0" font-size="6.5">п. 4 ст. 61.4 — иммунитет</text>

          <!-- Role nodes -->
          <rect x="28" y="168" width="108" height="56" rx="8" fill="rgba(99,179,237,0.12)" stroke="#63b3ed" stroke-width="1.3"/>
          <text x="82" y="186" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">Директор</text>
          <text x="82" y="200" text-anchor="middle" fill="#a0aec0" font-size="6.5">до ареста: отсрочка,</text>
          <text x="82" y="212" text-anchor="middle" fill="#a0aec0" font-size="6.5">мировое, погашение</text>
          <path d="M136 196 C170 196 200 205 208 210" stroke="#63b3ed" stroke-width="1.5" fill="none" stroke-dasharray="4 2"/>

          <rect x="28" y="248" width="108" height="56" rx="8" fill="rgba(94,234,212,0.1)" stroke="#5eead4" stroke-width="1.3"/>
          <text x="82" y="266" text-anchor="middle" fill="#b2f5ea" font-size="8" font-weight="700">КУ</text>
          <text x="82" y="280" text-anchor="middle" fill="#a0aec0" font-size="6.5">не ст. 61.2/61.3 —</text>
          <text x="82" y="292" text-anchor="middle" fill="#a0aec0" font-size="6.5">арест ≠ сделка</text>
          <path d="M136 276 C175 250 210 230 220 220" stroke="#5eead4" stroke-width="1.5" fill="none" stroke-dasharray="4 2"/>

          <rect x="384" y="168" width="108" height="56" rx="8" fill="rgba(252,129,129,0.12)" stroke="#fc8181" stroke-width="1.3"/>
          <text x="438" y="186" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="700">Кредиторы</text>
          <text x="438" y="200" text-anchor="middle" fill="#a0aec0" font-size="6.5">план, голосование</text>
          <text x="438" y="212" text-anchor="middle" fill="#a0aec0" font-size="6.5">ст. 181 · остаток массы</text>
          <path d="M384 196 C350 196 320 205 312 210" stroke="#fc8181" stroke-width="1.5" fill="none" stroke-dasharray="4 2"/>

          <rect x="384" y="248" width="108" height="56" rx="8" fill="rgba(183,148,244,0.1)" stroke="#b794f4" stroke-width="1.3"/>
          <text x="438" y="266" text-anchor="middle" fill="#d6bcfa" font-size="8" font-weight="700">Контрагенты</text>
          <text x="438" y="280" text-anchor="middle" fill="#a0aec0" font-size="6.5">п. 4 ст. 72 НК</text>
          <text x="438" y="292" text-anchor="middle" fill="#a0aec0" font-size="6.5">публичный арест</text>

          <!-- Bottom bar -->
          <rect x="24" y="316" width="472" height="18" rx="5" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
          <text x="260" y="328" text-anchor="middle" fill="#ecc94b" font-size="7" font-weight="600">ВС № 5/2026 · СКЭС оставила залог ФНС · управляющий проиграл по ст. 61.3</text>
        </svg>
        <p class="l24-boris-fns-zalogovyy-kreditor__chain-note"><strong>Критично:</strong> арест и регистрация залога (14–20.09.2022) до возбуждения банкротства (09.01.2023). Без этой связки залоговый статус ФНС в споре не возникает.</p>
      </div>

      <div class="l24-boris-fns-zalogovyy-kreditor__panel">
        <p class="l24-boris-fns-zalogovyy-kreditor__panel-title">Матрица защиты: кто что может после обзора ВС</p>
        <div class="l24-boris-fns-zalogovyy-kreditor__matrix" role="table" aria-label="Матрица ролей: директор, конкурсный управляющий, кредиторы против ФНС">
          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-h l24-boris-fns-zalogovyy-kreditor__matrix-h--sit" role="columnheader">Линия защиты</div>
          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-h l24-boris-fns-zalogovyy-kreditor__matrix-h--dir" role="columnheader">Директор</div>
          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-h l24-boris-fns-zalogovyy-kreditor__matrix-h--ku" role="columnheader">КУ</div>
          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-h l24-boris-fns-zalogovyy-kreditor__matrix-h--cred" role="columnheader">Кредиторы</div>
          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-h l24-boris-fns-zalogovyy-kreditor__matrix-h--fns" role="columnheader">ФНС</div>

          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-row" role="row">
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--sit" role="rowheader">Оспаривание залога по ст. 61.2 / 61.3</div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir" role="cell">— <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--low">не его процесс</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku" role="cell">Пробовали в А72-19547 — проигрыш <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--low">мин.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred" role="cell">Через управляющего — тот же барьер <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--low">мин.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns" role="cell">п. 4 ст. 61.4 — иммунитет <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--win">защита</span></div>
          </div>

          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-row" role="row">
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--sit" role="rowheader">Оспаривание законности ареста</div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir" role="cell">Налоговый спор: акт, сумма <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">факты</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku" role="cell">Параллельно банкротству <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">умер.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred" role="cell">Инициатива через КУ <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">умер.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns" role="cell">Публичные меры — доказывать нарушения процедуры</div>
          </div>

          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-row" role="row">
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--sit" role="rowheader">Границы предмета залога</div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir" role="cell">Сверка ЕГРН / реестра <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">умер.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku" role="cell">Исключить лишнее из залога <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">умер.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred" role="cell">Сохранить необременённые активы <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--high">цель</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns" role="cell">4+153 ед. — широкий охват в кейсе обзора</div>
          </div>

          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-row" role="row">
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--sit" role="rowheader">Работа до ареста</div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir" role="cell">Отсрочка ст. 64, погашение, реструктуризация <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--high">лучший</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku" role="cell">—</div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred" role="cell">Мониторинг ЕГРН / сайта ФНС <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--high">проф.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns" role="cell">п. 4 ст. 72 — публичное раскрытие ареста</div>
          </div>

          <div class="l24-boris-fns-zalogovyy-kreditor__matrix-row" role="row">
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--sit" role="rowheader">План / мировое соглашение</div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--dir" role="cell">Цена — признание приоритета залога <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">риск</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--ku" role="cell">Переговоры, ст. 181 <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">перегов.</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--cred" role="cell">Голос залогового кредитора <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--mid">блок</span></div>
            <div class="l24-boris-fns-zalogovyy-kreditor__matrix-cell l24-boris-fns-zalogovyy-kreditor__matrix-cell--fns" role="cell">70% выручки — рычаг на собрании <span class="l24-boris-fns-zalogovyy-kreditor__badge l24-boris-fns-zalogovyy-kreditor__badge--win">приор.</span></div>
          </div>
        </div>

        <p class="l24-boris-fns-zalogovyy-kreditor__verdict"><strong>Вывод для арбитража:</strong> после п. 1 обзора № 5/2026 тратить бюджет процедуры на оспаривание залога как «сделки» бессмысленно. Рабочие линии — налоговый спор об аресте, сужение предмета залога и превентивные меры до регистрации обременения.</p>
        <p class="l24-boris-fns-zalogovyy-kreditor__caption"><strong>Редакционная подпись.</strong> Матрица по фабуле дела № А72-19547/2022 и п. 1 обзора ВС № 5/2026 (постановление № 7А/2026 от 29.04.2026). Не заменяет правовой анализ по вашим актам проверки и выпискам ЕГРН.</p>
      </div>
    </div>

    <div class="l24-boris-fns-zalogovyy-kreditor__roles" aria-label="Четыре роли в споре с ФНС">
      <span class="l24-boris-fns-zalogovyy-kreditor__role l24-boris-fns-zalogovyy-kreditor__role--dir">Директор: превенция до ареста</span>
      <span class="l24-boris-fns-zalogovyy-kreditor__role l24-boris-fns-zalogovyy-kreditor__role--ku">КУ: не ст. 61.3 — арест и границы залога</span>
      <span class="l24-boris-fns-zalogovyy-kreditor__role l24-boris-fns-zalogovyy-kreditor__role--cred">Кредиторы: план, голосование, остаток массы</span>
      <span class="l24-boris-fns-zalogovyy-kreditor__role l24-boris-fns-zalogovyy-kreditor__role--fns">ФНС: залоговый кредитор · 70% · п. 4 ст. 61.4</span>
    </div>
  </div>
</section>
```

**Паспорт блока**
| Поле | Значение |
|------|----------|
| Якорь | `#l24-boris-fns-zalogovyy-kreditor-role-matrix` |
| Класс-обёртка | `.l24-boris-fns-zalogovyy-kreditor` |
| Размещение | после H2-4, перед H2-5 |
| Техника | static SVG + inline CSS, без canvas/script |
| Тема | матрица ролей: директор / КУ / кредиторы vs ФНС при налоговом аресте |

**Чеклист отличий от hero Алины**
- Не hero, не полноэкранный — врезка в теле лонгрида после H2-4
- Свой `id` якоря (`l24-boris-fns-zalogovyy-kreditor-role-matrix`), не пересекается с hero
- Без `<canvas>` и `<script>` (MCP-only)
- Контраст к hero: не сцена «первого экрана», а редакционная схема + таблица ролей для практиков ARB
- Палитра ARB navy/gold согласована с материалами обзора ВС, но композиция — сплит-сетка, не дубль hero

## Передача Наташе
- Вставить блок **после** закрывающего `</h3>` последнего H3 в секции H2-4 («Публичное раскрытие ареста…») и **перед** `<h2>Почему конкурсный управляющий не оспорит залог ФНС…</h2>`
- Добавить в TOC ссылку: `Матрица ролей` → `#l24-boris-fns-zalogovyy-kreditor-role-matrix`
- Не удалять и не оборачивать `<style>` внутри секции — CSS inline в блоке Бориса

SLUG: vs-obzor-5-2026-fns-zalogovyy-kreditor-bankrotstvo
