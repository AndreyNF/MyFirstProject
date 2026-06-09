=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Зал СИП: свидетельство бренда на столе судьи» — спор о неиспользовании разворачивается вокруг частичного «отщепления» классов МКТУ; правообладатель собирает доказательства реального оборота, истец доказывает заинтересованность |
| **Центральная метафора** | Свидетельство ТЗ, разделённое на зоны: охрана сохранена (бельё, класс 25) и прекращена (брюки, колготки); над сценой — таймлайн ст. 1486 (предложение → 2 мес. → 30 дн. → иск) и песочные часы трёхлетнего периода |
| **Пространство** | Светлый градиент «утро в СИП»; SVG — фасад Суда по интеллектуальным правам, сетка МКТУ, пакет доказательств использования, решение СИП-75/2025; не щит маркетплейса, не компенсация иностранцу, не весы ФНС |
| **Движение** | Только CSS: пульс сохранённой зоны свидетельства, мерцание прекращённых ячеек МКТУ, «течение» песка в часах, подсветка стрелок процедуры; `prefers-reduced-motion` отключает |
| **Палитра** | `#0f172a` текст, `#4338ca` СИП/акцент IP, `#059669` сохранённая охрана, `#dc2626` прекращение, `#475569` подзаголовок, `#a31830` CTA, `#f8fafc`–`#eef2f7` фон |
| **Аудитория** | Правообладатели брендов под угрозой иска по ст. 1486 и конкуренты/ИП, готовящие иск о досрочном прекращении чужого знака |

## Чеклист отличий от других hero

- [x] **Не компенсация иностранцу** (`l24-hero-vs-kompensaciya-…`): нет щита маркетплейса, Указа № 322, цепочки лицензия→иск — фокус **неиспользование + ст. 1486**
- [x] **Не Синергетик / POIZON**: нет суммы компенсации 766 млн и оспаривания регистрации — угол **досрочное прекращение охраны**
- [x] **Не обзор ВС № 4 (налог)**: нет ГЭС, ФНС, весов налога на имущество — инстанция **СИП 2026**, гл. **76 ГК / ст. 1486**
- [x] **Уникальная сцена**: фасад СИП + свидетельство с частичным прекращением по МКТУ + таймлайн 1486 + песочные часы 3 лет
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA: «Консультация по защите товарного знака» → `https://advokat-vsem.ru/`

