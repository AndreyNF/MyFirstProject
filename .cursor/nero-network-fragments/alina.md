=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Зал ВС: весы между колонией и дорогой» — реальный срок за смертельное ДТП перевешивает смягчающие, пока ВС не возвращает баланс через ст. 73 УК |
| **Центральная метафора** | Весы правосудия: на одной чаше — решётка колонии и «2 года реально»; на другой — открытая дорога, знак свободы и «условно + освобождение»; между ними — судебный зал ВС и определение № 41-УД26-25-К4 |
| **Пространство** | Светлый градиент «утро в зале ВС»; SVG — фасад Верховного суда, весы, дорога с разметкой, автомобильный след, карточка ст. 73 УК, 11 смягчающих vs 0 отягчающих; не СИП/ТЗ, не ФНС, не маркетплейс |
| **Движение** | Только CSS: покачивание весов в сторону «свободы», пульс дорожной разметки, мерцание решётки колонии, подсветка бейджа ст. 73; `prefers-reduced-motion` отключает |
| **Палитра** | `#0f172a` текст, `#4338ca` ВС/акцент, `#059669` условный срок/свобода, `#64748b` колония/реальный срок, `#475569` подзаголовок, `#a31830` CTA, `#f8fafc`–`#eef2f7` фон |
| **Аудитория** | Водители и родственники в уголовных делах о ДТП с погибшим; адвокаты, обжалующие немотивированный отказ от ст. 73 УК |

## Чеклист отличий от других hero

- [x] **Не СИП / товарный знак** (`l24-hero-sip-prekrashchenie-…`): нет свидетельства ТЗ, МКТУ, ст. 1486 — фокус **уголовное право, ДТП, ст. 73 УК**
- [x] **Не компенсация иностранцу / маркетплейс**: нет щита, Указа № 322 — угол **ВС 2026, гуманизация, условное осуждение**
- [x] **Не обзор ВС № 4 (налог)**: нет ГЭС, ФНС — инстанция **СК по уголовным делам ВС**, ч. 3 ст. 264 УК
- [x] **Уникальная сцена**: весы «колония ↔ дорога» + зал ВС + определение 41-УД26-25-К4 + смягчающие обстоятельства
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA: «Консультация по защите в уголовном деле о ДТП» → `https://advokat-vsem.ru/`

