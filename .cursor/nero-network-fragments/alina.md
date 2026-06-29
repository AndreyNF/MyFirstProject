=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Зал КС: лестница квалификации через снятый фильтр» — барьер «госдоля в капитале» больше не блокирует переход с ч. 4 на ч. 5 ст. 159 при подряде с госкомпанией |
| **Центральная метафора** | Двухуровневая «лестница порогов»: ч. 4 (тяжкое, ≥1 млн ₽) → ч. 5 (средняя тяжесть, ≥250 тыс. ₽); между ними — сломанный фильтр «субъект РФ в акционерах»; над сценой — постановление КС № 43-П/2026 и определение ВС № 64-УД26-2-К9 |
| **Пространство** | Светлый тёплый градиент «утро в зале КС»; SVG — фасад Конституционного суда, договор подряда ООО×ПАО, кабельная линия (кейс Шеврюкова), шкалы ущерба 2,16 млн ₽; не весы ДТП, не СИП, не ФНС |
| **Движение** | Только CSS: пульс бейджа КС, мерцание стрелки переквалификации, анимация «осыпания» барьера-фильтра, подсветка ч. 5; `prefers-reduced-motion` отключает |
| **Палитра** | `#0f172a` текст, `#92400e` КС/конституция, `#b45309` акцент, `#059669` ч. 5/смягчение, `#991b1b` ч. 4/тяжкое, `#475569` подзаголовок, `#a31830` CTA, `#fffbeb`–`#f8fafc` фон |
| **Аудитория** | Подрядчики, гендиректора, ИП при контрактах с ПАО/АО с госучастием; адвокаты по переквалификации мошенничества ст. 159 |

## Чеклист отличий от других hero

- [x] **Не весы ДТП / ст. 73** (`l24-hero-vs-gumanizaciya-dtp-…`): нет колонии и дороги — фокус **КС 2026, ст. 159, ч. 4→5, госакционер**
- [x] **Не СИП / товарный знак**: нет свидетельства ТЗ — угол **мошенничество в предпринимательской сфере**
- [x] **Не обзор ВС № 4 (налог)**: нет ФНС — инстанция **КС РФ + ВС по уголовному делу**
- [x] **Уникальная сцена**: лестница порогов ущерба + сломанный фильтр госдоли + договор подряда + кабельная линия Сахалинэнерго
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA: «Консультация по переквалификации мошенничества» → `https://advokat-vsem.ru/`

