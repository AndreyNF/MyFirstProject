=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Контурный шлюз спецмер» — периметр контроля по Указам № 81, 95, 322; сделки и платежи проходят через КПП с проверкой счетов «С»/«О»; обходные маршруты (дробление, цессия) получают штамп «НИЧТОЖНО» |
| **Центральная метафора** | Развилка юрисдикций: иностранный суд и арбитражная оговорка блокируются (ст. 248.1–248.2 АПК), стрелка ведёт в российский арбитражный зал под фасадом обзора ВС № 8/2026 |
| **Пространство** | Светлый холодный градиент «утро в арбитражном корпусе»; SVG — периметр-забор, три шлюза указов, цепочка дроблёных платежей, иск ФНС, контракт с иностранным кредитором; не весы, не банкротство, не налог на имущество |
| **Движение** | Только CSS: сканер на периметре, пульс штампа «НИЧТОЖНО», мерцание блокировки иностранного суда, поток стрелки к арбитражу; `prefers-reduced-motion` отключает |
| **Палитра** | `#0f172a` текст, `#1e3a8a` ВС/арбитраж, `#b45309` спецмеры/указы, `#991b1b` ничтожность, `#64748b` иностранная юрисдикция, `#475569` подзаголовок, `#a31830` CTA, `#f8fafc`–`#eef2f8` фон |
| **Аудитория** | Компании с расчётами с иностранными кредиторами, цессией, РИД; ответчики по искам ФНС/прокуратуры; юристы по ст. 248.1 АПК и оспариванию сделок |

## Чеклист отличий от других hero

- [x] **Не обзор ВС № 4 (налог на имущество)**: нет весов ФНС vs ГЭС/ОС — фокус **спецмеры, ничтожность, Указы 81/95/322**
- [x] **Не обзор ВС № 5 (субсидиарка)**: нет цепочки кредиторов и банкротного конвейера — угол **платежи, цессия, подсудность**
- [x] **Не КС / ст. 159**: нет лестницы квалификации — инстанция **Президиум ВС, постановление № 11А/2026**
- [x] **Уникальная сцена**: периметр-шлюз спецконтроля + дробление платежей + развилка «иностранный суд ↔ арбитраж РФ»
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA: «Консультация по арбитражному спору» → `https://advokat-vsem.ru/`