```html
<section id="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026" class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026" aria-label="ВС 2026: условное наказание вместо реального срока за смертельное ДТП — смягчающие обстоятельства и защита">
  <style>
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(158deg, #fefefe 0%, #f5f3ff 28%, #eef2f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 44% 40% at 90% 6%, rgba(67, 56, 202, 0.09) 0%, transparent 55%),
        radial-gradient(ellipse 38% 36% at 6% 94%, rgba(5, 150, 105, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__inner {
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
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__badge {
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
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #4338ca;
      flex-shrink: 0;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.42rem, 3.1vw, 2.2rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__h1-accent {
      color: #4338ca;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact--accent {
      border-color: #c4b5fd;
      color: #4338ca;
      background: #f5f3ff;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact--ok {
      border-color: #a7f3d0;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact--warn {
      border-color: #cbd5e1;
      color: #475569;
      background: #f1f5f9;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__cta {
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
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__cta:hover {
      background: #8b1528;
    }
    .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (prefers-reduced-motion: no-preference) {
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__scales {
        animation: hero-vsdtp-tilt 5s ease-in-out infinite;
        transform-origin: 250px 168px;
      }
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__road-dash {
        animation: hero-vsdtp-dash 3.5s linear infinite;
      }
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__bars {
        animation: hero-vsdtp-bars 4s ease-in-out infinite;
      }
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__art73 {
        animation: hero-vsdtp-pulse 3.8s ease-in-out infinite;
      }
    }
    @keyframes hero-vsdtp-tilt {
      0%, 100% { transform: rotate(-2deg); }
      50% { transform: rotate(3deg); }
    }
    @keyframes hero-vsdtp-dash {
      0% { stroke-dashoffset: 0; }
      100% { stroke-dashoffset: -24; }
    }
    @keyframes hero-vsdtp-bars {
      0%, 100% { opacity: 0.55; }
      50% { opacity: 0.9; }
    }
    @keyframes hero-vsdtp-pulse {
      0%, 100% { opacity: 0.85; }
      50% { opacity: 1; }
    }
    @media (prefers-reduced-motion: reduce) {
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__scales,
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__road-dash,
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__bars,
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__art73 {
        animation: none !important;
      }
    }
    @media (max-width: 900px) {
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__inner">
    <div class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__content">
      <div class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__badge">
        <span class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__badge-mark" aria-hidden="true"></span>
        UG · ВС 2026 · ст. 73 УК · № 41-УД26-25-К4
      </div>
      <h1 class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__h1">
        <span class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__h1-accent">ВС 2026: условное наказание вместо реального срока за смертельное ДТП</span> — смягчающие обстоятельства и защита
      </h1>
      <p class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__sub">
        Определение № 41-УД26-25-К4: когда суд обязан мотивировать отказ от ст. 73 УК и как ВС освобождает из колонии
      </p>
      <ul class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__facts">
        <li class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact--accent">ст. 73 УК РФ</li>
        <li class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact--ok">11 смягчающих · 0 отягчающих</li>
        <li class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact">ч. 3 ст. 264 УК</li>
        <li class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__fact--warn">2 года → условно</li>
      </ul>
      <a class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по защите в уголовном деле о ДТП</a>
    </div>
    <div class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Зал Верховного суда: весы правосудия между колонией и открытой дорогой — условное наказание по ст. 73 УК за смертельное ДТП">
        <defs>
          <linearGradient id="hero-vsdtp-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#ede9fe"/>
          </linearGradient>
          <linearGradient id="hero-vsdtp-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#5b21b6"/>
            <stop offset="100%" stop-color="#312e81"/>
          </linearGradient>
          <linearGradient id="hero-vsdtp-road" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#64748b"/>
            <stop offset="100%" stop-color="#475569"/>
          </linearGradient>
          <linearGradient id="hero-vsdtp-free" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#d1fae5"/>
            <stop offset="100%" stop-color="#6ee7b7"/>
          </linearGradient>
          <linearGradient id="hero-vsdtp-prison" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" stop-color="#e2e8f0"/>
            <stop offset="100%" stop-color="#94a3b8"/>
          </linearGradient>
          <pattern id="hero-vsdtp-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f5f3ff"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#e9d5ff" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-vsdtp-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="5" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.12"/>
          </filter>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-vsdtp-bg)" stroke="#c4b5fd" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-vsdtp-grid)" opacity="0.35"/>
        <!-- фасад ВС -->
        <g filter="url(#hero-vsdtp-shadow)" transform="translate(138, 12)">
          <rect x="0" y="38" width="224" height="54" rx="4" fill="url(#hero-vsdtp-vs)"/>
          <polygon points="112,0 224,38 0,38" fill="#6d28d9"/>
          <rect x="28" y="50" width="32" height="34" rx="2" fill="#4c1d95" opacity="0.45"/>
          <rect x="96" y="50" width="32" height="34" rx="2" fill="#4c1d95" opacity="0.45"/>
          <rect x="164" y="50" width="32" height="34" rx="2" fill="#4c1d95" opacity="0.45"/>
          <text x="112" y="60" text-anchor="middle" fill="#ede9fe" font-size="6.5" font-weight="800" letter-spacing="0.05em">ВЕРХОВНЫЙ СУД РФ</text>
          <text x="112" y="74" text-anchor="middle" fill="#c4b5fd" font-size="5.5" font-weight="600">СК по уголовным делам · 2026</text>
        </g>
        <!-- определение -->
        <g filter="url(#hero-vsdtp-shadow)" transform="translate(24, 52)">
          <rect width="108" height="68" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1"/>
          <text x="54" y="14" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">ОПРЕДЕЛЕНИЕ</text>
          <text x="54" y="28" text-anchor="middle" fill="#334155" font-size="5" font-weight="700">№ 41-УД26-25-К4</text>
          <text x="54" y="42" text-anchor="middle" fill="#64748b" font-size="4.5">05.06.2026 · РАПСИ</text>
          <rect x="10" y="50" width="88" height="12" rx="4" fill="#f5f3ff"/>
          <text x="54" y="59" text-anchor="middle" fill="#4338ca" font-size="4.5" font-weight="600">гуманизация · ст. 73</text>
        </g>
        <!-- ст. 73 УК -->
        <g class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__art73" filter="url(#hero-vsdtp-shadow)" transform="translate(368, 48)">
          <rect width="108" height="72" rx="8" fill="#fff" stroke="#059669" stroke-width="1.2"/>
          <text x="54" y="16" text-anchor="middle" fill="#047857" font-size="6" font-weight="800">ст. 73 УК РФ</text>
          <text x="54" y="30" text-anchor="middle" fill="#64748b" font-size="4.5">условное осуждение</text>
          <rect x="12" y="38" width="84" height="10" rx="3" fill="#ecfdf5" stroke="#6ee7b7"/>
          <text x="54" y="46" text-anchor="middle" fill="#047857" font-size="4.5" font-weight="700">исправление без изоляции</text>
          <text x="54" y="62" text-anchor="middle" fill="#334155" font-size="4.5">мотивировка отказа обязательна</text>
        </g>
        <!-- весы правосудия -->
        <g class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__scales" filter="url(#hero-vsdtp-shadow)">
          <line x1="250" y1="118" x2="250" y2="168" stroke="#4338ca" stroke-width="3" stroke-linecap="round"/>
          <circle cx="250" cy="118" r="6" fill="#4338ca"/>
          <line x1="168" y1="168" x2="332" y2="168" stroke="#4338ca" stroke-width="2.5" stroke-linecap="round"/>
          <!-- левая чаша: колония / реальный срок -->
          <line x1="168" y1="168" x2="168" y2="198" stroke="#64748b" stroke-width="1.5"/>
          <ellipse cx="168" cy="200" rx="52" ry="8" fill="#cbd5e1" opacity="0.6"/>
          <g class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__bars">
            <rect x="128" y="200" width="80" height="52" rx="6" fill="url(#hero-vsdtp-prison)" stroke="#64748b" stroke-width="1"/>
            <line x1="140" y1="208" x2="140" y2="244" stroke="#475569" stroke-width="2"/>
            <line x1="156" y1="208" x2="156" y2="244" stroke="#475569" stroke-width="2"/>
            <line x1="172" y1="208" x2="172" y2="244" stroke="#475569" stroke-width="2"/>
            <line x1="188" y1="208" x2="188" y2="244" stroke="#475569" stroke-width="2"/>
            <line x1="204" y1="208" x2="204" y2="244" stroke="#475569" stroke-width="2"/>
            <text x="168" y="268" text-anchor="middle" fill="#475569" font-size="5.5" font-weight="800">2 года реально</text>
            <text x="168" y="280" text-anchor="middle" fill="#64748b" font-size="4.5">нижние инстанции</text>
          </g>
          <!-- правая чаша: дорога / свобода -->
          <line x1="332" y1="168" x2="332" y2="198" stroke="#059669" stroke-width="1.5"/>
          <ellipse cx="332" cy="200" rx="52" ry="8" fill="#6ee7b7" opacity="0.5"/>
          <rect x="292" y="200" width="80" height="52" rx="6" fill="url(#hero-vsdtp-free)" stroke="#059669" stroke-width="1"/>
          <path d="M302 238 Q332 218 362 238" fill="none" stroke="#047857" stroke-width="2"/>
          <path class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__road-dash" d="M308 232 L318 232 M328 228 L338 228 M348 232 L358 232" stroke="#fff" stroke-width="2" stroke-dasharray="6 6" stroke-linecap="round"/>
          <circle cx="362" cy="232" r="5" fill="#4338ca" opacity="0.8"/>
          <text x="332" y="268" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="800">условно + свобода</text>
          <text x="332" y="280" text-anchor="middle" fill="#059669" font-size="4.5">освобождение из колонии</text>
        </g>
        <!-- дорога к весам -->
        <g transform="translate(80, 300)">
          <path d="M0 40 Q60 20 120 8 Q180 0 240 12 Q300 24 340 40" fill="none" stroke="url(#hero-vsdtp-road)" stroke-width="14" stroke-linecap="round"/>
          <path class="l24-hero-vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026__road-dash" d="M20 40 L40 38 M60 36 L80 34 M100 32 L120 30 M140 28 L160 26 M180 24 L200 22 M220 20 L240 18 M260 18 L280 20 M300 24 L320 28 M330 32 L350 36" stroke="#fbbf24" stroke-width="2" stroke-dasharray="8 8" stroke-linecap="round"/>
          <text x="170" y="58" text-anchor="middle" fill="#64748b" font-size="5" font-weight="600">ДТП · ч. 3 ст. 264 УК</text>
        </g>
        <!-- смягчающие обстоятельства -->
        <g filter="url(#hero-vsdtp-shadow)" transform="translate(24, 318)">
          <rect width="148" height="96" rx="8" fill="#fff" stroke="#059669" stroke-width="1"/>
          <text x="74" y="16" text-anchor="middle" fill="#047857" font-size="5.5" font-weight="800">СМЯГЧАЮЩИЕ</text>
          <text x="74" y="28" text-anchor="middle" fill="#64748b" font-size="4.5">совокупность · ст. 88 УПК</text>
          <rect x="10" y="36" width="62" height="12" rx="3" fill="#ecfdf5" stroke="#6ee7b7"/>
          <text x="41" y="45" text-anchor="middle" fill="#047857" font-size="4" font-weight="600">признание вины</text>
          <rect x="76" y="36" width="62" height="12" rx="3" fill="#ecfdf5" stroke="#6ee7b7"/>
          <text x="107" y="45" text-anchor="middle" fill="#047857" font-size="4" font-weight="600">возмещение вреда</text>
          <rect x="10" y="52" width="62" height="12" rx="3" fill="#ecfdf5" stroke="#6ee7b7"/>
          <text x="41" y="61" text-anchor="middle" fill="#047857" font-size="4" font-weight="600">примирение</text>
          <rect x="76" y="52" width="62" height="12" rx="3" fill="#ecfdf5" stroke="#6ee7b7"/>
          <text x="107" y="61" text-anchor="middle" fill="#047857" font-size="4" font-weight="600">волонтёрство</text>
          <rect x="10" y="68" width="128" height="12" rx="3" fill="#f5f3ff" stroke="#c4b5fd"/>
          <text x="74" y="77" text-anchor="middle" fill="#4338ca" font-size="4.5" font-weight="700">11 факторов · 0 отягчающих</text>
          <text x="74" y="90" text-anchor="middle" fill="#64748b" font-size="4">позиция потерпевших учтена</text>
        </g>
        <!-- судебный зал -->
        <g filter="url(#hero-vsdtp-shadow)" transform="translate(188, 318)">
          <rect width="120" height="96" rx="8" fill="#fff" stroke="#4338ca" stroke-width="1"/>
          <rect x="0" y="0" width="120" height="18" rx="8" fill="#f5f3ff"/>
          <text x="60" y="12" text-anchor="middle" fill="#4338ca" font-size="5.5" font-weight="800">СУДЕБНЫЙ ЗАЛ</text>
          <rect x="20" y="28" width="80" height="8" rx="2" fill="#4338ca" opacity="0.25"/>
          <rect x="36" y="44" width="48" height="6" rx="2" fill="#64748b" opacity="0.4"/>
          <circle cx="40" cy="62" r="8" fill="#ede9fe" stroke="#7c3aed"/>
          <circle cx="60" cy="62" r="8" fill="#ede9fe" stroke="#7c3aed"/>
          <circle cx="80" cy="62" r="8" fill="#ede9fe" stroke="#7c3aed"/>
          <text x="60" y="82" text-anchor="middle" fill="#334155" font-size="4.5" font-weight="600">мотивировка отказа</text>
          <text x="60" y="92" text-anchor="middle" fill="#991b1b" font-size="4">от ст. 73 — обязательна</text>
        </g>
        <!-- испытательный срок -->
        <g filter="url(#hero-vsdtp-shadow)" transform="translate(320, 318)">
          <rect width="72" height="96" rx="8" fill="#fff" stroke="#7c3aed" stroke-width="1"/>
          <text x="36" y="16" text-anchor="middle" fill="#5b21b6" font-size="5" font-weight="800">ИСПЫТ.</text>
          <text x="36" y="28" text-anchor="middle" fill="#64748b" font-size="4.5">срок 2 года</text>
          <circle cx="36" cy="54" r="22" fill="none" stroke="#c4b5fd" stroke-width="3"/>
          <path d="M36 32 A22 22 0 1 1 24 58" fill="none" stroke="#4338ca" stroke-width="3" stroke-linecap="round"/>
          <text x="36" y="58" text-anchor="middle" fill="#4338ca" font-size="8" font-weight="800">2</text>
          <text x="36" y="82" text-anchor="middle" fill="#334155" font-size="4.5">контроль</text>
          <text x="36" y="92" text-anchor="middle" fill="#64748b" font-size="4">без изоляции</text>
        </g>
        <!-- кассация -->
        <g filter="url(#hero-vsdtp-shadow)" transform="translate(404, 318)">
          <rect width="72" height="96" rx="8" fill="#fff" stroke="#a31830" stroke-width="1" opacity="0.95"/>
          <text x="36" y="16" text-anchor="middle" fill="#a31830" font-size="5" font-weight="800">КАССАЦИЯ</text>
          <path d="M18 44 L36 28 L54 44 L54 68 L18 68 Z" fill="#fef2f2" stroke="#fca5a5"/>
          <text x="36" y="52" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="700">ВС</text>
          <text x="36" y="82" text-anchor="middle" fill="#334155" font-size="4.5">изменил приговор</text>
          <text x="36" y="92" text-anchor="middle" fill="#64748b" font-size="4">освобождение</text>
        </g>
        <!-- автомобильный след -->
        <g transform="translate(400, 168)" opacity="0.85">
          <ellipse cx="0" cy="0" rx="14" ry="6" fill="none" stroke="#4338ca" stroke-width="1.2" stroke-dasharray="3 2"/>
          <ellipse cx="18" cy="4" rx="12" ry="5" fill="none" stroke="#4338ca" stroke-width="1" opacity="0.6"/>
          <ellipse cx="34" cy="8" rx="10" ry="4" fill="none" stroke="#4338ca" stroke-width="0.8" opacity="0.4"/>
        </g>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">ВС · ст. 73 УК · весы «колония ↔ дорога» · гуманизация · условное наказание за ДТП</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: vs-gumanizaciya-dtp-uslovnoe-nakazanie-smagchayushchie-2026
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>` и `<script>`.
