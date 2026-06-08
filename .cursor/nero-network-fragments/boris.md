=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `vs-google-earth-dokazatelstva-moshennichestvo-zashchita-2026`  
**Якорь:** `l24-boris-google-earth-evidence`  
**Размещение:** сразу после H2 «Выписки ЕГРН, показания свидетелей и заключения специалистов» (перед H3 «Выписка ЕГРН и соседние участки…») — якорь для Natasha.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **схема комплексной оценки улик** по ст. 88 УПК: Google Earth Pro vs выписки ЕГРН vs показания свидетелей в деле о мошенничестве (ст. 159 УК РФ).  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-google-earth-evidence" class="l24-boris-ge-evidence" aria-label="Схема оценки доказательств: Google Earth Pro, выписки ЕГРН и показания свидетелей при обвинении по ст. 159 УК РФ">
<style>
.l24-boris-ge-evidence {
  --ge-navy: #0c1f33;
  --ge-navy-soft: #163352;
  --ge-satellite: #38b2ac;
  --ge-satellite-dim: #2c7a7b;
  --ge-registry: #4299e1;
  --ge-witness: #68d391;
  --ge-danger: #fc8181;
  --ge-gold: #ecc94b;
  --ge-land: #9ae6b4;
  --ge-ink: #e2e8f0;
  --ge-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ge-evidence__shell {
  background: linear-gradient(152deg, var(--ge-navy) 0%, #122a42 48%, var(--ge-navy-soft) 100%);
  border: 1px solid rgba(56, 178, 172, 0.28);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(12, 31, 51, 0.32);
  color: var(--ge-ink);
}
.l24-boris-ge-evidence__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ge-gold);
}
.l24-boris-ge-evidence__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ge-evidence__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ge-muted);
  max-width: 72ch;
}
.l24-boris-ge-evidence__lead strong { color: #fff; }
.l24-boris-ge-evidence__split {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ge-evidence__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ge-evidence__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ge-gold);
}
.l24-boris-ge-evidence__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 300px;
  margin-bottom: 12px;
}
.l24-boris-ge-evidence__sources {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 0 0 12px;
  padding: 0;
  list-style: none;
}
.l24-boris-ge-evidence__source {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-top: 3px solid var(--ge-satellite);
  font-size: 0.72rem;
  line-height: 1.38;
}
.l24-boris-ge-evidence__source:nth-child(2) { border-top-color: var(--ge-registry); }
.l24-boris-ge-evidence__source:nth-child(3) { border-top-color: var(--ge-witness); }
.l24-boris-ge-evidence__source strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-ge-evidence__verdict {
  margin: 0;
  padding: 12px 14px;
  border-radius: 8px;
  background: rgba(236, 201, 75, 0.12);
  border: 1px solid rgba(236, 201, 75, 0.38);
  font-size: 0.78rem;
  line-height: 1.45;
  color: var(--ge-ink);
}
.l24-boris-ge-evidence__verdict strong { color: var(--ge-gold); }
.l24-boris-ge-evidence__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
.l24-boris-ge-evidence__matrix {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-ge-evidence__row {
  display: grid;
  grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
  gap: 8px 10px;
  align-items: start;
  padding: 10px 11px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.38;
}
.l24-boris-ge-evidence__row--gis { border-left: 3px solid var(--ge-satellite); }
.l24-boris-ge-evidence__row--egrn { border-left: 3px solid var(--ge-registry); }
.l24-boris-ge-evidence__row--wit { border-left: 3px solid var(--ge-witness); }
.l24-boris-ge-evidence__row--law { border-left: 3px solid var(--ge-gold); }
.l24-boris-ge-evidence__row-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-ge-evidence__row-text { color: var(--ge-muted); }
.l24-boris-ge-evidence__row-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-ge-evidence__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-ge-evidence__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-ge-evidence__vs-card--pros { border-color: rgba(252, 129, 129, 0.45); }
.l24-boris-ge-evidence__vs-card--def { border-color: rgba(104, 211, 145, 0.45); }
.l24-boris-ge-evidence__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-ge-evidence__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--ge-muted);
}
.l24-boris-ge-evidence__note em {
  font-style: normal;
  color: var(--ge-land);
  font-weight: 600;
}
.l24-boris-ge-evidence__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ge-evidence__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--ge-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-ge-evidence__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--ge-gold);
}
.l24-boris-ge-evidence__tag--art { border-color: rgba(56, 178, 172, 0.45); color: #b2f5ea; }
.l24-boris-ge-evidence__tag--def { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
@media (max-width: 900px) {
  .l24-boris-ge-evidence__split { grid-template-columns: 1fr; }
  .l24-boris-ge-evidence__sources { grid-template-columns: 1fr; }
  .l24-boris-ge-evidence__row { grid-template-columns: 1fr; gap: 4px; }
  .l24-boris-ge-evidence__vs { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-ge-evidence__shell">
    <p class="l24-boris-ge-evidence__eyebrow">ст. 88 УПК · ст. 159 УК · дело № 24-УД26-1-К4 · ВС 04.06.2026</p>
    <h3 class="l24-boris-ge-evidence__title">Схема оценки доказательств: Google Earth Pro, ЕГРН и свидетели</h3>
    <p class="l24-boris-ge-evidence__lead">В деле <strong>Сергея Аверченкова</strong> (Адыгея) Верховный суд отменил приговор по <strong>ст. 159 УК РФ</strong>: нижестоящие суды приняли протокол осмотра <strong>Google Earth Pro</strong> без мотивированного сопоставления с <strong>выписками ЕГРН</strong> и <strong>показаниями свидетелей</strong>. По <strong>ст. 88 УПК РФ</strong> ни одна улика не имеет заранее установленной силы — при противоречиях суд обязан указать, почему принял одни материалы и отверг другие.</p>

    <div class="l24-boris-ge-evidence__split">
      <div class="l24-boris-ge-evidence__panel">
        <p class="l24-boris-ge-evidence__panel-title">Три источника улик → комплексная оценка суда</p>
        <svg class="l24-boris-ge-evidence__scheme-svg" viewBox="0 0 580 280" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="ge-scheme-title ge-scheme-desc">
          <title id="ge-scheme-title">Схема сопоставления Google Earth Pro, выписки ЕГРН и показаний свидетелей при обвинении по ст. 159</title>
          <desc id="ge-scheme-desc">Три столпа доказательств сходятся к суду первой инстанции; при противоречии Верховный суд требует мотивированного выбора по ст. 88 УПК РФ, а не осуждения только по GIS-снимку</desc>
          <defs>
            <linearGradient id="ge-flow" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#38b2ac"/>
              <stop offset="50%" stop-color="#4299e1"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
            <marker id="ge-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
            <pattern id="ge-grid" width="12" height="12" patternUnits="userSpaceOnUse">
              <path d="M12 0 L0 0 0 12" fill="none" stroke="rgba(56,178,172,0.25)" stroke-width="0.5"/>
            </pattern>
          </defs>
          <!-- GIS column -->
          <rect x="24" y="36" width="148" height="108" rx="8" fill="rgba(44,122,122,0.35)" stroke="#38b2ac" stroke-width="1.5"/>
          <rect x="32" y="48" width="132" height="64" rx="4" fill="url(#ge-grid)"/>
          <circle cx="98" cy="72" r="14" fill="none" stroke="#fc8181" stroke-width="2" stroke-dasharray="4 2"/>
          <text x="98" y="76" text-anchor="middle" fill="#fc8181" font-size="10" font-weight="700">✕</text>
          <text x="98" y="44" text-anchor="middle" fill="#b2f5ea" font-size="9" font-weight="700">Google Earth Pro</text>
          <text x="98" y="124" text-anchor="middle" fill="#a0aec0" font-size="7.5">исторический слой · постройки не видны</text>
          <text x="98" y="136" text-anchor="middle" fill="#fed7d7" font-size="7.5">обвинение: «ложные сведения»</text>
          <!-- EGRN column -->
          <rect x="216" y="36" width="148" height="108" rx="8" fill="rgba(49,130,206,0.28)" stroke="#4299e1" stroke-width="1.5"/>
          <rect x="228" y="52" width="124" height="72" rx="4" fill="rgba(0,0,0,0.25)" stroke="#90cdf4" stroke-width="1"/>
          <text x="290" y="44" text-anchor="middle" fill="#bee3f8" font-size="9" font-weight="700">Выписка ЕГРН</text>
          <text x="238" y="68" fill="#e2e8f0" font-size="7">соседний уч. · постройка</text>
          <text x="238" y="82" fill="#e2e8f0" font-size="7">зарегистрирована</text>
          <text x="238" y="100" fill="#90cdf4" font-size="7">на том же снимке —</text>
          <text x="238" y="114" fill="#90cdf4" font-size="7">тоже «не видна»</text>
          <text x="290" y="136" text-anchor="middle" fill="#c6f6d5" font-size="7.5">сопоставительный тест</text>
          <!-- Witness column -->
          <rect x="408" y="36" width="148" height="108" rx="8" fill="rgba(47,133,90,0.28)" stroke="#68d391" stroke-width="1.5"/>
          <circle cx="452" cy="78" r="12" fill="#2f855a" stroke="#fff" stroke-width="1.5"/>
          <circle cx="500" cy="78" r="12" fill="#2f855a" stroke="#fff" stroke-width="1.5"/>
          <text x="482" y="44" text-anchor="middle" fill="#c6f6d5" font-size="9" font-weight="700">Свидетели</text>
          <text x="452" y="82" text-anchor="middle" fill="#fff" font-size="8">1</text>
          <text x="500" y="82" text-anchor="middle" fill="#fff" font-size="8">2</text>
          <text x="482" y="104" text-anchor="middle" fill="#e2e8f0" font-size="7.5">покупательница участка</text>
          <text x="482" y="118" text-anchor="middle" fill="#e2e8f0" font-size="7.5">+ очевидец постройки</text>
          <text x="482" y="136" text-anchor="middle" fill="#9ae6b4" font-size="7.5">постройка существовала</text>
          <!-- Convergence arrows -->
          <path d="M 98 156 L 98 188 L 290 188 L 290 208" stroke="#38b2ac" stroke-width="2" fill="none" marker-end="url(#ge-arrow)"/>
          <path d="M 290 156 L 290 188" stroke="#4299e1" stroke-width="2" fill="none"/>
          <path d="M 482 156 L 482 188 L 290 188" stroke="#68d391" stroke-width="2" fill="none"/>
          <!-- Lower courts (error) -->
          <rect x="168" y="212" width="244" height="36" rx="6" fill="rgba(252,129,129,0.22)" stroke="#fc8181" stroke-width="1.2"/>
          <text x="290" y="228" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="600">Суды 1-й / апелляции / кассации</text>
          <text x="290" y="240" text-anchor="middle" fill="#feb2b2" font-size="7.5">приняли GIS · не оценили ЕГРН и свидетелей</text>
          <!-- VS correction -->
          <rect x="108" y="252" width="364" height="24" rx="5" fill="rgba(236,201,75,0.18)" stroke="#ecc94b" stroke-width="1.5"/>
          <text x="290" y="268" text-anchor="middle" fill="#ecc94b" font-size="8.5" font-weight="700">ВС 04.06.2026 · ст. 88 УПК · отмена · новое апелляционное рассмотрение</text>
          <text x="290" y="18" text-anchor="middle" fill="#ecc94b" font-size="8" font-weight="600">Противоречие улик → обязательное сопоставление, не единственный снимок</text>
        </svg>
        <ul class="l24-boris-ge-evidence__sources" aria-label="Три типа доказательств в деле Аверченкова">
          <li class="l24-boris-ge-evidence__source">
            <strong>Google Earth Pro</strong>
            Протокол осмотра экрана; исторический аэрофотослой. Слабое звено: дата слоя, разрешение, объекты под кроной.
          </li>
          <li class="l24-boris-ge-evidence__source">
            <strong>ЕГРН</strong>
            Выписки о постройках на соседних участках — «не видны» на тех же снимках. Дискредитирует GIS как единственный источник.
          </li>
          <li class="l24-boris-ge-evidence__source">
            <strong>Свидетели</strong>
            Покупательница и второй свидетель подтвердили хозяйственную постройку. Суды не мотивировали отклонение.
          </li>
        </ul>
        <p class="l24-boris-ge-evidence__verdict"><strong>Вывод ВС:</strong> при противоречивых доказательствах существенного значения нельзя осудить по ст. 159, опираясь только на картографический слой — нужна таблица сопоставления и мотивы в приговоре.</p>
        <p class="l24-boris-ge-evidence__caption">Схема по материалам РАПСИ 04–06.06.2026; дело № 24-УД26-1-К4 · Аверченков · Республика Адыгея</p>
      </div>

      <div class="l24-boris-ge-evidence__panel">
        <p class="l24-boris-ge-evidence__panel-title">Матрица оценки по ст. 88 УПК (чек-лист защиты)</p>
        <div class="l24-boris-ge-evidence__vs">
          <div class="l24-boris-ge-evidence__vs-card l24-boris-ge-evidence__vs-card--pros">
            <strong>Обвинение</strong>
            GIS-снимок как «объективное» доказательство отсутствия постройки; протокол осмотра по ст. 166 УПК.
          </div>
          <div class="l24-boris-ge-evidence__vs-card l24-boris-ge-evidence__vs-card--def">
            <strong>Защита</strong>
            Сопоставительный тест ЕГРН, показания контрагента, заключения специалистов о методике фиксации аэрофото.
          </div>
        </div>
        <div class="l24-boris-ge-evidence__matrix">
          <div class="l24-boris-ge-evidence__row l24-boris-ge-evidence__row--gis">
            <span class="l24-boris-ge-evidence__row-label">Google Earth / GIS</span>
            <span class="l24-boris-ge-evidence__row-text">Допустим через протокол (<em>ст. 74, 166, 180 УПК</em>), но не заменяет комплекс. Проверить: версия ПО, дата слоя, координаты, масштаб.</span>
          </div>
          <div class="l24-boris-ge-evidence__row l24-boris-ge-evidence__row--egrn">
            <span class="l24-boris-ge-evidence__row-label">Выписка ЕГРН</span>
            <span class="l24-boris-ge-evidence__row-text">Соседние участки с зарегистрированными постройками, невидимыми на том же снимке — <em>контртест достоверности</em> картографического слоя.</span>
          </div>
          <div class="l24-boris-ge-evidence__row l24-boris-ge-evidence__row--wit">
            <span class="l24-boris-ge-evidence__row-label">Показания свидетелей</span>
            <span class="l24-boris-ge-evidence__row-text">Покупатель участка и очевидцы — прямое опровержение версии о «фиктивной» постройке; суд обязан мотивировать отклонение.</span>
          </div>
          <div class="l24-boris-ge-evidence__row l24-boris-ge-evidence__row--law">
            <span class="l24-boris-ge-evidence__row-label">ст. 88 УПК РФ</span>
            <span class="l24-boris-ge-evidence__row-text">Никакие улики без <em>заранее установленной силы</em>; противоречия разрешаются сопоставлением; в приговоре — мотивы принятия и отклонения.</span>
          </div>
        </div>
        <p class="l24-boris-ge-evidence__note"><em>ст. 159 УК РФ:</em> умысел и обман должны быть доказаны до регистрации права; цифровой снимок без ЕГРН, свидетелей и экспертизы методики — недостаточная база для приговора после позиции ВС 2026 года.</p>
      </div>
    </div>

    <div class="l24-boris-ge-evidence__foot" aria-label="Контекст дела">
      <span class="l24-boris-ge-evidence__tag l24-boris-ge-evidence__tag--case">ВС 04.06.2026 · № 24-УД26-1-К4</span>
      <span class="l24-boris-ge-evidence__tag l24-boris-ge-evidence__tag--art">ст. 159 УК · льготная приватизация · Росреестр</span>
      <span class="l24-boris-ge-evidence__tag l24-boris-ge-evidence__tag--def">Защита: комплексная оценка, не один скриншот</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 про ЕГРН, свидетелей и специалистов
- [x] Свой `id`: `l24-boris-google-earth-evidence` (не hero `#l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым hero Алины (земельный / уголовный кейс)
- [x] Сплит «схема трёх источников улик + вердикт ВС | матрица оценки по ст. 88 УПК»
