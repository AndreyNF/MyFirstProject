=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО
ЯКОРЬ: l24-boris-vs-moshennichestvo-umysel

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Статья** | ВС отменил приговор директору МУП за мошенничество по ч. 3 ст. 159 — муниципальный контракт |
| **SLUG** | `vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026` |
| **Якорь** | `l24-boris-vs-moshennichestvo-umysel` |
| **Тема** | Split/grid «Гражданский спор ↔ Уголовное дело» — 4 узла защиты: контракт исполнен, акты без претензий, экспертиза ≠ умысел, зарплата ≠ корысть |
| **Размещение** | После H2-3 «Гражданский спор или уголовное дело: когда переплата по контракту не равна мошенничеству» |
| **Режим** | Контраст к hero: карта границы ответственности в теле статьи; MCP-only — inline CSS + SVG, без `<canvas>` и `<script>` |
| **Палитра** | Тёмный navy `#0c1f33`–`#163352`; гражданский: teal `#38b2ac` / `#68d391`; уголовный: crimson `#fc8181` / `#dc2626`; ВС: gold `#ecc94b`; контракт 44-ФЗ: blue `#4299e1` |

## Чеклист отличий от hero Алины

- [x] Не полноэкранный первый экран — блок в теле лонгрида
- [x] Другой `id`: `l24-boris-vs-moshennichestvo-umysel` (не hero-id Алины)
- [x] Сплит «Гражданский спор ↔ Уголовное дело» + 4 узла — не дублирует сцену hero
- [x] Без `<canvas>` и `<script>` — только inline CSS + SVG + grid
- [x] CTA в блоке **не вставлять**

