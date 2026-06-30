=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Образовательная экосистема под судебным штампом» — сеть учебников, пособий и EdTech-узлов вокруг аббревиатуры «ВПР»; монопольная лицензия снимается президиумом СИП |
| **Центральная метафора** | Комбинированный знак «ВПР» (буквы на красных квадратах) в центре образовательного контура; весы правосудия СИП сверху; штамп «АННУЛИРОВАНО» перечёркивает свидетельство № 652761 |
| **Пространство** | Светлый тёплый градиент «утро в библиотеке / кабинет оценки качества»; SVG — стопка книг, рабочие тетради, узлы ФИОКО и издательства, лицензионные стрелки, разорванная монополия |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#0f172a` текст, `#4338ca` СИП/ИС, `#dc2626` квадраты ТЗ «ВПР», `#991b1b` штамп аннулирования, `#059669` образовательная экосистема, `#b45309` госпроект/ФГОС, `#475569` подзаголовок, `#fefefe`–`#f0fdf4` фон |
| **Аудитория** | Издатели, EdTech, репетиторы; получившие претензию или иск по «ВПР»; юристы по оспариванию госаббревиатур |

## Чеклист отличий от других hero

- [x] **Не СИП-565**: нет эстоппеля бывшего участника — фабула **монополия правообладателя на госаббревиатуру**
- [x] **Не sip-prekrashchenie**: не неиспользование/ст. 1486 — угол **злоупотребление правом + ст. 10, 1483**
- [x] **Не poizon/sinergetik**: не компенсация 1515 — **прекращение охраны регистрации**
- [x] **Не обзор ВС № 8**: не спецмеры/арбитраж — инстанция **Президиум СИП, дело СИП-844/2025**
- [x] Уникальная сцена: образовательный контур + буквы ВПР на красных квадратах + весы + штамп «АННУЛИРОВАНО»
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA в hero **не вставлять** (по замечанию Артура)

