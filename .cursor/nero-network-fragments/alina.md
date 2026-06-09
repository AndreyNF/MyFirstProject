=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Промышленная весовая палата арбитража» — спор ФНС о доначислении налога на имущество разворачивается на фоне ГЭС и заводского цеха; весы сравнивают тяжесть налогового требования с доказательствами движимого ОС |
| **Центральная метафора** | Стальные весы арбитража: на одной чаше — акт ФНС «налог на имущество» и доначисление; на другой — инвентарные карточки ГЭС (компрессоры, котлы) и паспорт сооружения; над сценой — обзор ВС № 4/2026 |
| **Пространство** | Светлый градиент «утро над промзоной»; SVG — плотина ГЭС с водосбросом, заводские трубы, гидротурбина, налоговая декларация; не золотые весы суда и не цепочка банкротства |
| **Движение** | Только CSS: покачивание чаш весов, пульс воды у плотины, мерцание строки доначисления; `prefers-reduced-motion` отключает |
| **Палитра** | `#0f172a` текст, `#1e3a8a` ВС/акцент, `#0369a1` вода/ГЭС, `#475569` подзаголовок, `#a31830` ФНС/доначисление, `#f8fafc`–`#eef2f7` фон |
| **Аудитория** | Директора и CFO компаний с производственными активами, энергетикой, складскими комплексами — оспаривание доначислений в арбитраже |

## Чеклист отличий от других hero

- [x] **Не обзор № 5** (`l24-hero-vs-obzor-5-2026-subs`): нет золотых весов кредитор/субсидиарка, цепочки должник→банк, реестра банкротства — фокус **налог на имущество + ГЭС/завод + ФНС**
- [x] **Не Google Earth** (`l24-hero-vs-google-earth-…`): нет GIS/ЕГРН/ст. 159 — инстанция **обзор 4/2026**, гл. **30 НК**
- [x] **Уникальная сцена**: плотина ГЭС + завод + стальные весы арбитража + налоговый акт ФНС vs инвентарные ОС
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA: «Получить консультацию» → `https://advokat-vsem.ru/`