```html
<section id="l24-boris-vs-moshennichestvo-umysel" class="l24-boris-vs-mos-umysel" aria-label="Граница гражданского спора и уголовного дела: дело Столярова, ВС № 85-УД26-2-К1, ч. 3 ст. 159 УК">
<style>
.l24-boris-vs-mos-umysel {
  --bm-navy: #0c1f33;
  --bm-navy-soft: #163352;
  --bm-civil: #38b2ac;
  --bm-civil-soft: #68d391;
  --bm-civil-bg: rgba(56, 178, 172, 0.14);
  --bm-crim: #fc8181;
  --bm-crim-dark: #dc2626;
  --bm-crim-bg: rgba(220, 38, 38, 0.12);
  --bm-gold: #ecc94b;
  --bm-blue: #4299e1;
  --bm-muted: #a0aec0;
  --bm-txt: #e2e8f0;
  margin: 48px 0;
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
}
.l24-boris-vs-mos-umysel__shell {
  background: linear-gradient(152deg, var(--bm-navy) 0%, #122a42 48%, var(--bm-navy-soft) 100%);
  border: 1px solid rgba(56, 178, 172, 0.28);
  border-radius: 14px;
  padding: 32px 28px 24px;
  color: var(--bm-txt);
  box-shadow: 0 18px 48px rgba(12, 31, 51, 0.32);
}
.l24-boris-vs-mos-umysel__eyebrow {
  margin: 0 0 8px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bm-gold);
}
.l24-boris-vs-mos-umysel__title {
  margin: 0 0 10px;
  font-size: clamp(1.15rem, 2.4vw, 1.42rem);
  line-height: 1.25;
  color: #fff;
  font-weight: 700;
}
.l24-boris-vs-mos-umysel__lead {
  margin: 0 0 24px;
  font-size: 0.95rem;
  line-height: 1.55;
  color: var(--bm-muted);
  max-width: 72ch;
}
.l24-boris-vs-mos-umysel__lead strong { color: #fff; }
.l24-boris-vs-mos-umysel__split {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 18px;
  margin-bottom: 20px;
}
.l24-boris-vs-mos-umysel__pole {
  border-radius: 10px;
  padding: 16px 14px;
  text-align: center;
}
.l24-boris-vs-mos-umysel__pole--civil {
  background: var(--bm-civil-bg);
  border: 1px solid rgba(56, 178, 172, 0.38);
}
.l24-boris-vs-mos-umysel__pole--crim {
  background: var(--bm-crim-bg);
  border: 1px solid rgba(252, 129, 129, 0.38);
}
.l24-boris-vs-mos-umysel__pole-hd {
  margin: 0 0 6px;
  font-size: 0.78rem;
  font-weight: 800;
  letter-spacing: 0.06em;
  text-transform: uppercase;
}
.l24-boris-vs-mos-umysel__pole--civil .l24-boris-vs-mos-umysel__pole-hd { color: #b2f5ea; }
.l24-boris-vs-mos-umysel__pole--crim .l24-boris-vs-mos-umysel__pole-hd { color: #fed7d7; }
.l24-boris-vs-mos-umysel__pole-sub {
  margin: 0;
  font-size: 0.76rem;
  line-height: 1.4;
  color: var(--bm-muted);
}
.l24-boris-vs-mos-umysel__scheme-svg {
  display: block;
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}
.l24-boris-vs-mos-umysel__grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 18px;
}
.l24-boris-vs-mos-umysel__node {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 14px 12px;
  text-align: center;
  border-top: 3px solid var(--bm-civil);
}
.l24-boris-vs-mos-umysel__node:nth-child(2) { border-top-color: var(--bm-blue); }
.l24-boris-vs-mos-umysel__node:nth-child(3) { border-top-color: var(--bm-gold); }
.l24-boris-vs-mos-umysel__node:nth-child(4) { border-top-color: var(--bm-civil-soft); }
.l24-boris-vs-mos-umysel__node-tag {
  display: block;
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--bm-gold);
  margin-bottom: 6px;
  letter-spacing: 0.04em;
}
.l24-boris-vs-mos-umysel__node-label {
  display: block;
  font-size: 0.8rem;
  line-height: 1.35;
  color: #cbd5e1;
  font-weight: 600;
}
.l24-boris-vs-mos-umysel__node-label small {
  display: block;
  margin-top: 5px;
  font-size: 0.68rem;
  font-weight: 500;
  color: var(--bm-muted);
  line-height: 1.35;
}
.l24-boris-vs-mos-umysel__verdict {
  margin: 0 0 16px;
  padding: 14px 16px;
  border-radius: 10px;
  background: rgba(236, 201, 75, 0.12);
  border: 1px solid rgba(236, 201, 75, 0.38);
  font-size: 0.84rem;
  line-height: 1.5;
  color: var(--bm-muted);
}
.l24-boris-vs-mos-umysel__verdict strong { color: var(--bm-gold); }
.l24-boris-vs-mos-umysel__foot {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding-top: 14px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}
.l24-boris-vs-mos-umysel__tag {
  font-size: 0.72rem;
  font-weight: 600;
  padding: 6px 10px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.05);
  color: var(--bm-txt);
  border: 1px solid rgba(255, 255, 255, 0.13);
}
.l24-boris-vs-mos-umysel__tag--case { border-color: rgba(236, 201, 75, 0.5); color: var(--bm-gold); }
.l24-boris-vs-mos-umysel__tag--civil { border-color: rgba(56, 178, 172, 0.45); color: #b2f5ea; }
.l24-boris-vs-mos-umysel__tag--crim { border-color: rgba(252, 129, 129, 0.45); color: #fed7d7; }
.l24-boris-vs-mos-umysel__tag--law { border-color: rgba(66, 153, 225, 0.45); color: #bee3f8; }
@media (max-width: 800px) {
  .l24-boris-vs-mos-umysel__grid { grid-template-columns: 1fr 1fr; }
  .l24-boris-vs-mos-umysel__split { grid-template-columns: 1fr; }
  .l24-boris-vs-mos-umysel__shell { padding: 24px 18px 20px; }
}
@media (max-width: 480px) {
  .l24-boris-vs-mos-umysel__grid { grid-template-columns: 1fr; }
}
</style>

<div class="l24-boris-vs-mos-umysel__shell">
  <p class="l24-boris-vs-mos-umysel__eyebrow">UG · ч. 3 ст. 159 · 44-ФЗ · дело № 85-УД26-2-К1 · ВС 14.05.2026</p>
  <h3 class="l24-boris-vs-mos-umysel__title">Гражданский спор ↔ Уголовное дело: четыре узла, которые сдвигают границу к защите</h3>
  <p class="l24-boris-vs-mos-umysel__lead">В деле <strong>Столярова</strong> (МУП МРЭП, контракт <strong>612 144 ₽</strong> на ремонт переправы) Верховный суд отменил приговор по <strong>ч. 3 ст. 159 УК РФ</strong>: переплата по экспертизе не равна мошенничеству, если контракт исполнен, акты подписаны без претензий, а деньги ушли на зарплату сотрудников — не в личную корысть директора.</p>

  <div class="l24-boris-vs-mos-umysel__split" role="group" aria-label="Два полюса: гражданский спор и уголовное дело">
    <div class="l24-boris-vs-mos-umysel__pole l24-boris-vs-mos-umysel__pole--civil">
      <p class="l24-boris-vs-mos-umysel__pole-hd">Гражданский спор</p>
      <p class="l24-boris-vs-mos-umysel__pole-sub">Переплата, убытки, неосновательное обогащение — после приёмки работ</p>
    </div>
    <div class="l24-boris-vs-mos-umysel__pole l24-boris-vs-mos-umysel__pole--crim">
      <p class="l24-boris-vs-mos-umysel__pole-hd">Уголовное дело</p>
      <p class="l24-boris-vs-mos-umysel__pole-sub">ч. 3 ст. 159 — умысел на хищение <em>до</em> получения денег, корыстная цель</p>
    </div>
  </div>

  <svg class="l24-boris-vs-mos-umysel__scheme-svg" viewBox="0 0 720 220" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="bm159t bm159d">
    <title id="bm159t">Схема границы гражданского спора и уголовного дела при муниципальном контракте — дело Столярова</title>
    <desc id="bm159d">Четыре аргумента защиты (контракт исполнен, акты без претензий, экспертиза не заменяет умысел, зарплата не корысть) сдвигают спор из уголовной плоскости в гражданскую — позиция ВС РФ № 85-УД26-2-К1</desc>
    <defs>
      <marker id="bm159-arr-c" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
        <polygon points="0 0, 8 3.5, 0 7" fill="#38b2ac"/>
      </marker>
      <marker id="bm159-arr-r" markerWidth="8" markerHeight="7" refX="1" refY="3.5" orient="auto">
        <polygon points="8 0, 0 3.5, 8 7" fill="#fc8181"/>
      </marker>
    </defs>

    <!-- Центральная граница -->
    <line x1="360" y1="18" x2="360" y2="202" stroke="rgba(236,201,75,0.45)" stroke-width="2" stroke-dasharray="6,5"/>
    <text x="360" y="14" text-anchor="middle" fill="#ecc94b" font-size="7" font-weight="700" font-family="system-ui,sans-serif" letter-spacing=".05em">ГРАНИЦА</text>

    <!-- Левый полюс: гражданский -->
    <rect x="16" y="28" width="148" height="164" rx="10" fill="rgba(56,178,172,0.12)" stroke="#38b2ac" stroke-width="1.5"/>
    <text x="90" y="50" text-anchor="middle" fill="#b2f5ea" font-size="8.5" font-weight="800" font-family="system-ui,sans-serif">ГРАЖДАНСКИЙ</text>
    <text x="90" y="64" text-anchor="middle" fill="#b2f5ea" font-size="8.5" font-weight="800" font-family="system-ui,sans-serif">СПОР</text>
    <text x="90" y="84" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-family="system-ui,sans-serif">иск о переплате</text>
    <text x="90" y="96" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-family="system-ui,sans-serif">убытки · 44-ФЗ</text>
    <rect x="32" y="108" width="116" height="22" rx="5" fill="rgba(56,178,172,0.22)" stroke="#68d391" stroke-width="1"/>
    <text x="90" y="122" text-anchor="middle" fill="#c6f6d5" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">дело Столярова →</text>
    <text x="90" y="148" text-anchor="middle" fill="#68d391" font-size="7" font-weight="700" font-family="system-ui,sans-serif">Пленум № 48:</text>
    <text x="90" y="160" text-anchor="middle" fill="#94a3b8" font-size="6.2" font-family="system-ui,sans-serif">неисполнение ≠ мошенничество</text>
    <text x="90" y="172" text-anchor="middle" fill="#94a3b8" font-size="6.2" font-family="system-ui,sans-serif">само по себе</text>

    <!-- Правый полюс: уголовный -->
    <rect x="556" y="28" width="148" height="164" rx="10" fill="rgba(220,38,38,0.1)" stroke="#fc8181" stroke-width="1.5"/>
    <text x="630" y="50" text-anchor="middle" fill="#fed7d7" font-size="8.5" font-weight="800" font-family="system-ui,sans-serif">УГОЛОВНОЕ</text>
    <text x="630" y="64" text-anchor="middle" fill="#fed7d7" font-size="8.5" font-weight="800" font-family="system-ui,sans-serif">ДЕЛО</text>
    <text x="630" y="84" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-family="system-ui,sans-serif">ч. 3 ст. 159 УК</text>
    <text x="630" y="96" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-family="system-ui,sans-serif">умысел + корысть</text>
    <rect x="572" y="108" width="116" height="22" rx="5" fill="rgba(220,38,38,0.18)" stroke="#fc8181" stroke-width="1"/>
    <text x="630" y="122" text-anchor="middle" fill="#feb2b2" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">← нужно доказать</text>
    <text x="630" y="148" text-anchor="middle" fill="#fc8181" font-size="7" font-weight="700" font-family="system-ui,sans-serif">экспертиза «470 000 ₽»</text>
    <text x="630" y="160" text-anchor="middle" fill="#94a3b8" font-size="6.2" font-family="system-ui,sans-serif">недостаточна без</text>
    <text x="630" y="172" text-anchor="middle" fill="#94a3b8" font-size="6.2" font-family="system-ui,sans-serif">умысла до оплаты</text>

    <!-- 4 узла (центр) -->
    <rect x="188" y="36" width="124" height="36" rx="7" fill="rgba(56,178,172,0.2)" stroke="#38b2ac" stroke-width="1.3"/>
    <text x="250" y="52" text-anchor="middle" fill="#e2e8f0" font-size="7" font-weight="700" font-family="system-ui,sans-serif">① Контракт исполнен</text>
    <text x="250" y="64" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">612 144 ₽ · работы сделаны</text>
    <line x1="188" y1="54" x2="164" y2="90" stroke="#38b2ac" stroke-width="1.4" marker-end="url(#bm159-arr-c)"/>

    <rect x="408" y="36" width="124" height="36" rx="7" fill="rgba(66,153,225,0.18)" stroke="#4299e1" stroke-width="1.3"/>
    <text x="470" y="52" text-anchor="middle" fill="#e2e8f0" font-size="7" font-weight="700" font-family="system-ui,sans-serif">② Акты без претензий</text>
    <text x="470" y="64" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">приёмка заказчиком · КС-2</text>
    <line x1="408" y1="54" x2="196" y2="100" stroke="#4299e1" stroke-width="1.4" marker-end="url(#bm159-arr-c)"/>

    <rect x="188" y="148" width="124" height="36" rx="7" fill="rgba(236,201,75,0.16)" stroke="#ecc94b" stroke-width="1.3"/>
    <text x="250" y="164" text-anchor="middle" fill="#e2e8f0" font-size="7" font-weight="700" font-family="system-ui,sans-serif">③ Экспертиза ≠ умысел</text>
    <text x="250" y="176" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">разница стоимости · не хищение</text>
    <line x1="188" y1="166" x2="164" y2="130" stroke="#ecc94b" stroke-width="1.4" marker-end="url(#bm159-arr-c)"/>

    <rect x="408" y="148" width="124" height="36" rx="7" fill="rgba(104,211,145,0.16)" stroke="#68d391" stroke-width="1.3"/>
    <text x="470" y="164" text-anchor="middle" fill="#e2e8f0" font-size="7" font-weight="700" font-family="system-ui,sans-serif">④ Зарплата ≠ корысть</text>
    <text x="470" y="176" text-anchor="middle" fill="#94a3b8" font-size="5.8" font-family="system-ui,sans-serif">сотрудники МУП · не личная польза</text>
    <line x1="408" y1="166" x2="196" y2="120" stroke="#68d391" stroke-width="1.4" marker-end="url(#bm159-arr-c)"/>

    <!-- Центральный вердикт ВС -->
    <rect x="248" y="88" width="224" height="44" rx="8" fill="rgba(236,201,75,0.14)" stroke="#ecc94b" stroke-width="1.6"/>
    <text x="360" y="106" text-anchor="middle" fill="#ecc94b" font-size="7.5" font-weight="800" font-family="system-ui,sans-serif">ВС 14.05.2026 · № 85-УД26-2-К1</text>
    <text x="360" y="120" text-anchor="middle" fill="#fde68a" font-size="6.5" font-family="system-ui,sans-serif">отмена приговора · ГП РФ поддержал защиту</text>

    <!-- Стрелки от уголовного (блокированы) -->
    <line x1="532" y1="54" x2="360" y2="110" stroke="#fc8181" stroke-width="1" stroke-dasharray="4,3" opacity="0.45" marker-end="url(#bm159-arr-r)"/>
    <line x1="532" y1="166" x2="360" y2="118" stroke="#fc8181" stroke-width="1" stroke-dasharray="4,3" opacity="0.45" marker-end="url(#bm159-arr-r)"/>

    <text x="360" y="208" text-anchor="middle" fill="#64748b" font-size="6.2" font-family="system-ui,sans-serif">Четыре узла → гражданская плоскость · уголовная требует умысел до оплаты</text>
  </svg>

  <div class="l24-boris-vs-mos-umysel__grid" role="list" aria-label="Четыре узла границы ответственности">
    <div class="l24-boris-vs-mos-umysel__node" role="listitem">
      <span class="l24-boris-vs-mos-umysel__node-tag">узел ①</span>
      <span class="l24-boris-vs-mos-umysel__node-label">Контракт исполнен<small>Работы по переправе выполнены МУП МРЭП; оплата 612 144 ₽ в пределах цены контракта</small></span>
    </div>
    <div class="l24-boris-vs-mos-umysel__node" role="listitem">
      <span class="l24-boris-vs-mos-umysel__node-tag">узел ②</span>
      <span class="l24-boris-vs-mos-umysel__node-label">Акты без претензий<small>Заказчик подписал акт приёмки без оговорок — спор о «переплате» после факта исполнения</small></span>
    </div>
    <div class="l24-boris-vs-mos-umysel__node" role="listitem">
      <span class="l24-boris-vs-mos-umysel__node-tag">узел ③</span>
      <span class="l24-boris-vs-mos-umysel__node-label">Экспертиза ≠ умысел<small>Заключение о разнице стоимости (470 000 ₽) не заменяет доказывание умысла на хищение до получения денег</small></span>
    </div>
    <div class="l24-boris-vs-mos-umysel__node" role="listitem">
      <span class="l24-boris-vs-mos-umysel__node-tag">узел ④</span>
      <span class="l24-boris-vs-mos-umysel__node-label">Зарплата ≠ корысть<small>Средства на заработную плату сотрудников, выполнявших работы — не личное обогащение директора</small></span>
    </div>
  </div>

  <p class="l24-boris-vs-mos-umysel__verdict"><strong>Вывод ВС:</strong> при надлежащем исполнении муниципального контракта и приёмке без претензий переплата по экспертизе остаётся в зоне гражданского спора — пока не доказан заведомый обман и умысел на хищение до оплаты (Пленум ВС № 48, п. 9–10).</p>

  <div class="l24-boris-vs-mos-umysel__foot" aria-label="Нормативная база блока">
    <span class="l24-boris-vs-mos-umysel__tag l24-boris-vs-mos-umysel__tag--case">ВС 14.05.2026 · № 85-УД26-2-К1 · Столяров</span>
    <span class="l24-boris-vs-mos-umysel__tag l24-boris-vs-mos-umysel__tag--crim">ч. 3 ст. 159 УК · крупный размер</span>
    <span class="l24-boris-vs-mos-umysel__tag l24-boris-vs-mos-umysel__tag--civil">гражданский спор · переплата</span>
    <span class="l24-boris-vs-mos-umysel__tag l24-boris-vs-mos-umysel__tag--law">44-ФЗ · п. 9 ч. 1 ст. 93 · экстренный контракт</span>
    <span class="l24-boris-vs-mos-umysel__tag l24-boris-vs-mos-umysel__tag--law">Пленум ВС № 48 · умысел до получения</span>
  </div>
</div>
</section>
```

## Передача Наташе

- **Якорь:** `l24-boris-vs-moshennichestvo-umysel`
- **После H2-3:** «Гражданский спор или уголовное дело: когда переплата по контракту не равна мошенничеству»
- **Перед:** H2-4 «Умысел до получения денег: Пленум ВС № 48 и доказывание корыстной цели»
- **MCP-only:** без `<canvas>` и `<script>` — только inline CSS + SVG + grid
