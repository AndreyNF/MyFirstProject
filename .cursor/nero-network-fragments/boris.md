=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `sip-sinergetik-766-mln-otmena-kompensaciya-tz`  
**Якорь:** `l24-boris-sip-sinergetik-instances`  
**Размещение:** сразу после H2 «Инстанции: от отказа до 766 млн и обратно» (перед H3 «Первая инстанция…») или после вводного абзаца H2 «Судебная практика СИП 2026» — по сетке Natasha; якорь для вставки блока.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **маршрут 3 инстанций** + чек-лист оснований **ответчика**.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-sip-sinergetik-instances" class="l24-boris-sinergetik" aria-label="Дело Синергетик: три инстанции — отказ, 766 млн на апелляции, отмена в СИП — и основания ответчика">
<style>
.l24-boris-sinergetik {
  --sin-navy: #0f2744;
  --sin-navy-soft: #1a365d;
  --sin-first: #48bb78;
  --sin-appeal: #ed8936;
  --sin-sip: #c53030;
  --sin-gold: #ecc94b;
  --sin-mint: #68d391;
  --sin-ink: #e2e8f0;
  --sin-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-sinergetik__shell {
  background: linear-gradient(148deg, var(--sin-navy) 0%, #152a45 52%, var(--sin-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--sin-ink);
}
.l24-boris-sinergetik__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--sin-gold);
}
.l24-boris-sinergetik__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-sinergetik__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--sin-muted);
  max-width: 68ch;
}
.l24-boris-sinergetik__lead strong { color: #fff; }
.l24-boris-sinergetik__split {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-sinergetik__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-sinergetik__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--sin-gold);
}
.l24-boris-sinergetik__route-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 248px;
  margin-bottom: 12px;
}
.l24-boris-sinergetik__stages {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-sinergetik__stage {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-left: 3px solid var(--sin-first);
  font-size: 0.74rem;
  line-height: 1.4;
}
.l24-boris-sinergetik__stage:nth-child(2) { border-left-color: var(--sin-appeal); }
.l24-boris-sinergetik__stage:nth-child(3) { border-left-color: var(--sin-sip); }
.l24-boris-sinergetik__stage--wide {
  grid-column: 1 / -1;
  border-left-color: var(--sin-mint);
}
.l24-boris-sinergetik__stage strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 3px;
}
.l24-boris-sinergetik__amounts {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-sinergetik__amount {
  padding: 10px 8px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  text-align: center;
  font-size: 0.72rem;
  line-height: 1.35;
}
.l24-boris-sinergetik__amount--claim {
  grid-column: 1 / -1;
  border-color: rgba(237, 137, 54, 0.45);
  background: rgba(237, 137, 54, 0.12);
}
.l24-boris-sinergetik__amount-label {
  display: block;
  font-size: 0.66rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--sin-muted);
  margin-bottom: 4px;
}
.l24-boris-sinergetik__amount-value {
  display: block;
  font-size: 0.88rem;
  font-weight: 800;
  color: #fff;
}
.l24-boris-sinergetik__grounds {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-sinergetik__ground {
  display: grid;
  grid-template-columns: minmax(0, 1.05fr) minmax(0, 0.95fr);
  gap: 8px 10px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-sinergetik__ground--mix { border-left: 3px solid var(--sin-first); }
.l24-boris-sinergetik__ground--desc { border-left: 3px solid var(--sin-gold); }
.l24-boris-sinergetik__ground--abuse { border-left: 3px solid var(--sin-appeal); }
.l24-boris-sinergetik__ground--comp { border-left: 3px solid var(--sin-sip); }
.l24-boris-sinergetik__ground-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-sinergetik__ground-text {
  color: var(--sin-muted);
}
.l24-boris-sinergetik__ground-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-sinergetik__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-sinergetik__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-sinergetik__vs-card--risk { border-color: rgba(237, 137, 54, 0.45); }
.l24-boris-sinergetik__vs-card--win { border-color: rgba(104, 211, 145, 0.45); }
.l24-boris-sinergetik__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-sinergetik__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--sin-muted);
}
.l24-boris-sinergetik__note em {
  font-style: normal;
  color: var(--sin-mint);
  font-weight: 600;
}
.l24-boris-sinergetik__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-sinergetik__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--sin-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-sinergetik__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--sin-gold);
}
.l24-boris-sinergetik__tag--def { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
.l24-boris-sinergetik__tag--claim { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-sinergetik__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
@media (max-width: 900px) {
  .l24-boris-sinergetik__split { grid-template-columns: 1fr; }
  .l24-boris-sinergetik__stages { grid-template-columns: 1fr; }
  .l24-boris-sinergetik__stage--wide { grid-column: auto; }
  .l24-boris-sinergetik__ground {
    grid-template-columns: 1fr;
    gap: 4px;
  }
  .l24-boris-sinergetik__vs { grid-template-columns: 1fr; }
  .l24-boris-sinergetik__amounts { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-sinergetik__shell">
    <p class="l24-boris-sinergetik__eyebrow">ст. 1484 · 1515 · 10 ч. 2 · А43-1470/2024 · С01-1920/2025 · ТЗ № 312760</p>
    <h3 class="l24-boris-sinergetik__title">Три инстанции «Синергетик»: отказ → 766 млн → отмена в СИП</h3>
    <p class="l24-boris-sinergetik__lead">Иск ИП Богуславской к ООО «<strong>Синергетик</strong>» за слоган «<strong>я ♥ свою семью!</strong>» на упаковке прошёл полный цикл арбитража: <strong>первая инстанция отказала</strong>, <strong>апелляция взыскала 766 050 650 ₽</strong>, <strong>СИП 20.03.2026 отменил</strong> постановление апелляции и оставил отказ. Справа — четыре блока защиты <strong>ответчика</strong>, на которых держалось решение кассации.</p>

    <div class="l24-boris-sinergetik__split">
      <div class="l24-boris-sinergetik__panel">
        <p class="l24-boris-sinergetik__panel-title">Маршрут дела № А43-1470/2024</p>
        <svg class="l24-boris-sinergetik__route-svg" viewBox="0 0 540 210" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="sin-route-title sin-route-desc">
          <title id="sin-route-title">Схема: 1-я инстанция отказ, апелляция 766 млн, СИП отмена</title>
          <desc id="sin-route-desc">Арбитраж Нижегородской области отказал в иске. Первый ААС взыскал 766 млн. СИП отменил апелляцию и оставил отказ.</desc>
          <defs>
            <linearGradient id="sin-inst-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#48bb78"/>
              <stop offset="42%" stop-color="#ed8936"/>
              <stop offset="100%" stop-color="#48bb78"/>
            </linearGradient>
            <marker id="sin-arr-up" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#68d391"/>
            </marker>
            <marker id="sin-arr-down" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0 0 L8 4 L0 8 Z" fill="#ed8936"/>
            </marker>
          </defs>
          <path d="M 72 72 L 270 72 L 468 72" stroke="url(#sin-inst-line)" stroke-width="4" stroke-linecap="round" fill="none"/>
          <path d="M 270 72 L 270 118" stroke="#ed8936" stroke-width="2.5" fill="none" marker-end="url(#sin-arr-down)"/>
          <path d="M 270 118 L 468 118 L 468 72" stroke="#68d391" stroke-width="2.5" fill="none" marker-end="url(#sin-arr-up)"/>

          <circle cx="72" cy="72" r="28" fill="#2f855a" stroke="#fff" stroke-width="2"/>
          <text x="72" y="68" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">1-я</text>
          <text x="72" y="80" text-anchor="middle" fill="#c6f6d5" font-size="7">отказ</text>

          <circle cx="270" cy="72" r="30" fill="#c05621" stroke="#fff" stroke-width="2"/>
          <text x="270" y="68" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Апелл.</text>
          <text x="270" y="80" text-anchor="middle" fill="#feebc8" font-size="7">766 млн</text>

          <circle cx="468" cy="72" r="28" fill="#c53030" stroke="#fff" stroke-width="2"/>
          <text x="468" y="68" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">СИП</text>
          <text x="468" y="80" text-anchor="middle" fill="#fed7d7" font-size="7">20.03.26</text>

          <rect x="32" y="128" width="140" height="36" rx="6" fill="rgba(0,0,0,0.35)"/>
          <text x="102" y="144" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="600">упаковка целиком</text>
          <text x="102" y="156" text-anchor="middle" fill="#e2e8f0" font-size="7">злоупотребление · ст. 10</text>

          <rect x="200" y="138" width="140" height="36" rx="6" fill="rgba(237,137,54,0.2)" stroke="#ed8936" stroke-width="1"/>
          <text x="270" y="154" text-anchor="middle" fill="#faf089" font-size="8" font-weight="700">766 050 650 ₽</text>
          <text x="270" y="166" text-anchor="middle" fill="#e2e8f0" font-size="7">+ запрет · 250 тыс./наруш.</text>

          <rect x="368" y="128" width="140" height="36" rx="6" fill="rgba(0,0,0,0.35)"/>
          <text x="438" y="144" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="600">отмена апелляции</text>
          <text x="438" y="156" text-anchor="middle" fill="#e2e8f0" font-size="7">отказ сохранён</text>

          <text x="72" y="38" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="600">~10,7 млрд → отказ</text>
          <text x="270" y="38" text-anchor="middle" fill="#feb2b2" font-size="8" font-weight="600">сходство «до смешения»</text>
          <text x="468" y="38" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="600">нет смешения</text>

          <text x="270" y="196" text-anchor="middle" fill="#a0aec0" font-size="7">период компенсации: 01.08.2022 – 31.07.2024 · ТЗ «Я ЛЮБЛЮ СВОЮ СЕМЬЮ» № 312760</text>
        </svg>

        <div class="l24-boris-sinergetik__amounts" aria-label="Суммы по инстанциям">
          <div class="l24-boris-sinergetik__amount">
            <span class="l24-boris-sinergetik__amount-label">1-я инстанция</span>
            <span class="l24-boris-sinergetik__amount-value">0 ₽</span>
          </div>
          <div class="l24-boris-sinergetik__amount">
            <span class="l24-boris-sinergetik__amount-label">Апелляция</span>
            <span class="l24-boris-sinergetik__amount-value">766 млн</span>
          </div>
          <div class="l24-boris-sinergetik__amount">
            <span class="l24-boris-sinergetik__amount-label">СИП</span>
            <span class="l24-boris-sinergetik__amount-value">отмена</span>
          </div>
          <div class="l24-boris-sinergetik__amount l24-boris-sinergetik__amount--claim">
            <span class="l24-boris-sinergetik__amount-label">Лицензия истца за тот же период vs иск</span>
            <span class="l24-boris-sinergetik__amount-value">~451 тыс. ₽ · разрыв ~1830×</span>
          </div>
        </div>

        <ol class="l24-boris-sinergetik__stages">
          <li class="l24-boris-sinergetik__stage">
            <strong>АС Нижегородской области</strong>
            Отказ: фраза — элемент дизайна; SYNERGETIC доминирует; признаки злоупотребления правом.
          </li>
          <li class="l24-boris-sinergetik__stage">
            <strong>1-й ААС</strong>
            Сходство до смешения; 766 050 650 ₽ по ст. 1515; запрет оборота; неустойка 250 000 ₽ за нарушение.
          </li>
          <li class="l24-boris-sinergetik__stage">
            <strong>СИП · 20.03.2026</strong>
            № С01-1920/2025: отмена апелляции; сильные/слабые элементы не оценены; отказ в силе.
          </li>
          <li class="l24-boris-sinergetik__stage l24-boris-sinergetik__stage--wide">
            <strong>≠ POIZON (оспаривание регистрации)</strong>
            Здесь знак № 312760 действовал — спор о нарушении и компенсации на этикетке FMCG, не об аннулировании свидетельства.
          </li>
        </ol>
        <p class="l24-boris-sinergetik__caption">Хронология по Sostav, BBNP, постановлению СИП от 20.03.2026</p>
      </div>

      <div class="l24-boris-sinergetik__panel">
        <p class="l24-boris-sinergetik__panel-title">Основания ответчика (чек-лист)</p>
        <div class="l24-boris-sinergetik__vs">
          <div class="l24-boris-sinergetik__vs-card l24-boris-sinergetik__vs-card--risk">
            <strong>Риск апелляции</strong>
            Формальное сходство слов («люблю» / ♥ / «семью») без анализа всей упаковки → полный расчёт истца.
          </div>
          <div class="l24-boris-sinergetik__vs-card l24-boris-sinergetik__vs-card--win">
            <strong>Линия СИП</strong>
            Нет смешения при доминировании бренда ответчика; использование не как чужого ТЗ; злоупотребление истца.
          </div>
        </div>
        <div class="l24-boris-sinergetik__grounds">
          <div class="l24-boris-sinergetik__ground l24-boris-sinergetik__ground--mix">
            <span class="l24-boris-sinergetik__ground-label">Смешение · ст. 1484</span>
            <span class="l24-boris-sinergetik__ground-text">Сравнение <em>упаковки в целом</em>: SYNERGETIC, цвет, композиция; потребитель не путает с ТЗ № 312760 при формальном сходстве фразы.</span>
          </div>
          <div class="l24-boris-sinergetik__ground l24-boris-sinergetik__ground--desc">
            <span class="l24-boris-sinergetik__ground-label">Описательность · ст. 1483</span>
            <span class="l24-boris-sinergetik__ground-text">Общеупотребимая формула о семье; СИП — «разумные ожидания» правообладателя при регистрации; слоган как <em>декор</em>, не маркировка происхождения.</span>
          </div>
          <div class="l24-boris-sinergetik__ground l24-boris-sinergetik__ground--abuse">
            <span class="l24-boris-sinergetik__ground-label">Злоупотребление · ст. 10 ч. 2</span>
            <span class="l24-boris-sinergetik__ground-text">Портфель <em>400+</em> ТЗ; давление на FMCG; разрыв лицензии (~451 тыс.) и требований (766 млн) — недобросовестность истца.</span>
          </div>
          <div class="l24-boris-sinergetik__ground l24-boris-sinergetik__ground--comp">
            <span class="l24-boris-sinergetik__ground-label">Расчёт компенсации · ст. 1515</span>
            <span class="l24-boris-sinergetik__ground-text">Нет нарушения → нет взыскания; альтернативный расчёт, период 2022–2024, соразмерность; оспаривать и <em>неустойку 250 000 ₽</em> за нарушение запрета.</span>
          </div>
        </div>
        <p class="l24-boris-sinergetik__note"><em>Кассация в СИП</em> после проигрыша в апелляции — типичный путь при крупных исках по ТЗ (гл. 37 АПК). Не дублировать спор по существу, если решение 1-й инстанции полное и в вашу пользу.</p>
      </div>
    </div>

    <div class="l24-boris-sinergetik__foot" aria-label="Роли в споре">
      <span class="l24-boris-sinergetik__tag l24-boris-sinergetik__tag--case">А43-1470/2024 · Богуславская / «Синергетик»</span>
      <span class="l24-boris-sinergetik__tag l24-boris-sinergetik__tag--def">Ответчик: упаковка · отзыв · кассация СИП</span>
      <span class="l24-boris-sinergetik__tag l24-boris-sinergetik__tag--claim">Истец: 10,7 млрд → 766 млн · 01.08.22–31.07.24</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 про инстанции / судебную практику
- [x] Свой `id`: `l24-boris-sip-sinergetik-instances` (не hero `#l24-hero-sip-sinergetik-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + SVG
- [x] Сплит «маршрут 3 инстанций | чек-лист ответчика», глубина как `l24-boris-poizon-sip`