```html
<section id="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026" class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026" aria-label="КС РФ 2026: доля государства не отягчает мошенничество — переквалификация с ч. 4 на ч. 5 ст. 159">
  <style>
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(158deg, #fefefe 0%, #fffbeb 26%, #f8fafc 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 42% 38% at 92% 8%, rgba(180, 83, 9, 0.08) 0%, transparent 55%),
        radial-gradient(ellipse 36% 34% at 4% 92%, rgba(5, 150, 105, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__inner {
      position: relative;
      z-index: 1;
      max-width: 1200px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1.04fr 0.96fr;
      gap: 44px;
      align-items: center;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(15, 23, 42, 0.1);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #b45309;
      flex-shrink: 0;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.38rem, 3vw, 2.12rem);
      line-height: 1.24;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__h1-accent {
      color: #92400e;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact--ks {
      border-color: #fcd34d;
      color: #92400e;
      background: #fffbeb;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact--ok {
      border-color: #a7f3d0;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__cta {
      display: inline-block;
      background: #a31830;
      color: #fff !important;
      padding: 14px 28px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(163, 24, 48, 0.2);
      line-height: 1.35;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__cta:hover {
      background: #8b1528;
    }
    .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__ks-pulse {
        animation: hero-ks159-pulse 3.6s ease-in-out infinite;
      }
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__arrow {
        animation: hero-ks159-arrow 2.8s ease-in-out infinite;
      }
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__barrier {
        animation: hero-ks159-crumble 4.2s ease-in-out infinite;
      }
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__ch5 {
        animation: hero-ks159-glow 3.4s ease-in-out infinite;
      }
    }
    @keyframes hero-ks159-pulse {
      0%, 100% { opacity: 0.88; }
      50% { opacity: 1; }
    }
    @keyframes hero-ks159-arrow {
      0%, 100% { transform: translateY(0); opacity: 0.75; }
      50% { transform: translateY(6px); opacity: 1; }
    }
    @keyframes hero-ks159-crumble {
      0%, 100% { opacity: 0.35; transform: translateX(0); }
      50% { opacity: 0.15; transform: translateX(4px); }
    }
    @keyframes hero-ks159-glow {
      0%, 100% { filter: drop-shadow(0 0 0 transparent); }
      50% { filter: drop-shadow(0 0 6px rgba(5, 150, 105, 0.45)); }
    }
    @media (prefers-reduced-motion: reduce) {
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__ks-pulse,
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__arrow,
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__barrier,
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__ch5 {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__inner">
    <div class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__content">
      <div class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__badge">
        <span class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__badge-mark" aria-hidden="true"></span>
        UG · КС РФ 2026 · ст. 159 · № 43-П/2026
      </div>
      <h1 class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__h1">
        <span class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__h1-accent">КС РФ 2026: доля государства в компании не отягчает мошенничество</span> — переквалификация с ч. 4 на ч. 5 ст. 159 (постановление № 43-П/2026)
      </h1>
      <p class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__sub">
        Подряд с госкомпанией, ущерб 2+ млн ₽: почему суды ошибочно отказывали в ч. 5 ст. 159 из-за акционера-субъекта РФ — и что это меняет для защиты бизнеса
      </p>
      <ul class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__facts">
        <li class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact--ks">№ 43-П/2026 · 29.06.2026</li>
        <li class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact--warn">ч. 4 → ч. 5 ст. 159</li>
        <li class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact">ущерб 2,16 млн ₽</li>
        <li class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__fact--ok">госдоля ≠ барьер</li>
      </ul>
      <a class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по переквалификации мошенничества</a>
    </div>
    <div class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Конституционный суд: лестница переквалификации с ч. 4 на ч. 5 ст. 159 — снят фильтр госдоли в капитале потерпевшей госкомпании">
        <defs>
          <linearGradient id="hero-ks159-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fffbeb"/>
            <stop offset="100%" stop-color="#f8fafc"/>
          </linearGradient>
          <linearGradient id="hero-ks159-ks" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#b45309"/>
            <stop offset="100%" stop-color="#78350f"/>
          </linearGradient>
          <linearGradient id="hero-ks159-ch4" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#fecaca"/>
            <stop offset="100%" stop-color="#f87171"/>
          </linearGradient>
          <linearGradient id="hero-ks159-ch5" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#d1fae5"/>
            <stop offset="100%" stop-color="#6ee7b7"/>
          </linearGradient>
          <pattern id="hero-ks159-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#fffbeb"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#fde68a" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-ks159-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-ks159-bg)" stroke="#fcd34d" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-ks159-grid)" opacity="0.3"/>
        <!-- фасад КС РФ -->
        <g class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__ks-pulse" filter="url(#hero-ks159-shadow)" transform="translate(138, 10)">
          <rect x="0" y="40" width="224" height="56" rx="4" fill="url(#hero-ks159-ks)"/>
          <polygon points="112,0 224,40 0,40" fill="#d97706"/>
          <rect x="20" y="52" width="28" height="36" rx="2" fill="#78350f" opacity="0.45"/>
          <rect x="98" y="52" width="28" height="36" rx="2" fill="#78350f" opacity="0.45"/>
          <rect x="176" y="52" width="28" height="36" rx="2" fill="#78350f" opacity="0.45"/>
          <text x="112" y="62" text-anchor="middle" fill="#fffbeb" font-size="6" font-weight="800" letter-spacing="0.04em">КОНСТИТУЦИОННЫЙ СУД РФ</text>
          <text x="112" y="76" text-anchor="middle" fill="#fde68a" font-size="5.5" font-weight="600">постановление № 43-П/2026</text>
        </g>
        <!-- постановление КС -->
        <g filter="url(#hero-ks159-shadow)" transform="translate(20, 52)">
          <rect width="110" height="70" rx="8" fill="#fff" stroke="#b45309" stroke-width="1.2"/>
          <text x="55" y="14" text-anchor="middle" fill="#92400e" font-size="5.5" font-weight="800">ПОСТАНОВЛЕНИЕ</text>
          <text x="55" y="28" text-anchor="middle" fill="#334155" font-size="5" font-weight="700">№ 43-П/2026</text>
          <text x="55" y="42" text-anchor="middle" fill="#64748b" font-size="4.5">29.06.2026 · РАПСИ</text>
          <rect x="10" y="50" width="90" height="12" rx="4" fill="#fffbeb"/>
          <text x="55" y="59" text-anchor="middle" fill="#92400e" font-size="4.2" font-weight="600">госдоля не отягчает</text>
        </g>
        <!-- определение ВС -->
        <g filter="url(#hero-ks159-shadow)" transform="translate(370, 48)">
          <rect width="108" height="74" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1"/>
          <text x="54" y="14" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">ВС РФ</text>
          <text x="54" y="28" text-anchor="middle" fill="#334155" font-size="4.8" font-weight="700">№ 64-УД26-2-К9</text>
          <text x="54" y="42" text-anchor="middle" fill="#64748b" font-size="4.5">25.02.2026 · Шеврюков</text>
          <rect x="10" y="50" width="88" height="12" rx="4" fill="#f5f3ff"/>
          <text x="54" y="59" text-anchor="middle" fill="#4338ca" font-size="4.2" font-weight="600">переквалификация ч. 4→5</text>
        </g>
        <!-- лестница квалификации -->
        <g filter="url(#hero-ks159-shadow)">
          <!-- ч. 4 верхняя ступень -->
          <rect x="188" y="128" width="124" height="52" rx="8" fill="url(#hero-ks159-ch4)" stroke="#991b1b" stroke-width="1.2"/>
          <text x="250" y="146" text-anchor="middle" fill="#7f1d1d" font-size="6" font-weight="800">ч. 4 ст. 159</text>
          <text x="250" y="160" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="700">тяжкое · до 10 лет</text>
          <text x="250" y="174" text-anchor="middle" fill="#7f1d1d" font-size="4.5">особо крупный ≥ 1 млн ₽</text>
          <!-- стрелка вниз -->
          <g class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__arrow">
            <path d="M250 184 L250 208" stroke="#059669" stroke-width="2.5" stroke-linecap="round"/>
            <path d="M244 202 L250 212 L256 202" fill="#059669"/>
            <text x="250" y="222" text-anchor="middle" fill="#047857" font-size="5" font-weight="700">переквалификация</text>
          </g>
          <!-- сломанный фильтр -->
          <g class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__barrier">
            <rect x="156" y="228" width="188" height="22" rx="4" fill="#fef2f2" stroke="#fca5a5" stroke-width="1" stroke-dasharray="6 4"/>
            <text x="250" y="242" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="700" text-decoration="line-through">фильтр: субъект РФ в акционерах</text>
          </g>
          <!-- ч. 5 нижняя ступень -->
          <g class="l24-hero-ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026__ch5">
            <rect x="188" y="258" width="124" height="52" rx="8" fill="url(#hero-ks159-ch5)" stroke="#059669" stroke-width="1.4"/>
            <text x="250" y="276" text-anchor="middle" fill="#047857" font-size="6" font-weight="800">ч. 5 ст. 159</text>
            <text x="250" y="290" text-anchor="middle" fill="#059669" font-size="5" font-weight="700">средняя тяжесть · до 5 лет</text>
            <text x="250" y="304" text-anchor="middle" fill="#047857" font-size="4.5">значительный ≥ 250 тыс. ₽</text>
          </g>
        </g>
        <!-- договор подряда -->
        <g filter="url(#hero-ks159-shadow)" transform="translate(24, 318)">
          <rect width="132" height="96" rx="8" fill="#fff" stroke="#334155" stroke-width="1"/>
          <text x="66" y="16" text-anchor="middle" fill="#0f172a" font-size="5.5" font-weight="800">ДОГОВОР ПОДРЯДА</text>
          <rect x="10" y="24" width="52" height="28" rx="4" fill="#f1f5f9" stroke="#94a3b8"/>
          <text x="36" y="38" text-anchor="middle" fill="#334155" font-size="4.5" font-weight="700">ООО</text>
          <text x="36" y="48" text-anchor="middle" fill="#64748b" font-size="4">подрядчик</text>
          <text x="66" y="42" text-anchor="middle" fill="#64748b" font-size="6">×</text>
          <rect x="70" y="24" width="52" height="28" rx="4" fill="#fffbeb" stroke="#b45309"/>
          <text x="96" y="38" text-anchor="middle" fill="#92400e" font-size="4.5" font-weight="700">ПАО</text>
          <text x="96" y="48" text-anchor="middle" fill="#64748b" font-size="4">госакционер</text>
          <line x1="10" y1="58" x2="122" y2="58" stroke="#e2e8f0"/>
          <text x="66" y="72" text-anchor="middle" fill="#334155" font-size="4.5">обе — коммерческие</text>
          <text x="66" y="84" text-anchor="middle" fill="#64748b" font-size="4">ст. 50 ГК РФ · ч. 5 ст. 159</text>
        </g>
        <!-- шкала ущерба -->
        <g filter="url(#hero-ks159-shadow)" transform="translate(168, 318)">
          <rect width="164" height="96" rx="8" fill="#fff" stroke="#64748b" stroke-width="1"/>
          <text x="82" y="16" text-anchor="middle" fill="#0f172a" font-size="5.5" font-weight="800">ЛОВУШКА ПОРОГОВ</text>
          <text x="82" y="28" text-anchor="middle" fill="#64748b" font-size="4.5">дело Шеврюкова · 2 159 315 ₽</text>
          <rect x="10" y="36" width="144" height="10" rx="3" fill="#fef2f2"/>
          <rect x="10" y="36" width="108" height="10" rx="3" fill="#f87171"/>
          <text x="82" y="44" text-anchor="middle" fill="#7f1d1d" font-size="4" font-weight="600">ч. 4: особо крупный (≥1 млн)</text>
          <rect x="10" y="54" width="144" height="10" rx="3" fill="#ecfdf5"/>
          <rect x="10" y="54" width="48" height="10" rx="3" fill="#34d399"/>
          <text x="82" y="62" text-anchor="middle" fill="#047857" font-size="4" font-weight="600">ч. 5: значительный (≥250 тыс.)</text>
          <text x="82" y="78" text-anchor="middle" fill="#334155" font-size="4.5" font-weight="600">4 года → 2 года условно</text>
          <text x="82" y="90" text-anchor="middle" fill="#64748b" font-size="4">Сахалинэнерго · Южно-Сахалинск</text>
        </g>
        <!-- кабельная линия -->
        <g filter="url(#hero-ks159-shadow)" transform="translate(344, 318)">
          <rect width="132" height="96" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1"/>
          <text x="66" y="16" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">КЕЙС ШЕВРЮКОВА</text>
          <path d="M16 72 Q40 48 66 56 Q92 64 116 44" fill="none" stroke="#64748b" stroke-width="3" stroke-linecap="round"/>
          <path d="M16 72 Q40 68 66 70" fill="none" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 3" opacity="0.6"/>
          <circle cx="66" cy="56" r="6" fill="#fde68a" stroke="#b45309"/>
          <circle cx="116" cy="44" r="5" fill="#6ee7b7" stroke="#059669"/>
          <text x="66" y="84" text-anchor="middle" fill="#334155" font-size="4.5">реконструкция кабеля</text>
          <text x="66" y="92" text-anchor="middle" fill="#64748b" font-size="4">видимость исполнения</text>
        </g>
        <!-- пирог акционеров -->
        <g transform="translate(400, 168)" opacity="0.9">
          <circle cx="0" cy="0" r="22" fill="#fff" stroke="#b45309" stroke-width="1"/>
          <path d="M0 0 L0 -22 A22 22 0 0 1 18 -12 Z" fill="#fcd34d"/>
          <path d="M0 0 L18 -12 A22 22 0 0 1 22 0 Z" fill="#fde68a"/>
          <text x="0" y="4" text-anchor="middle" fill="#92400e" font-size="5" font-weight="700">ПАО</text>
          <text x="0" y="32" text-anchor="middle" fill="#64748b" font-size="4">доля субъекта РФ</text>
          <text x="0" y="42" text-anchor="middle" fill="#059669" font-size="4" font-weight="600">≠ барьер ч. 5</text>
        </g>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">КС № 43-П/2026 · лестница ч. 4→5 · снят фильтр госакционера · защита подрядчиков</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: ks-dolya-gosudarstva-moshennichestvo-st-159-perekvalifikaciya-2026
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>` и `<script>`.