```html
<section id="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns" class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns" aria-label="Обзор ВС № 4/2026: налог на имущество организаций в арбитраже — как оспорить ФНС">
  <style>
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f3f6fa 38%, #eef2f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 44% 40% at 90% 6%, rgba(3, 105, 161, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 38% 36% at 6% 94%, rgba(30, 58, 138, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__inner {
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
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__badge {
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
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #0369a1;
      flex-shrink: 0;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.44rem, 3.2vw, 2.24rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__h1-accent {
      color: #1e3a8a;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact--accent {
      border-color: #bae6fd;
      color: #0369a1;
      background: #f0f9ff;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__cta {
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
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__cta:hover {
      background: #8b1528;
    }
    .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__scale-beam {
        animation: hero-ni4-scale 5.6s ease-in-out infinite;
        transform-origin: 250px 108px;
      }
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__pan-fns {
        animation: hero-ni4-pan-down 5.6s ease-in-out infinite;
      }
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__pan-biz {
        animation: hero-ni4-pan-up 5.6s ease-in-out infinite;
      }
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__water {
        animation: hero-ni4-water 3.8s ease-in-out infinite;
      }
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fns-stamp {
        animation: hero-ni4-stamp 4.2s ease-in-out infinite;
      }
    }
    @keyframes hero-ni4-scale {
      0%, 100% { transform: rotate(0deg); }
      40% { transform: rotate(3deg); }
      60% { transform: rotate(-2.5deg); }
    }
    @keyframes hero-ni4-pan-down {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(4px); }
    }
    @keyframes hero-ni4-pan-up {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-5px); }
    }
    @keyframes hero-ni4-water {
      0%, 100% { opacity: 0.55; }
      50% { opacity: 0.9; }
    }
    @keyframes hero-ni4-stamp {
      0%, 100% { opacity: 0.7; }
      50% { opacity: 1; }
    }
    @media (prefers-reduced-motion: reduce) {
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__scale-beam,
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__pan-fns,
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__pan-biz,
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__water,
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fns-stamp {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__inner">
    <div class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__content">
      <div class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__badge">
        <span class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__badge-mark" aria-hidden="true"></span>
        ARB · обзор ВС № 4/2026 · гл. 30 НК · май 2026
      </div>
      <h1 class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__h1">
        <span class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__h1-accent">Обзор ВС № 4/2026: налог на имущество организаций в арбитраже</span> — как оспорить ФНС
      </h1>
      <p class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__sub">
        16 позиций ВС о движимом и недвижимом имуществе, сооружениях и сделках — стратегия защиты бизнеса в арбитражном споре с налоговой
      </p>
      <ul class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__facts">
        <li class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact--accent">гл. 30 НК РФ</li>
        <li class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact">движимое / недвижимое</li>
        <li class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact">ГЭС · сооружения</li>
        <li class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fact--warn">доначисление ФНС</li>
      </ul>
      <a class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Получить консультацию</a>
    </div>
    <div class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Промышленная весовая палата: весы арбитража сравнивают налоговый акт ФНС с инвентарными ОС ГЭС и заводского оборудования; обзор ВС № 4/2026">
        <defs>
          <linearGradient id="hero-ni4-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e8eef5"/>
          </linearGradient>
          <linearGradient id="hero-ni4-water" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#7dd3fc"/>
            <stop offset="50%" stop-color="#0ea5e9"/>
            <stop offset="100%" stop-color="#0369a1"/>
          </linearGradient>
          <linearGradient id="hero-ni4-steel" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#94a3b8"/>
            <stop offset="100%" stop-color="#475569"/>
          </linearGradient>
          <linearGradient id="hero-ni4-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e40af"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hero-ni4-paper" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hero-ni4-factory" x1="0%" y1="100%" x2="0%" y2="0%">
            <stop offset="0%" stop-color="#64748b"/>
            <stop offset="100%" stop-color="#94a3b8"/>
          </linearGradient>
          <pattern id="hero-ni4-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f1f5f9"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#e2e8f0" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-ni4-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-ni4-bg)" stroke="#cbd5e1" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-ni4-grid)" opacity="0.45"/>
        <!-- ГЭС: плотина и вода -->
        <g transform="translate(16, 200)">
          <path d="M0 120 L0 60 L48 20 L96 60 L96 120 Z" fill="#64748b" stroke="#475569" stroke-width="1.2"/>
          <rect x="20" y="48" width="12" height="72" rx="2" fill="#334155"/>
          <rect x="40" y="48" width="12" height="72" rx="2" fill="#334155"/>
          <rect x="60" y="48" width="12" height="72" rx="2" fill="#334155"/>
          <path class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__water" d="M96 72 Q140 68 180 76 Q220 84 260 72 L260 120 L96 120 Z" fill="url(#hero-ni4-water)" opacity="0.75"/>
          <ellipse cx="130" cy="78" rx="28" ry="6" fill="#bae6fd" opacity="0.5"/>
          <text x="48" y="14" text-anchor="middle" fill="#0369a1" font-size="6" font-weight="700">ГЭС</text>
          <!-- турбина -->
          <circle cx="48" cy="100" r="14" fill="none" stroke="#0ea5e9" stroke-width="2"/>
          <path d="M48 86 L48 114 M34 100 L62 100 M38 88 L58 112 M58 88 L38 112" stroke="#0ea5e9" stroke-width="1.2"/>
        </g>
        <!-- завод -->
        <g transform="translate(380, 168)" filter="url(#hero-ni4-shadow)">
          <rect x="0" y="48" width="88" height="72" fill="url(#hero-ni4-factory)" rx="2"/>
          <rect x="12" y="20" width="20" height="28" fill="#475569"/>
          <rect x="56" y="28" width="16" height="20" fill="#475569"/>
          <rect x="8" y="56" width="14" height="10" fill="#fef3c7" stroke="#d97706" stroke-width="0.8"/>
          <rect x="28" y="56" width="14" height="10" fill="#fef3c7" stroke="#d97706" stroke-width="0.8"/>
          <rect x="48" y="56" width="14" height="10" fill="#fef3c7" stroke="#d97706" stroke-width="0.8"/>
          <rect x="68" y="56" width="14" height="10" fill="#fef3c7" stroke="#d97706" stroke-width="0.8"/>
          <line x1="22" y1="20" x2="22" y2="8" stroke="#94a3b8" stroke-width="3"/>
          <circle cx="22" cy="6" r="4" fill="#cbd5e1" opacity="0.6"/>
          <line x1="64" y1="28" x2="64" y2="14" stroke="#94a3b8" stroke-width="2.5"/>
          <circle cx="64" cy="12" r="3" fill="#cbd5e1" opacity="0.5"/>
          <text x="44" y="132" text-anchor="middle" fill="#475569" font-size="5.5" font-weight="600">цех · ОС</text>
        </g>
        <!-- ВС: обзор -->
        <g filter="url(#hero-ni4-shadow)" transform="translate(168, 18)">
          <rect x="0" y="34" width="164" height="48" rx="4" fill="url(#hero-ni4-vs)"/>
          <polygon points="82,0 164,34 0,34" fill="#1e40af"/>
          <text x="82" y="52" text-anchor="middle" fill="#e2e8f0" font-size="6.5" font-weight="800" letter-spacing="0.05em">ОБЗОР ВС № 4/2026</text>
          <text x="82" y="66" text-anchor="middle" fill="#93c5fd" font-size="5.5" font-weight="600">налог на имущество · арбитраж</text>
          <text x="82" y="88" text-anchor="middle" fill="#1e3a8a" font-size="6.5" font-weight="700">29.04.2026 · 6А/2026</text>
        </g>
        <!-- стальные весы арбитража -->
        <g class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__scale-beam" filter="url(#hero-ni4-shadow)" transform="translate(0, 0)">
          <rect x="238" y="100" width="24" height="100" rx="3" fill="url(#hero-ni4-steel)" stroke="#334155" stroke-width="1"/>
          <rect x="222" y="92" width="56" height="12" rx="4" fill="url(#hero-ni4-steel)" stroke="#334155" stroke-width="1"/>
          <line x1="250" y1="100" x2="250" y2="72" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
          <line x1="148" y1="72" x2="352" y2="72" stroke="#334155" stroke-width="3" stroke-linecap="round"/>
          <!-- чаша ФНС (левая, тяжелее) -->
          <g class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__pan-fns">
            <line x1="168" y1="72" x2="168" y2="118" stroke="#475569" stroke-width="2"/>
            <path d="M128 118 Q168 132 208 118 L208 138 Q168 152 128 138 Z" fill="#fef2f2" stroke="#f87171" stroke-width="1.2"/>
            <g transform="translate(136, 108)">
              <rect width="64" height="44" rx="4" fill="url(#hero-ni4-paper)" stroke="#a31830" stroke-width="1.2"/>
              <rect x="0" y="0" width="64" height="12" rx="4" fill="#fef2f2"/>
              <text x="32" y="9" text-anchor="middle" fill="#a31830" font-size="5" font-weight="800">ФНС</text>
              <text x="32" y="22" text-anchor="middle" fill="#334155" font-size="4.5" font-weight="700">налог на имущество</text>
              <rect x="6" y="28" width="52" height="4" rx="1" fill="#fee2e2"/>
              <text class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__fns-stamp" x="32" y="40" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="800">ДОНАЧИСЛЕНИЕ</text>
            </g>
          </g>
          <!-- чаша бизнеса (правая, легче — защита) -->
          <g class="l24-hero-vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns__pan-biz">
            <line x1="332" y1="72" x2="332" y2="110" stroke="#475569" stroke-width="2"/>
            <path d="M292 110 Q332 124 372 110 L372 130 Q332 144 292 130 Z" fill="#f0f9ff" stroke="#38bdf8" stroke-width="1.2"/>
            <rect x="300" y="96" width="36" height="22" rx="3" fill="#fff" stroke="#0ea5e9" stroke-width="0.8"/>
            <text x="318" y="106" text-anchor="middle" fill="#0369a1" font-size="4" font-weight="700">компрессор</text>
            <text x="318" y="114" text-anchor="middle" fill="#64748b" font-size="3.5">ОС-08</text>
            <rect x="340" y="98" width="28" height="18" rx="3" fill="#fff" stroke="#0ea5e9" stroke-width="0.8"/>
            <text x="354" y="108" text-anchor="middle" fill="#0369a1" font-size="4" font-weight="700">котёл</text>
            <text x="354" y="114" text-anchor="middle" fill="#64748b" font-size="3.5">движимое</text>
          </g>
          <text x="250" y="218" text-anchor="middle" fill="#1e3a8a" font-size="6.5" font-weight="700">арбитраж · гл. 25 АПК</text>
        </g>
        <!-- налоговая декларация на столе -->
        <g filter="url(#hero-ni4-shadow)" transform="translate(28, 300)">
          <rect width="120" height="76" rx="8" fill="url(#hero-ni4-paper)" stroke="#cbd5e1" stroke-width="1.2"/>
          <text x="60" y="16" text-anchor="middle" fill="#334155" font-size="6" font-weight="800">РАСЧЁТ НАЛОГА</text>
          <text x="60" y="28" text-anchor="middle" fill="#64748b" font-size="5">гл. 30 НК РФ · ст. 374–376</text>
          <rect x="10" y="36" width="100" height="4" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="44" width="80" height="4" rx="1" fill="#e2e8f0"/>
          <rect x="10" y="52" width="90" height="4" rx="1" fill="#bae6fd"/>
          <rect x="10" y="60" width="70" height="4" rx="1" fill="#bbf7d0"/>
          <text x="60" y="72" text-anchor="middle" fill="#0369a1" font-size="5" font-weight="600">ОКОФ · инвентарный объект</text>
        </g>
        <!-- письмо ФНС -->
        <g filter="url(#hero-ni4-shadow)" transform="translate(156, 318)">
          <rect width="108" height="58" rx="6" fill="#fff" stroke="#fecaca" stroke-width="1"/>
          <rect x="0" y="0" width="108" height="14" rx="6" fill="#fef2f2"/>
          <text x="54" y="10" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="800">ПИСЬМО ФНС 07.05.2026</text>
          <text x="54" y="28" text-anchor="middle" fill="#475569" font-size="4.5">БС-36-21/3766@</text>
          <text x="54" y="40" text-anchor="middle" fill="#64748b" font-size="4.5">обзор → все ИФНС</text>
          <text x="54" y="52" text-anchor="middle" fill="#a31830" font-size="4.5" font-weight="700">волна проверок</text>
        </g>
        <!-- сооружение vs движимое -->
        <g filter="url(#hero-ni4-shadow)" transform="translate(280, 308)">
          <rect width="96" height="68" rx="8" fill="#fff" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
          <text x="48" y="16" text-anchor="middle" fill="#334155" font-size="5.5" font-weight="800">п. 4–8 обзора</text>
          <text x="48" y="30" text-anchor="middle" fill="#64748b" font-size="5">сооружение целиком?</text>
          <line x1="12" y1="38" x2="84" y2="38" stroke="#e2e8f0"/>
          <text x="48" y="50" text-anchor="middle" fill="#0369a1" font-size="5" font-weight="600">движимое ОС</text>
          <text x="48" y="62" text-anchor="middle" fill="#166534" font-size="5" font-weight="600">защита в арбитраже</text>
        </g>
        <!-- сделки взаимозависимых -->
        <g filter="url(#hero-ni4-shadow)" transform="translate(388, 300)">
          <rect width="88" height="76" rx="8" fill="#fff" stroke="#1e3a8a" stroke-width="1"/>
          <text x="44" y="16" text-anchor="middle" fill="#1e3a8a" font-size="5.5" font-weight="800">п. 11</text>
          <text x="44" y="30" text-anchor="middle" fill="#475569" font-size="5">рыночная стоимость</text>
          <text x="44" y="42" text-anchor="middle" fill="#64748b" font-size="4.5">взаимозависимые</text>
          <rect x="10" y="50" width="68" height="16" rx="4" fill="#eff6ff" stroke="#93c5fd"/>
          <text x="44" y="61" text-anchor="middle" fill="#1e40af" font-size="4.5" font-weight="600">пересчёт базы</text>
        </g>
        <!-- молоток арбитража -->
        <g transform="translate(420, 228)">
          <rect x="0" y="20" width="48" height="10" rx="3" fill="#64748b"/>
          <rect x="36" y="8" width="14" height="24" rx="3" fill="#475569"/>
          <text x="24" y="44" text-anchor="middle" fill="#64748b" font-size="5" font-weight="600">АПК</text>
        </g>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">ГЭС · завод · движимое ОС · сооружения · оспаривание ФНС в арбитраже</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>` и `<script>`.
