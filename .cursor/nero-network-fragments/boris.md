=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**SLUG:** `vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany`  
**Якорь:** `l24-boris-vs-kompensaciya-ukaz322`  
**Размещение:** сразу после H2 «Иностранный правообладатель и недружественные страны: Указ Президента № 322» (перед H3 «Недружественные страны товарный знак и пп. «в» п. 17…») — якорь для Natasha.  
**Режим:** тёмная панель в теле статьи (контраст со светлым hero Алины) — **цепочка лицензия → цессия → иск к ИП на МП** + чек-лист проверки **пп. «в» п. 17** Указа № 322.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<canvas>` и `<script>`.

```html
<section id="l24-boris-vs-kompensaciya-ukaz322" class="l24-boris-ukaz322" aria-label="Цепочка права на товарный знак: иностранный правообладатель, лицензия, цессия, иск к ИП на маркетплейсе и проверка пп. в п. 17 Указа № 322">
<style>
.l24-boris-ukaz322 {
  --uk-navy: #0f2744;
  --uk-navy-soft: #1a365d;
  --uk-foreign: #ed8936;
  --uk-license: #4299e1;
  --uk-cession: #9f7aea;
  --uk-claim: #fc8181;
  --uk-check: #68d391;
  --uk-gold: #ecc94b;
  --uk-mint: #9ae6b4;
  --uk-ink: #e2e8f0;
  --uk-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ukaz322__shell {
  background: linear-gradient(148deg, var(--uk-navy) 0%, #152a45 52%, var(--uk-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--uk-ink);
}
.l24-boris-ukaz322__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--uk-gold);
}
.l24-boris-ukaz322__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ukaz322__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--uk-muted);
  max-width: 68ch;
}
.l24-boris-ukaz322__lead strong { color: #fff; }
.l24-boris-ukaz322__split {
  display: grid;
  grid-template-columns: minmax(0, 1.12fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-ukaz322__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-ukaz322__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--uk-gold);
}
.l24-boris-ukaz322__route-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 260px;
  margin-bottom: 12px;
}
.l24-boris-ukaz322__stages {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-ukaz322__stage {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-left: 3px solid var(--uk-foreign);
  font-size: 0.74rem;
  line-height: 1.4;
}
.l24-boris-ukaz322__stage:nth-child(2) { border-left-color: var(--uk-license); }
.l24-boris-ukaz322__stage:nth-child(3) { border-left-color: var(--uk-cession); }
.l24-boris-ukaz322__stage:nth-child(4) { border-left-color: var(--uk-claim); }
.l24-boris-ukaz322__stage:nth-child(5) { border-left-color: var(--uk-check); }
.l24-boris-ukaz322__stage--wide {
  grid-column: 1 / -1;
  border-left-color: var(--uk-gold);
}
.l24-boris-ukaz322__stage strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 3px;
}
.l24-boris-ukaz322__instances {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  margin: 12px 0 0;
}
.l24-boris-ukaz322__inst {
  padding: 8px 9px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.7rem;
  line-height: 1.35;
  text-align: center;
}
.l24-boris-ukaz322__inst strong {
  display: block;
  color: #fff;
  font-size: 0.74rem;
  margin-bottom: 2px;
}
.l24-boris-ukaz322__inst--vs { border-color: rgba(236, 201, 75, 0.45); }
.l24-boris-ukaz322__grounds {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-ukaz322__ground {
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
.l24-boris-ukaz322__ground--chain { border-left: 3px solid var(--uk-cession); }
.l24-boris-ukaz322__ground--decree { border-left: 3px solid var(--uk-gold); }
.l24-boris-ukaz322__ground--pv { border-left: 3px solid var(--uk-check); }
.l24-boris-ukaz322__ground--size { border-left: 3px solid var(--uk-license); }
.l24-boris-ukaz322__ground-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-ukaz322__ground-text {
  color: var(--uk-muted);
}
.l24-boris-ukaz322__ground-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-ukaz322__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-ukaz322__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-ukaz322__vs-card--plaintiff { border-color: rgba(252, 129, 129, 0.45); }
.l24-boris-ukaz322__vs-card--defendant { border-color: rgba(104, 211, 145, 0.45); }
.l24-boris-ukaz322__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-ukaz322__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--uk-muted);
}
.l24-boris-ukaz322__note em {
  font-style: normal;
  color: var(--uk-mint);
  font-weight: 600;
}
.l24-boris-ukaz322__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ukaz322__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--uk-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-ukaz322__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--uk-gold);
}
.l24-boris-ukaz322__tag--def { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
.l24-boris-ukaz322__tag--claim { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-ukaz322__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
@media (max-width: 900px) {
  .l24-boris-ukaz322__split { grid-template-columns: 1fr; }
  .l24-boris-ukaz322__stages { grid-template-columns: 1fr; }
  .l24-boris-ukaz322__stage--wide { grid-column: auto; }
  .l24-boris-ukaz322__instances { grid-template-columns: 1fr; }
  .l24-boris-ukaz322__ground {
    grid-template-columns: 1fr;
    gap: 4px;
  }
  .l24-boris-ukaz322__vs { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-ukaz322__shell">
    <p class="l24-boris-ukaz322__eyebrow">Указ № 322 · пп. «в» п. 17 · ВС 05.06.2026 · ст. 1252.1 · маркетплейс</p>
    <h3 class="l24-boris-ukaz322__title">Цепочка права: иностранец → лицензия → цессия → иск → проверка Указа № 322</h3>
    <p class="l24-boris-ukaz322__lead">По фабуле, которую разъяснил <strong>Верховный суд 5 июня 2026 года</strong>, иск о <strong>компенсации за нарушение товарного знака</strong> к <strong>ИП на маркетплейсе</strong> идёт от российского цессионария, но право выросло из <strong>иностранного правообладателя</strong> через <strong>исключительную лицензию</strong> и <strong>цессию</strong>. Суды <strong>обязаны</strong> проверить недружественные действия правообладателя и <strong>пп. «в» п. 17</strong> Указа № 322 — нельзя решать спор только по «иностранному паспорту» ТЗ.</p>

    <div class="l24-boris-ukaz322__split">
      <div class="l24-boris-ukaz322__panel">
        <p class="l24-boris-ukaz322__panel-title">Маршрут передачи права и иска (по РАПСИ)</p>
        <svg class="l24-boris-ukaz322__route-svg" viewBox="0 0 560 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="uk322-route-title uk322-route-desc">
          <title id="uk322-route-title">Схема: иностранный правообладатель, лицензия, цессия, иск к ИП, проверка пп. в п. 17</title>
          <desc id="uk322-route-desc">Международная компания из недружественной юрисдикции передаёт право через исключительную лицензию российской фирме, затем цессию права требования компенсации третьему лицу; иск к ИП на маркетплейсе; суд проверяет пп. в пункте 17 Указа Президента № 322</desc>
          <defs>
            <linearGradient id="uk322-chain-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#ed8936"/>
              <stop offset="28%" stop-color="#4299e1"/>
              <stop offset="52%" stop-color="#9f7aea"/>
              <stop offset="76%" stop-color="#fc8181"/>
              <stop offset="100%" stop-color="#68d391"/>
            </linearGradient>
            <marker id="uk322-arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
              <path d="M0,0 L8,4 L0,8 Z" fill="#ecc94b"/>
            </marker>
          </defs>
          <line x1="48" y1="92" x2="512" y2="92" stroke="url(#uk322-chain-line)" stroke-width="4" stroke-linecap="round" marker-end="url(#uk322-arrow)"/>
          <circle cx="56" cy="92" r="26" fill="#ed8936" stroke="#fff" stroke-width="2"/>
          <text x="56" y="88" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="700">Иностр.</text>
          <text x="56" y="100" text-anchor="middle" fill="#1a202c" font-size="7">правообл.</text>
          <circle cx="152" cy="92" r="24" fill="#3182ce" stroke="#fff" stroke-width="2"/>
          <text x="152" y="88" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Лицензия</text>
          <text x="152" y="100" text-anchor="middle" fill="#bee3f8" font-size="7">исключ.</text>
          <circle cx="256" cy="92" r="24" fill="#805ad5" stroke="#fff" stroke-width="2"/>
          <text x="256" y="88" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Цессия</text>
          <text x="256" y="100" text-anchor="middle" fill="#e9d8fd" font-size="7">требование</text>
          <circle cx="368" cy="92" r="26" fill="#e53e3e" stroke="#fff" stroke-width="2"/>
          <text x="368" y="88" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Иск</text>
          <text x="368" y="100" text-anchor="middle" fill="#fed7d7" font-size="7">ИП · МП</text>
          <circle cx="488" cy="92" r="28" fill="#2f855a" stroke="#ecc94b" stroke-width="2.5"/>
          <text x="488" y="86" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">пп. «в»</text>
          <text x="488" y="98" text-anchor="middle" fill="#c6f6d5" font-size="7">п. 17 · № 322</text>
          <rect x="24" y="132" width="96" height="24" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="72" y="148" text-anchor="middle" fill="#fbd38d" font-size="7.5">междунар. ТЗ · недруж. юрисд.</text>
          <rect x="116" y="132" width="72" height="24" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="152" y="148" text-anchor="middle" fill="#90cdf4" font-size="7.5">росс. лицензиат</text>
          <rect x="212" y="132" width="88" height="24" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="256" y="148" text-anchor="middle" fill="#d6bcfa" font-size="7.5">процессуал. истец</text>
          <rect x="324" y="132" width="88" height="24" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="368" y="148" text-anchor="middle" fill="#feb2b2" font-size="7.5">сходное обозначение</text>
          <rect x="432" y="132" width="104" height="24" rx="4" fill="rgba(47,133,90,0.45)"/>
          <text x="484" y="148" text-anchor="middle" fill="#9ae6b4" font-size="7.5">обязанность суда · ВС 2026</text>
          <text x="280" y="52" text-anchor="middle" fill="#ecc94b" font-size="8.5" font-weight="600">Деньги по цепочке могут уходить за рубеж — суд проверяет добросовестность</text>
          <text x="56" y="178" text-anchor="middle" fill="#a0aec0" font-size="7">счёт «О» · п. 2</text>
          <text x="256" y="178" text-anchor="middle" fill="#a0aec0" font-size="7">обход? · аффилир.</text>
          <text x="488" y="178" text-anchor="middle" fill="#9ae6b4" font-size="7">исполнение договоров</text>
          <path d="M 56 118 L 56 128" stroke="#ed8936" stroke-width="2" fill="none"/>
          <path d="M 256 116 L 256 128" stroke="#9f7aea" stroke-width="2" fill="none"/>
          <path d="M 368 118 L 368 128" stroke="#fc8181" stroke-width="2" fill="none"/>
          <path d="M 488 120 L 488 128" stroke="#68d391" stroke-width="2" fill="none"/>
        </svg>
        <ol class="l24-boris-ukaz322__stages">
          <li class="l24-boris-ukaz322__stage">
            <strong>Иностранный правообладатель</strong>
            Международная регистрация ТЗ; юрисдикция из перечня недружественных — режим Указа № 322.
          </li>
          <li class="l24-boris-ukaz322__stage">
            <strong>Исключительная лицензия</strong>
            Российской компании — основание для защиты знака; уступка права требования не всегда без согласия.
          </li>
          <li class="l24-boris-ukaz322__stage">
            <strong>Цессия компенсации</strong>
            Право требования уступлено третьему лицу — формально «российский» истец в суде.
          </li>
          <li class="l24-boris-ukaz322__stage">
            <strong>Иск к ИП на маркетплейсе</strong>
            «Сходное» обозначение на карточке; ответчик — продавец, не площадка (ст. 1253.1 ГК).
          </li>
          <li class="l24-boris-ukaz322__stage l24-boris-ukaz322__stage--wide">
            <strong>Проверка пп. «в» п. 17 · ВС 05.06.2026</strong>
            Апелляция не исследовала статус правообладателя → отмена актов → новое рассмотрение с дифференцированным подходом.
          </li>
        </ol>
        <div class="l24-boris-ukaz322__instances" aria-label="Инстанции по фабуле ВС">
          <div class="l24-boris-ukaz322__inst">
            <strong>1-я инстанция</strong>
            взыскала компенсацию
          </div>
          <div class="l24-boris-ukaz322__inst">
            <strong>Апелляция / кассация</strong>
            отменили — «иностранный ТЗ»
          </div>
          <div class="l24-boris-ukaz322__inst l24-boris-ukaz322__inst--vs">
            <strong>ВС 05.06.2026</strong>
            на пересмотр + Указ № 322
          </div>
        </div>
        <p class="l24-boris-ukaz322__caption">Схема по сообщению РАПСИ / пресс-службы ВС; номер дела в открытом доступе не опубликован</p>
      </div>

      <div class="l24-boris-ukaz322__panel">
        <p class="l24-boris-ukaz322__panel-title">Что проверяет суд (чек-лист ответчика)</p>
        <div class="l24-boris-ukaz322__vs">
          <div class="l24-boris-ukaz322__vs-card l24-boris-ukaz322__vs-card--plaintiff">
            <strong>Истец (цессионарий)</strong>
            Должен доказать цепочку права, объём нарушения и законность взыскания; иностранное происхождение само по себе не даёт автопобеды (А56-2577/2023).
          </div>
          <div class="l24-boris-ukaz322__vs-card l24-boris-ukaz322__vs-card--defendant">
            <strong>Ответчик (ИП на МП)</strong>
            Вправе требовать исследования лицензии, цессии, счёта «О» и пп. «в» п. 17 — не только спорить о визуальном сходстве.
          </div>
        </div>
        <div class="l24-boris-ukaz322__grounds">
          <div class="l24-boris-ukaz322__ground l24-boris-ukaz322__ground--chain">
            <span class="l24-boris-ukaz322__ground-label">Лицензия → цессия</span>
            <span class="l24-boris-ukaz322__ground-text">Действительность уступки, <em>аффилированность</em>, мнимость, условие о перечислении 100% иностранцу; обход счёта «О» (СИП 02.2026).</span>
          </div>
          <div class="l24-boris-ukaz322__ground l24-boris-ukaz322__ground--decree">
            <span class="l24-boris-ukaz322__ground-label">Указ № 322 · п. 2, 11, 13</span>
            <span class="l24-boris-ukaz322__ground-text">Компенсация на спецсчёт «О»; без согласия правообладателя должник вправе <em>не платить</em>; публикация реквизитов (п. 8).</span>
          </div>
          <div class="l24-boris-ukaz322__ground l24-boris-ukaz322__ground--pv">
            <span class="l24-boris-ukaz322__ground-label">пп. «в» п. 17</span>
            <span class="l24-boris-ukaz322__ground-text">Указ <em>не применяется</em>, если правообладатель из пп. «а» п. 1 <em>надлежащим образом исполняет</em> договоры с российскими контрагентами — суд обязан установить.</span>
          </div>
          <div class="l24-boris-ukaz322__ground l24-boris-ukaz322__ground--size">
            <span class="l24-boris-ukaz322__ground-label">Размер · ст. 1252.1</span>
            <span class="l24-boris-ukaz322__ground-text">Лимит <em>10 млн ₽</em> с 2026; бремя доказывания объёма на истце; снижение для добросовестного нарушителя (п. 7).</span>
          </div>
        </div>
        <p class="l24-boris-ukaz322__note"><em>Пп. «в» п. 17</em> — не универсальный щит: при доказанном обходе платёжного режима суды отказывают в исключении (дела А50-18845/2024, А50-20994/2024). Доводы ответчика должны опираться на <em>документы</em>, а не только на недружественность.</p>
      </div>
    </div>

    <div class="l24-boris-ukaz322__foot" aria-label="Роли в споре">
      <span class="l24-boris-ukaz322__tag l24-boris-ukaz322__tag--case">ВС 05.06.2026 · Указ Президента № 322</span>
      <span class="l24-boris-ukaz322__tag l24-boris-ukaz322__tag--def">Ответчик: ИП-продавец на маркетплейсе</span>
      <span class="l24-boris-ukaz322__tag l24-boris-ukaz322__tag--claim">Истец: цессионарий по цепочке лицензия → цессия</span>
    </div>
  </div>
</section>
```

**Чеклист отличий от hero Алины**
- [x] Не полноэкранный блок; в теле статьи после H2 про Указ № 322
- [x] Свой `id`: `l24-boris-vs-kompensaciya-ukaz322` (не hero `#l24-hero-…`)
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Тёмная панель — контраст со светлым hero Алины (IP, маркетплейс)
- [x] Сплит «цепочка права + инстанции | чек-лист пп. «в» п. 17 и Указа № 322»