```html
<section id="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026" class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026" aria-label="СИП 2026: досрочное прекращение товарного знака за неиспользование — заинтересованность и защита бренда">
  <style>
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f5f3ff 32%, #eef2f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 42% 38% at 88% 8%, rgba(67, 56, 202, 0.08) 0%, transparent 55%),
        radial-gradient(ellipse 36% 34% at 8% 92%, rgba(5, 150, 105, 0.05) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__inner {
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
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__badge {
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
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #4338ca;
      flex-shrink: 0;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.42rem, 3.1vw, 2.2rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__h1-accent {
      color: #4338ca;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact--accent {
      border-color: #c4b5fd;
      color: #4338ca;
      background: #f5f3ff;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact--ok {
      border-color: #a7f3d0;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cta {
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
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cta:hover {
      background: #8b1528;
    }
    .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cert-keep {
        animation: hero-siptz-keep 4.4s ease-in-out infinite;
      }
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cert-drop {
        animation: hero-siptz-drop 3.6s ease-in-out infinite;
      }
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__hourglass {
        animation: hero-siptz-sand 4s ease-in-out infinite;
      }
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__proc-arrow {
        animation: hero-siptz-arrow 3.2s ease-in-out infinite;
      }
    }
    @keyframes hero-siptz-keep {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.82; }
    }
    @keyframes hero-siptz-drop {
      0%, 100% { opacity: 0.45; }
      50% { opacity: 0.85; }
    }
    @keyframes hero-siptz-sand {
      0%, 100% { opacity: 0.5; transform: translateY(0); }
      50% { opacity: 0.95; transform: translateY(2px); }
    }
    @keyframes hero-siptz-arrow {
      0%, 100% { opacity: 0.55; }
      50% { opacity: 1; }
    }
    @media (prefers-reduced-motion: reduce) {
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cert-keep,
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cert-drop,
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__hourglass,
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__proc-arrow {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__inner">
    <div class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__content">
      <div class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__badge">
        <span class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__badge-mark" aria-hidden="true"></span>
        IP · СИП 2026 · ст. 1486 ГК · СИП-75/2025
      </div>
      <h1 class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__h1">
        <span class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__h1-accent">СИП 2026: досрочное прекращение товарного знака за неиспользование</span> — заинтересованность и защита бренда
      </h1>
      <p class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__sub">
        Решения СИП-75/2025 и практика 2026: частичное прекращение охраны, бремя доказывания и стратегия для правообладателя и истца
      </p>
      <ul class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__facts">
        <li class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact--accent">ст. 1486 ГК РФ</li>
        <li class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact">частичное прекращение · МКТУ</li>
        <li class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact--ok">заинтересованность истца</li>
        <li class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__fact--warn">бремя доказывания</li>
      </ul>
      <a class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по защите товарного знака</a>
    </div>
    <div class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Зал СИП: свидетельство товарного знака с частичным прекращением охраны по классам МКТУ, таймлайн ст. 1486 и песочные часы трёхлетнего неиспользования">
        <defs>
          <linearGradient id="hero-siptz-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#ede9fe"/>
          </linearGradient>
          <linearGradient id="hero-siptz-sip" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#5b21b6"/>
            <stop offset="100%" stop-color="#312e81"/>
          </linearGradient>
          <linearGradient id="hero-siptz-paper" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hero-siptz-keep" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#d1fae5"/>
            <stop offset="100%" stop-color="#6ee7b7"/>
          </linearGradient>
          <linearGradient id="hero-siptz-drop" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#fee2e2"/>
            <stop offset="100%" stop-color="#fecaca"/>
          </linearGradient>
          <pattern id="hero-siptz-grid" width="18" height="18" patternUnits="userSpaceOnUse">
            <rect width="18" height="18" fill="#f5f3ff"/>
            <path d="M18 0 L0 0 0 18" fill="none" stroke="#e9d5ff" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-siptz-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-siptz-bg)" stroke="#c4b5fd" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-siptz-grid)" opacity="0.4"/>
        <!-- фасад СИП -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(148, 14)">
          <rect x="0" y="36" width="204" height="52" rx="4" fill="url(#hero-siptz-sip)"/>
          <polygon points="102,0 204,36 0,36" fill="#6d28d9"/>
          <rect x="24" y="48" width="28" height="32" rx="2" fill="#4c1d95" opacity="0.5"/>
          <rect x="88" y="48" width="28" height="32" rx="2" fill="#4c1d95" opacity="0.5"/>
          <rect x="152" y="48" width="28" height="32" rx="2" fill="#4c1d95" opacity="0.5"/>
          <text x="102" y="58" text-anchor="middle" fill="#ede9fe" font-size="6.5" font-weight="800" letter-spacing="0.06em">СУД ПО ИНТЕЛЛЕКТУАЛЬНЫМ ПРАВАМ</text>
          <text x="102" y="72" text-anchor="middle" fill="#c4b5fd" font-size="5.5" font-weight="600">ст. 1486 ГК · гл. 76 · 2026</text>
        </g>
        <!-- песочные часы 3 года -->
        <g class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__hourglass" filter="url(#hero-siptz-shadow)" transform="translate(28, 52)">
          <path d="M20 0 L36 0 L28 22 L36 44 L20 44 L12 22 Z" fill="#fff" stroke="#4338ca" stroke-width="1.2"/>
          <path d="M16 8 L32 8 L28 22 L24 22 Z" fill="#c4b5fd" opacity="0.7"/>
          <path d="M24 22 L28 22 L32 36 L16 36 Z" fill="#a78bfa" opacity="0.55"/>
          <text x="20" y="56" text-anchor="middle" fill="#4338ca" font-size="5" font-weight="700">3 года</text>
          <text x="20" y="66" text-anchor="middle" fill="#64748b" font-size="4.5">неиспользование</text>
        </g>
        <!-- таймлайн процедуры -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(360, 48)">
          <rect width="112" height="72" rx="8" fill="#fff" stroke="#c4b5fd" stroke-width="1"/>
          <text x="56" y="14" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">ПРОЦЕДУРА</text>
          <text x="56" y="26" text-anchor="middle" fill="#64748b" font-size="4.5">п. 1 ст. 1486</text>
          <rect x="8" y="32" width="22" height="14" rx="3" fill="#f5f3ff" stroke="#a78bfa"/>
          <text x="19" y="42" text-anchor="middle" fill="#4338ca" font-size="4" font-weight="700">письмо</text>
          <line class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__proc-arrow" x1="32" y1="39" x2="40" y2="39" stroke="#4338ca" stroke-width="1.2" marker-end="url(#hero-siptz-arr)"/>
          <rect x="40" y="32" width="22" height="14" rx="3" fill="#f5f3ff" stroke="#a78bfa"/>
          <text x="51" y="42" text-anchor="middle" fill="#4338ca" font-size="4" font-weight="700">2 мес.</text>
          <line class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__proc-arrow" x1="64" y1="39" x2="72" y2="39" stroke="#4338ca" stroke-width="1.2"/>
          <rect x="72" y="32" width="22" height="14" rx="3" fill="#fef2f2" stroke="#f87171"/>
          <text x="83" y="42" text-anchor="middle" fill="#991b1b" font-size="4" font-weight="700">30 дн.</text>
          <text x="56" y="62" text-anchor="middle" fill="#334155" font-size="4.5" font-weight="600">иск в СИП</text>
        </g>
        <marker id="hero-siptz-arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
          <path d="M0 0 L6 3 L0 6 Z" fill="#4338ca"/>
        </marker>
        <!-- свидетельство ТЗ -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(118, 118)">
          <rect width="264" height="148" rx="10" fill="url(#hero-siptz-paper)" stroke="#94a3b8" stroke-width="1.4"/>
          <rect x="0" y="0" width="264" height="22" rx="10" fill="#f5f3ff"/>
          <rect x="0" y="12" width="264" height="10" fill="#f5f3ff"/>
          <text x="132" y="15" text-anchor="middle" fill="#4338ca" font-size="7" font-weight="800">СВИДЕТЕЛЬСТВО НА ТОВАРНЫЙ ЗНАК</text>
          <circle cx="42" cy="52" r="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.2"/>
          <text x="42" y="56" text-anchor="middle" fill="#5b21b6" font-size="14" font-weight="800">®</text>
          <text x="132" y="48" text-anchor="middle" fill="#0f172a" font-size="8" font-weight="700">класс 25 МКТУ · одежда</text>
          <text x="132" y="62" text-anchor="middle" fill="#64748b" font-size="5.5">СИП-75/2025 · 30.03.2026</text>
          <!-- сохранённая зона -->
          <g class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cert-keep">
            <rect x="16" y="78" width="108" height="54" rx="6" fill="url(#hero-siptz-keep)" stroke="#059669" stroke-width="1"/>
            <text x="70" y="94" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="800">ОХРАНА СОХРАНЕНА</text>
            <text x="70" y="108" text-anchor="middle" fill="#065f46" font-size="5">нижнее бельё</text>
            <text x="70" y="120" text-anchor="middle" fill="#065f46" font-size="5">бюстгальтеры</text>
            <path d="M24 126 L36 118 L48 126" fill="none" stroke="#059669" stroke-width="1.5" stroke-linecap="round"/>
          </g>
          <!-- прекращённая зона -->
          <g class="l24-hero-sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026__cert-drop">
            <rect x="140" y="78" width="108" height="54" rx="6" fill="url(#hero-siptz-drop)" stroke="#dc2626" stroke-width="1" stroke-dasharray="4 3"/>
            <text x="194" y="94" text-anchor="middle" fill="#991b1b" font-size="5.5" font-weight="800">ПРЕКРАЩЕНО</text>
            <text x="194" y="108" text-anchor="middle" fill="#b91c1c" font-size="5">брюки · колготки</text>
            <text x="194" y="120" text-anchor="middle" fill="#b91c1c" font-size="5">корсеты · трусы</text>
            <line x1="148" y1="100" x2="240" y2="118" stroke="#dc2626" stroke-width="1.5"/>
            <line x1="148" y1="118" x2="240" y2="100" stroke="#dc2626" stroke-width="1.5"/>
          </g>
        </g>
        <!-- сетка МКТУ -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(24, 286)">
          <rect width="140" height="88" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="1"/>
          <text x="70" y="16" text-anchor="middle" fill="#334155" font-size="5.5" font-weight="800">КЛАССЫ МКТУ</text>
          <rect x="10" y="24" width="28" height="22" rx="3" fill="#ecfdf5" stroke="#6ee7b7"/>
          <text x="24" y="38" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="700">25✓</text>
          <rect x="42" y="24" width="28" height="22" rx="3" fill="#fef2f2" stroke="#fca5a5"/>
          <text x="56" y="38" text-anchor="middle" fill="#991b1b" font-size="4.5" font-weight="700">25✗</text>
          <rect x="74" y="24" width="28" height="22" rx="3" fill="#f5f3ff" stroke="#c4b5fd"/>
          <text x="88" y="38" text-anchor="middle" fill="#4338ca" font-size="4.5" font-weight="700">6</text>
          <rect x="106" y="24" width="28" height="22" rx="3" fill="#f5f3ff" stroke="#c4b5fd"/>
          <text x="120" y="38" text-anchor="middle" fill="#4338ca" font-size="4.5" font-weight="700">19</text>
          <text x="70" y="58" text-anchor="middle" fill="#64748b" font-size="4.5">частичное прекращение</text>
          <text x="70" y="72" text-anchor="middle" fill="#4338ca" font-size="4.5" font-weight="600">по позициям свидетельства</text>
          <text x="70" y="84" text-anchor="middle" fill="#334155" font-size="4.5">СИП-898/2025 · BARTON'S</text>
        </g>
        <!-- доказательства использования -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(178, 292)">
          <rect width="108" height="82" rx="8" fill="#fff" stroke="#059669" stroke-width="1"/>
          <text x="54" y="14" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="800">ДОКАЗАТЕЛЬСТВА</text>
          <text x="54" y="26" text-anchor="middle" fill="#64748b" font-size="4.5">бремя на правообладателе</text>
          <rect x="10" y="34" width="88" height="5" rx="1" fill="#d1fae5"/>
          <rect x="10" y="44" width="72" height="5" rx="1" fill="#a7f3d0"/>
          <rect x="10" y="54" width="80" height="5" rx="1" fill="#6ee7b7"/>
          <text x="54" y="70" text-anchor="middle" fill="#334155" font-size="4.5">УПД · каталоги · договоры</text>
          <text x="54" y="78" text-anchor="middle" fill="#64748b" font-size="4">реальное vs символическое</text>
        </g>
        <!-- заинтересованность истца -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(300, 286)">
          <rect width="96" height="88" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1"/>
          <text x="48" y="16" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">ИСТЕЦ</text>
          <text x="48" y="28" text-anchor="middle" fill="#64748b" font-size="4.5">заинтересованность</text>
          <circle cx="48" cy="50" r="14" fill="#f5f3ff" stroke="#a78bfa" stroke-width="1"/>
          <text x="48" y="54" text-anchor="middle" fill="#5b21b6" font-size="6" font-weight="800">ИП</text>
          <text x="48" y="72" text-anchor="middle" fill="#334155" font-size="4.5">заявка + деятельность</text>
          <text x="48" y="82" text-anchor="middle" fill="#64748b" font-size="4">СП-23/20 · реальное намерение</text>
        </g>
        <!-- решение СИП-75 -->
        <g filter="url(#hero-siptz-shadow)" transform="translate(406, 286)">
          <rect width="70" height="88" rx="8" fill="#fff" stroke="#7c3aed" stroke-width="1"/>
          <rect x="0" y="0" width="70" height="16" rx="8" fill="#f5f3ff"/>
          <text x="35" y="11" text-anchor="middle" fill="#5b21b6" font-size="4.5" font-weight="800">СИП-75</text>
          <text x="35" y="30" text-anchor="middle" fill="#334155" font-size="4.5" font-weight="700">30.03.26</text>
          <text x="35" y="44" text-anchor="middle" fill="#64748b" font-size="4">частичное</text>
          <text x="35" y="56" text-anchor="middle" fill="#64748b" font-size="4">удовлетворение</text>
          <rect x="8" y="64" width="54" height="14" rx="4" fill="#ede9fe"/>
          <text x="35" y="74" text-anchor="middle" fill="#4338ca" font-size="4" font-weight="600">практика 2026</text>
        </g>
        <!-- защита бренда -->
        <g transform="translate(400, 168)">
          <path d="M0 28 L24 8 L48 28 L48 52 Q24 68 0 52 Z" fill="#ecfdf5" stroke="#059669" stroke-width="1.2"/>
          <text x="24" y="36" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="800">BRAND</text>
          <text x="24" y="48" text-anchor="middle" fill="#065f46" font-size="4.5">защита</text>
        </g>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">СИП · ст. 1486 · частичное прекращение · заинтересованность · доказательства использования</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: sip-prekrashchenie-tz-neispolzovanie-zainteresovannost-2026
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>` и `<script>`.
