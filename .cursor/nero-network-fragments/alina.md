=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-sro-sozidanie-fas-35-mln`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Арена выбора площадки» — Президиум ВС 01.07.2026: штраф 3,5 млн СРО «Созидание» за навязывание аккредитованных ЭТП; антимонопольный спор ФАС vs СРО в контуре банкротных торгов |
| **Центральная метафора** | Весы над рядом электронных площадок: чаша ФАС перевешивает — СРО не вправе запирать «свои» ЭТП; над сценой — фасад Президиума ВС и маятник инстанций |
| **Пространство** | ARB-градиент (#fefefe → #f0f4fa → #eff6ff); SVG — здание ВС, весы ФАС/СРО, три ЭТП-площадки, гавель торгов, бейдж 3,5 млн ₽ |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#1e3a5f` navy; `#2563eb` ARB-blue; `#0d9488` банкротство; `#ea580c` ФАС; `#0f172a` текст; `#475569` подзаголовок |
| **Аудитория** | Арбитражные управляющие, СРО, операторы ЭТП, кредиторы — выбор площадки для торгов по банкротству без риска дисциплинарки и штрафа ФАС |

## Чеклист отличий от других hero

- [x] **Не prodazha-kvartiry**: не UG/ст. 159 — **ARB: банкротство + антимонопольный спор**
- [x] **Не osparivanie-bankrotstvo**: не ст. 61.2/жильё — **ЭТП, аккредитация СРО, ч. 5 ст. 11 135-ФЗ**
- [x] **Не obzor-8/specmery**: не спецмеры/Указы — **ФАС vs СРО «Созидание», дело А40-232008/2023**
- [x] Уникальная сцена: **ВС + весы ФАС/СРО + три ЭТП-площадки + гавель торгов + штраф 3,5 млн**
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Badge **ARB · Президиум ВС 01.07.2026 · А40-232008/2023**; chips: 3,5 млн ₽, ч. 5 ст. 11 135-ФЗ, ст. 20.3 127-ФЗ, ФАС vs СРО

