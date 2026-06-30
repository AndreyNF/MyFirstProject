=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok`  
**Якорь:** `l24-boris-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map`  
**Размещение для Наташи:** сразу **после H2 «Ничтожность сделок в обход спецпорядка (ст. 10, 168 ГК РФ)»** (после последнего H3 «Отличие ничтожной сделки от оспоримой в спорах о спецмерах»), **перед H2 «Продажа недвижимости без разрешения Правкомиссии (Указ № 81)»**.  
**Режим:** тёмная панель в теле статьи (**контраст** со светлым hero Алины по обзору ВС № 8/2026) — **карта трёх рисков + SVG «счёт С / 10 млн ₽ / счёт О»** вместо перечисления 22 позиций.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Метафора** | «Три коридора риска» от центрального узла спецмер (Указы 81/95/322) — сделки/платежи, ИС, санкционный процесс |
| **Цифры-крючки** | 10 млн ₽/мес., счета «С»/«О», 6+ млрд ₽ дробления, 46,5% порта, 22 позиции → 3 блока |
| **Палитра** | Тёмный navy `#0c1829`–`#1e3a5f` (контраст hero); риск `#f87171`; порог `#fbbf24`; ИС `#a78bfa`; процесс `#38bdf8` |
| **Композиция** | Сплит: SVG-карта счетов и указов \| сетка из 3 карточек риска + теги |

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после 2-й секции H2
- [x] Свой `id`: `l24-boris-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map` (не `l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым ARB-hero Алины (обзор ВС, спецмеры)
- [x] Сплит «SVG счёт С / 10 млн / счёт О + три коридора» | «3 карточки риска по п. 1–21»

```html
<section id="l24-boris-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map" class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map" aria-label="Обзор ВС № 8/2026: карта рисков ничтожности сделок — счета С и О, порог 10 млн рублей, три блока для бизнеса">
<style>
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map {
  --vs8rm-ink: #0c1829;
  --vs8rm-navy: #152238;
  --vs8rm-navy-soft: #1e3a5f;
  --vs8rm-gold: #fbbf24;
  --vs8rm-risk: #f87171;
  --vs8rm-risk-soft: #fecaca;
  --vs8rm-deal: #fb923c;
  --vs8rm-ip: #a78bfa;
  --vs8rm-ip-soft: #ddd6fe;
  --vs8rm-proc: #38bdf8;
  --vs8rm-proc-soft: #bae6fd;
  --vs8rm-muted: #94a3b8;
  --vs8rm-text: #e2e8f0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__shell {
  background: linear-gradient(152deg, var(--vs8rm-ink) 0%, var(--vs8rm-navy) 46%, var(--vs8rm-navy-soft) 100%);
  border: 1px solid rgba(56, 189, 248, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(12, 24, 41, 0.38);
  color: var(--vs8rm-text);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--vs8rm-gold);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--vs8rm-muted);
  max-width: 72ch;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__lead strong { color: #fff; }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__split {
  display: grid;
  grid-template-columns: minmax(0, 1.08fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__panel {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--vs8rm-gold);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__map-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 340px;
  margin-bottom: 12px;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__accounts {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account {
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border-top: 3px solid var(--vs8rm-proc);
  font-size: 0.72rem;
  line-height: 1.38;
  text-align: center;
  color: var(--vs8rm-muted);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account:nth-child(1) { border-top-color: var(--vs8rm-proc); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account:nth-child(2) { border-top-color: var(--vs8rm-gold); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account:nth-child(3) { border-top-color: var(--vs8rm-ip); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account strong {
  display: block;
  color: #fff;
  font-size: 0.82rem;
  margin-bottom: 4px;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(251, 191, 36, 0.1);
  border: 1px solid rgba(251, 191, 36, 0.35);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--vs8rm-text);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__verdict strong { color: var(--vs8rm-gold); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(148, 163, 184, 0.88);
  text-align: center;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risks {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk {
  margin: 0;
  padding: 14px 12px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.24);
  border-left: 3px solid var(--vs8rm-deal);
  font-size: 0.76rem;
  line-height: 1.42;
  color: #cbd5e1;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk--ip { border-left-color: var(--vs8rm-ip); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk--proc { border-left-color: var(--vs8rm-proc); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-tag {
  display: inline-block;
  margin-bottom: 6px;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  background: rgba(251, 146, 60, 0.18);
  color: var(--vs8rm-deal);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk--ip .vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-tag {
  background: rgba(167, 139, 250, 0.18);
  color: var(--vs8rm-ip);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk--proc .vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-tag {
  background: rgba(56, 189, 248, 0.18);
  color: var(--vs8rm-proc);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk strong {
  display: block;
  color: #fff;
  font-size: 0.82rem;
  margin-bottom: 5px;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk em {
  font-style: normal;
  font-weight: 600;
  color: #fff;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-facts {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-top: 8px;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact {
  font-size: 0.66rem;
  font-weight: 600;
  padding: 3px 7px;
  border-radius: 4px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--vs8rm-muted);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__note {
  margin: 12px 0 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--vs8rm-muted);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__note em {
  font-style: normal;
  color: var(--vs8rm-risk-soft);
  font-weight: 600;
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--vs8rm-text);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag--doc {
  border-color: rgba(251, 191, 36, 0.5);
  color: var(--vs8rm-gold);
}
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag--law { border-color: rgba(248, 113, 113, 0.45); color: var(--vs8rm-risk-soft); }
.vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag--proc { border-color: rgba(56, 189, 248, 0.45); color: var(--vs8rm-proc-soft); }
@media (max-width: 900px) {
  .vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__split { grid-template-columns: 1fr; }
  .vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__accounts { grid-template-columns: 1fr; }
}
</style>

  <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__shell">
    <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__eyebrow">ARB · обзор ВС № 8/2026 · № 11А/2026 · 17.06.2026 · Указы 81, 95, 322</p>
    <h3 class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__title">22 позиции ВС → три коридора риска: сделки, ИС и санкционный процесс</h3>
    <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__lead">Обзор не требует заучивать все 22 пункта: суды группируют практику вокруг <strong>ничтожности с момента сделки</strong> (ст. 10, 168 ГК РФ), спецсчетов <strong>«С»</strong> и <strong>«О»</strong> и порога <strong>10 млн ₽/мес.</strong> ФНС, Генпрокуратура и прокуратура активно оспаривают обходные схемы; суд вправе проверить уступку <strong>сам</strong> (п. 7).</p>

    <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__split">
      <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__panel">
        <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__panel-title">Узел спецмер: счёт «С» · 10 млн ₽ · счёт «О»</p>
        <svg class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__map-svg" viewBox="0 0 560 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="vs8rm-map-title vs8rm-map-desc">
          <title id="vs8rm-map-title">Карта рисков обзора ВС № 8/2026: три блока от узла спецмер и спецсчетов</title>
          <desc id="vs8rm-map-desc">Центральный узел Указы 81, 95, 322 со счетами С и О и порогом 10 миллионов рублей; три коридора риска — сделки и платежи, интеллектуальная собственность, санкционный процесс</desc>
          <defs>
            <linearGradient id="vs8rm-hub" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#1e3a5f"/>
              <stop offset="100%" stop-color="#0c1829"/>
            </linearGradient>
            <marker id="vs8rm-arr-deal" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#fb923c"/>
            </marker>
            <marker id="vs8rm-arr-ip" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#a78bfa"/>
            </marker>
            <marker id="vs8rm-arr-proc" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#38bdf8"/>
            </marker>
          </defs>

          <rect x="4" y="4" width="552" height="312" rx="14" fill="rgba(0,0,0,0.22)" stroke="#334155" stroke-width="1"/>

          <!-- Central hub -->
          <circle cx="280" cy="118" r="52" fill="url(#vs8rm-hub)" stroke="#fbbf24" stroke-width="2"/>
          <text x="280" y="104" text-anchor="middle" fill="#fbbf24" font-size="8" font-weight="700">СПЕЦМЕРЫ</text>
          <text x="280" y="118" text-anchor="middle" fill="#fff" font-size="7" font-weight="600">Указы 81 · 95 · 322</text>
          <text x="280" y="132" text-anchor="middle" fill="#94a3b8" font-size="6.5">ст. 10, 168 ГК РФ</text>

          <!-- Account S -->
          <rect x="88" y="168" width="96" height="56" rx="8" fill="#0f2744" stroke="#38bdf8" stroke-width="1.8"/>
          <text x="136" y="188" text-anchor="middle" fill="#38bdf8" font-size="9" font-weight="800">счёт «С»</text>
          <text x="136" y="202" text-anchor="middle" fill="#bae6fd" font-size="6.5">Указ № 95</text>
          <text x="136" y="214" text-anchor="middle" fill="#94a3b8" font-size="6">кредиторы</text>
          <path d="M184 196 L228 148" stroke="#38bdf8" stroke-width="1.8" fill="none"/>

          <!-- 10 mln threshold -->
          <rect x="232" y="178" width="96" height="56" rx="8" fill="#422006" stroke="#fbbf24" stroke-width="2"/>
          <text x="280" y="198" text-anchor="middle" fill="#fbbf24" font-size="10" font-weight="800">10 млн ₽</text>
          <text x="280" y="212" text-anchor="middle" fill="#fde68a" font-size="6.5">/ мес. · единоврем.</text>
          <text x="280" y="224" text-anchor="middle" fill="#94a3b8" font-size="6">п. 3–4 обзора</text>
          <line x1="280" y1="170" x2="280" y2="178" stroke="#fbbf24" stroke-width="1.8"/>

          <!-- Account O -->
          <rect x="376" y="168" width="96" height="56" rx="8" fill="#2e1065" stroke="#a78bfa" stroke-width="1.8"/>
          <text x="424" y="188" text-anchor="middle" fill="#a78bfa" font-size="9" font-weight="800">счёт «О»</text>
          <text x="424" y="202" text-anchor="middle" fill="#ddd6fe" font-size="6.5">Указ № 322</text>
          <text x="424" y="214" text-anchor="middle" fill="#94a3b8" font-size="6">правообладатели</text>
          <path d="M376 196 L332 148" stroke="#a78bfa" stroke-width="1.8" fill="none"/>

          <!-- Corridor 1: deals -->
          <path d="M228 88 L72 52" stroke="#fb923c" stroke-width="2.2" fill="none" marker-end="url(#vs8rm-arr-deal)"/>
          <rect x="8" y="24" width="128" height="58" rx="8" fill="rgba(251,146,60,0.14)" stroke="#fb923c" stroke-width="1.6"/>
          <text x="72" y="44" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Сделки и платежи</text>
          <text x="72" y="58" text-anchor="middle" fill="#fb923c" font-size="6.5" font-weight="600">п. 1–9</text>
          <text x="72" y="72" text-anchor="middle" fill="#94a3b8" font-size="5.8">недвижимость · дробление · цессия</text>

          <!-- Corridor 2: IP -->
          <path d="M332 88 L488 52" stroke="#a78bfa" stroke-width="2.2" fill="none" marker-end="url(#vs8rm-arr-ip)"/>
          <rect x="424" y="24" width="128" height="58" rx="8" fill="rgba(167,139,250,0.14)" stroke="#a78bfa" stroke-width="1.6"/>
          <text x="488" y="44" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">ИС и лицензии</text>
          <text x="488" y="58" text-anchor="middle" fill="#a78bfa" font-size="6.5" font-weight="600">п. 10–12</text>
          <text x="488" y="72" text-anchor="middle" fill="#94a3b8" font-size="5.8">РИД · счёт «О» · п. 17 «в»</text>

          <!-- Corridor 3: process -->
          <path d="M280 170 L280 248" stroke="#38bdf8" stroke-width="2.2" fill="none" marker-end="url(#vs8rm-arr-proc)"/>
          <rect x="196" y="248" width="168" height="58" rx="8" fill="rgba(56,189,248,0.12)" stroke="#38bdf8" stroke-width="1.6"/>
          <text x="280" y="268" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Санкционный процесс</text>
          <text x="280" y="282" text-anchor="middle" fill="#38bdf8" font-size="6.5" font-weight="600">п. 13–21</text>
          <text x="280" y="296" text-anchor="middle" fill="#94a3b8" font-size="5.8">ст. 248 АПК · иностр. арбитраж</text>

          <!-- Nullity stamp -->
          <rect x="196" y="88" width="168" height="22" rx="5" fill="rgba(248,113,113,0.16)" stroke="#f87171" stroke-width="1" stroke-dasharray="4 2"/>
          <text x="280" y="102" text-anchor="middle" fill="#fecaca" font-size="6.5" font-weight="700">НИЧТОЖНОСТЬ · с момента сделки · п. 7 — суд сам</text>

          <!-- decree badges -->
          <rect x="16" y="248" width="52" height="20" rx="4" fill="#1e3a5f" stroke="#64748b"/>
          <text x="42" y="261" text-anchor="middle" fill="#cbd5e1" font-size="6" font-weight="600">№ 81</text>
          <rect x="76" y="248" width="52" height="20" rx="4" fill="#1e3a5f" stroke="#64748b"/>
          <text x="102" y="261" text-anchor="middle" fill="#cbd5e1" font-size="6" font-weight="600">№ 95</text>
          <rect x="136" y="248" width="52" height="20" rx="4" fill="#1e3a5f" stroke="#64748b"/>
          <text x="162" y="261" text-anchor="middle" fill="#cbd5e1" font-size="6" font-weight="600">№ 322</text>
        </svg>

        <ul class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__accounts" aria-label="Спецсчета и пороги по Указам 95 и 322">
          <li class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account">
            <strong>счёт «С»</strong>
            Платежи иностранным кредиторам &gt; 10 млн ₽/мес. (Указ № 95)
          </li>
          <li class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account">
            <strong>10 млн ₽</strong>
            Дробление &lt; лимита не спасает — смотрят совокупность (п. 4: 6+ млрд ₽)
          </li>
          <li class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__account">
            <strong>счёт «О»</strong>
            Расчёты с правообладателями РИД — только с разрешения Правкомиссии (№ 322)
          </li>
        </ul>
        <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__verdict"><strong>Формула ВС:</strong> формальное соблюдение лимита по каждому платежу <em>не является иммунитетом</em> — суды оценивают суть операций и цепочки уступок.</p>
        <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__caption">Схема по обзору ВС № 8/2026 (постановление № 11А/2026 от 17.06.2026)</p>
      </div>

      <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__panel">
        <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__panel-title">Три блока риска для арбитражного спора</p>
        <ul class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risks">
          <li class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk">
            <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-tag">п. 1–9 · Указы 81, 95, 322</span>
            <strong>Сделки и платежи</strong>
            КП недвижимости без Правкомиссии — ничтожна (№ 81); платёж &gt; 10 млн ₽ не через «С» — ничтожен (п. 3, истец <em>ФНС</em>); искусственное дробление кредитов — ничтожно (п. 4); уступка и мировое соглашение-обход — отказ суда (п. 5–9).
            <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-facts">
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">6+ млрд ₽</span>
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">46,5% порта</span>
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">ФНС · Генпрокуратура</span>
            </div>
          </li>
          <li class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk--ip">
            <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-tag">п. 10–12 · РИД</span>
            <strong>ИС и лицензии</strong>
            Спецпорядок № 322 — на <em>все</em> обязательства по РИД, включая деликт (п. 10). Правообладатель снимает счёт «О», доказав работу в РФ (п. 11, п. 17 «в»). Принудительная лицензия — крайняя мера при злоупотреблении патентом (п. 12).
            <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-facts">
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">счёт «О»</span>
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">п. 17 «в»</span>
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">ст. 1362 ГК</span>
            </div>
          </li>
          <li class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk--proc">
            <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-tag">п. 13–21 · АПК</span>
            <strong>Санкционный процесс</strong>
            Брокер и банк — ограниченная ответственность при санкционных блокировках (п. 13–14). <em>Ст. 248.1–248.2 АПК</em>: арбитражная оговорка не блокирует подсудность РФ; запрет въезда = санкция (п. 15–17). Иностранные решения — проверка публичного порядка (п. 19–20); судебная неустойка за иностранное разбирательство (п. 21).
            <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-facts">
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">ст. 248.1 АПК</span>
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">Euroclear</span>
              <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__risk-fact">публичный порядок</span>
            </div>
          </li>
        </ul>
        <p class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__note"><em>Ответчик:</em> иск ФНС о ничтожности платежа, суд проверит цессию сам. <em>Истец:</em> пересмотр по вновь открывшимся обстоятельствам (п. 8, ст. 309–311 АПК).</p>
      </div>
    </div>

    <div class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__foot" aria-label="Контекст обзора ВС № 8/2026">
      <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag--doc">ВС № 8/2026 · № 11А/2026 · 22 позиции</span>
      <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag--law">ст. 10, 168 ГК · ничтожность</span>
      <span class="vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map__tag--proc">ст. 248.1–248.2 АПК · подсудность РФ</span>
    </div>
  </div>
</section>
```

## Передача Наташе

- **Якорь вставки:** `#l24-boris-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok-risk-map`
- **После H2:** «Ничтожность сделок в обход спецпорядка (ст. 10, 168 ГК РФ)»
- **Перед H2:** «Продажа недвижимости без разрешения Правкомиссии (Указ № 81)»
- **MCP-only:** без `<canvas>` и `<script>`
