=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026`  
**Якорь:** `l24-boris-sip1486-matrix`  
**Размещение:** сразу после H3 «Процедура ст. 1486: предложение правообладателю — 2 месяца — иск в СИП в 30 дней» (внутри H2 «Статья 1486 ГК РФ»), перед H2 «Заинтересованность в прекращении товарного знака» — якорь для Natasha.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **процедура ст. 1486 + матрица бремени доказывания** по практике СИП-75/2025, СИП-898/2025 и обзору ВС № 1/2026.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-sip1486-matrix" class="l24-boris-sip1486-matrix" aria-label="Ст. 1486 ГК РФ: процедура досрочного прекращения товарного знака и бремя доказывания правообладателя и истца">
<style>
.l24-boris-sip1486-matrix {
  --sip-navy: #0f1c2e;
  --sip-navy-soft: #1a3050;
  --sip-plaintiff: #63b3ed;
  --sip-owner: #f6ad55;
  --sip-save: #68d391;
  --sip-stop: #fc8181;
  --sip-gold: #ecc94b;
  --sip-ink: #e2e8f0;
  --sip-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-sip1486-matrix__shell {
  background: linear-gradient(155deg, var(--sip-navy) 0%, #152a45 50%, var(--sip-navy-soft) 100%);
  border: 1px solid rgba(99, 179, 237, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 28, 46, 0.34);
  color: var(--sip-ink);
}
.l24-boris-sip1486-matrix__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sip-gold);
}
.l24-boris-sip1486-matrix__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-sip1486-matrix__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--sip-muted);
  max-width: 72ch;
}
.l24-boris-sip1486-matrix__lead strong { color: #fff; }
.l24-boris-sip1486-matrix__split {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-sip1486-matrix__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-sip1486-matrix__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--sip-gold);
}
.l24-boris-sip1486-matrix__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 340px;
  margin-bottom: 12px;
}
.l24-boris-sip1486-matrix__steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.l24-boris-sip1486-matrix__step {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-top: 3px solid var(--sip-plaintiff);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-sip1486-matrix__step:nth-child(2) { border-top-color: var(--sip-gold); }
.l24-boris-sip1486-matrix__step:nth-child(3) { border-top-color: var(--sip-owner); }
.l24-boris-sip1486-matrix__step:nth-child(4) { border-top-color: #b794f4; }
.l24-boris-sip1486-matrix__step:nth-child(5) { border-top-color: var(--sip-save); grid-column: span 3; }
.l24-boris-sip1486-matrix__step strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-sip1486-matrix__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.12);
  border: 1px solid rgba(236, 201, 75, 0.38);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--sip-ink);
}
.l24-boris-sip1486-matrix__verdict strong { color: var(--sip-gold); }
.l24-boris-sip1486-matrix__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
.l24-boris-sip1486-matrix__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-sip1486-matrix__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-sip1486-matrix__vs-card--plaintiff { border-color: rgba(99, 179, 237, 0.45); }
.l24-boris-sip1486-matrix__vs-card--owner { border-color: rgba(246, 173, 85, 0.45); }
.l24-boris-sip1486-matrix__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-sip1486-matrix__matrix {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-sip1486-matrix__row {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 0.55fr) minmax(0, 1.15fr);
  gap: 8px 10px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-sip1486-matrix__row--plaintiff { border-left: 3px solid var(--sip-plaintiff); }
.l24-boris-sip1486-matrix__row--owner { border-left: 3px solid var(--sip-owner); }
.l24-boris-sip1486-matrix__row--both { border-left: 3px solid var(--sip-gold); }
.l24-boris-sip1486-matrix__row-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-sip1486-matrix__row-who {
  font-weight: 700;
  font-size: 0.72rem;
  padding: 3px 7px;
  border-radius: 4px;
  text-align: center;
  align-self: start;
}
.l24-boris-sip1486-matrix__row-who--plaintiff {
  background: rgba(99, 179, 237, 0.2);
  color: #bee3f8;
  border: 1px solid rgba(99, 179, 237, 0.45);
}
.l24-boris-sip1486-matrix__row-who--owner {
  background: rgba(246, 173, 85, 0.2);
  color: #fbd38d;
  border: 1px solid rgba(246, 173, 85, 0.45);
}
.l24-boris-sip1486-matrix__row-text { color: var(--sip-muted); }
.l24-boris-sip1486-matrix__row-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-sip1486-matrix__partial {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-sip1486-matrix__partial-card {
  padding: 10px;
  border-radius: 8px;
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-sip1486-matrix__partial-card--save {
  background: rgba(104, 211, 145, 0.14);
  border: 1px solid rgba(104, 211, 145, 0.4);
}
.l24-boris-sip1486-matrix__partial-card--stop {
  background: rgba(252, 129, 129, 0.14);
  border: 1px solid rgba(252, 129, 129, 0.4);
}
.l24-boris-sip1486-matrix__partial-card strong {
  display: block;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-sip1486-matrix__partial-card--save strong { color: #c6f6d5; }
.l24-boris-sip1486-matrix__partial-card--stop strong { color: #fed7d7; }
.l24-boris-sip1486-matrix__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--sip-muted);
}
.l24-boris-sip1486-matrix__note em {
  font-style: normal;
  color: #bee3f8;
  font-weight: 600;
}
.l24-boris-sip1486-matrix__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-sip1486-matrix__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--sip-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-sip1486-matrix__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--sip-gold);
}
.l24-boris-sip1486-matrix__tag--art { border-color: rgba(99, 179, 237, 0.45); color: #bee3f8; }
.l24-boris-sip1486-matrix__tag--def { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
@media (max-width: 900px) {
  .l24-boris-sip1486-matrix__split { grid-template-columns: 1fr; }
  .l24-boris-sip1486-matrix__steps { grid-template-columns: 1fr; }
  .l24-boris-sip1486-matrix__step:nth-child(5) { grid-column: auto; }
  .l24-boris-sip1486-matrix__row { grid-template-columns: 1fr; gap: 4px; }
  .l24-boris-sip1486-matrix__row-who { justify-self: start; }
  .l24-boris-sip1486-matrix__vs { grid-template-columns: 1fr; }
  .l24-boris-sip1486-matrix__partial { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-sip1486-matrix__shell">
    <p class="l24-boris-sip1486-matrix__eyebrow">ст. 1486 ГК РФ · гл. 76 · СИП-75/2025 · 30.03.2026 · СИП-898/2025</p>
    <h3 class="l24-boris-sip1486-matrix__title">Процедура ст. 1486 и бремя доказывания: истец vs правообладатель</h3>
    <p class="l24-boris-sip1486-matrix__lead">Досрочное прекращение охраны ТЗ — <strong>строго процессуальный маршрут</strong>: предложение → 2 месяца → иск в СИП в 30 дней. В суде бремя разделено: <strong>истец</strong> доказывает заинтересованность, <strong>правообладатель</strong> — реальное использование по каждой позиции свидетельства (п. 3 ст. 1486). По <strong>СИП-75/2025</strong> это дало частичное прекращение: бельё сохранено, брюки и колготки — нет.</p>

    <div class="l24-boris-sip1486-matrix__split">
      <div class="l24-boris-sip1486-matrix__panel">
        <p class="l24-boris-sip1486-matrix__panel-title">Схема процедуры ст. 1486 (предложение → 2 мес. → иск → частичное прекращение)</p>
        <svg class="l24-boris-sip1486-matrix__scheme-svg" viewBox="0 0 600 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="sip1486-scheme-title sip1486-scheme-desc">
          <title id="sip1486-scheme-title">Процедура досрочного прекращения товарного знака по ст. 1486 ГК РФ</title>
          <desc id="sip1486-scheme-desc">Пять этапов: предложение правообладателю, ожидание двух месяцев, иск в СИП в течение тридцати дней, судебное разделение бремени доказывания, частичное прекращение охраны по позициям МКТУ</desc>
          <defs>
            <linearGradient id="sip1486-flow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#63b3ed"/>
              <stop offset="50%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
            <marker id="sip1486-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
          </defs>

          <text x="300" y="18" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="600">ст. 1486 ГК РФ · расчётный период = 3 года до предложения</text>

          <!-- Step 1: Proposal -->
          <rect x="24" y="34" width="108" height="72" rx="8" fill="rgba(49,130,206,0.28)" stroke="#63b3ed" stroke-width="1.5"/>
          <text x="78" y="52" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">ШАГ 1</text>
          <text x="78" y="66" text-anchor="middle" fill="#e2e8f0" font-size="7">Предложение</text>
          <text x="78" y="78" text-anchor="middle" fill="#a0aec0" font-size="6.5">отказ / отчуждение</text>
          <text x="78" y="90" text-anchor="middle" fill="#a0aec0" font-size="6.5">адрес из реестра</text>
          <rect x="36" y="96" width="84" height="12" rx="3" fill="rgba(99,179,237,0.2)" stroke="#63b3ed" stroke-width="0.8"/>
          <text x="78" y="105" text-anchor="middle" fill="#bee3f8" font-size="6.5" font-weight="600">п. 1 ст. 1486</text>

          <!-- Arrow 1→2 -->
          <line x1="132" y1="70" x2="158" y2="70" stroke="#ecc94b" stroke-width="2" marker-end="url(#sip1486-arrow)"/>

          <!-- Step 2: 2 months -->
          <rect x="160" y="34" width="108" height="72" rx="8" fill="rgba(236,201,75,0.15)" stroke="#ecc94b" stroke-width="1.5"/>
          <text x="214" y="52" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="700">ШАГ 2</text>
          <text x="214" y="66" text-anchor="middle" fill="#e2e8f0" font-size="7">2 месяца</text>
          <text x="214" y="78" text-anchor="middle" fill="#a0aec0" font-size="6.5">отказ / молчание</text>
          <text x="214" y="90" text-anchor="middle" fill="#a0aec0" font-size="6.5">правообладателя</text>
          <circle cx="214" cy="100" r="10" fill="none" stroke="#ecc94b" stroke-width="1.5" stroke-dasharray="3 2"/>
          <text x="214" y="103" text-anchor="middle" fill="#ecc94b" font-size="6" font-weight="700">60</text>

          <!-- Arrow 2→3 -->
          <line x1="268" y1="70" x2="294" y2="70" stroke="#ecc94b" stroke-width="2" marker-end="url(#sip1486-arrow)"/>

          <!-- Step 3: Lawsuit 30 days -->
          <rect x="296" y="34" width="108" height="72" rx="8" fill="rgba(237,137,54,0.22)" stroke="#f6ad55" stroke-width="1.5"/>
          <text x="350" y="52" text-anchor="middle" fill="#fbd38d" font-size="8" font-weight="700">ШАГ 3</text>
          <text x="350" y="66" text-anchor="middle" fill="#e2e8f0" font-size="7">Иск в СИП</text>
          <text x="350" y="78" text-anchor="middle" fill="#a0aec0" font-size="6.5">в течение 30 дней</text>
          <text x="350" y="90" text-anchor="middle" fill="#a0aec0" font-size="6.5">пропуск = заново</text>
          <rect x="312" y="96" width="76" height="12" rx="3" fill="rgba(246,173,85,0.2)" stroke="#f6ad55" stroke-width="0.8"/>
          <text x="350" y="105" text-anchor="middle" fill="#fbd38d" font-size="6.5" font-weight="600">СИП-898: 01.10</text>

          <!-- Arrow 3→4 -->
          <line x1="404" y1="70" x2="430" y2="70" stroke="#ecc94b" stroke-width="2" marker-end="url(#sip1486-arrow)"/>

          <!-- Step 4: Court -->
          <rect x="432" y="34" width="144" height="72" rx="8" fill="rgba(128,90,213,0.22)" stroke="#b794f4" stroke-width="1.5"/>
          <text x="504" y="52" text-anchor="middle" fill="#d6bcfa" font-size="8" font-weight="700">ШАГ 4 · СУД</text>
          <text x="504" y="66" text-anchor="middle" fill="#63b3ed" font-size="6.5">Истец → заинтересованность</text>
          <text x="504" y="78" text-anchor="middle" fill="#f6ad55" font-size="6.5">Правообладатель → использование</text>
          <text x="504" y="90" text-anchor="middle" fill="#a0aec0" font-size="6.5">п. 3 ст. 1486 · СП-23/20</text>
          <text x="504" y="100" text-anchor="middle" fill="#a0aec0" font-size="6">по каждой позиции МКТУ</text>

          <!-- Down arrow to partial -->
          <path d="M 300 106 L 300 128" stroke="#ecc94b" stroke-width="2" fill="none" marker-end="url(#sip1486-arrow)"/>

          <!-- Step 5: Partial termination -->
          <rect x="80" y="132" width="440" height="88" rx="10" fill="rgba(0,0,0,0.32)" stroke="url(#sip1486-flow)" stroke-width="1.5"/>
          <text x="300" y="150" text-anchor="middle" fill="#fff" font-size="8.5" font-weight="700">ШАГ 5 · Частичное прекращение охраны (СИП-75/2025, 30.03.2026)</text>

          <rect x="100" y="162" width="180" height="48" rx="6" fill="rgba(104,211,145,0.18)" stroke="#68d391" stroke-width="1.2"/>
          <text x="190" y="178" text-anchor="middle" fill="#c6f6d5" font-size="7.5" font-weight="700">ОХРАНА СОХРАНЕНА</text>
          <text x="190" y="192" text-anchor="middle" fill="#9ae6b4" font-size="6.5">нижнее бельё · бюстгальтеры</text>
          <text x="190" y="204" text-anchor="middle" fill="#a0aec0" font-size="6">доказаны реальные продажи</text>

          <rect x="320" y="162" width="180" height="48" rx="6" fill="rgba(252,129,129,0.18)" stroke="#fc8181" stroke-width="1.2"/>
          <text x="410" y="178" text-anchor="middle" fill="#fed7d7" font-size="7.5" font-weight="700">ОХРАНА ПРЕКРАЩЕНА</text>
          <text x="410" y="192" text-anchor="middle" fill="#feb2b2" font-size="6.5">брюки · колготки · корсеты</text>
          <text x="410" y="204" text-anchor="middle" fill="#a0aec0" font-size="6">нет убедительных доказательств</text>

          <!-- Timeline bar -->
          <rect x="40" y="236" width="520" height="28" rx="6" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.12)" stroke-width="1"/>
          <rect x="48" y="244" width="120" height="12" rx="3" fill="rgba(99,179,237,0.35)"/>
          <rect x="176" y="244" width="80" height="12" rx="3" fill="rgba(236,201,75,0.35)"/>
          <rect x="264" y="244" width="56" height="12" rx="3" fill="rgba(246,173,85,0.35)"/>
          <rect x="328" y="244" width="224" height="12" rx="3" fill="rgba(104,211,145,0.25)"/>
          <text x="108" y="253" text-anchor="middle" fill="#bee3f8" font-size="6">предложение</text>
          <text x="216" y="253" text-anchor="middle" fill="#ecc94b" font-size="6">2 мес.</text>
          <text x="292" y="253" text-anchor="middle" fill="#fbd38d" font-size="6">30 дн.</text>
          <text x="440" y="253" text-anchor="middle" fill="#9ae6b4" font-size="6">рассмотрение в СИП → частичный итог</text>

          <!-- 3-year period note -->
          <rect x="40" y="276" width="520" height="32" rx="6" fill="rgba(236,201,75,0.1)" stroke="rgba(236,201,75,0.35)" stroke-width="1"/>
          <text x="300" y="290" text-anchor="middle" fill="#ecc94b" font-size="7" font-weight="600">Расчётный период неиспользования: 3 года до даты предложения (не до иска)</text>
          <text x="300" y="302" text-anchor="middle" fill="#a0aec0" font-size="6.5">СИП-75/2025: период отсчитан от направления предложения иностранному правообладателю</text>
        </svg>

        <ol class="l24-boris-sip1486-matrix__steps" aria-label="Пять шагов процедуры ст. 1486">
          <li class="l24-boris-sip1486-matrix__step">
            <strong>Предложение</strong>
            Отказ от ТЗ или договор отчуждения — по адресу из реестра Роспатента. Запускает расчётный период (−3 года).
          </li>
          <li class="l24-boris-sip1486-matrix__step">
            <strong>2 месяца</strong>
            Правообладатель отказывается, предлагает отчуждение или молчит — после истечения срока открывается окно для иска.
          </li>
          <li class="l24-boris-sip1486-matrix__step">
            <strong>Иск в СИП · 30 дней</strong>
            Пропуск срока = новое предложение с нуля. СИП-898/2025: предложение 01.07.2025 → иск 01.10.2025.
          </li>
          <li class="l24-boris-sip1486-matrix__step">
            <strong>Суд</strong>
            Истец доказывает заинтересованность (СП-23/20). Правообладатель — использование по каждой позиции свидетельства.
          </li>
          <li class="l24-boris-sip1486-matrix__step">
            <strong>Частичное прекращение</strong>
            СИП-75/2025: бельё и бюстгальтеры сохранены; брюки, колготки, корсеты — охрана прекращена. Однородность для истца, детализация — для правообладателя.
          </li>
        </ol>
        <p class="l24-boris-sip1486-matrix__verdict"><strong>84% исков</strong> в 1 пол. 2025 г. удовлетворены СИП (124 из 147) — но большинство проигрышей правообладателей связано с формальными ошибками доказывания, а не с отсутствием использования в принципе.</p>
        <p class="l24-boris-sip1486-matrix__caption">Схема по ст. 1486 ГК РФ · решение СИП от 30.03.2026, дело № СИП-75/2025</p>
      </div>

      <div class="l24-boris-sip1486-matrix__panel">
        <p class="l24-boris-sip1486-matrix__panel-title">Правообладатель vs истец: бремя доказывания</p>
        <div class="l24-boris-sip1486-matrix__vs">
          <div class="l24-boris-sip1486-matrix__vs-card l24-boris-sip1486-matrix__vs-card--plaintiff">
            <strong>Истец (атака)</strong>
            Заинтересованность + реальное намерение. Одной заявки в Роспатент мало — нужна совокупность (СИП-898/2025). Проверить авторское право за ТЗ (обзор ВС № 1/2026).
          </div>
          <div class="l24-boris-sip1486-matrix__vs-card l24-boris-sip1486-matrix__vs-card--owner">
            <strong>Правообладатель (оборона)</strong>
            Реальное использование за 3 года до предложения — по каждой позиции МКТУ отдельно (п. 3 ст. 1486). Скриншоты без дат, закупки вместо продаж — не принимаются.
          </div>
        </div>
        <div class="l24-boris-sip1486-matrix__matrix">
          <div class="l24-boris-sip1486-matrix__row l24-boris-sip1486-matrix__row--plaintiff">
            <span class="l24-boris-sip1486-matrix__row-label">Заинтересованность</span>
            <span class="l24-boris-sip1486-matrix__row-who l24-boris-sip1486-matrix__row-who--plaintiff">Истец</span>
            <span class="l24-boris-sip1486-matrix__row-text">Реальное намерение + подготовительные действия + <em>однородность товаров</em> (СП-23/20, п. 165 Пленума ВС № 10). Заявка в Роспатент — лишь один из элементов совокупности.</span>
          </div>
          <div class="l24-boris-sip1486-matrix__row l24-boris-sip1486-matrix__row--plaintiff">
            <span class="l24-boris-sip1486-matrix__row-label">Правомерность после прекращения</span>
            <span class="l24-boris-sip1486-matrix__row-who l24-boris-sip1486-matrix__row-who--plaintiff">Истец</span>
            <span class="l24-boris-sip1486-matrix__row-text">Обзор ВС № 1/2026 («Фиксики»/Симка): истец обязан доказать, что сможет <em>правомерно</em> использовать обозначение. Авторское право на персонажа блокирует «освобождение» ТЗ.</span>
          </div>
          <div class="l24-boris-sip1486-matrix__row l24-boris-sip1486-matrix__row--owner">
            <span class="l24-boris-sip1486-matrix__row-label">Использование ТЗ</span>
            <span class="l24-boris-sip1486-matrix__row-who l24-boris-sip1486-matrix__row-who--owner">Правообладатель</span>
            <span class="l24-boris-sip1486-matrix__row-text">п. 3 ст. 1486: <em>реальное</em> введение в оборот за расчётный период. По каждой позиции свидетельства — отдельно. СИП-75/2025: бельё доказано, брюки — нет.</span>
          </div>
          <div class="l24-boris-sip1486-matrix__row l24-boris-sip1486-matrix__row--owner">
            <span class="l24-boris-sip1486-matrix__row-label">Лицензиат / форма знака</span>
            <span class="l24-boris-sip1486-matrix__row-who l24-boris-sip1486-matrix__row-who--owner">Правообладатель</span>
            <span class="l24-boris-sip1486-matrix__row-text">Использование лицензиатом элементов по отдельности <em>≠</em> использование зарегистрированного ТЗ (СИП-410/2024). Существенное изменение существа знака не засчитывается (п. 2 ст. 1486).</span>
          </div>
          <div class="l24-boris-sip1486-matrix__row l24-boris-sip1486-matrix__row--both">
            <span class="l24-boris-sip1486-matrix__row-label">Символическое vs реальное</span>
            <span class="l24-boris-sip1486-matrix__row-who l24-boris-sip1486-matrix__row-who--owner">Правообладатель</span>
            <span class="l24-boris-sip1486-matrix__row-text">СИП-898/2025: скриншоты вне периода, без дат, документы «закупка» вместо «продажа» — отклонены. Производство без реализации — не использование.</span>
          </div>
        </div>
        <div class="l24-boris-sip1486-matrix__partial" aria-label="Итог СИП-75/2025 по позициям МКТУ">
          <div class="l24-boris-sip1486-matrix__partial-card l24-boris-sip1486-matrix__partial-card--save">
            <strong>Сохранено · СИП-75/2025</strong>
            Нижнее бельё, бюстгальтеры — приняты накладные и доказательства реальных продаж в расчётном периоде.
          </div>
          <div class="l24-boris-sip1486-matrix__partial-card l24-boris-sip1486-matrix__partial-card--stop">
            <strong>Прекращено · СИП-75/2025</strong>
            Брюки, трусы, колготки, корсеты — правообладатель не подтвердил использование по этим позициям.
          </div>
        </div>
        <p class="l24-boris-sip1486-matrix__note"><em>Асимметрия СП-23/20:</em> истцу достаточно однородных товаров, правообладатель обязан доказывать использование <em>по каждой конкретной позиции</em> перечня — это ключ к стратегии частичного сохранения знака.</p>
      </div>
    </div>

    <div class="l24-boris-sip1486-matrix__foot" aria-label="Контекст практики СИП 2026">
      <span class="l24-boris-sip1486-matrix__tag l24-boris-sip1486-matrix__tag--case">СИП-75/2025 · 30.03.2026</span>
      <span class="l24-boris-sip1486-matrix__tag l24-boris-sip1486-matrix__tag--art">ст. 1486 ГК РФ · п. 1–3</span>
      <span class="l24-boris-sip1486-matrix__tag l24-boris-sip1486-matrix__tag--def">Защита: УПД + даты в периоде + по позициям</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H3 «Процедура ст. 1486…» (внутри H2 «Статья 1486 ГК РФ»)
- [x] Свой `id`: `l24-boris-sip1486-matrix` (не hero `#l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым hero Алины (IP / досрочное прекращение ТЗ)
- [x] Сплит «схема процедуры ст. 1486 (5 шагов + частичное прекращение) | матрица бремени доказывания истец vs правообладатель»