```html
<section id="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok" class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok" aria-label="ВС РФ обзор № 8/2026: спецмеры в арбитраже — ничтожность сделок в обход Указов № 81, 95, 322">
  <style>
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f4f7fb 36%, #eef2f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 44% 40% at 92% 6%, rgba(30, 58, 138, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 38% 36% at 4% 94%, rgba(180, 83, 9, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__inner {
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
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__badge {
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
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #b45309;
      flex-shrink: 0;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.38rem, 3vw, 2.1rem);
      line-height: 1.24;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__h1-accent {
      color: #1e3a8a;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact--spec {
      border-color: #fcd34d;
      color: #92400e;
      background: #fffbeb;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact--arb {
      border-color: #93c5fd;
      color: #1e40af;
      background: #eff6ff;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__cta {
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
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__cta:hover {
      background: #8b1528;
    }
    .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__scan {
        animation: hero-sm8-scan 4.4s linear infinite;
      }
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__void {
        animation: hero-sm8-void 3.2s ease-in-out infinite;
      }
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__foreign-block {
        animation: hero-sm8-block 3.6s ease-in-out infinite;
      }
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__arb-flow {
        animation: hero-sm8-flow 2.8s ease-in-out infinite;
      }
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__split {
        animation: hero-sm8-split 4s ease-in-out infinite;
      }
    }
    @keyframes hero-sm8-scan {
      0% { transform: translateX(-180px); opacity: 0; }
      15% { opacity: 0.55; }
      85% { opacity: 0.55; }
      100% { transform: translateX(180px); opacity: 0; }
    }
    @keyframes hero-sm8-void {
      0%, 100% { opacity: 0.72; transform: scale(1); }
      50% { opacity: 1; transform: scale(1.04); }
    }
    @keyframes hero-sm8-block {
      0%, 100% { opacity: 0.45; }
      50% { opacity: 0.85; }
    }
    @keyframes hero-sm8-flow {
      0%, 100% { transform: translateX(0); opacity: 0.8; }
      50% { transform: translateX(8px); opacity: 1; }
    }
    @keyframes hero-sm8-split {
      0%, 100% { opacity: 0.6; }
      50% { opacity: 1; }
    }
    @media (prefers-reduced-motion: reduce) {
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__scan,
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__void,
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__foreign-block,
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__arb-flow,
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__split {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__inner">
    <div class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__content">
      <div class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__badge">
        <span class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__badge-mark" aria-hidden="true"></span>
        ARB · обзор ВС № 8/2026 · спецмеры · № 11А/2026
      </div>
      <h1 class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__h1">
        <span class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__h1-accent">ВС РФ обзор № 8/2026: спецмеры в арбитраже — ничтожность сделок в обход Указов № 81, 95, 322</span> (постановление № 11А/2026)
      </h1>
      <p class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__sub">
        22 позиции ВС: какие сделки и платежи суды признают ничтожными, когда ФНС оспаривает расчёты с иностранными кредиторами
      </p>
      <ul class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__facts">
        <li class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact--spec">Указы № 81 / 95 / 322</li>
        <li class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact--warn">ничтожность · ст. 10, 168 ГК</li>
        <li class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact">счёт «С» / «О» · &gt;10 млн ₽</li>
        <li class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__fact--arb">ст. 248.1 АПК · 22 позиции</li>
      </ul>
      <a class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по арбитражному спору</a>
    </div>
    <div class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Контурный шлюз спецмер: платежи и сделки в обход Указов 81, 95, 322 получают штамп ничтожности; спор переходит в российский арбитраж по ст. 248.1 АПК — обзор ВС № 8/2026">
        <defs>
          <linearGradient id="hero-sm8-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e8eef5"/>
          </linearGradient>
          <linearGradient id="hero-sm8-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e40af"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hero-sm8-gate" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#fde68a"/>
            <stop offset="100%" stop-color="#f59e0b"/>
          </linearGradient>
          <linearGradient id="hero-sm8-scan" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#38bdf8" stop-opacity="0"/>
            <stop offset="50%" stop-color="#38bdf8" stop-opacity="0.45"/>
            <stop offset="100%" stop-color="#38bdf8" stop-opacity="0"/>
          </linearGradient>
          <pattern id="hero-sm8-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f1f5f9"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-sm8-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-sm8-bg)" stroke="#cbd5e1" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-sm8-grid)" opacity="0.4"/>
        <!-- фасад ВС + обзор -->
        <g filter="url(#hero-sm8-shadow)" transform="translate(138, 8)">
          <rect x="0" y="38" width="224" height="54" rx="4" fill="url(#hero-sm8-vs)"/>
          <polygon points="112,0 224,38 0,38" fill="#1e40af"/>
          <text x="112" y="56" text-anchor="middle" fill="#e2e8f0" font-size="6" font-weight="800" letter-spacing="0.04em">ОБЗОР ВС № 8/2026</text>
          <text x="112" y="70" text-anchor="middle" fill="#93c5fd" font-size="5.5" font-weight="600">спецмеры · ничтожность сделок</text>
          <text x="112" y="84" text-anchor="middle" fill="#bfdbfe" font-size="5">17.06.2026 · постановление № 11А/2026</text>
        </g>
        <!-- периметр спецконтроля -->
        <g filter="url(#hero-sm8-shadow)">
          <rect x="36" y="108" width="428" height="188" rx="10" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="10 6"/>
          <text x="250" y="124" text-anchor="middle" fill="#92400e" font-size="5.5" font-weight="800">КОНТУР СПЕЦИАЛЬНЫХ ЭКОНОМИЧЕСКИХ МЕР</text>
          <rect class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__scan" x="36" y="128" width="60" height="168" fill="url(#hero-sm8-scan)" opacity="0.5"/>
          <!-- три шлюза указов -->
          <g transform="translate(72, 136)">
            <rect width="96" height="44" rx="6" fill="url(#hero-sm8-gate)" stroke="#d97706" stroke-width="1"/>
            <text x="48" y="18" text-anchor="middle" fill="#78350f" font-size="6" font-weight="800">УКАЗ № 81</text>
            <text x="48" y="30" text-anchor="middle" fill="#92400e" font-size="4.5">контроль · недвижимость</text>
            <text x="48" y="40" text-anchor="middle" fill="#78350f" font-size="4">Правкомиссия</text>
          </g>
          <g transform="translate(202, 136)">
            <rect width="96" height="44" rx="6" fill="url(#hero-sm8-gate)" stroke="#d97706" stroke-width="1"/>
            <text x="48" y="18" text-anchor="middle" fill="#78350f" font-size="6" font-weight="800">УКАЗ № 95</text>
            <text x="48" y="30" text-anchor="middle" fill="#92400e" font-size="4.5">платежи · счёт «С»</text>
            <text x="48" y="40" text-anchor="middle" fill="#78350f" font-size="4">&gt;10 млн ₽/мес.</text>
          </g>
          <g transform="translate(332, 136)">
            <rect width="96" height="44" rx="6" fill="url(#hero-sm8-gate)" stroke="#d97706" stroke-width="1"/>
            <text x="48" y="18" text-anchor="middle" fill="#78350f" font-size="6" font-weight="800">УКАЗ № 322</text>
            <text x="48" y="30" text-anchor="middle" fill="#92400e" font-size="4.5">РИД · счёт «О»</text>
            <text x="48" y="40" text-anchor="middle" fill="#78350f" font-size="4">цессия · лицензии</text>
          </g>
        </g>
        <!-- дробление платежей (обход) -->
        <g class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__split" filter="url(#hero-sm8-shadow)" transform="translate(48, 192)">
          <text x="70" y="0" text-anchor="middle" fill="#64748b" font-size="4.5" font-weight="700">дробление &lt;10 млн</text>
          <rect x="0" y="6" width="44" height="28" rx="4" fill="#fff" stroke="#94a3b8" stroke-width="0.8"/>
          <text x="22" y="22" text-anchor="middle" fill="#334155" font-size="4">9,8 млн</text>
          <rect x="48" y="6" width="44" height="28" rx="4" fill="#fff" stroke="#94a3b8" stroke-width="0.8"/>
          <text x="70" y="22" text-anchor="middle" fill="#334155" font-size="4">9,5 млн</text>
          <path d="M22 38 L22 52 M70 38 L70 52 M22 52 L70 52 L90 68" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 2"/>
          <text x="100" y="72" fill="#64748b" font-size="4">цепочка &gt;6 млрд ₽</text>
        </g>
        <!-- платёж без счёта С — ничтожен -->
        <g filter="url(#hero-sm8-shadow)" transform="translate(168, 188)">
          <rect width="88" height="56" rx="6" fill="#fff" stroke="#f87171" stroke-width="1.2"/>
          <text x="44" y="14" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="800">ПЛАТЁЖ 15.11.2022</text>
          <text x="44" y="26" text-anchor="middle" fill="#334155" font-size="4.5">&gt;10 млн ₽ · не счёт «С»</text>
          <text x="44" y="38" text-anchor="middle" fill="#64748b" font-size="4">иностранный кредитор</text>
          <g class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__void">
            <ellipse cx="44" cy="48" rx="34" ry="10" fill="none" stroke="#dc2626" stroke-width="2"/>
            <text x="44" y="51" text-anchor="middle" fill="#991b1b" font-size="5.5" font-weight="900">НИЧТОЖНО</text>
          </g>
        </g>
        <!-- иск ФНС -->
        <g filter="url(#hero-sm8-shadow)" transform="translate(272, 188)">
          <rect width="72" height="56" rx="6" fill="#fef2f2" stroke="#a31830" stroke-width="1"/>
          <text x="36" y="16" text-anchor="middle" fill="#a31830" font-size="5.5" font-weight="800">ИСК ФНС</text>
          <text x="36" y="30" text-anchor="middle" fill="#334155" font-size="4.5">оспаривание</text>
          <text x="36" y="42" text-anchor="middle" fill="#64748b" font-size="4">расчётов · п. 3</text>
          <text x="36" y="52" text-anchor="middle" fill="#991b1b" font-size="4" font-weight="700">апелляция → да</text>
        </g>
        <!-- цессия — ничтожна -->
        <g filter="url(#hero-sm8-shadow)" transform="translate(356, 188)">
          <rect width="96" height="56" rx="6" fill="#fff" stroke="#cbd5e1" stroke-width="1"/>
          <text x="48" y="14" text-anchor="middle" fill="#334155" font-size="5" font-weight="800">УСТУПКА</text>
          <text x="48" y="26" text-anchor="middle" fill="#64748b" font-size="4.5">займ · лицензия · ТЗ</text>
          <text x="48" y="38" text-anchor="middle" fill="#64748b" font-size="4">обход «С» / «О»</text>
          <text x="48" y="50" text-anchor="middle" fill="#991b1b" font-size="4.5" font-weight="700">п. 5–7 обзора</text>
        </g>
        <!-- развилка юрисдикций -->
        <g filter="url(#hero-sm8-shadow)" transform="translate(28, 308)">
          <text x="100" y="0" text-anchor="middle" fill="#1e3a8a" font-size="5.5" font-weight="800">РАЗВИЛКА ПОДСУДНОСТИ</text>
          <!-- иностранный суд — блок -->
          <g class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__foreign-block">
            <rect x="0" y="10" width="108" height="72" rx="8" fill="#f1f5f9" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4"/>
            <rect x="0" y="10" width="108" height="16" rx="8" fill="#e2e8f0"/>
            <text x="54" y="22" text-anchor="middle" fill="#64748b" font-size="5" font-weight="700">ИНОСТР. СУД</text>
            <text x="54" y="40" text-anchor="middle" fill="#94a3b8" font-size="4.5">арбитражная оговорка</text>
            <text x="54" y="52" text-anchor="middle" fill="#94a3b8" font-size="4.5">запрет въезда · виза</text>
            <line x1="18" y1="62" x2="90" y2="30" stroke="#dc2626" stroke-width="2.5"/>
            <line x1="18" y1="30" x2="90" y2="62" stroke="#dc2626" stroke-width="2.5"/>
          </g>
          <!-- стрелка к арбитражу РФ -->
          <g class="l24-hero-vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok__arb-flow">
            <path d="M120 46 L168 46" stroke="#1e40af" stroke-width="2.5" marker-end="url(#hero-sm8-arrow)"/>
            <text x="144" y="40" text-anchor="middle" fill="#1e40af" font-size="4.5" font-weight="700">ст. 248.1</text>
          </g>
          <!-- российский арбитраж -->
          <rect x="176" y="10" width="124" height="72" rx="8" fill="#eff6ff" stroke="#1e40af" stroke-width="1.4"/>
          <rect x="176" y="10" width="124" height="16" rx="8" fill="#1e40af"/>
          <text x="238" y="22" text-anchor="middle" fill="#eff6ff" font-size="5" font-weight="800">АРБИТРАЖ РФ</text>
          <text x="238" y="40" text-anchor="middle" fill="#334155" font-size="4.5">санкции · Euroclear</text>
          <text x="238" y="52" text-anchor="middle" fill="#334155" font-size="4.5">п. 15–17 обзора</text>
          <text x="238" y="66" text-anchor="middle" fill="#1e40af" font-size="4.5" font-weight="700">компетенция РФ</text>
        </g>
        <!-- счётчики позиций -->
        <g filter="url(#hero-sm8-shadow)" transform="translate(340, 308)">
          <rect width="132" height="82" rx="8" fill="#fff" stroke="#1e3a8a" stroke-width="1"/>
          <text x="66" y="18" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="800">22 ПОЗИЦИИ</text>
          <rect x="12" y="26" width="108" height="5" rx="2" fill="#e2e8f0"/>
          <rect x="12" y="26" width="108" height="5" rx="2" fill="#3b82f6"/>
          <text x="66" y="44" text-anchor="middle" fill="#334155" font-size="4.5">ничтожность · цессия</text>
          <text x="66" y="56" text-anchor="middle" fill="#334155" font-size="4.5">мировое · ст. 248.2</text>
          <text x="66" y="68" text-anchor="middle" fill="#64748b" font-size="4">ст. 10, 168 ГК · 309–311 АПК</text>
          <text x="66" y="78" text-anchor="middle" fill="#059669" font-size="4" font-weight="600">защита добросовестных · п. 11</text>
        </g>
        <defs>
          <marker id="hero-sm8-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0 0 L6 3 L0 6 Z" fill="#1e40af"/>
          </marker>
        </defs>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">обзор 8/2026 · контур спецмер · ничтожность в обход · арбитраж vs иностранный суд</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: vs-obzor-8-2026-specmery-arbitrazh-nichtozhnost-sdelok
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>` и `<script>`.
