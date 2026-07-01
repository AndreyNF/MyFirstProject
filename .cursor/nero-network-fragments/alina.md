=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Мост между контрактом и уголовным делом» — Калужская обл., МУП МРЭП, экстренный ремонт переправы после урагана, спор 612 144 ₽ превращается в ч. 3 ст. 159, ВС отменяет приговор |
| **Центральная метафора** | Переправа-мост над водой (факт исполнения работ); весы правосудия: «обвинение / экспертиза» vs «контракт принят»; муниципальный контракт 44-ФЗ; фасад ВС с делом № 85-УД26-2-К1 |
| **Пространство** | UG-градиент Legis24 (#fff7f7 → #f0f0f8); SVG — мост, контракт, весы, здание МУП, блоки фактов (Пленум № 48, умысел, зарплата) |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#a31830` UG-акцент, `#1e3a5f` ВС, `#4338ca` контракт/44-ФЗ, `#059669` исполнение/приёмка, `#dc2626` обвинение, `#0f172a` текст |
| **Аудитория** | Директора МУП и муниципальных предприятий; подрядчики по 44-ФЗ; адвокаты по ст. 159 на кассации |

## Чеклист отличий от других hero

- [x] **Не условный срок (18-УД26-4-К4)**: не ст. 73 — угол **ч. 3 ст. 159, муниципальный контракт, умысел не доказан**
- [x] **Не Пленум № 42 ARB**: тип **UG**, не банкротство/субсидиарка
- [x] **Не завышение цен ч. 4**: работы **выполнены и приняты**, не организованная группа
- [x] Уникальная сцена: **мост-переправа** + контракт 612 144 ₽ + весы «обвинение vs исполнение» + МУП
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Badge **UG · ВС 2026**; chips: ч.3 ст.159, №85-УД26-2-К1, 612 144 ₽, Пленум №48

```html
<section id="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026" class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026" aria-label="ВС отменил приговор директору МУП за мошенничество: работы по контракту выполнены, умысел не доказан">
  <style>
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(150deg, #fefefe 0%, #fff7f7 40%, #f0f0f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 44% 40% at 92% 8%, rgba(163, 24, 48, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 38% 34% at 5% 92%, rgba(67, 56, 202, 0.04) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__inner {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.05fr 0.95fr;
      gap: 44px;
      align-items: center;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(163, 24, 48, 0.18);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #a31830;
      flex-shrink: 0;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.35rem, 2.9vw, 2.1rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__h1-accent {
      color: #a31830;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.45vw, 1.08rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact--red {
      border-color: #fecaca;
      color: #a31830;
      background: #fff7f7;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact--blue {
      border-color: #c4b5fd;
      color: #4338ca;
      background: #f5f3ff;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact--ok {
      border-color: #a7f3d0;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__inner {
        grid-template-columns: 1fr;
      }
      .l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__visual {
        order: -1;
        max-height: 320px;
        overflow: hidden;
      }
    }
  </style>

  <div class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__inner">
    <div class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__content">
      <div class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__badge">
        <span class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__badge-mark" aria-hidden="true"></span>
        UG · ВС 2026
      </div>
      <h1 class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__h1">
        <span class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__h1-accent">ВС отменил приговор директору МУП за мошенничество:</span> работы по контракту выполнены, умысел не доказан
      </h1>
      <p class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__sub">
        Когда спор по муниципальному контракту становится уголовным делом по ч. 3 ст. 159 — и как защитить руководителя на кассации
      </p>
      <ul class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__facts">
        <li class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact--red">ч. 3 ст. 159 УК РФ</li>
        <li class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact">№ 85-УД26-2-К1</li>
        <li class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact--blue">612 144 ₽</li>
        <li class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__fact--ok">Пленум № 48</li>
      </ul>
    </div>

    <div class="l24-hero-vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:520px" role="img" aria-label="Мост-переправа, муниципальный контракт и весы правосудия: ВС отменил приговор директору МУП — работы приняты, умысел на хищение не доказан, дело № 85-УД26-2-К1">
        <defs>
          <linearGradient id="hm159-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fafafa"/>
            <stop offset="100%" stop-color="#fff7f7"/>
          </linearGradient>
          <linearGradient id="hm159-water" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#dbeafe"/>
            <stop offset="100%" stop-color="#93c5fd"/>
          </linearGradient>
          <linearGradient id="hm159-navy" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a5f"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="hm159-bridge" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#64748b"/>
            <stop offset="50%" stop-color="#475569"/>
            <stop offset="100%" stop-color="#64748b"/>
          </linearGradient>
          <pattern id="hm159-dots" width="14" height="14" patternUnits="userSpaceOnUse">
            <circle cx="7" cy="7" r="1" fill="#fecaca" opacity="0.45"/>
          </pattern>
          <filter id="hm159-sh" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.1"/>
          </filter>
        </defs>

        <!-- Background -->
        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hm159-bg)" stroke="#fecaca" stroke-width="1.2"/>
        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hm159-dots)" opacity="0.5"/>

        <!-- Top court badge -->
        <g filter="url(#hm159-sh)" transform="translate(148,14)">
          <rect x="0" y="28" width="224" height="48" rx="5" fill="url(#hm159-navy)"/>
          <polygon points="112,4 218,28 6,28" fill="#1a3a6e"/>
          <text x="112" y="48" text-anchor="middle" fill="#e2e8f0" font-size="6.5" font-weight="800" letter-spacing="0.04em">ВС РФ · дело № 85-УД26-2-К1</text>
          <text x="112" y="62" text-anchor="middle" fill="#93c5fd" font-size="5.5">СК по уголовным делам · 14.05.2026 · МУП МРЭП</text>
        </g>

        <!-- Scales of justice above bridge -->
        <rect x="248" y="82" width="6" height="72" rx="3" fill="#334155"/>
        <rect x="220" y="150" width="62" height="7" rx="3.5" fill="#475569"/>
        <circle cx="251" cy="80" r="7" fill="#334155"/>
        <line x1="148" y1="98" x2="354" y2="92" stroke="#475569" stroke-width="4" stroke-linecap="round"/>
        <circle cx="251" cy="95" r="5" fill="#64748b"/>

        <!-- Left pan: OBVINENIE (lighter, higher) -->
        <line x1="162" y1="99" x2="152" y2="128" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2"/>
        <line x1="178" y1="99" x2="188" y2="128" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2"/>
        <g filter="url(#hm159-sh)" transform="translate(124,126)">
          <ellipse cx="58" cy="6" rx="60" ry="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
          <rect x="0" y="4" width="118" height="58" rx="7" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
          <text x="59" y="18" text-anchor="middle" fill="#991b1b" font-size="6" font-weight="800">ОБВИНЕНИЕ</text>
          <text x="59" y="30" text-anchor="middle" fill="#b91c1c" font-size="5">экспертиза «переплаты»</text>
          <text x="59" y="41" text-anchor="middle" fill="#b91c1c" font-size="5">«распорядился сам»</text>
          <text x="59" y="52" text-anchor="middle" fill="#b91c1c" font-size="5">умысел презюмирован</text>
        </g>

        <!-- Right pan: KONTRAKT ISPOLNEN (heavier, lower) -->
        <line x1="332" y1="93" x2="326" y2="118" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2"/>
        <line x1="348" y1="93" x2="354" y2="118" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="3,2"/>
        <g filter="url(#hm159-sh)" transform="translate(318,116)">
          <ellipse cx="52" cy="7" rx="54" ry="7" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
          <rect x="0" y="5" width="106" height="68" rx="7" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
          <text x="53" y="20" text-anchor="middle" fill="#047857" font-size="6" font-weight="800">КОНТРАКТ ИСПОЛНЕН</text>
          <text x="53" y="32" text-anchor="middle" fill="#065f46" font-size="5">✓ работы приняты</text>
          <text x="53" y="43" text-anchor="middle" fill="#065f46" font-size="5">✓ 612 144 ₽ в пределах</text>
          <text x="53" y="54" text-anchor="middle" fill="#065f46" font-size="5">✓ зарплата сотрудникам</text>
          <rect x="8" y="58" width="90" height="13" rx="4" fill="#059669"/>
          <text x="53" y="68" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="700">ВС: умысел не доказан</text>
        </g>

        <!-- Water + bridge (pereprava) -->
        <rect x="28" y="248" width="464" height="52" rx="4" fill="url(#hm159-water)" opacity="0.55"/>
        <path d="M28 272 Q80 262 130 272 T230 268 T330 272 T464 268 L464 300 L28 300 Z" fill="url(#hm159-water)" opacity="0.35"/>
        <!-- Bridge deck -->
        <rect x="48" y="228" width="424" height="14" rx="3" fill="url(#hm159-bridge)"/>
        <!-- Bridge supports -->
        <rect x="118" y="240" width="10" height="58" rx="2" fill="#475569"/>
        <rect x="251" y="240" width="10" height="58" rx="2" fill="#475569"/>
        <rect x="384" y="240" width="10" height="58" rx="2" fill="#475569"/>
        <!-- Bridge railings -->
        <line x1="48" y1="222" x2="472" y2="222" stroke="#94a3b8" stroke-width="2"/>
        <line x1="48" y1="218" x2="472" y2="218" stroke="#cbd5e1" stroke-width="1"/>
        <!-- Repair workers hint -->
        <circle cx="180" cy="218" r="5" fill="#fbbf24" stroke="#b45309" stroke-width="1"/>
        <rect x="174" y="210" width="12" height="6" rx="2" fill="#f59e0b"/>
        <text x="260" y="220" text-anchor="middle" fill="#e2e8f0" font-size="5.5" font-weight="700">РЕМОНТ ПЕРЕПРАВЫ · 44-ФЗ</text>

        <!-- Left bank: MUNICIPAL CONTRACT -->
        <g filter="url(#hm159-sh)" transform="translate(24,188)">
          <rect width="118" height="88" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1.3"/>
          <rect width="118" height="18" rx="8" fill="#4338ca"/>
          <rect y="10" width="118" height="8" fill="#4338ca"/>
          <text x="59" y="13" text-anchor="middle" fill="#e0e7ff" font-size="5.5" font-weight="800">МУНИЦ. КОНТРАКТ</text>
          <text x="59" y="30" text-anchor="middle" fill="#334155" font-size="5">п. 9 ч. 1 ст. 93 44-ФЗ</text>
          <text x="59" y="42" text-anchor="middle" fill="#4338ca" font-size="6.5" font-weight="800">612 144 ₽</text>
          <text x="59" y="54" text-anchor="middle" fill="#64748b" font-size="5">после урагана · экстренно</text>
          <text x="59" y="66" text-anchor="middle" fill="#64748b" font-size="5">Козельский р-н · Калужская обл.</text>
          <rect x="10" y="72" width="98" height="11" rx="3" fill="#f5f3ff"/>
          <text x="59" y="80" text-anchor="middle" fill="#4338ca" font-size="4.8" font-weight="600">приёмка без претензий</text>
        </g>

        <!-- Right bank: MUP building -->
        <g filter="url(#hm159-sh)" transform="translate(378,188)">
          <rect width="118" height="88" rx="8" fill="#fff" stroke="#a31830" stroke-width="1.3"/>
          <rect x="20" y="14" width="78" height="52" rx="3" fill="#f1f5f9" stroke="#cbd5e1" stroke-width="1"/>
          <polygon points="59,6 98,16 20,16" fill="#a31830"/>
          <rect x="32" y="26" width="14" height="12" rx="1" fill="#dbeafe"/>
          <rect x="52" y="26" width="14" height="12" rx="1" fill="#dbeafe"/>
          <rect x="72" y="26" width="14" height="12" rx="1" fill="#dbeafe"/>
          <rect x="46" y="48" width="26" height="18" rx="2" fill="#334155"/>
          <text x="59" y="74" text-anchor="middle" fill="#a31830" font-size="6" font-weight="800">МУП МРЭП</text>
          <text x="59" y="84" text-anchor="middle" fill="#64748b" font-size="4.8">и.о. директора · Столяров</text>
        </g>

        <!-- VS verdict box -->
        <g filter="url(#hm159-sh)" transform="translate(196,308)">
          <rect width="128" height="42" rx="8" fill="url(#hm159-navy)"/>
          <text x="64" y="15" text-anchor="middle" fill="#93c5fd" font-size="5.5" font-weight="700">ВЕРХОВНЫЙ СУД РФ</text>
          <text x="64" y="27" text-anchor="middle" fill="#fff" font-size="6.5" font-weight="800">ПРИГОВОР ОТМЕНЁН</text>
          <text x="64" y="38" text-anchor="middle" fill="#6ee7b7" font-size="5">новое апелляционное рассмотрение</text>
        </g>

        <!-- Bottom three info boxes -->
        <g filter="url(#hm159-sh)" transform="translate(18,358)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#a31830" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#a31830" font-size="6" font-weight="800">ч. 3 ст. 159 УК РФ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">мошенничество · крупный размер</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">умысел до получения денег</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">корыстная цель обязательна</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#fff7f7"/>
          <text x="77" y="63" text-anchor="middle" fill="#a31830" font-size="5" font-weight="600">ВС: экспертиза ≠ умысел</text>
        </g>
        <g filter="url(#hm159-sh)" transform="translate(183,358)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#4338ca" font-size="6" font-weight="800">Пленум ВС № 48</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">мошенничество · п. 14–15</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">умысел возникает до оплаты</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">заведомый отказ от исполнения</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#f5f3ff"/>
          <text x="77" y="63" text-anchor="middle" fill="#4338ca" font-size="5" font-weight="600">26.11.2008 · актуально в 2026</text>
        </g>
        <g filter="url(#hm159-sh)" transform="translate(348,358)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#059669" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#059669" font-size="6" font-weight="800">ГРАЖДАНСКОЕ ≠ УГОЛОВНОЕ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">спор о стоимости работ</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">иск 470 000 ₽ отменён</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">ГП РФ поддержал защиту</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#ecfdf5"/>
          <text x="77" y="63" text-anchor="middle" fill="#059669" font-size="5" font-weight="600">адвокат Р. Шилов · кассация</text>
        </g>

        <text x="260" y="432" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-weight="600">ВС 2026 · ч. 3 ст. 159 · муниципальный контракт · умысел · МУП · 44-ФЗ</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе

SLUG: vs-moshennichestvo-municipalnyj-kontrakt-umysel-st-159-2026
H1_для_hero: ВС отменил приговор директору МУП за мошенничество: работы по контракту выполнены, умысел не доказан
ПОДЗАГОЛОВОК_HERO: Когда спор по муниципальному контракту становится уголовным делом по ч. 3 ст. 159 — и как защитить руководителя на кассации
ТИП_СТАТЬИ: UG — уголовное право / практика ВС
СЛЕДУЮЩИЙ_ШАГ: Наташа (сборка + публикация)
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>` и CTA в hero.
