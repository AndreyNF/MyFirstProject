=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО

**Slug:** `dosudebnaya-zashchita-po-ugolovnomu-delu`  
**Режим:** продолжение UG-темы (досудебная защита) — тёмный редакционный блок в теле; hero остаётся светлым «дорожная карта», Борис даёт **матрицу стадия × статус** и легенду «сказать / молчание / только с адвокатом».

**Вставка для Наташи:** заменяет маркер `<!-- BORIS_ANCHOR -->` сразу после вводного абзаца к H2 «Матрица «стадия × статус»: что можно, что нельзя» (вместо markdown-таблицы в лонгриде). **Перед** H2 «Права подозреваемого на досудебной стадии». Якорь TOC: `#ym-matrix-dosudeb`.

**Техника:** только inline `<style>` + static SVG; **без** `<canvas>`, **без** `<script>`.

```html
<section id="l24-boris-ug-dosudeb-matrix" class="l24-boris-ug-dosudeb" aria-label="Досудебная защита: матрица стадия × статус">
<style>
.l24-boris-ug-dosudeb {
  --ugd-navy: #0f2744;
  --ugd-navy-soft: #1a365d;
  --ugd-blue: #63b3ed;
  --ugd-gold: #ecc94b;
  --ugd-teal: #4fd1c5;
  --ugd-mint: #68d391;
  --ugd-warn: #fc8181;
  --ugd-muted: #a0aec0;
  --ugd-say: #68d391;
  --ugd-quiet: #ecc94b;
  --ugd-law: #fc8181;
  margin: 48px 0;
  padding: 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-ug-dosudeb__shell {
  background: linear-gradient(148deg, var(--ugd-navy) 0%, #152a45 52%, var(--ugd-navy-soft) 100%);
  border: 1px solid rgba(99, 179, 237, 0.22);
  border-radius: 14px;
  padding: 32px 28px 26px;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 20px 52px rgba(15, 39, 68, 0.32);
  color: #e2e8f0;
}
.l24-boris-ug-dosudeb__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ugd-gold);
}
.l24-boris-ug-dosudeb__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-ug-dosudeb__lead {
  margin: 0 0 20px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--ugd-muted);
  max-width: 72ch;
}
.l24-boris-ug-dosudeb__lead strong { color: #fff; }
.l24-boris-ug-dosudeb__legend {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 0 0 18px;
  padding: 0;
  list-style: none;
}
.l24-boris-ug-dosudeb__legend-item {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin: 0;
  padding: 6px 10px;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 600;
  background: rgba(0, 0, 0, 0.25);
  border: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-ug-dosudeb__legend-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}
.l24-boris-ug-dosudeb__legend-dot--say { background: var(--ugd-say); }
.l24-boris-ug-dosudeb__legend-dot--quiet { background: var(--ugd-quiet); }
.l24-boris-ug-dosudeb__legend-dot--law { background: var(--ugd-law); }
.l24-boris-ug-dosudeb__split {
  display: grid;
  grid-template-columns: minmax(0, 0.42fr) minmax(0, 1.58fr);
  gap: 20px;
  align-items: start;
}
.l24-boris-ug-dosudeb__rail {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 16px 14px;
}
.l24-boris-ug-dosudeb__rail-title {
  margin: 0 0 12px;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--ugd-gold);
}
.l24-boris-ug-dosudeb__stages-svg {
  display: block;
  width: 100%;
  height: auto;
  max-height: 280px;
  margin-bottom: 12px;
}
.l24-boris-ug-dosudeb__deadlines {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.l24-boris-ug-dosudeb__deadline {
  margin: 0;
  padding: 8px 9px;
  border-radius: 7px;
  background: rgba(0, 0, 0, 0.22);
  font-size: 0.72rem;
  line-height: 1.38;
  color: var(--ugd-muted);
  border-left: 3px solid var(--ugd-blue);
}
.l24-boris-ug-dosudeb__deadline:nth-child(2) { border-left-color: var(--ugd-warn); }
.l24-boris-ug-dosudeb__deadline:nth-child(3) { border-left-color: var(--ugd-teal); }
.l24-boris-ug-dosudeb__deadline strong {
  display: block;
  color: #fff;
  font-size: 0.76rem;
  margin-bottom: 2px;
}
.l24-boris-ug-dosudeb__matrix-wrap {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
.l24-boris-ug-dosudeb__matrix {
  display: grid;
  grid-template-columns: minmax(108px, 0.95fr) repeat(3, minmax(0, 1fr));
  gap: 6px;
  min-width: 520px;
}
.l24-boris-ug-dosudeb__corner,
.l24-boris-ug-dosudeb__colhead,
.l24-boris-ug-dosudeb__rowhead {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  line-height: 1.3;
}
.l24-boris-ug-dosudeb__corner {
  padding: 10px 8px;
  color: var(--ugd-muted);
  align-self: end;
}
.l24-boris-ug-dosudeb__colhead {
  padding: 10px 8px;
  text-align: center;
  color: var(--ugd-blue);
  background: rgba(99, 179, 237, 0.12);
  border-radius: 8px 8px 0 0;
}
.l24-boris-ug-dosudeb__colhead:nth-child(3) { color: var(--ugd-warn); background: rgba(252, 129, 129, 0.12); }
.l24-boris-ug-dosudeb__colhead:nth-child(4) { color: var(--ugd-teal); background: rgba(79, 209, 197, 0.12); }
.l24-boris-ug-dosudeb__rowhead {
  padding: 12px 10px;
  color: #fff;
  background: rgba(0, 0, 0, 0.28);
  border-radius: 8px 0 0 8px;
  border-left: 3px solid var(--ugd-gold);
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 3px;
}
.l24-boris-ug-dosudeb__rowhead span {
  font-size: 0.62rem;
  font-weight: 500;
  text-transform: none;
  color: var(--ugd-muted);
  letter-spacing: 0;
}
.l24-boris-ug-dosudeb__rowhead--det { border-left-color: var(--ugd-warn); }
.l24-boris-ug-dosudeb__rowhead--inv { border-left-color: var(--ugd-teal); }
.l24-boris-ug-dosudeb__cell {
  margin: 0;
  padding: 11px 10px;
  border-radius: 8px;
  background: rgba(0, 0, 0, 0.22);
  border: 1px solid rgba(255, 255, 255, 0.08);
  font-size: 0.74rem;
  line-height: 1.42;
  color: #cbd5e0;
}
.l24-boris-ug-dosudeb__cell--na {
  background: rgba(0, 0, 0, 0.12);
  color: var(--ugd-muted);
  text-align: center;
  font-style: italic;
}
.l24-boris-ug-dosudeb__tactic {
  display: inline-block;
  margin: 0 0 6px;
  padding: 3px 7px;
  border-radius: 5px;
  font-size: 0.62rem;
  font-weight: 800;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.l24-boris-ug-dosudeb__tactic--say {
  background: rgba(104, 211, 145, 0.2);
  color: #9ae6b4;
  border: 1px solid rgba(104, 211, 145, 0.45);
}
.l24-boris-ug-dosudeb__tactic--quiet {
  background: rgba(236, 201, 75, 0.15);
  color: #faf089;
  border: 1px solid rgba(236, 201, 75, 0.4);
}
.l24-boris-ug-dosudeb__tactic--law {
  background: rgba(252, 129, 129, 0.15);
  color: #fed7d7;
  border: 1px solid rgba(252, 129, 129, 0.4);
}
.l24-boris-ug-dosudeb__cell strong {
  color: #fff;
  font-weight: 600;
}
.l24-boris-ug-dosudeb__cell em {
  font-style: normal;
  color: var(--ugd-teal);
  font-weight: 600;
}
.l24-boris-ug-dosudeb__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-top: 18px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.12);
}
.l24-boris-ug-dosudeb__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.08);
  color: #e2e8f0;
}
.l24-boris-ug-dosudeb__tag--144 { border: 1px solid var(--ugd-blue); color: #bee3f8; }
.l24-boris-ug-dosudeb__tag--92 { border: 1px solid var(--ugd-warn); color: #fed7d7; }
.l24-boris-ug-dosudeb__tag--182 { border: 1px solid var(--ugd-teal); color: #b2f5ea; }
.l24-boris-ug-dosudeb__caption {
  margin: 12px 0 0;
  font-size: 0.74rem;
  line-height: 1.45;
  color: var(--ugd-muted);
}
@media (max-width: 900px) {
  .l24-boris-ug-dosudeb__split { grid-template-columns: 1fr; }
}
</style>

  <div class="l24-boris-ug-dosudeb__shell">
    <p class="l24-boris-ug-dosudeb__eyebrow">УПК РФ · ст. 46–47 · 144–145 · 182 · 2026</p>
    <h3 class="l24-boris-ug-dosudeb__title" id="ym-matrix-dosudeb">Матрица «стадия × статус»: что сказать, когда молчать, когда только с адвокатом</h3>
    <p class="l24-boris-ug-dosudeb__lead">Одна и та же фраза на <strong>проверке (ст. 144)</strong> и на <strong>допросе подозреваемого</strong> работает по-разному. Сетка ниже — тактика для <strong>свидетеля</strong>, <strong>подозреваемого</strong> и <strong>директора юрлица</strong>; слева — три стадии досудебного производства и ключевые сроки.</p>

    <ul class="l24-boris-ug-dosudeb__legend" aria-label="Легенда тактики">
      <li class="l24-boris-ug-dosudeb__legend-item"><span class="l24-boris-ug-dosudeb__legend-dot l24-boris-ug-dosudeb__legend-dot--say" aria-hidden="true"></span> Можно сказать — кратко, по вопросу</li>
      <li class="l24-boris-ug-dosudeb__legend-item"><span class="l24-boris-ug-dosudeb__legend-dot l24-boris-ug-dosudeb__legend-dot--quiet" aria-hidden="true"></span> Молчание / осторожность</li>
      <li class="l24-boris-ug-dosudeb__legend-item"><span class="l24-boris-ug-dosudeb__legend-dot l24-boris-ug-dosudeb__legend-dot--law" aria-hidden="true"></span> Только с адвокатом</li>
    </ul>

    <div class="l24-boris-ug-dosudeb__split">
      <aside class="l24-boris-ug-dosudeb__rail" aria-label="Стадии досудебного производства">
        <p class="l24-boris-ug-dosudeb__rail-title">Три стадии</p>
        <svg class="l24-boris-ug-dosudeb__stages-svg" viewBox="0 0 200 268" xmlns="http://www.w3.org/2000/svg" role="img" aria-hidden="true">
          <defs>
            <linearGradient id="ugd-stage-line" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stop-color="#63b3ed"/>
              <stop offset="50%" stop-color="#ecc94b"/>
              <stop offset="100%" stop-color="#4fd1c5"/>
            </linearGradient>
          </defs>
          <line x1="36" y1="28" x2="36" y2="240" stroke="url(#ugd-stage-line)" stroke-width="3" stroke-linecap="round"/>
          <circle cx="36" cy="36" r="14" fill="#2b6cb0" stroke="#fff" stroke-width="2"/>
          <text x="36" y="40" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">1</text>
          <rect x="58" y="18" width="128" height="36" rx="7" fill="rgba(99,179,237,0.2)" stroke="#63b3ed"/>
          <text x="122" y="34" text-anchor="middle" fill="#bee3f8" font-size="8" font-weight="700">Проверка ст. 144</text>
          <text x="122" y="46" text-anchor="middle" fill="#a0aec0" font-size="7">3 / 10 / 30 суток</text>
          <circle cx="36" cy="118" r="14" fill="#c53030" stroke="#fff" stroke-width="2"/>
          <text x="36" y="122" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">2</text>
          <rect x="58" y="100" width="128" height="36" rx="7" fill="rgba(252,129,129,0.15)" stroke="#fc8181"/>
          <text x="122" y="116" text-anchor="middle" fill="#fed7d7" font-size="8" font-weight="700">Задержание + 24 ч</text>
          <text x="122" y="128" text-anchor="middle" fill="#a0aec0" font-size="7">ст. 91–92 УПК</text>
          <circle cx="36" cy="200" r="14" fill="#2f855a" stroke="#fff" stroke-width="2"/>
          <text x="36" y="204" text-anchor="middle" fill="#fff" font-size="9" font-weight="700">3</text>
          <rect x="58" y="182" width="128" height="36" rx="7" fill="rgba(79,209,197,0.15)" stroke="#4fd1c5"/>
          <text x="122" y="198" text-anchor="middle" fill="#b2f5ea" font-size="8" font-weight="700">Следствие</text>
          <text x="122" y="210" text-anchor="middle" fill="#a0aec0" font-size="7">допрос · обыск ст. 182</text>
          <path d="M 36 50 L 36 102" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" stroke-dasharray="3 3"/>
          <path d="M 36 132 L 36 184" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1.5" stroke-dasharray="3 3"/>
        </svg>
        <ul class="l24-boris-ug-dosudeb__deadlines">
          <li class="l24-boris-ug-dosudeb__deadline"><strong>Проверка</strong>объяснения ≠ допрос; риск «обыска до возбуждения» — оспаривать</li>
          <li class="l24-boris-ug-dosudeb__deadline"><strong>24 часа</strong>допрос задержанного; свидание с защитником <em>до</em> допроса (ч. 4–5 ст. 92)</li>
          <li class="l24-boris-ug-dosudeb__deadline"><strong>Следствие</strong>отказ — п. 2 ч. 4 ст. 46 / п. 3 ч. 4 ст. 47, не только ст. 51 КРФ</li>
        </ul>
      </aside>

      <div class="l24-boris-ug-dosudeb__matrix-wrap">
        <div class="l24-boris-ug-dosudeb__matrix" role="table" aria-label="Матрица стадия × статус: тактика на досудебной стадии">
          <div class="l24-boris-ug-dosudeb__corner" role="columnheader">Стадия ↓ / Статус →</div>
          <div class="l24-boris-ug-dosudeb__colhead" role="columnheader">Свидетель</div>
          <div class="l24-boris-ug-dosudeb__colhead" role="columnheader">Подозреваемый</div>
          <div class="l24-boris-ug-dosudeb__colhead" role="columnheader">Директор юрлица</div>

          <div class="l24-boris-ug-dosudeb__rowhead" role="rowheader">Проверка<span>ст. 144–145 УПК</span></div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--say">Сказать</span>
            <strong>Явка по вызову.</strong> Отвечать на вопросы о деле; по себе и близким — <em>ст. 51 Конституции</em>. Риск перевода в подозреваемого — согласовать с адвокатом.
          </div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--quiet">Осторожно</span>
            Статуса ещё нет — это <strong>объяснения</strong>, не допрос. Сильная позиция → версия для отказа в возбуждении; риск 159/177 → сдержанность.
          </div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--law">С адвокатом</span>
            <strong>Единая линия</strong> компании; документы по запросу — через юриста; не смешивать личное и корпоративное в одном протоколе.
          </div>

          <div class="l24-boris-ug-dosudeb__rowhead l24-boris-ug-dosudeb__rowhead--det" role="rowheader">Задержание + 24 ч<span>ст. 91–92 УПК</span></div>
          <div class="l24-boris-ug-dosudeb__cell l24-boris-ug-dosudeb__cell--na" role="cell">—</div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--law">Только с адвокатом</span>
            Допрос не позднее <strong>24 ч</strong>; до него — свидание с защитником наедине. Фраза: «<em>Показания дам в присутствии защитника</em>» (ст. 92).
          </div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--law">Только с адвокатом</span>
            Уведомить корпоративного адвоката; <strong>не подписывать</strong> протоколы без юриста; уведомление родных — не позднее 12 ч (ч. 3 ст. 46).
          </div>

          <div class="l24-boris-ug-dosudeb__rowhead l24-boris-ug-dosudeb__rowhead--inv" role="rowheader">Следствие<span>допрос · обыск</span></div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--say">Сказать</span>
            <strong>Кратко по факту.</strong> Ложные показания — <em>ст. 307 УК</em>; без «додумывания» и оправданий. Отказ только по ст. 51 (о себе/близких).
          </div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--quiet">Молчание</span>
            Право <strong>отказаться от показаний</strong> — п. 2 ч. 4 ст. 46 / п. 3 ч. 4 ст. 47 УПК. Не «беседа без протокола»; замечания к протоколу — обязательно.
          </div>
          <div class="l24-boris-ug-dosudeb__cell" role="cell">
            <span class="l24-boris-ug-dosudeb__tactic l24-boris-ug-dosudeb__tactic--law">С адвокатом</span>
            <strong>Обыск в офисе</strong> — защитник вправе присутствовать (ч. 11 ст. 182); фиксировать отказ в допуске → <em>ст. 75 УПК</em>. Не трогать серверы без юриста.
          </div>
        </div>
      </div>
    </div>

    <div class="l24-boris-ug-dosudeb__foot" aria-label="Связка стадий и норм">
      <span class="l24-boris-ug-dosudeb__tag l24-boris-ug-dosudeb__tag--144">144: объяснения ≠ допрос</span>
      <span class="l24-boris-ug-dosudeb__tag l24-boris-ug-dosudeb__tag--92">92: защитник до допроса</span>
      <span class="l24-boris-ug-dosudeb__tag l24-boris-ug-dosudeb__tag--182">182: адвокат на обыске</span>
      <span class="l24-boris-ug-dosudeb__tag">Допрос / опрос / беседа — разные форматы</span>
    </div>
    <p class="l24-boris-ug-dosudeb__caption">Схема к разделу о досудебной защите — не заменяет консультацию адвоката; тактику согласуйте по конкретному делу (в т.ч. ст. 159 и 177 УК).</p>
  </div>
</section>
```

