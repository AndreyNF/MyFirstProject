=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026`  
**Якорь:** `boris-theft-fraud-map`  
**Размещение для Наташи:** сразу **после H3 «Типовые схемы: перевод под влиянием обмана vs тайное хищение после доступа»** (после markdown-таблицы сценариев в тексте Жени/Артура), **перед H3 «Переквалификация со ст. 159 на ст. 158 и обратно»** и **перед primary CTA** «Следствие квалифицировало дело как мошенничество…».  
**Режим:** тёмная панель в теле статьи (**контраст** со светлым UG-hero Алины по Пленуму № 19) — **карта разграничения 158/159** слева + **сетка цифровых сценариев списания** справа.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Метафора** | «Развилка обмана» — один телефонный звонок может вести к ст. 159 или ст. 158 в зависимости от того, кто инициировал перевод и было ли списание тайным |
| **Цифры-крючки** | Пленум № 19 · 16.06.2026 · п. 2 и п. 25.1 Пленума № 29 · окончание кражи = **списание** · п. «г» ч. 3 ст. 158 · ≤ 2 500 ₽ → ст. 158.1 |
| **Палитра** | Тёмный navy `#0c1222`–`#1a2744` (контраст hero); кража `#dc2626` / `#f87171`; мошенничество `#7c3aed` / `#c4b5fd`; цифровой рубль `#059669`; списание `#f59e0b`; нейтраль `#94a3b8` |
| **Композиция** | Сплит: SVG-карта решений 158 vs 159 \| SVG-сетка 5 цифровых сценариев + HTML-таблица квалификации |

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 «Кража или мошенничество»
- [x] Свой `id`: `boris-theft-fraud-map` (не `l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым UG-hero (navy/судебная палитра Legis24)
- [x] Сплит «карта разграничения» \| «сетка цифровых списаний по Пленуму № 19»

```html
<section id="boris-theft-fraud-map" class="boris-theft-fraud-map" aria-label="Пленум ВС № 19: карта разграничения кражи (ст. 158) и мошенничества (ст. 159) при цифровых списаниях">
<style>
.boris-theft-fraud-map {
  --tf-ink: #0c1222;
  --tf-navy: #1a2744;
  --tf-navy-soft: #243352;
  --tf-theft: #dc2626;
  --tf-theft-soft: #fca5a5;
  --tf-fraud: #7c3aed;
  --tf-fraud-soft: #c4b5fd;
  --tf-digital: #059669;
  --tf-digital-soft: #6ee7b7;
  --tf-debit: #f59e0b;
  --tf-debit-soft: #fde68a;
  --tf-muted: #94a3b8;
  --tf-text: #e2e8f0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.boris-theft-fraud-map__shell {
  background: linear-gradient(152deg, var(--tf-ink) 0%, var(--tf-navy) 46%, var(--tf-navy-soft) 100%);
  border: 1px solid rgba(30, 58, 138, 0.35);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(12, 18, 34, 0.45);
  color: var(--tf-text);
}
.boris-theft-fraud-map__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--tf-debit);
}
.boris-theft-fraud-map__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.boris-theft-fraud-map__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--tf-muted);
  max-width: 72ch;
}
.boris-theft-fraud-map__lead strong { color: #fff; }
.boris-theft-fraud-map__lead em {
  font-style: normal;
  color: var(--tf-debit-soft);
  font-weight: 600;
}
.boris-theft-fraud-map__split {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.boris-theft-fraud-map__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.boris-theft-fraud-map__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--tf-debit);
}
.boris-theft-fraud-map__map-svg,
.boris-theft-fraud-map__grid-svg {
  display: block;
  width: 100%;
  height: auto;
}
.boris-theft-fraud-map__map-svg { max-height: 340px; margin-bottom: 12px; }
.boris-theft-fraud-map__grid-svg { max-height: 220px; margin-bottom: 14px; }
.boris-theft-fraud-map__branches {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.boris-theft-fraud-map__branch {
  padding: 12px 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  font-size: 0.72rem;
  line-height: 1.42;
  color: var(--tf-muted);
}
.boris-theft-fraud-map__branch--theft {
  border-top: 3px solid var(--tf-theft);
}
.boris-theft-fraud-map__branch--fraud {
  border-top: 3px solid var(--tf-fraud);
}
.boris-theft-fraud-map__branch strong {
  display: block;
  margin-bottom: 4px;
  font-size: 0.78rem;
  color: #fff;
}
.boris-theft-fraud-map__branch--theft strong { color: var(--tf-theft-soft); }
.boris-theft-fraud-map__branch--fraud strong { color: var(--tf-fraud-soft); }
.boris-theft-fraud-map__quote {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(245, 158, 11, 0.1);
  border: 1px solid rgba(245, 158, 11, 0.32);
  font-size: 0.76rem;
  line-height: 1.48;
  color: var(--tf-text);
  font-style: italic;
}
.boris-theft-fraud-map__quote cite {
  display: block;
  margin-top: 8px;
  font-style: normal;
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--tf-debit);
  letter-spacing: 0.03em;
}
.boris-theft-fraud-map__table-wrap {
  overflow-x: auto;
  margin: 0 0 12px;
  border-radius: 8px;
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.boris-theft-fraud-map__table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.72rem;
  line-height: 1.38;
}
.boris-theft-fraud-map__table th,
.boris-theft-fraud-map__table td {
  padding: 9px 10px;
  text-align: left;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  vertical-align: top;
}
.boris-theft-fraud-map__table th {
  background: rgba(0, 0, 0, 0.32);
  color: #fff;
  font-weight: 700;
  font-size: 0.68rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.boris-theft-fraud-map__table tr:last-child td { border-bottom: none; }
.boris-theft-fraud-map__table td { color: var(--tf-muted); }
.boris-theft-fraud-map__table td strong { color: #fff; }
.boris-theft-fraud-map__qual--theft {
  color: var(--tf-theft-soft) !important;
  font-weight: 700;
  white-space: nowrap;
}
.boris-theft-fraud-map__qual--fraud {
  color: var(--tf-fraud-soft) !important;
  font-weight: 700;
  white-space: nowrap;
}
.boris-theft-fraud-map__note {
  margin: 0;
  padding: 10px 12px;
  border-radius: 8px;
  background: rgba(5, 150, 105, 0.12);
  border: 1px solid rgba(5, 150, 105, 0.35);
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--tf-text);
}
.boris-theft-fraud-map__note strong { color: var(--tf-digital-soft); }
.boris-theft-fraud-map__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(148, 163, 184, 0.88);
  text-align: center;
}
.boris-theft-fraud-map__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.boris-theft-fraud-map__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--tf-text);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.boris-theft-fraud-map__tag--plenum { border-color: rgba(245, 158, 11, 0.5); color: var(--tf-debit-soft); }
.boris-theft-fraud-map__tag--theft { border-color: rgba(220, 38, 38, 0.5); color: var(--tf-theft-soft); }
.boris-theft-fraud-map__tag--fraud { border-color: rgba(124, 58, 237, 0.5); color: var(--tf-fraud-soft); }
.boris-theft-fraud-map__tag--digital { border-color: rgba(5, 150, 105, 0.5); color: var(--tf-digital-soft); }
@media (max-width: 900px) {
  .boris-theft-fraud-map__split { grid-template-columns: 1fr; }
  .boris-theft-fraud-map__branches { grid-template-columns: 1fr; }
}
</style>

  <div class="boris-theft-fraud-map__shell">
    <p class="boris-theft-fraud-map__eyebrow">UG · Пленум ВС № 19 · 16.06.2026 · ст. 158 vs ст. 159</p>
    <h3 class="boris-theft-fraud-map__title">Кража или мошенничество: карта квалификации при цифровых списаниях</h3>
    <p class="boris-theft-fraud-map__lead">Пленум № 19 закрепил критерий ВС: если обман служил <strong>только доступу</strong> к счёту, а деньги списаны <strong>тайно</strong> — это <strong>кража</strong> (ст. 158, в т.ч. п. «г» ч. 3). Если потерпевший <strong>сам инициировал перевод</strong> — <strong>мошенничество</strong> (ст. 159). Для безналичных ДС преступление окончено с момента <em>списания</em> (п. 6 Пленума № 29).</p>

    <div class="boris-theft-fraud-map__split">
      <div class="boris-theft-fraud-map__panel">
        <p class="boris-theft-fraud-map__panel-title">Карта решений: обман → квалификация</p>
        <svg class="boris-theft-fraud-map__map-svg" viewBox="0 0 560 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="tf-map-title tf-map-desc">
          <title id="tf-map-title">Разграничение кражи и мошенничества по Пленуму ВС № 19</title>
          <desc id="tf-map-desc">Дерево решений: при тайном списании после обмана для доступа — ст. 158; при добровольном переводе потерпевшим — ст. 159</desc>
          <defs>
            <linearGradient id="tf-axis" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#f59e0b"/>
              <stop offset="50%" stop-color="#64748b"/>
              <stop offset="100%" stop-color="#334155"/>
            </linearGradient>
            <marker id="tf-arr" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#94a3b8"/>
            </marker>
            <marker id="tf-arr-theft" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#f87171"/>
            </marker>
            <marker id="tf-arr-fraud" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#c4b5fd"/>
            </marker>
          </defs>

          <rect x="4" y="4" width="552" height="312" rx="14" fill="rgba(0,0,0,0.22)" stroke="#334155" stroke-width="1"/>

          <!-- Root -->
          <rect x="196" y="20" width="168" height="48" rx="10" fill="rgba(245,158,11,0.14)" stroke="#f59e0b" stroke-width="1.8"/>
          <text x="280" y="40" text-anchor="middle" fill="#fde68a" font-size="7" font-weight="800">ОБМАН ПРИ ХИЩЕНИИ ДС</text>
          <text x="280" y="54" text-anchor="middle" fill="#e2e8f0" font-size="6.5" font-weight="600">телефон · СМС · «сотрудник банка»</text>
          <line x1="280" y1="68" x2="280" y2="88" stroke="url(#tf-axis)" stroke-width="2.5"/>

          <!-- Question 1 -->
          <rect x="176" y="88" width="208" height="44" rx="8" fill="rgba(100,116,139,0.18)" stroke="#64748b" stroke-width="1.5"/>
          <text x="280" y="106" text-anchor="middle" fill="#fff" font-size="6.8" font-weight="700">Кто инициировал изъятие денег?</text>
          <text x="280" y="120" text-anchor="middle" fill="#94a3b8" font-size="6">перевод / распоряжение vs тайное списание</text>

          <!-- Left branch: victim transfers -->
          <path d="M176 110 L88 110 L88 168" stroke="#c4b5fd" stroke-width="2" fill="none" marker-end="url(#tf-arr-fraud)"/>
          <rect x="20" y="168" width="136" height="56" rx="8" fill="rgba(124,58,237,0.14)" stroke="#7c3aed" stroke-width="1.8"/>
          <text x="88" y="188" text-anchor="middle" fill="#c4b5fd" font-size="6.5" font-weight="800">ПОТЕРПЕВШИЙ САМ</text>
          <text x="88" y="202" text-anchor="middle" fill="#e2e8f0" font-size="6">перевод на «безопасный счёт»</text>
          <text x="88" y="214" text-anchor="middle" fill="#94a3b8" font-size="5.8">открытое распоряжение</text>

          <!-- Right branch: secret debit -->
          <path d="M384 110 L472 110 L472 168" stroke="#f87171" stroke-width="2" fill="none" marker-end="url(#tf-arr-theft)"/>
          <rect x="404" y="168" width="136" height="56" rx="8" fill="rgba(220,38,38,0.14)" stroke="#dc2626" stroke-width="1.8"/>
          <text x="472" y="188" text-anchor="middle" fill="#fca5a5" font-size="6.5" font-weight="800">ВИНОВНЫЙ ТАЙНО</text>
          <text x="472" y="202" text-anchor="middle" fill="#e2e8f0" font-size="6">списание с карты / кошелька</text>
          <text x="472" y="214" text-anchor="middle" fill="#94a3b8" font-size="5.8">код СМС «только для доступа»</text>

          <!-- Question 2 center -->
          <path d="M280 132 L280 168" stroke="#64748b" stroke-width="1.5" fill="none" marker-end="url(#tf-arr)"/>
          <rect x="196" y="168" width="168" height="44" rx="8" fill="rgba(100,116,139,0.12)" stroke="#475569" stroke-width="1.2"/>
          <text x="280" y="186" text-anchor="middle" fill="#cbd5e1" font-size="6.5" font-weight="600">Обман = способ завладения?</text>
          <text x="280" y="200" text-anchor="middle" fill="#94a3b8" font-size="5.8">или лишь прикрытие для доступа</text>

          <!-- Outcomes -->
          <path d="M88 224 L88 252" stroke="#7c3aed" stroke-width="2" fill="none" marker-end="url(#tf-arr-fraud)"/>
          <rect x="24" y="252" width="128" height="52" rx="8" fill="rgba(124,58,237,0.2)" stroke="#7c3aed" stroke-width="2"/>
          <text x="88" y="272" text-anchor="middle" fill="#c4b5fd" font-size="8" font-weight="800">ст. 159</text>
          <text x="88" y="286" text-anchor="middle" fill="#e2e8f0" font-size="6">мошенничество</text>
          <text x="88" y="298" text-anchor="middle" fill="#94a3b8" font-size="5.5">обман = завладение</text>

          <path d="M472 224 L472 252" stroke="#dc2626" stroke-width="2.5" fill="none" marker-end="url(#tf-arr-theft)"/>
          <rect x="408" y="252" width="128" height="52" rx="8" fill="rgba(220,38,38,0.2)" stroke="#dc2626" stroke-width="2"/>
          <text x="472" y="270" text-anchor="middle" fill="#fca5a5" font-size="8" font-weight="800">ст. 158</text>
          <text x="472" y="284" text-anchor="middle" fill="#e2e8f0" font-size="6">кража · п. «г» ч. 3</text>
          <text x="472" y="296" text-anchor="middle" fill="#94a3b8" font-size="5.5">п. 2 · п. 25.1 Пленума</text>

          <!-- Center outcome: depends -->
          <path d="M280 212 L280 252" stroke="#059669" stroke-width="2" fill="none" marker-end="url(#tf-arr)"/>
          <rect x="196" y="252" width="168" height="52" rx="8" fill="rgba(5,150,105,0.14)" stroke="#059669" stroke-width="1.5"/>
          <text x="280" y="272" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="700">ЦИФРОВОЙ РУБЛЬ / ДС</text>
          <text x="280" y="286" text-anchor="middle" fill="#e2e8f0" font-size="6">окончание = списание</text>
          <text x="280" y="298" text-anchor="middle" fill="#94a3b8" font-size="5.5">п. 6 · п. 11 Пленума № 29</text>

          <!-- Debit moment indicator -->
          <g transform="translate(16, 248)">
            <rect width="52" height="28" rx="6" fill="rgba(245,158,11,0.15)" stroke="#f59e0b" stroke-width="1"/>
            <text x="26" y="14" text-anchor="middle" fill="#fde68a" font-size="5.5" font-weight="700">СПИСАНИЕ</text>
            <text x="26" y="24" text-anchor="middle" fill="#94a3b8" font-size="5">= ущерб</text>
          </g>
        </svg>

        <ul class="boris-theft-fraud-map__branches" aria-label="Два итога разграничения">
          <li class="boris-theft-fraud-map__branch boris-theft-fraud-map__branch--theft">
            <strong>Кража · ст. 158</strong>
            Обман только для доступа → тайное списание с карты, кошелька или счёта цифрового рубля. П. 25.1: даже без взлома ПО.
          </li>
          <li class="boris-theft-fraud-map__branch boris-theft-fraud-map__branch--fraud">
            <strong>Мошенничество · ст. 159</strong>
            Потерпевший сам перевёл деньги или передал доступ — виновный распорядился имуществом открыто.
          </li>
        </ul>
        <blockquote class="boris-theft-fraud-map__quote">
          «Если виновное лицо использовало обман либо злоупотребление доверием только для обеспечения или облегчения доступа к имуществу… но при этом само изъятие имущества осуществило тайно, то его действия образуют состав кражи.»
          <cite>п. 2 Пленума ВС № 29 (ред. Пленума № 19 от 16.06.2026)</cite>
        </blockquote>
        <p class="boris-theft-fraud-map__caption">Логика ВС: не всякий обман при хищении = мошенничество</p>
      </div>

      <div class="boris-theft-fraud-map__panel">
        <p class="boris-theft-fraud-map__panel-title">Цифровые сценарии: списание и статья УК</p>
        <svg class="boris-theft-fraud-map__grid-svg" viewBox="0 0 320 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="tf-grid-title tf-grid-desc">
          <title id="tf-grid-title">Схемы цифровых списаний: кража или мошенничество</title>
          <desc id="tf-grid-desc">Пять типовых сценариев хищения безналичных денежных средств и цифрового рубля по разъяснениям Пленума № 19</desc>

          <!-- Row 1: SMS + Transfer -->
          <rect x="8" y="8" width="148" height="88" rx="8" fill="rgba(220,38,38,0.1)" stroke="#dc2626" stroke-width="1.2"/>
          <text x="82" y="26" text-anchor="middle" fill="#fca5a5" font-size="6" font-weight="800">КОД ИЗ СМС</text>
          <rect x="20" y="34" width="36" height="24" rx="4" fill="#1e293b" stroke="#475569"/>
          <text x="38" y="50" text-anchor="middle" fill="#fde68a" font-size="7" font-weight="700">SMS</text>
          <path d="M58 46 L72 46" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#tf-arr-theft)"/>
          <rect x="72" y="34" width="36" height="24" rx="4" fill="#1e293b" stroke="#dc2626"/>
          <text x="90" y="48" text-anchor="middle" fill="#fca5a5" font-size="5.5" font-weight="700">− ₽</text>
          <path d="M108 46 L122 46" stroke="#94a3b8" stroke-width="1"/>
          <rect x="122" y="36" width="24" height="20" rx="3" fill="rgba(220,38,38,0.25)" stroke="#dc2626"/>
          <text x="134" y="50" text-anchor="middle" fill="#fca5a5" font-size="5" font-weight="700">158</text>
          <text x="82" y="72" text-anchor="middle" fill="#94a3b8" font-size="5.5">тайное списание · п. 25.1</text>
          <text x="82" y="84" text-anchor="middle" fill="#64748b" font-size="5">п. «г» ч. 3 ст. 158</text>

          <rect x="164" y="8" width="148" height="88" rx="8" fill="rgba(124,58,237,0.1)" stroke="#7c3aed" stroke-width="1.2"/>
          <text x="238" y="26" text-anchor="middle" fill="#c4b5fd" font-size="6" font-weight="800">«БЕЗОПАСНЫЙ СЧЁТ»</text>
          <circle cx="200" cy="48" r="14" fill="rgba(100,116,139,0.3)" stroke="#94a3b8"/>
          <text x="200" y="51" text-anchor="middle" fill="#e2e8f0" font-size="6">👤</text>
          <path d="M214 48 L228 48" stroke="#c4b5fd" stroke-width="1.5" marker-end="url(#tf-arr-fraud)"/>
          <rect x="228" y="36" width="36" height="24" rx="4" fill="#1e293b" stroke="#7c3aed"/>
          <text x="246" y="50" text-anchor="middle" fill="#c4b5fd" font-size="5.5" font-weight="700">→ ₽</text>
          <rect x="276" y="36" width="24" height="20" rx="3" fill="rgba(124,58,237,0.25)" stroke="#7c3aed"/>
          <text x="288" y="50" text-anchor="middle" fill="#c4b5fd" font-size="5" font-weight="700">159</text>
          <text x="238" y="72" text-anchor="middle" fill="#94a3b8" font-size="5.5">сам инициировал перевод</text>
          <text x="238" y="84" text-anchor="middle" fill="#64748b" font-size="5">мошенничество</text>

          <!-- Row 2: Digital ruble + Dropper -->
          <rect x="8" y="104" width="148" height="88" rx="8" fill="rgba(5,150,105,0.1)" stroke="#059669" stroke-width="1.2"/>
          <text x="82" y="122" text-anchor="middle" fill="#6ee7b7" font-size="6" font-weight="800">ЦИФРОВОЙ РУБЛЬ</text>
          <rect x="24" y="132" width="44" height="28" rx="5" fill="#064e3b" stroke="#059669"/>
          <text x="46" y="146" text-anchor="middle" fill="#6ee7b7" font-size="5.5" font-weight="700">CBDC</text>
          <text x="46" y="156" text-anchor="middle" fill="#94a3b8" font-size="4.5">счёт ЦВ</text>
          <path d="M70 146 L88 146" stroke="#f59e0b" stroke-width="1.5" marker-end="url(#tf-arr-theft)"/>
          <text x="108" y="142" fill="#fde68a" font-size="5.5" font-weight="600">списание</text>
          <text x="108" y="154" fill="#94a3b8" font-size="5">без согласия</text>
          <rect x="122" y="136" width="24" height="20" rx="3" fill="rgba(220,38,38,0.25)" stroke="#dc2626"/>
          <text x="134" y="150" text-anchor="middle" fill="#fca5a5" font-size="5" font-weight="700">158</text>
          <text x="82" y="178" text-anchor="middle" fill="#64748b" font-size="5">п. 11 · безналичные ДС · не крипто</text>

          <rect x="164" y="104" width="148" height="88" rx="8" fill="rgba(220,38,38,0.08)" stroke="#475569" stroke-width="1.2"/>
          <text x="238" y="122" text-anchor="middle" fill="#fca5a5" font-size="6" font-weight="800">ДРОППЕР / КАРТА</text>
          <rect x="178" y="134" width="32" height="22" rx="4" fill="#1e293b" stroke="#64748b"/>
          <text x="194" y="149" text-anchor="middle" fill="#e2e8f0" font-size="5">CARD</text>
          <path d="M212 145 L226 145" stroke="#94a3b8" stroke-width="1"/>
          <rect x="226" y="132" width="32" height="26" rx="4" fill="rgba(0,0,0,0.3)" stroke="#f59e0b"/>
          <text x="242" y="149" text-anchor="middle" fill="#fde68a" font-size="5">данные</text>
          <path d="M260 145 L274 145" stroke="#f87171" stroke-width="1.5" marker-end="url(#tf-arr-theft)"/>
          <rect x="276" y="136" width="24" height="20" rx="3" fill="rgba(220,38,38,0.25)" stroke="#dc2626"/>
          <text x="288" y="150" text-anchor="middle" fill="#fca5a5" font-size="5" font-weight="700">158</text>
          <text x="238" y="168" text-anchor="middle" fill="#94a3b8" font-size="5.5">обман → данные → тайное списание</text>
          <text x="238" y="180" text-anchor="middle" fill="#64748b" font-size="5">не ст. 159 при тайности</text>
        </svg>

        <div class="boris-theft-fraud-map__table-wrap">
          <table class="boris-theft-fraud-map__table">
            <thead>
              <tr>
                <th scope="col">Сценарий</th>
                <th scope="col">Механизм</th>
                <th scope="col">Статья</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Код из СМС</strong></td>
                <td>Обман → доступ → <strong>тайное</strong> списание с карты/счёта</td>
                <td class="boris-theft-fraud-map__qual--theft">ст. 158 п. «г» ч. 3</td>
              </tr>
              <tr>
                <td><strong>«Безопасный счёт»</strong></td>
                <td>Потерпевший <strong>сам</strong> инициировал перевод</td>
                <td class="boris-theft-fraud-map__qual--fraud">ст. 159</td>
              </tr>
              <tr>
                <td><strong>Цифровой рубль</strong></td>
                <td>Тайное списание со счёта цифровой валюты; окончание — момент списания</td>
                <td class="boris-theft-fraud-map__qual--theft">ст. 158</td>
              </tr>
              <tr>
                <td><strong>Дроппер / курьер</strong></td>
                <td>Данные карты под обманом → скрытое изъятие без взлома ПО</td>
                <td class="boris-theft-fraud-map__qual--theft">ст. 158 · п. 25.1</td>
              </tr>
              <tr>
                <td><strong>Серия списаний</strong></td>
                <td>Несколько операций с одного счёта при едином умысле</td>
                <td class="boris-theft-fraud-map__qual--theft">единое хищение · п. 25.3</td>
              </tr>
            </tbody>
          </table>
        </div>
        <p class="boris-theft-fraud-map__note"><strong>Защита:</strong> при квалификации по ст. 159 требуйте пересмотр, если доказано тайное списание; при п. «г» ч. 3 — учитывайте сумму и способ (аргументы смягчения). Пленум № 48 — о <em>мошенничестве</em>; № 19 — о <em>краже</em> и границе 158/159.</p>
        <p class="boris-theft-fraud-map__caption">Таблица-схема по п. 2, 6, 11, 25.1–25.3 Пленума № 29 (ред. 16.06.2026)</p>
      </div>
    </div>

    <div class="boris-theft-fraud-map__foot" aria-label="Нормативный контекст Пленума № 19">
      <span class="boris-theft-fraud-map__tag boris-theft-fraud-map__tag--plenum">Пленум ВС № 19 · 16.06.2026</span>
      <span class="boris-theft-fraud-map__tag boris-theft-fraud-map__tag--theft">ст. 158 · п. «г» ч. 3</span>
      <span class="boris-theft-fraud-map__tag boris-theft-fraud-map__tag--fraud">ст. 159 · мошенничество</span>
      <span class="boris-theft-fraud-map__tag boris-theft-fraud-map__tag--digital">цифровой рубль · CBDC</span>
    </div>
  </div>
</section>
```

## Передача Наташе

- **Якорь вставки:** `#boris-theft-fraud-map`
- **После H3:** «Типовые схемы: перевод под влиянием обмана vs тайное хищение после доступа»
- **Перед:** H3 «Переквалификация со ст. 159 на ст. 158…» и primary CTA Артура
- **MCP-only:** без `<canvas>` и `<script>`