```html
<section id="l24-hero-vs-sro-sozidanie-fas-35-mln" class="l24-hero-vs-sro-sozidanie-fas-35-mln" aria-label="Президиум ВС 01.07.2026: штраф 3,5 млн СРО Созидание за запрет неаккредитованных ЭТП — ФАС vs СРО, дело А40-232008/2023">
  <style>
    .l24-hero-vs-sro-sozidanie-fas-35-mln {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f0f4fa 42%, #eff6ff 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 40% 36% at 92% 10%, rgba(37, 99, 235, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 34% 32% at 6% 90%, rgba(13, 148, 136, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__inner {
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
    .l24-hero-vs-sro-sozidanie-fas-35-mln__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(30, 58, 95, 0.14);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #2563eb;
      flex-shrink: 0;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.32rem, 2.85vw, 2.08rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__h1-accent {
      color: #1e3a5f;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.45vw, 1.08rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__fact--fine {
      border-color: #fed7aa;
      color: #c2410c;
      background: #fff7ed;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__fact--blue {
      border-color: #93c5fd;
      color: #1e3a5f;
      background: #eff6ff;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__fact--teal {
      border-color: #5eead4;
      color: #0f766e;
      background: #f0fdfa;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__fact--fas {
      border-color: #fdba74;
      color: #ea580c;
      background: #fff7ed;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__cta {
      display: inline-block;
      background: #1e3a5f;
      color: #fff !important;
      padding: 14px 28px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.95rem;
      text-decoration: none;
      box-shadow: 0 4px 14px rgba(30, 58, 95, 0.22);
      line-height: 1.35;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__cta:hover {
      background: #152a47;
    }
    .l24-hero-vs-sro-sozidanie-fas-35-mln__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-vs-sro-sozidanie-fas-35-mln {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-sro-sozidanie-fas-35-mln__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-sro-sozidanie-fas-35-mln__visual {
        order: -1;
        max-height: 320px;
        overflow: hidden;
      }
    }
  </style>

  <div class="l24-hero-vs-sro-sozidanie-fas-35-mln__inner">
    <div class="l24-hero-vs-sro-sozidanie-fas-35-mln__content">
      <div class="l24-hero-vs-sro-sozidanie-fas-35-mln__badge">
        <span class="l24-hero-vs-sro-sozidanie-fas-35-mln__badge-mark" aria-hidden="true"></span>
        ARB · Президиум ВС 01.07.2026 · А40-232008/2023
      </div>
      <h1 class="l24-hero-vs-sro-sozidanie-fas-35-mln__h1">
        <span class="l24-hero-vs-sro-sozidanie-fas-35-mln__h1-accent">Президиум ВС 01.07.2026: штраф 3,5 млн СРО «Созидание» за запрет неаккредитованных площадок</span> — что меняется для арбитражных управляющих
      </h1>
      <p class="l24-hero-vs-sro-sozidanie-fas-35-mln__sub">
        ФАС vs СРО: можно ли проводить торги по банкротству на ЭТП без аккредитации союза — разбор дела № А40-232008/2023 и стратегия защиты
      </p>
      <ul class="l24-hero-vs-sro-sozidanie-fas-35-mln__facts">
        <li class="l24-hero-vs-sro-sozidanie-fas-35-mln__fact l24-hero-vs-sro-sozidanie-fas-35-mln__fact--fine">штраф 3,5 млн ₽</li>
        <li class="l24-hero-vs-sro-sozidanie-fas-35-mln__fact l24-hero-vs-sro-sozidanie-fas-35-mln__fact--fas">ФАС vs СРО «Созидание»</li>
        <li class="l24-hero-vs-sro-sozidanie-fas-35-mln__fact l24-hero-vs-sro-sozidanie-fas-35-mln__fact--blue">ч. 5 ст. 11 135-ФЗ</li>
        <li class="l24-hero-vs-sro-sozidanie-fas-35-mln__fact l24-hero-vs-sro-sozidanie-fas-35-mln__fact--teal">ст. 20.3 127-ФЗ · ЭТП</li>
      </ul>
      <a class="l24-hero-vs-sro-sozidanie-fas-35-mln__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по арбитражному спору</a>
    </div>

    <div class="l24-hero-vs-sro-sozidanie-fas-35-mln__visual" aria-hidden="true">
      <svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:520px" role="img" aria-label="ФАС vs СРО Созидание: Президиум ВС подтвердил штраф 3,5 млн за навязывание аккредитованных ЭТП — весы правосудия, здание суда и электронные торговые площадки по банкротству, дело А40-232008/2023">
        <defs>
          <linearGradient id="hvsfas-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fafafa"/>
            <stop offset="50%" stop-color="#f0f4fa"/>
            <stop offset="100%" stop-color="#eff6ff"/>
          </linearGradient>
          <linearGradient id="hvsfas-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#2563eb"/>
            <stop offset="100%" stop-color="#1e3a5f"/>
          </linearGradient>
          <linearGradient id="hvsfas-fas" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fb923c"/>
            <stop offset="100%" stop-color="#ea580c"/>
          </linearGradient>
          <linearGradient id="hvsfas-sro" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#64748b"/>
            <stop offset="100%" stop-color="#334155"/>
          </linearGradient>
          <linearGradient id="hvsfas-etp" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#5eead4"/>
            <stop offset="100%" stop-color="#0d9488"/>
          </linearGradient>
          <linearGradient id="hvsfas-building" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#e2e8f0"/>
            <stop offset="100%" stop-color="#cbd5e1"/>
          </linearGradient>
          <pattern id="hvsfas-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f8fafc"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#dbeafe" stroke-width="0.4"/>
          </pattern>
          <filter id="hvsfas-sh" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#1e3a5f" flood-opacity="0.12"/>
          </filter>
        </defs>

        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hvsfas-bg)" stroke="#bfdbfe" stroke-width="1.2"/>
        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hvsfas-grid)" opacity="0.35"/>

        <!-- VS Presidium building -->
        <g filter="url(#hvsfas-sh)" transform="translate(148,10)">
          <rect x="0" y="36" width="224" height="52" rx="4" fill="url(#hvsfas-vs)"/>
          <polygon points="112,2 224,36 0,36" fill="#1e40af"/>
          <rect x="88" y="14" width="48" height="18" rx="2" fill="#1e3a5f" opacity="0.5"/>
          <text x="112" y="52" text-anchor="middle" fill="#e0e7ff" font-size="6.5" font-weight="800" letter-spacing="0.04em">ПРЕЗИДИУМ ВС РФ</text>
          <text x="112" y="64" text-anchor="middle" fill="#93c5fd" font-size="5.5" font-weight="600">01.07.2026 · надзор · ФАС победила</text>
          <text x="112" y="76" text-anchor="middle" fill="#bfdbfe" font-size="5">отмена СКЭС 05.11.2025</text>
        </g>

        <!-- Scales of justice: FAS vs SRO -->
        <g filter="url(#hvsfas-sh)" transform="translate(168,78)">
          <line x1="92" y1="4" x2="92" y2="52" stroke="#1e3a5f" stroke-width="2.5"/>
          <rect x="72" y="50" width="40" height="8" rx="3" fill="#1e3a5f"/>
          <line x1="28" y1="18" x2="156" y2="18" stroke="#1e3a5f" stroke-width="2"/>
          <!-- FAS pan (lower/heavier - winning) -->
          <line x1="28" y1="18" x2="28" y2="38" stroke="#ea580c" stroke-width="1.2"/>
          <path d="M8 38 L28 30 L48 38 L48 48 L8 48 Z" fill="#fff7ed" stroke="#ea580c" stroke-width="1.4"/>
          <text x="28" y="44" text-anchor="middle" fill="#ea580c" font-size="5" font-weight="800">ФАС</text>
          <!-- SRO pan (higher/lighter - losing) -->
          <line x1="156" y1="18" x2="156" y2="32" stroke="#64748b" stroke-width="1.2"/>
          <path d="M136 32 L156 26 L176 32 L176 42 L136 42 Z" fill="#f1f5f9" stroke="#64748b" stroke-width="1.4"/>
          <text x="156" y="38" text-anchor="middle" fill="#475569" font-size="4.8" font-weight="800">СРО</text>
          <text x="92" y="68" text-anchor="middle" fill="#1e3a5f" font-size="5" font-weight="700">антимонопольный запрет перевесил</text>
        </g>

        <!-- Fine badge 3.5 mln -->
        <g filter="url(#hvsfas-sh)" transform="translate(18,88)">
          <rect width="108" height="54" rx="8" fill="url(#hvsfas-fas)" stroke="#c2410c" stroke-width="1"/>
          <text x="54" y="16" text-anchor="middle" fill="#ffedd5" font-size="5.5" font-weight="700">ШТРАФ ФАС</text>
          <text x="54" y="34" text-anchor="middle" fill="#fff" font-size="13" font-weight="900">3,5 млн</text>
          <text x="54" y="46" text-anchor="middle" fill="#fed7aa" font-size="5">ч. 5 ст. 14.32 КоАП</text>
        </g>

        <!-- SRO Sozidanie block with lock -->
        <g filter="url(#hvsfas-sh)" transform="translate(394,82)">
          <rect width="108" height="64" rx="8" fill="#fff" stroke="#64748b" stroke-width="1.2"/>
          <text x="54" y="16" text-anchor="middle" fill="#334155" font-size="5.5" font-weight="800">СРО «СОЗИДАНИЕ»</text>
          <text x="54" y="28" text-anchor="middle" fill="#64748b" font-size="4.5">только «свои» ЭТП</text>
          <rect x="38" y="34" width="32" height="22" rx="4" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1"/>
          <rect x="46" y="40" width="16" height="12" rx="2" fill="#64748b"/>
          <circle cx="54" cy="44" r="3" fill="#fbbf24"/>
          <text x="54" y="62" text-anchor="middle" fill="#94a3b8" font-size="4.5" font-weight="600">устав п. 6.2</text>
        </g>

        <!-- Three ETP platforms row -->
        <text x="260" y="158" text-anchor="middle" fill="#0f766e" font-size="5.5" font-weight="800">ЭЛЕКТРОННЫЕ ТОРГОВЫЕ ПЛОЩАДКИ · БАНКРОТСТВО</text>

        <!-- ETP 1: accredited (open) -->
        <g filter="url(#hvsfas-sh)" transform="translate(28,168)">
          <rect width="108" height="72" rx="8" fill="#fff" stroke="#0d9488" stroke-width="1.4"/>
          <rect x="0" y="0" width="108" height="18" rx="8" fill="url(#hvsfas-etp)"/>
          <text x="54" y="12" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="800">МЭТС</text>
          <rect x="12" y="26" width="84" height="10" rx="2" fill="#ccfbf1"/>
          <rect x="12" y="40" width="60" height="8" rx="2" fill="#e2e8f0"/>
          <rect x="12" y="52" width="72" height="8" rx="2" fill="#e2e8f0"/>
          <circle cx="88" cy="30" r="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
          <path d="M84 30 L87 33 L92 27" fill="none" stroke="#16a34a" stroke-width="1.2"/>
          <text x="54" y="68" text-anchor="middle" fill="#0f766e" font-size="4.5" font-weight="600">аккредитована</text>
        </g>

        <!-- ETP 2: Arbitat (not in SRO - central case) -->
        <g filter="url(#hvsfas-sh)" transform="translate(148,162)">
          <rect width="124" height="84" rx="8" fill="#fff" stroke="#2563eb" stroke-width="1.6"/>
          <rect x="0" y="0" width="124" height="20" rx="8" fill="#2563eb"/>
          <text x="62" y="13" text-anchor="middle" fill="#fff" font-size="6" font-weight="800">«АРБИТАТ»</text>
          <text x="62" y="30" text-anchor="middle" fill="#64748b" font-size="4.5">дело Балтком</text>
          <rect x="14" y="36" width="96" height="10" rx="2" fill="#dbeafe"/>
          <rect x="14" y="50" width="70" height="8" rx="2" fill="#e2e8f0"/>
          <rect x="14" y="62" width="80" height="8" rx="2" fill="#e2e8f0"/>
          <rect x="20" y="72" width="84" height="10" rx="3" fill="#eff6ff"/>
          <text x="62" y="80" text-anchor="middle" fill="#2563eb" font-size="4.5" font-weight="700">не в «Созидании»</text>
        </g>

        <!-- ETP 3: open market -->
        <g filter="url(#hvsfas-sh)" transform="translate(284,168)">
          <rect width="108" height="72" rx="8" fill="#fff" stroke="#0d9488" stroke-width="1.4"/>
          <rect x="0" y="0" width="108" height="18" rx="8" fill="url(#hvsfas-etp)"/>
          <text x="54" y="12" text-anchor="middle" fill="#fff" font-size="5" font-weight="800">АЛЬФА-ЛОТ</text>
          <rect x="12" y="26" width="84" height="10" rx="2" fill="#ccfbf1"/>
          <rect x="12" y="40" width="60" height="8" rx="2" fill="#e2e8f0"/>
          <rect x="12" y="52" width="72" height="8" rx="2" fill="#e2e8f0"/>
          <circle cx="88" cy="30" r="8" fill="#dcfce7" stroke="#16a34a" stroke-width="1"/>
          <path d="M84 30 L87 33 L92 27" fill="none" stroke="#16a34a" stroke-width="1.2"/>
          <text x="54" y="68" text-anchor="middle" fill="#0f766e" font-size="4.5" font-weight="600">другая СРО</text>
        </g>

        <!-- ETP 4: CDT -->
        <g filter="url(#hvsfas-sh)" transform="translate(404,168)">
          <rect width="96" height="72" rx="8" fill="#fff" stroke="#0d9488" stroke-width="1.4"/>
          <rect x="0" y="0" width="96" height="18" rx="8" fill="url(#hvsfas-etp)"/>
          <text x="48" y="12" text-anchor="middle" fill="#fff" font-size="5" font-weight="800">ЦДТ</text>
          <rect x="10" y="26" width="76" height="10" rx="2" fill="#ccfbf1"/>
          <rect x="10" y="40" width="52" height="8" rx="2" fill="#e2e8f0"/>
          <rect x="10" y="52" width="64" height="8" rx="2" fill="#e2e8f0"/>
          <text x="48" y="68" text-anchor="middle" fill="#0f766e" font-size="4.5" font-weight="600">свобода выбора</text>
        </g>

        <!-- Arrows: SRO lock vs open choice -->
        <path d="M126 118 Q126 148 82 162" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
        <path d="M394 118 Q394 148 438 162" fill="none" stroke="#ea580c" stroke-width="1.2" stroke-dasharray="4 3"/>
        <text x="260" y="148" text-anchor="middle" fill="#64748b" font-size="4.8" font-weight="600">координация → отказ от «чужих» ЭТП</text>

        <!-- Auction gavel -->
        <g filter="url(#hvsfas-sh)" transform="translate(228,252)">
          <rect x="0" y="0" width="64" height="12" rx="4" fill="#1e3a5f"/>
          <rect x="24" y="10" width="16" height="28" rx="3" fill="#334155"/>
          <ellipse cx="32" cy="42" rx="28" ry="6" fill="#e2e8f0" opacity="0.7"/>
          <text x="32" y="56" text-anchor="middle" fill="#1e3a5f" font-size="5.5" font-weight="800">ТОРГИ</text>
          <text x="32" y="66" text-anchor="middle" fill="#64748b" font-size="4.5">по банкротству</text>
        </g>

        <!-- Arbitration court building (ASGM) -->
        <g filter="url(#hvsfas-sh)" transform="translate(18,248)">
          <rect x="8" y="24" width="88" height="56" rx="4" fill="url(#hvsfas-building)" stroke="#64748b" stroke-width="1"/>
          <polygon points="52,8 96,24 8,24" fill="#94a3b8" stroke="#64748b" stroke-width="0.8"/>
          <rect x="22" y="36" width="14" height="16" rx="1" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.6"/>
          <rect x="42" y="36" width="14" height="16" rx="1" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.6"/>
          <rect x="62" y="36" width="14" height="16" rx="1" fill="#bfdbfe" stroke="#3b82f6" stroke-width="0.6"/>
          <rect x="36" y="58" width="32" height="22" rx="2" fill="#fef3c7" stroke="#d97706" stroke-width="0.8"/>
          <text x="52" y="88" text-anchor="middle" fill="#1e3a5f" font-size="5" font-weight="800">АСГМ</text>
          <text x="52" y="98" text-anchor="middle" fill="#64748b" font-size="4.5">3 инстанции → ФАС</text>
        </g>

        <!-- Case card -->
        <g filter="url(#hvsfas-sh)" transform="translate(308,248)">
          <rect width="130" height="72" rx="8" fill="#fff" stroke="#2563eb" stroke-width="1.2"/>
          <text x="65" y="16" text-anchor="middle" fill="#2563eb" font-size="6" font-weight="800">ДЕЛО №</text>
          <text x="65" y="32" text-anchor="middle" fill="#0f172a" font-size="8" font-weight="900">А40-232008/2023</text>
          <line x1="14" y1="40" x2="116" y2="40" stroke="#e2e8f0" stroke-width="1"/>
          <text x="65" y="52" text-anchor="middle" fill="#64748b" font-size="4.8">Петрова · дисциплинарка 50 000 ₽</text>
          <text x="65" y="62" text-anchor="middle" fill="#64748b" font-size="4.8">жалоба в ФАС → предписание</text>
          <rect x="14" y="66" width="102" height="10" rx="3" fill="#eff6ff"/>
          <text x="65" y="74" text-anchor="middle" fill="#2563eb" font-size="4.5" font-weight="600">ст. 20.3 · любая СРО</text>
        </g>

        <!-- Pendulum instances -->
        <g filter="url(#hvsfas-sh)" transform="translate(448,248)">
          <text x="32" y="8" text-anchor="middle" fill="#64748b" font-size="4.5" font-weight="700">МАЯТНИК</text>
          <line x1="32" y1="12" x2="32" y2="28" stroke="#94a3b8" stroke-width="1"/>
          <circle cx="32" cy="30" r="4" fill="#1e3a5f"/>
          <path d="M32 34 L8 58 L56 58 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="1" opacity="0.9"/>
          <text x="32" y="50" text-anchor="middle" fill="#2563eb" font-size="4">ФАС</text>
          <text x="32" y="68" text-anchor="middle" fill="#64748b" font-size="4">СКЭС→СРО</text>
          <text x="32" y="78" text-anchor="middle" fill="#ea580c" font-size="4" font-weight="700">Президиум→ФАС</text>
        </g>

        <!-- Bottom info row -->
        <g filter="url(#hvsfas-sh)" transform="translate(18,332)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#ea580c" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#ea580c" font-size="6" font-weight="800">ФАС</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">ч. 5 ст. 11 135-ФЗ</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">незаконная координация</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">предписание + 3,5 млн</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#fff7ed"/>
          <text x="77" y="63" text-anchor="middle" fill="#ea580c" font-size="5" font-weight="600">победа 01.07.2026</text>
        </g>
        <g filter="url(#hvsfas-sh)" transform="translate(183,332)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#0d9488" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#0f766e" font-size="6" font-weight="800">АРБИТРАЖНЫЙ УПРАВЛЯЮЩИЙ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">выбор ЭТП · ст. 20.3</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">аккредитация в любой СРО</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">лимит расходов ст. 20.7</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#f0fdfa"/>
          <text x="77" y="63" text-anchor="middle" fill="#0f766e" font-size="5" font-weight="600">свобода площадки</text>
        </g>
        <g filter="url(#hvsfas-sh)" transform="translate(348,332)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#64748b" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#475569" font-size="6" font-weight="800">СРО «СОЗИДАНИЕ»</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">запрет «чужих» ЭТП</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">дисциплинарка до 500 000</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">аккредитация до 500 000 ₽</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#f1f5f9"/>
          <text x="77" y="63" text-anchor="middle" fill="#94a3b8" font-size="5" font-weight="600">устав под предписанием</text>
        </g>

        <text x="260" y="432" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-weight="600">ARB · банкротство · ЭТП · ФАС vs СРО · Президиум ВС 2026</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе

SLUG: vs-sro-sozidanie-fas-35-mln-akreditaciya-ploshchadok-2026
H1_для_hero: Президиум ВС 01.07.2026: штраф 3,5 млн СРО «Созидание» за запрет неаккредитованных площадок — что меняется для арбитражных управляющих
ПОДЗАГОЛОВОК_HERO: ФАС vs СРО: можно ли проводить торги по банкротству на ЭТП без аккредитации союза — разбор дела № А40-232008/2023 и стратегия защиты
ТИП_СТАТЬИ: ARB — арбитраж
СЛЕДУЮЩИЙ_ШАГ: Наташа (сборка + публикация)
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>`.