**Паспорт блока**

| Поле | Значение |
|------|----------|
| `id` секции | `#l24-boris-ug-dosudeb-matrix` |
| Якорь TOC / Наташа | `#ym-matrix-dosudeb` (заголовок h3 внутри блока) |
| Класс корня | `l24-boris-ug-dosudeb` |
| Якорь вставки | `<!-- BORIS_ANCHOR -->` (замена markdown-таблицы матрицы) |
| Композиция | сплит: SVG-рельс стадий + сетка 3×3 (проверка / задержание / следствие × свидетель / подозреваемый / директор) |
| Hero Алины | не дублировать: без fullscreen, без тех же `id` |
| MCP | без `<script>` и `<canvas>` |

### Чеклист отличий от hero Алины

- [x] Не hero: блок в теле лонгрида (`margin: 48px 0`), не `min-height: 100vh`
- [x] Контраст: тёмный UG-navy + gold/teal/warn (hero — светлая «дорожная карта» досудебной защиты)
- [x] Тема продолжения: стадии УПК и статусы — углубление **тактики**, не повтор hero-сцены
- [x] Редакционная обвязка: eyebrow, lead, легенда, рельс стадий, матрица, теги, подпись
- [x] Static SVG + inline CSS только
- [x] Уникальные префиксы и `id` градиентов (`ugd-stage-line`)
- [x] Якорь: `#ym-matrix-dosudeb`; вставка на месте `BORIS_ANCHOR`
