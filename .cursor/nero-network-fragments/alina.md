=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-maloznachitelnost-krazha-st-14`

**Размер:** `min-height: 88vh` / `88dvh`; padding `112px 24px 72px`; grid `1.04fr 0.96fr`; mobile visual `max-height: 320px`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Зал весов малозначительности» — кассация ВС № 11-УД26-3-К6: кража в «Магните» 5 674,25 ₽, три инстанции признали вину, ВС прекратил дело по ч. 2 ст. 14 УК |
| **Центральная метафора** | Весы правосудия: тяжёлая чаша «формальный состав ч. 1 ст. 158» vs лёгкая «общественная опасность» — перевес малозначительности; кассационная лестница инстанций с отменой приговора |
| **Пространство** | UG-градиент (#fefefe → #f5f3ff → #f0fdf4); SVG — колоннада ВС, весы, чек кассы самообслуживания, три печати «виновна» перечёркнуты, бейдж реабилитации |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#1e293b` navy; `#4f46e5` UG-indigo; `#059669` прекращение; `#b91c1c` формальное обвинение; `#0f172a` текст; `#475569` подзаголовок |
| **Аудитория** | Обвиняемые по «мелкой» краже, защитники — кассация, малозначительность, возмещение ущерба, реабилитация |

## Чеклист отличий от других hero

- [x] **Не sro-sozidanie**: не ARB/ЭТП/ФАС — **UG: кража, ч. 2 ст. 14 УК, кассация**
- [x] **Не prodazha-kvartiry**: не ст. 159/мошенничество — **ч. 1 ст. 158, малозначительность**
- [x] **Не gumanizaciya-dtp**: не ДТП/ст. 76 — **хищение в гипермаркете, п. 25.4 Пленума № 29**
- [x] Уникальная сцена: **весы состав vs опасность + лестница 3 инстанций → ВС + чек «Магнит» + возмещение + реабилитация**
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Badge **UG · ВС 14.04.2026 · № 11-УД26-3-К6**; chips: 5 674,25 ₽, ч. 2 ст. 14 УК, ч. 1 ст. 158 УК, п. 25.4 Пленума № 29

