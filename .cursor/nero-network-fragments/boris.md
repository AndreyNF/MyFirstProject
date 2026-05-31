=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Якорь Наташи:** `l24-boris-poizon-sip-osporenie`  
**Размещение:** после H2 «Оспаривание регистрации товарного знака: когда идут в СИП, а не только в Роспатент» (перед H3 «Оспаривание товарного знака в Роспатенте vs судебное оспаривание» или сразу после вводного абзаца раздела).  
**Режим:** контраст к hero — процессуальная «карта двух инстанций» вместо новостного кадра POIZON.  
**Legis24 MCP-only:** static SVG + inline CSS, без `<script>` и `<canvas>`.

```html
<section id="l24-boris-poizon-sip-osporenie" class="l24-boris-poizon-sip" aria-label="Оспаривание регистрации товарного знака: Роспатент, СИП и президиум — маршрут и основания">
<style>
.l24-boris-poizon-sip {
  --pos-navy: #0f2744;
  --pos-navy-soft: #1a365d;
  --pos-rospatent: #3182ce;
  --pos-gold: #ecc94b;
  --pos-sip: #c53030;
  --pos-presidium: #d69e2e;
  --pos-mint: #68d391;
  --pos-ink: #e2e8f0;
  --pos-muted: #a0aec0;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-poizon-sip__shell {
  background: linear-gradient(148deg, var(--pos-navy) 0%, #152a45 52%, var(--pos-navy-soft) 100%);
  border: 1px solid rgba(236, 201, 75, 0.24);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: 0 18px 48px rgba(15, 39, 68, 0.28);
  color: var(--pos-ink);
}
.l24-boris-poizon-sip__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--pos-gold);
}
.l24-boris-poizon-sip__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-poizon-sip__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--pos-muted);
  max-width: 68ch;
}
.l24-boris-poizon-sip__lead strong { color: #fff; }
.l24-boris-poizon-sip__split {
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr);
  gap: 24px;
  align-items: stretch;
}
.l24-boris-poizon-sip__panel {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px 18px;
}
.l24-boris-poizon-sip__panel-title {
  margin: 0 0 14px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--pos-gold);
}
.l24-boris-poizon-sip__route-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 248px;
  margin-bottom: 12px;
}
.l24-boris-poizon-sip__stages {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
  margin: 0;
  padding: 0;
  list-style: none;
}
.l24-boris-poizon-sip__stage {
  margin: 0;
  padding: 10px 9px;
  background: rgba(0, 0, 0, 0.22);
  border-radius: 8px;
  border-left: 3px solid var(--pos-rospatent);
  font-size: 0.74rem;
  line-height: 1.4;
}
.l24-boris-poizon-sip__stage:nth-child(2) { border-left-color: var(--pos-rospatent); }
.l24-boris-poizon-sip__stage:nth-child(3) { border-left-color: var(--pos-sip); }
.l24-boris-poizon-sip__stage:nth-child(4) { border-left-color: var(--pos-presidium); }
.l24-boris-poizon-sip__stage--wide {
  grid-column: 1 / -1;
  border-left-color: var(--pos-mint);
}
.l24-boris-poizon-sip__stage strong {
  display: block;
  color: #fff;
  font-size: 0.78rem;
  margin-bottom: 3px;
}
.l24-boris-poizon-sip__grounds {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin: 0 0 12px;
}
.l24-boris-poizon-sip__ground {
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
.l24-boris-poizon-sip__ground--patent { border-left: 3px solid var(--pos-rospatent); }
.l24-boris-poizon-sip__ground--gk { border-left: 3px solid var(--pos-gold); }
.l24-boris-poizon-sip__ground--comp { border-left: 3px solid var(--pos-sip); }
.l24-boris-poizon-sip__ground--term { border-left: 3px solid var(--pos-presidium); }
.l24-boris-poizon-sip__ground-label {
  font-weight: 700;
  color: #fff;
  font-size: 0.78rem;
}
.l24-boris-poizon-sip__ground-text {
  color: var(--pos-muted);
}
.l24-boris-poizon-sip__ground-text em {
  font-style: normal;
  color: #fff;
  font-weight: 600;
}
.l24-boris-poizon-sip__vs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin: 0 0 10px;
}
.l24-boris-poizon-sip__vs-card {
  padding: 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.28);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.72rem;
  line-height: 1.4;
}
.l24-boris-poizon-sip__vs-card--admin { border-color: rgba(49, 130, 206, 0.45); }
.l24-boris-poizon-sip__vs-card--court { border-color: rgba(197, 48, 48, 0.45); }
.l24-boris-poizon-sip__vs-card strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 4px;
}
.l24-boris-poizon-sip__note {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.45;
  color: var(--pos-muted);
}
.l24-boris-poizon-sip__note em {
  font-style: normal;
  color: var(--pos-mint);
  font-weight: 600;
}
.l24-boris-poizon-sip__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-poizon-sip__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.06);
  color: var(--pos-ink);
  border: 1px solid rgba(255, 255, 255, 0.14);
}
.l24-boris-poizon-sip__tag--case {
  border-color: rgba(236, 201, 75, 0.5);
  color: var(--pos-gold);
}
.l24-boris-poizon-sip__tag--attack { border-color: rgba(104, 211, 145, 0.45); color: #c6f6d5; }
.l24-boris-poizon-sip__tag--def { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-poizon-sip__caption {
  margin: 10px 0 0;
  font-size: 0.7rem;
  line-height: 1.4;
  color: rgba(160, 174, 192, 0.88);
  text-align: center;
}
@media (max-width: 900px) {
  .l24-boris-poizon-sip__split { grid-template-columns: 1fr; }
  .l24-boris-poizon-sip__stages { grid-template-columns: 1fr; }
  .l24-boris-poizon-sip__stage--wide { grid-column: auto; }
  .l24-boris-poizon-sip__ground {
    grid-template-columns: 1fr;
    gap: 4px;
  }
  .l24-boris-poizon-sip__vs { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-poizon-sip__shell">
    <p class="l24-boris-poizon-sip__eyebrow">ст. 1512–1513 · 1513 п. 4 · СИП-1182/2024 · POIZON</p>
    <h3 class="l24-boris-poizon-sip__title">Оспаривание регистрации: Роспатент → СИП → президиум</h3>
    <p class="l24-boris-poizon-sip__lead">После выдачи свидетельства спор о <strong>недействительности регистрации</strong> часто идёт в два рубежа: <strong>возражение в Роспатент</strong> (палата по патентным спорам) и, если ведомство отказало, — <strong>иск в СИП</strong> по ст. 1513 п. 4 ГК РФ. В деле <strong>DEWU vs ООО «Пойзон»</strong> именно так: отклонённое возражение → суд → кассация в <strong>президиум СИП</strong> (апелляции у СИП нет).</p>

    <div class="l24-boris-poizon-sip__split">
      <div class="l24-boris-poizon-sip__panel">
        <p class="l24-boris-poizon-sip__panel-title">Маршрут POIZON (пострегистрационное оспаривание)</p>
        <svg class="l24-boris-poizon-sip__route-svg" viewBox="0 0 540 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="pos-route-title pos-route-desc">
          <title id="pos-route-title">Схема: Роспатент, СИП, президиум СИП</title>
          <desc id="pos-route-desc">Регистрация знака, возражение в Роспатенте, отказ в удовлетворении, иск в СИП, решение о недействительности, кассация в президиум СИП</desc>
          <defs>
            <linearGradient id="pos-osp-line" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#3182ce"/>
              <stop offset="45%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#c53030"/>
            </linearGradient>
          </defs>
          <line x1="52" y1="88" x2="488" y2="88" stroke="url(#pos-osp-line)" stroke-width="4" stroke-linecap="round"/>
          <circle cx="68" cy="88" r="24" fill="#3182ce" stroke="#fff" stroke-width="2"/>
          <text x="68" y="84" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Рег.</text>
          <text x="68" y="96" text-anchor="middle" fill="#fff" font-size="7">12.2023</text>
          <circle cx="168" cy="88" r="24" fill="#2b6cb0" stroke="#fff" stroke-width="2"/>
          <text x="168" y="86" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">Роспат.</text>
          <text x="168" y="98" text-anchor="middle" fill="#e2e8f0" font-size="7">возраж.</text>
          <circle cx="288" cy="88" r="26" fill="#c53030" stroke="#fff" stroke-width="2"/>
          <text x="288" y="86" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">СИП</text>
          <text x="288" y="98" text-anchor="middle" fill="#fed7d7" font-size="7">1182/24</text>
          <circle cx="408" cy="88" r="24" fill="#d69e2e" stroke="#fff" stroke-width="2"/>
          <text x="408" y="86" text-anchor="middle" fill="#1a202c" font-size="8" font-weight="700">Презид.</text>
          <text x="408" y="98" text-anchor="middle" fill="#1a202c" font-size="7">1 мес.</text>
          <circle cx="488" cy="88" r="18" fill="#2f855a" stroke="#fff" stroke-width="2"/>
          <text x="488" y="92" text-anchor="middle" fill="#fff" font-size="8" font-weight="700">ВС</text>
          <rect x="118" y="128" width="100" height="22" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="168" y="143" text-anchor="middle" fill="#feb2b2" font-size="8">отказ возражения</text>
          <rect x="238" y="128" width="100" height="22" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="288" y="143" text-anchor="middle" fill="#9ae6b4" font-size="8">недействит. охраны</text>
          <rect x="358" y="128" width="100" height="22" rx="4" fill="rgba(0,0,0,0.35)"/>
          <text x="408" y="143" text-anchor="middle" fill="#faf089" font-size="8">кассация</text>
          <text x="68" y="52" text-anchor="middle" fill="#90cdf4" font-size="8" font-weight="600">№ 983757 / 1026380</text>
          <text x="288" y="52" text-anchor="middle" fill="#feb2b2" font-size="8" font-weight="600">май 2026 · резолютивная</text>
          <text x="488" y="52" text-anchor="middle" fill="#9ae6b4" font-size="8" font-weight="600">при основаниях</text>
          <path d="M 168 112 L 168 124" stroke="#ecc94b" stroke-width="2" fill="none"/>
          <path d="M 288 114 L 288 126" stroke="#ecc94b" stroke-width="2" fill="none"/>
        </svg>
        <ol class="l24-boris-poizon-sip__stages">
          <li class="l24-boris-poizon-sip__stage">
            <strong>Регистрация</strong>
            Свидетельство выдано — риск не снят: сильный глобальный бренд может оспорить позже.
          </li>
          <li class="l24-boris-poizon-sip__stage">
            <strong>Возражение (ППС)</strong>
            Дешевле и быстрее суда; сроки по ст. 1513 (часто до 5 лет с публикации для ряда оснований).
          </li>
          <li class="l24-boris-poizon-sip__stage">
            <strong>Иск в СИП</strong>
            Оспаривание решения Роспатента + признание регистрации недействительной; недобросовестная конкуренция (ст. 10, 14.4, 14.8).
          </li>
          <li class="l24-boris-poizon-sip__stage">
            <strong>Президиум СИП</strong>
            Кассация 1 месяц; решения СИП вступают в силу немедленно (ст. 273 АПК).
          </li>
          <li class="l24-boris-poizon-sip__stage l24-boris-poizon-sip__stage--wide">
            <strong>≠ отказ при подаче заявки (A15)</strong>
            Там знак не выдан; здесь — пострегистрационное оспаривание уже действующей охраны.
          </li>
        </ol>
        <p class="l24-boris-poizon-sip__caption">Схема по публичной хронологии СИП-1182/2024; статус № 1026380 — по мотивировке полного акта</p>
      </div>

      <div class="l24-boris-poizon-sip__panel">
        <p class="l24-boris-poizon-sip__panel-title">Основания оспаривания (чек-лист)</p>
        <div class="l24-boris-poizon-sip__vs">
          <div class="l24-boris-poizon-sip__vs-card l24-boris-poizon-sip__vs-card--admin">
            <strong>Роспатент</strong>
            Возражение против регистрации; частичная недействительность (пример: класс 35, 2025).
          </div>
          <div class="l24-boris-poizon-sip__vs-card l24-boris-poizon-sip__vs-card--court">
            <strong>СИП</strong>
            Решение ведомства + полная/частичная недействительность + поведение при регистрации.
          </div>
        </div>
        <div class="l24-boris-poizon-sip__grounds">
          <div class="l24-boris-poizon-sip__ground l24-boris-poizon-sip__ground--patent">
            <span class="l24-boris-poizon-sip__ground-label">ст. 1483 п. 6–7, 10</span>
            <span class="l24-boris-poizon-sip__ground-text">Введение в <em>заблуждение</em>, сходство до смешения, конфликт с ранними правами (POIZON / Пойзон / Dewu).</span>
          </div>
          <div class="l24-boris-poizon-sip__ground l24-boris-poizon-sip__ground--gk">
            <span class="l24-boris-poizon-sip__ground-label">ст. 1512–1513</span>
            <span class="l24-boris-poizon-sip__ground-text">Основания и порядок признания <em>регистрации</em> или <em>охраны</em> недействительной (полностью или по классам МКТУ).</span>
          </div>
          <div class="l24-boris-poizon-sip__ground l24-boris-poizon-sip__ground--comp">
            <span class="l24-boris-poizon-sip__ground-label">ст. 10 · 14.4 · 14.8</span>
            <span class="l24-boris-poizon-sip__ground-text">Недобросовестная конкуренция при приобретении знака; суд не ограничен формальной легальностью акта Роспатента (п. 169 ППВС № 10).</span>
          </div>
          <div class="l24-boris-poizon-sip__ground l24-boris-poizon-sip__ground--term">
            <span class="l24-boris-poizon-sip__ground-label">Срок · доказательства</span>
            <span class="l24-boris-poizon-sip__ground-text">5 лет с публикации (п. 2 ст. 1512) для ряда оснований; пакет: известность, опросы, домен, маркетплейс, класс 35.</span>
          </div>
        </div>
        <p class="l24-boris-poizon-sip__note"><em>Не путать со ст. 1515</em> — она про ответственность за использование знака, а не про аннулирование свидетельства. После недействительности продолжение обозначения на МП — отдельный риск (214-ФЗ, один абзац в тексте).</p>
      </div>
    </div>

    <div class="l24-boris-poizon-sip__foot" aria-label="Роли в споре">
      <span class="l24-boris-poizon-sip__tag l24-boris-poizon-sip__tag--case">СИП-1182/2024 · DEWU / ООО «Пойзон»</span>
      <span class="l24-boris-poizon-sip__tag l24-boris-poizon-sip__tag--attack">Атакующий бренд: возражение → СИП → доказательства известности</span>
      <span class="l24-boris-poizon-sip__tag l24-boris-poizon-sip__tag--def">Держатель регистрации: президиум СИП, авторство, первое использование в РФ</span>
    </div>
  </div>
</section>
```

**Паспорт блока**
- `id` / якорь: `l24-boris-poizon-sip-osporenie`
- Класс корня: `l24-boris-poizon-sip`
- Отличие от hero Алины: не дублировать canvas/id hero; здесь процессуальная схема, не новостной кадр
- Отличие от A15 (`l24-boris-tz-route`): не письма при подаче заявки, а пострегистрационное оспаривание и СИП
- Отличие от A9 (`l24-boris-tz-ip-track`): не МП→претензия→компенсация, а Роспатент→СИП→президиум