```html
<section id="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie" class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie" aria-label="СИП 2026: Президиум аннулировал товарный знак «ВПР» издательства «Просвещение»">
  <style>
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f4faf6 38%, #eef6f2 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 42% 38% at 90% 8%, rgba(67, 56, 202, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 36% 34% at 6% 92%, rgba(5, 150, 105, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__inner {
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
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__badge {
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
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #dc2626;
      flex-shrink: 0;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.38rem, 3vw, 2.1rem);
      line-height: 1.24;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__h1-accent {
      color: #4338ca;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact--sip {
      border-color: #c4b5fd;
      color: #4338ca;
      background: #f5f3ff;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact--edu {
      border-color: #a7f3d0;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__inner">
    <div class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__content">
      <div class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__badge">
        <span class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__badge-mark" aria-hidden="true"></span>
        IP · СИП 2026 · ТЗ «ВПР» · СИП-844/2025
      </div>
      <h1 class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__h1">
        <span class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__h1-accent">СИП 2026: Президиум аннулировал товарный знак «ВПР» издательства «Просвещение»</span>
      </h1>
      <p class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__sub">
        Злоупотребление правом и монополия на аббревиатуру госпроекта — полное прекращение охраны (дело СИП-844/2025)
      </p>
      <ul class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__facts">
        <li class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact--sip">Президиум СИП · 01.06.2026</li>
        <li class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact--warn">ст. 10 + 1483 ГК РФ</li>
        <li class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact">свидетельство № 652761</li>
        <li class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__fact--edu">ФИОКО vs Роспатент</li>
      </ul>
    </div>
    <div class="l24-hero-sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Образовательная экосистема вокруг аббревиатуры ВПР: весы СИП, свидетельство № 652761 и штамп полного аннулирования охраны товарного знака">
        <defs>
          <linearGradient id="hero-vpr-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#ecfdf5"/>
          </linearGradient>
          <linearGradient id="hero-vpr-sip" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#4338ca"/>
            <stop offset="100%" stop-color="#312e81"/>
          </linearGradient>
          <linearGradient id="hero-vpr-book" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#d1fae5"/>
            <stop offset="100%" stop-color="#a7f3d0"/>
          </linearGradient>
          <pattern id="hero-vpr-grid" width="18" height="18" patternUnits="userSpaceOnUse">
            <rect width="18" height="18" fill="#f0fdf4"/>
            <path d="M18 0 L0 0 0 18" fill="none" stroke="#dcfce7" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-vpr-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="4" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.1"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-vpr-bg)" stroke="#cbd5e1" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-vpr-grid)" opacity="0.45"/>
        <!-- фасад СИП -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(158, 8)">
          <rect x="0" y="36" width="184" height="48" rx="4" fill="url(#hero-vpr-sip)"/>
          <polygon points="92,0 184,36 0,36" fill="#4338ca"/>
          <text x="92" y="52" text-anchor="middle" fill="#e0e7ff" font-size="6" font-weight="800" letter-spacing="0.04em">ПРЕЗИДИУМ СИП</text>
          <text x="92" y="64" text-anchor="middle" fill="#c7d2fe" font-size="5">дело СИП-844/2025 · 01.06.2026</text>
          <text x="92" y="76" text-anchor="middle" fill="#a5b4fc" font-size="4.5">полное прекращение охраны</text>
        </g>
        <!-- весы правосудия -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(210, 58)">
          <line x1="40" y1="8" x2="40" y2="28" stroke="#4338ca" stroke-width="2"/>
          <line x1="16" y1="12" x2="64" y2="12" stroke="#4338ca" stroke-width="2.2"/>
          <path d="M16 12 L8 24 L24 24 Z" fill="#eef2ff" stroke="#4338ca" stroke-width="1"/>
          <path d="M64 12 L56 24 L72 24 Z" fill="#eef2ff" stroke="#4338ca" stroke-width="1"/>
          <circle cx="8" cy="26" r="3" fill="#059669" opacity="0.85"/>
          <circle cx="24" cy="26" r="3" fill="#059669" opacity="0.85"/>
          <circle cx="56" cy="26" r="3" fill="#dc2626" opacity="0.85"/>
          <circle cx="72" cy="26" r="3" fill="#dc2626" opacity="0.85"/>
          <text x="16" y="34" text-anchor="middle" fill="#047857" font-size="3.5" font-weight="700">ФИОКО</text>
          <text x="64" y="34" text-anchor="middle" fill="#991b1b" font-size="3.5" font-weight="700">ТЗ</text>
        </g>
        <!-- образовательный контур -->
        <g filter="url(#hero-vpr-shadow)">
          <rect x="36" y="108" width="428" height="188" rx="12" fill="none" stroke="#059669" stroke-width="1.8" stroke-dasharray="8 5"/>
          <text x="250" y="124" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="800">ОБРАЗОВАТЕЛЬНАЯ ЭКОСИСТЕМА · ФГОС</text>
          <!-- узлы экосистемы -->
          <g transform="translate(52, 136)">
            <rect width="72" height="40" rx="6" fill="#fff" stroke="#6ee7b7" stroke-width="1"/>
            <text x="36" y="16" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="700">УЧЕБНИКИ</text>
            <text x="36" y="28" text-anchor="middle" fill="#64748b" font-size="4">класс 16 МКТУ</text>
            <text x="36" y="36" text-anchor="middle" fill="#64748b" font-size="3.5">книги · пособия</text>
          </g>
          <g transform="translate(140, 136)">
            <rect width="72" height="40" rx="6" fill="#fff" stroke="#6ee7b7" stroke-width="1"/>
            <text x="36" y="16" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="700">EdTech</text>
            <text x="36" y="28" text-anchor="middle" fill="#64748b" font-size="4">класс 09 · 41</text>
            <text x="36" y="36" text-anchor="middle" fill="#64748b" font-size="3.5">ПО · экзамены</text>
          </g>
          <g transform="translate(288, 136)">
            <rect width="72" height="40" rx="6" fill="#fff" stroke="#6ee7b7" stroke-width="1"/>
            <text x="36" y="16" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="700">РОСОБРНАДЗОР</text>
            <text x="36" y="28" text-anchor="middle" fill="#64748b" font-size="4">ФИОКО</text>
            <text x="36" y="36" text-anchor="middle" fill="#64748b" font-size="3.5">госоценка</text>
          </g>
          <g transform="translate(376, 136)">
            <rect width="72" height="40" rx="6" fill="#fff" stroke="#fca5a5" stroke-width="1"/>
            <text x="36" y="16" text-anchor="middle" fill="#991b1b" font-size="4.5" font-weight="700">ЛИЦЕНЗИИ</text>
            <text x="36" y="28" text-anchor="middle" fill="#64748b" font-size="4">«Просвещение»</text>
            <text x="36" y="36" text-anchor="middle" fill="#991b1b" font-size="3.5">монополия</text>
          </g>
          <!-- связи -->
          <path d="M88 156 L140 156 M212 156 L288 156 M360 156 L376 156" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 2"/>
          <path d="M412 176 L412 200 L250 200 L88 200 L88 176" fill="none" stroke="#6ee7b7" stroke-width="1.2"/>
        </g>
        <!-- стопка книг слева -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(44, 196)">
          <rect x="0" y="24" width="52" height="10" rx="2" fill="#047857"/>
          <rect x="2" y="14" width="48" height="10" rx="2" fill="#059669"/>
          <rect x="4" y="4" width="44" height="10" rx="2" fill="url(#hero-vpr-book)"/>
          <text x="26" y="12" text-anchor="middle" fill="#065f46" font-size="4" font-weight="700">ВПР</text>
          <text x="26" y="42" text-anchor="middle" fill="#64748b" font-size="3.5">до 2018</text>
        </g>
        <!-- тетрадь справа -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(404, 200)">
          <rect width="44" height="56" rx="3" fill="#fff" stroke="#cbd5e1" stroke-width="1"/>
          <line x1="10" y1="14" x2="34" y2="14" stroke="#e2e8f0" stroke-width="1"/>
          <line x1="10" y1="22" x2="34" y2="22" stroke="#e2e8f0" stroke-width="1"/>
          <line x1="10" y1="30" x2="28" y2="30" stroke="#e2e8f0" stroke-width="1"/>
          <text x="22" y="46" text-anchor="middle" fill="#b45309" font-size="4" font-weight="700">ФГОС</text>
        </g>
        <!-- центральный знак ВПР на красных квадратах -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(168, 168)">
          <rect width="164" height="88" rx="8" fill="#fff" stroke="#cbd5e1" stroke-width="1.2"/>
          <text x="82" y="14" text-anchor="middle" fill="#64748b" font-size="4.5" font-weight="700">свидетельство № 652761</text>
          <g transform="translate(18, 22)">
            <rect x="0" y="0" width="36" height="36" rx="4" fill="#dc2626"/>
            <text x="18" y="26" text-anchor="middle" fill="#fff" font-size="16" font-weight="900">В</text>
            <rect x="44" y="0" width="36" height="36" rx="4" fill="#dc2626"/>
            <text x="62" y="26" text-anchor="middle" fill="#fff" font-size="16" font-weight="900">П</text>
            <rect x="88" y="0" width="36" height="36" rx="4" fill="#dc2626"/>
            <text x="106" y="26" text-anchor="middle" fill="#fff" font-size="16" font-weight="900">Р</text>
          </g>
          <text x="82" y="78" text-anchor="middle" fill="#64748b" font-size="4">всероссийские проверочные работы</text>
          <!-- штамп аннулирования -->
          <g transform="translate(22, 30)">
            <ellipse cx="60" cy="22" rx="58" ry="18" fill="none" stroke="#dc2626" stroke-width="2.5" transform="rotate(-12 60 22)"/>
            <text x="60" y="18" text-anchor="middle" fill="#991b1b" font-size="7" font-weight="900" transform="rotate(-12 60 22)">АННУЛИРОВАНО</text>
            <text x="60" y="30" text-anchor="middle" fill="#991b1b" font-size="4.5" font-weight="700" transform="rotate(-12 60 22)">01.06.2026</text>
          </g>
        </g>
        <!-- частичное vs полное -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(48, 308)">
          <text x="100" y="0" text-anchor="middle" fill="#4338ca" font-size="5" font-weight="800">ЛОВУШКА ЧАСТИЧНОГО ИСКЛЮЧЕНИЯ</text>
          <rect x="0" y="10" width="96" height="52" rx="6" fill="#fff" stroke="#fcd34d" stroke-width="1"/>
          <text x="48" y="26" text-anchor="middle" fill="#92400e" font-size="4.5" font-weight="700">Роспатент</text>
          <text x="48" y="38" text-anchor="middle" fill="#64748b" font-size="4">16.06.2025 · частично</text>
          <text x="48" y="50" text-anchor="middle" fill="#92400e" font-size="3.5">родовые позиции МКТУ</text>
          <path d="M104 36 L132 36" stroke="#4338ca" stroke-width="2" marker-end="url(#hero-vpr-arr)"/>
          <rect x="140" y="10" width="108" height="52" rx="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.2"/>
          <text x="194" y="26" text-anchor="middle" fill="#991b1b" font-size="4.5" font-weight="800">Президиум СИП</text>
          <text x="194" y="38" text-anchor="middle" fill="#334155" font-size="4">полное прекращение</text>
          <text x="194" y="50" text-anchor="middle" fill="#991b1b" font-size="3.5">ст. 10 · 1483 ГК</text>
        </g>
        <!-- блок злоупотребления -->
        <g filter="url(#hero-vpr-shadow)" transform="translate(280, 308)">
          <rect width="192" height="72" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1"/>
          <text x="96" y="18" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">ЗЛОУПОТРЕБЛЕНИЕ ПРАВОМ</text>
          <text x="96" y="32" text-anchor="middle" fill="#334155" font-size="4.5">госаббревиатура ≠ бренд</text>
          <text x="96" y="44" text-anchor="middle" fill="#64748b" font-size="4">лицензирование описательного</text>
          <text x="96" y="56" text-anchor="middle" fill="#64748b" font-size="4">обозначения · 100 000 ₽ госпошлины</text>
          <text x="96" y="66" text-anchor="middle" fill="#059669" font-size="3.5" font-weight="600">без компенсации по ст. 1515</text>
        </g>
        <defs>
          <marker id="hero-vpr-arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0 0 L6 3 L0 6 Z" fill="#4338ca"/>
          </marker>
        </defs>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">СИП-844/2025 · ВПР · образовательная экосистема · штамп аннулирования · весы правосудия</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: sip-vpr-prosveshchenie-annulirovanie-tovarnyj-znak-zloupotreblenie
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>` и CTA в hero.