```html
<section id="l24-hero-vs-maloznachitelnost-krazha-st-14" class="l24-hero-vs-maloznachitelnost-krazha-st-14" aria-label="ВС РФ прекратил дело о краже как малозначительное: кассация № 11-УД26-3-К6, ч. 2 ст. 14 УК и ч. 1 ст. 158 УК">
  <style>
    .l24-hero-vs-maloznachitelnost-krazha-st-14 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(148deg, #fefefe 0%, #f5f3ff 44%, #f0fdf4 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 38% 34% at 94% 8%, rgba(79, 70, 229, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 32% 30% at 4% 92%, rgba(5, 150, 105, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__inner {
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
    .l24-hero-vs-maloznachitelnost-krazha-st-14__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(30, 41, 59, 0.14);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #4f46e5;
      flex-shrink: 0;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.32rem, 2.85vw, 2.08rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__h1-accent {
      color: #312e81;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.45vw, 1.08rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__fact--sum {
      border-color: #c4b5fd;
      color: #4c1d95;
      background: #f5f3ff;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__fact--st14 {
      border-color: #6ee7b7;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__fact--st158 {
      border-color: #fca5a5;
      color: #b91c1c;
      background: #fef2f2;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__fact--plenum {
      border-color: #93c5fd;
      color: #1e3a5f;
      background: #eff6ff;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__cta {
      display: inline-block;
      background: #312e81;
      color: #fff !important;
      padding: 14px 28px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(49, 46, 129, 0.22);
      line-height: 1.35;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__cta:hover {
      background: #1e1b4b;
    }
    .l24-hero-vs-maloznachitelnost-krazha-st-14__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-vs-maloznachitelnost-krazha-st-14 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-maloznachitelnost-krazha-st-14__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-maloznachitelnost-krazha-st-14__visual {
        order: -1;
        max-height: 320px;
        overflow: hidden;
      }
    }
  </style>

  <div class="l24-hero-vs-maloznachitelnost-krazha-st-14__inner">
    <div class="l24-hero-vs-maloznachitelnost-krazha-st-14__content">
      <div class="l24-hero-vs-maloznachitelnost-krazha-st-14__badge">
        <span class="l24-hero-vs-maloznachitelnost-krazha-st-14__badge-mark" aria-hidden="true"></span>
        UG · ВС 14.04.2026 · № 11-УД26-3-К6
      </div>
      <h1 class="l24-hero-vs-maloznachitelnost-krazha-st-14__h1">
        <span class="l24-hero-vs-maloznachitelnost-krazha-st-14__h1-accent">ВС РФ прекратил дело о краже как малозначительное: ч. 2 ст. 14 УК и защита в кассации</span>
      </h1>
      <p class="l24-hero-vs-maloznachitelnost-krazha-st-14__sub">
        Кассация отменила приговор по ч. 1 ст. 158 УК — когда формальный состав не даёт осуждения
      </p>
      <ul class="l24-hero-vs-maloznachitelnost-krazha-st-14__facts">
        <li class="l24-hero-vs-maloznachitelnost-krazha-st-14__fact l24-hero-vs-maloznachitelnost-krazha-st-14__fact--sum">5 674,25 ₽</li>
        <li class="l24-hero-vs-maloznachitelnost-krazha-st-14__fact l24-hero-vs-maloznachitelnost-krazha-st-14__fact--st14">ч. 2 ст. 14 УК</li>
        <li class="l24-hero-vs-maloznachitelnost-krazha-st-14__fact l24-hero-vs-maloznachitelnost-krazha-st-14__fact--st158">ч. 1 ст. 158 УК</li>
        <li class="l24-hero-vs-maloznachitelnost-krazha-st-14__fact l24-hero-vs-maloznachitelnost-krazha-st-14__fact--plenum">п. 25.4 Пленума № 29</li>
      </ul>
      <a class="l24-hero-vs-maloznachitelnost-krazha-st-14__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по уголовному делу о краже</a>
    </div>

    <div class="l24-hero-vs-maloznachitelnost-krazha-st-14__visual" aria-hidden="true">
      <svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:520px" role="img" aria-label="Кассация ВС: весы правосудия — формальный состав ч. 1 ст. 158 УК перевешен малозначительностью по ч. 2 ст. 14 УК; три инстанции отменены, дело прекращено, реабилитация">
        <defs>
          <linearGradient id="hvmz-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fafafa"/>
            <stop offset="50%" stop-color="#f5f3ff"/>
            <stop offset="100%" stop-color="#f0fdf4"/>
          </linearGradient>
          <linearGradient id="hvmz-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#6366f1"/>
            <stop offset="100%" stop-color="#312e81"/>
          </linearGradient>
          <linearGradient id="hvmz-green" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#34d399"/>
            <stop offset="100%" stop-color="#059669"/>
          </linearGradient>
          <linearGradient id="hvmz-red" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f87171"/>
            <stop offset="100%" stop-color="#b91c1c"/>
          </linearGradient>
          <pattern id="hvmz-col" width="24" height="24" patternUnits="userSpaceOnUse">
            <rect width="24" height="24" fill="#f8fafc"/>
            <line x1="12" y1="0" x2="12" y2="24" stroke="#e0e7ff" stroke-width="0.5"/>
          </pattern>
          <filter id="hvmz-sh" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#312e81" flood-opacity="0.12"/>
          </filter>
        </defs>

        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hvmz-bg)" stroke="#c4b5fd" stroke-width="1.2"/>
        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hvmz-col)" opacity="0.3"/>

        <!-- VS cassation pediment -->
        <g filter="url(#hvmz-sh)" transform="translate(158,8)">
          <rect x="0" y="38" width="204" height="48" rx="4" fill="url(#hvmz-vs)"/>
          <polygon points="102,2 204,38 0,38" fill="#4338ca"/>
          <circle cx="102" cy="22" r="10" fill="#1e1b4b" opacity="0.35"/>
          <path d="M97 22 L100 25 L107 18" fill="none" stroke="#a5b4fc" stroke-width="1.5"/>
          <text x="102" y="54" text-anchor="middle" fill="#e0e7ff" font-size="6.5" font-weight="800" letter-spacing="0.04em">ВЕРХОВНЫЙ СУД РФ</text>
          <text x="102" y="66" text-anchor="middle" fill="#a5b4fc" font-size="5.5" font-weight="600">кассация · 14.04.2026</text>
          <text x="102" y="78" text-anchor="middle" fill="#c7d2fe" font-size="5">№ 11-УД26-3-К6 · прекращено</text>
        </g>

        <!-- Cassation ladder: 3 instances crossed, VS on top -->
        <g filter="url(#hvmz-sh)" transform="translate(18,62)">
          <text x="54" y="8" text-anchor="middle" fill="#64748b" font-size="5" font-weight="700">ИНСТАНЦИИ</text>
          <!-- Step 1: мировой -->
          <rect x="4" y="14" width="100" height="28" rx="5" fill="#fff" stroke="#fca5a5" stroke-width="1.2"/>
          <text x="54" y="26" text-anchor="middle" fill="#b91c1c" font-size="5" font-weight="700">мировой судья</text>
          <text x="54" y="36" text-anchor="middle" fill="#94a3b8" font-size="4.5">виновна · ст. 92 УК</text>
          <line x1="12" y1="42" x2="96" y2="20" stroke="#dc2626" stroke-width="1.5"/>
          <!-- Step 2: апелляция -->
          <rect x="4" y="48" width="100" height="28" rx="5" fill="#fff" stroke="#fca5a5" stroke-width="1.2"/>
          <text x="54" y="60" text-anchor="middle" fill="#b91c1c" font-size="5" font-weight="700">апелляция</text>
          <text x="54" y="70" text-anchor="middle" fill="#94a3b8" font-size="4.5">без изменений</text>
          <line x1="12" y1="76" x2="96" y2="54" stroke="#dc2626" stroke-width="1.5"/>
          <!-- Step 3: 6-й КСОЮ -->
          <rect x="4" y="82" width="100" height="28" rx="5" fill="#fff" stroke="#fca5a5" stroke-width="1.2"/>
          <text x="54" y="94" text-anchor="middle" fill="#b91c1c" font-size="5" font-weight="700">6-й КСОЮ</text>
          <text x="54" y="104" text-anchor="middle" fill="#94a3b8" font-size="4.5">без изменений</text>
          <line x1="12" y1="110" x2="96" y2="88" stroke="#dc2626" stroke-width="1.5"/>
          <!-- VS arrow down -->
          <path d="M54 118 L54 132" stroke="#4f46e5" stroke-width="2"/>
          <polygon points="54,138 48,128 60,128" fill="#4f46e5"/>
          <text x="54" y="150" text-anchor="middle" fill="#059669" font-size="5" font-weight="800">ВС → отмена</text>
        </g>

        <!-- Central scales: formal composition vs public danger -->
        <g filter="url(#hvmz-sh)" transform="translate(148,88)">
          <line x1="112" y1="0" x2="112" y2="56" stroke="#312e81" stroke-width="2.5"/>
          <rect x="88" y="54" width="48" height="8" rx="3" fill="#312e81"/>
          <line x1="32" y1="16" x2="192" y2="16" stroke="#312e81" stroke-width="2.2" transform="rotate(-8 112 16)"/>
          <!-- Left pan: heavy formal composition (lower) -->
          <line x1="32" y1="16" x2="32" y2="44" stroke="#b91c1c" stroke-width="1.2" transform="rotate(-8 32 16)"/>
          <path d="M8 44 L32 34 L56 44 L56 58 L8 58 Z" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.4"/>
          <text x="32" y="50" text-anchor="middle" fill="#b91c1c" font-size="4.5" font-weight="800">ст. 158</text>
          <text x="32" y="56" text-anchor="middle" fill="#dc2626" font-size="3.8">состав ✓</text>
          <!-- Right pan: light insignificance (higher) -->
          <line x1="192" y1="16" x2="192" y2="28" stroke="#059669" stroke-width="1.2" transform="rotate(-8 192 16)"/>
          <path d="M168 28 L192 22 L216 28 L216 40 L168 40 Z" fill="#ecfdf5" stroke="#059669" stroke-width="1.4"/>
          <text x="192" y="34" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="800">ст. 14</text>
          <text x="192" y="40" text-anchor="middle" fill="#059669" font-size="3.8">малознач.</text>
          <!-- Feather on right pan -->
          <path d="M188 20 Q200 14 208 22 Q196 24 188 20" fill="#6ee7b7" opacity="0.8"/>
          <text x="112" y="76" text-anchor="middle" fill="#312e81" font-size="5.2" font-weight="700">общественная опасность перевесила</text>
        </g>

        <!-- Hypermarket receipt / self-checkout -->
        <g filter="url(#hvmz-sh)" transform="translate(388,62)">
          <rect width="112" height="88" rx="8" fill="#fff" stroke="#94a3b8" stroke-width="1.2"/>
          <rect x="0" y="0" width="112" height="18" rx="8" fill="#64748b"/>
          <text x="56" y="12" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="800">«МАГНИТ»</text>
          <text x="56" y="28" text-anchor="middle" fill="#64748b" font-size="4.5">касса самообслуживания</text>
          <rect x="10" y="34" width="92" height="6" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="44" width="72" height="5" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="52" width="80" height="5" rx="1" fill="#e2e8f0"/>
          <line x1="10" y1="62" x2="102" y2="62" stroke="#cbd5e1" stroke-width="0.8" stroke-dasharray="3 2"/>
          <text x="56" y="72" text-anchor="middle" fill="#4c1d95" font-size="7" font-weight="900">5 674,25 ₽</text>
          <text x="56" y="82" text-anchor="middle" fill="#94a3b8" font-size="4">16 лет · Бугульма</text>
        </g>

        <!-- Reimbursement arrow -->
        <g filter="url(#hvmz-sh)" transform="translate(388,158)">
          <rect width="112" height="36" rx="6" fill="#ecfdf5" stroke="#6ee7b7" stroke-width="1"/>
          <path d="M20 18 L40 18 L36 14 M40 18 L36 22" fill="none" stroke="#059669" stroke-width="1.2"/>
          <circle cx="52" cy="18" r="8" fill="#fff" stroke="#059669" stroke-width="1"/>
          <text x="52" y="21" text-anchor="middle" fill="#059669" font-size="6" font-weight="800">₽</text>
          <text x="78" y="16" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="700">возмещение</text>
          <text x="78" y="26" text-anchor="middle" fill="#64748b" font-size="4">родственниками</text>
        </g>

        <!-- Art 14 UK badge -->
        <g filter="url(#hvmz-sh)" transform="translate(18,178)">
          <rect width="108" height="54" rx="8" fill="url(#hvmz-green)" stroke="#047857" stroke-width="1"/>
          <text x="54" y="16" text-anchor="middle" fill="#d1fae5" font-size="5.5" font-weight="700">Ч. 2 СТ. 14 УК</text>
          <text x="54" y="32" text-anchor="middle" fill="#fff" font-size="8" font-weight="900">малозначи-</text>
          <text x="54" y="44" text-anchor="middle" fill="#fff" font-size="8" font-weight="900">тельность</text>
        </g>

        <!-- Rehabilitation stamp -->
        <g filter="url(#hvmz-sh)" transform="translate(388,202)">
          <circle cx="56" cy="36" r="34" fill="none" stroke="#059669" stroke-width="2" stroke-dasharray="4 3"/>
          <circle cx="56" cy="36" r="28" fill="#ecfdf5" stroke="#34d399" stroke-width="1.2"/>
          <path d="M44 36 L52 44 L70 26" fill="none" stroke="#059669" stroke-width="2.5"/>
          <text x="56" y="58" text-anchor="middle" fill="#047857" font-size="5" font-weight="800">реабилитация</text>
          <text x="56" y="68" text-anchor="middle" fill="#64748b" font-size="4.5">ст. 133 УПК</text>
        </g>

        <!-- Cassation document roll -->
        <g filter="url(#hvmz-sh)" transform="translate(148,178)">
          <rect width="224" height="72" rx="8" fill="#fff" stroke="#4f46e5" stroke-width="1.2"/>
          <rect x="0" y="0" width="224" height="16" rx="8" fill="#eef2ff"/>
          <text x="112" y="11" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">КАССАЦИОННОЕ ОПРЕДЕЛЕНИЕ</text>
          <text x="14" y="30" fill="#334155" font-size="4.8">формальный состав ≠ преступление</text>
          <text x="14" y="42" fill="#64748b" font-size="4.5">п. 2 ч. 1 ст. 24 УПК · отсутствие состава</text>
          <text x="14" y="54" fill="#64748b" font-size="4.5">п. 25.4 Пленума ВС № 29 · кража</text>
          <rect x="14" y="58" width="196" height="12" rx="3" fill="#f0fdf4"/>
          <text x="112" y="67" text-anchor="middle" fill="#059669" font-size="4.8" font-weight="700">не ст. 92 УК — прекращение дела</text>
        </g>

        <!-- Justice columns -->
        <g opacity="0.45">
          <rect x="30" y="268" width="10" height="72" rx="2" fill="#e0e7ff"/>
          <rect x="480" y="268" width="10" height="72" rx="2" fill="#e0e7ff"/>
        </g>

        <!-- Bottom info cards -->
        <g filter="url(#hvmz-sh)" transform="translate(18,268)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#b91c1c" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#b91c1c" font-size="6" font-weight="800">ФОРМАЛЬНЫЙ СОСТАВ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">ч. 1 ст. 158 УК · кража</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">сумма &gt; 2 500 ₽</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">3 суда: вина признана</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#fef2f2"/>
          <text x="77" y="63" text-anchor="middle" fill="#b91c1c" font-size="5" font-weight="600">≠ осуждение</text>
        </g>
        <g filter="url(#hvmz-sh)" transform="translate(183,268)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#4f46e5" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#4338ca" font-size="6" font-weight="800">КАССАЦИЯ ВС</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">жалоба адвоката</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">отмена всех актов</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">новая оценка опасности</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#eef2ff"/>
          <text x="77" y="63" text-anchor="middle" fill="#4f46e5" font-size="5" font-weight="600">защита в кассации</text>
        </g>
        <g filter="url(#hvmz-sh)" transform="translate(348,268)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#059669" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#047857" font-size="6" font-weight="800">МАЛОЗНАЧИТЕЛЬНОСТЬ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">ч. 2 ст. 14 УК</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">ущерб возмещён</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">нет последствий</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#ecfdf5"/>
          <text x="77" y="63" text-anchor="middle" fill="#059669" font-size="5" font-weight="600">дело прекращено</text>
        </g>

        <!-- Gavel subtle -->
        <g filter="url(#hvmz-sh)" transform="translate(238,348)">
          <rect x="0" y="0" width="44" height="10" rx="3" fill="#312e81"/>
          <rect x="16" y="8" width="12" height="22" rx="2" fill="#4338ca"/>
          <ellipse cx="22" cy="34" rx="20" ry="5" fill="#e0e7ff" opacity="0.6"/>
        </g>

        <text x="260" y="432" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-weight="600">UG · кража · малозначительность · кассация ВС · дайджест № 7/2026</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе

SLUG: vs-maloznachitelnost-krazha-st-14-zashchita-kassaciya-2026
H1_для_hero: ВС РФ прекратил дело о краже как малозначительное: ч. 2 ст. 14 УК и защита в кассации
ПОДЗАГОЛОВОК_HERO: Кассация отменила приговор по ч. 1 ст. 158 УК — когда формальный состав не даёт осуждения
ТИП_СТАТЬИ: UG — уголовное право
СЛЕДУЮЩИЙ_ШАГ: Наташа (сборка + публикация)
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>`.
