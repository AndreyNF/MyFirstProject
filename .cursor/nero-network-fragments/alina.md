=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Арбитражный вес сделки с жильём» — обзор ВС 01.07.2026, 20 позиций после «эффекта Долиной», спор ФУ и добросовестного покупателя по ст. 61.2 |
| **Центральная метафора** | Квартира + стопка документов сделки (ДКП, дарственная); весы: «ФУ оспорит» vs «покупатель защитит»; бейдж обзора ВС 01.07.2026 и ст. 61.2 |
| **Пространство** | ARB-градиент (#f8fafc → #eef2f8); SVG — жилой дом, договор, весы, блок 20 позиций |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#1e3a8a`, `#0369a1` ARB; `#a31830` CTA; `#0f172a` текст |
| **Аудитория** | Покупатели квартир, должники, финансовые управляющие, кредиторы в арбитраже |

## Чеклист отличий от других hero

- [x] **Не vs-moshennichestvo (UG)**: не мост/МУП/ст. 159 — угол **ст. 61.2, жильё, банкротство**
- [x] **Не plenum-42**: не субсидиарка/директор — **оспаривание сделок с квартирой**
- [x] Уникальная сцена: **квартира + документы сделки** + весы «ФУ оспорит / покупатель защитит»
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] Badge **ARB · обзор ВС 01.07.2026 · ст. 61.2**; chips: 20 позиций, дарение, >20% цена, добросовестный покупатель

```html
<section id="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026" class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026" aria-label="Обзор ВС 2026: оспаривание сделок с жильём в банкротстве — дарение, цена, мнимость">
  <style>
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(152deg, #fefefe 0%, #f3f6fa 36%, #eef2f8 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 42% 38% at 88% 8%, rgba(3, 105, 161, 0.08) 0%, transparent 55%),
        radial-gradient(ellipse 36% 34% at 8% 92%, rgba(30, 58, 138, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__inner {
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
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.95);
      border: 1px solid rgba(30, 58, 138, 0.14);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #0369a1;
      flex-shrink: 0;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.32rem, 2.85vw, 2.08rem);
      line-height: 1.22;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__h1-accent {
      color: #1e3a8a;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.45vw, 1.08rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0 0 26px;
      padding: 0;
      list-style: none;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--blue {
      border-color: #bae6fd;
      color: #0369a1;
      background: #f0f9ff;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--navy {
      border-color: #93c5fd;
      color: #1e3a8a;
      background: #eff6ff;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--warn {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--ok {
      border-color: #a7f3d0;
      color: #047857;
      background: #ecfdf5;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__cta {
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
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__cta:hover {
      background: #8b1528;
    }
    .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__visual {
        order: -1;
        max-height: 320px;
        overflow: hidden;
      }
    }
  </style>

  <div class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__inner">
    <div class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__content">
      <div class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__badge">
        <span class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__badge-mark" aria-hidden="true"></span>
        ARB · обзор ВС 01.07.2026 · ст. 61.2
      </div>
      <h1 class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__h1">
        <span class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__h1-accent">Обзор ВС 2026: оспаривание сделок с жильём в банкротстве</span> — дарение, цена, мнимость
      </h1>
      <p class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__sub">
        20 позиций после «эффекта Долиной»: когда ФУ оспорит продажу квартиры, а покупатель защитит сделку
      </p>
      <ul class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__facts">
        <li class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--navy">20 позиций</li>
        <li class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--blue">дарение</li>
        <li class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--warn">&gt;20% цена</li>
        <li class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__fact--ok">добросовестный покупатель</li>
      </ul>
      <a class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по оспариванию и защите сделки с жильём</a>
    </div>

    <div class="l24-hero-vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 520 440" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:520px" role="img" aria-label="Квартира и документы сделки на весах арбитража: ФУ оспорит продажу или покупатель защитит сделку — обзор ВС 01.07.2026, ст. 61.2, 20 позиций">
        <defs>
          <linearGradient id="hos612-bg" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#e8eef5"/>
          </linearGradient>
          <linearGradient id="hos612-navy" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a8a"/>
            <stop offset="100%" stop-color="#0f2744"/>
          </linearGradient>
          <linearGradient id="hos612-sky" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0369a1"/>
            <stop offset="100%" stop-color="#1e3a8a"/>
          </linearGradient>
          <linearGradient id="hos612-paper" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fff"/>
            <stop offset="100%" stop-color="#f1f5f9"/>
          </linearGradient>
          <linearGradient id="hos612-brick" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#cbd5e1"/>
            <stop offset="100%" stop-color="#94a3b8"/>
          </linearGradient>
          <pattern id="hos612-grid" width="18" height="18" patternUnits="userSpaceOnUse">
            <rect width="18" height="18" fill="#f1f5f9"/>
            <path d="M18 0 L0 0 0 18" fill="none" stroke="#e2e8f0" stroke-width="0.5"/>
          </pattern>
          <filter id="hos612-sh" x="-8%" y="-8%" width="116%" height="116%">
            <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.1"/>
          </filter>
        </defs>

        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hos612-bg)" stroke="#cbd5e1" stroke-width="1.2"/>
        <rect x="10" y="12" width="500" height="416" rx="16" fill="url(#hos612-grid)" opacity="0.45"/>

        <!-- VS review badge -->
        <g filter="url(#hos612-sh)" transform="translate(138,14)">
          <rect x="0" y="26" width="244" height="50" rx="6" fill="url(#hos612-navy)"/>
          <polygon points="122,4 238,26 6,26" fill="#1e3a8a"/>
          <text x="122" y="46" text-anchor="middle" fill="#e2e8f0" font-size="6.5" font-weight="800" letter-spacing="0.04em">ВС РФ · обзор 01.07.2026</text>
          <text x="122" y="60" text-anchor="middle" fill="#7dd3fc" font-size="5.5">20 позиций · жильё · «эффект Долиной»</text>
        </g>

        <!-- Scales pillar -->
        <rect x="254" y="78" width="6" height="78" rx="3" fill="#475569"/>
        <circle cx="257" cy="76" r="7" fill="#334155"/>
        <line x1="138" y1="94" x2="376" y2="88" stroke="#475569" stroke-width="4.5" stroke-linecap="round"/>
        <circle cx="257" cy="91" r="5" fill="#64748b"/>

        <!-- Left pan: FU OSPORIT (higher, lighter) -->
        <line x1="168" y1="95" x2="158" y2="124" stroke="#94a3b8" stroke-width="1.5"/>
        <line x1="184" y1="95" x2="194" y2="124" stroke="#94a3b8" stroke-width="1.5"/>
        <g filter="url(#hos612-sh)" transform="translate(118,122)">
          <ellipse cx="58" cy="6" rx="60" ry="6" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
          <rect x="0" y="4" width="118" height="62" rx="7" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
          <text x="59" y="18" text-anchor="middle" fill="#991b1b" font-size="6" font-weight="800">ФУ ОСПОРИТ</text>
          <text x="59" y="30" text-anchor="middle" fill="#b91c1c" font-size="5">п. 1–2 ст. 61.2</text>
          <text x="59" y="41" text-anchor="middle" fill="#b91c1c" font-size="5">дарение · &gt;20% цена</text>
          <text x="59" y="52" text-anchor="middle" fill="#b91c1c" font-size="5">мнимость сделки</text>
          <rect x="8" y="56" width="102" height="11" rx="3" fill="#fee2e2"/>
          <text x="59" y="64" text-anchor="middle" fill="#dc2626" font-size="5" font-weight="600">подозрительная сделка</text>
        </g>

        <!-- Right pan: POKUPATEL ZASHCHITIT (lower, heavier) -->
        <line x1="338" y1="89" x2="332" y2="114" stroke="#94a3b8" stroke-width="1.5"/>
        <line x1="354" y1="89" x2="360" y2="114" stroke="#94a3b8" stroke-width="1.5"/>
        <g filter="url(#hos612-sh)" transform="translate(324,112)">
          <ellipse cx="52" cy="7" rx="54" ry="7" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
          <rect x="0" y="5" width="106" height="72" rx="7" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
          <text x="53" y="20" text-anchor="middle" fill="#047857" font-size="6" font-weight="800">ПОКУПАТЕЛЬ ЗАЩИТИТ</text>
          <text x="53" y="32" text-anchor="middle" fill="#065f46" font-size="5">ст. 61.4 · осмотрительность</text>
          <text x="53" y="43" text-anchor="middle" fill="#065f46" font-size="5">заверения · ячейка</text>
          <text x="53" y="54" text-anchor="middle" fill="#065f46" font-size="5">307-ЭС25-13338</text>
          <rect x="8" y="58" width="90" height="13" rx="4" fill="#059669"/>
          <text x="53" y="68" text-anchor="middle" fill="#fff" font-size="5.5" font-weight="700">ВС: отказ ФУ</text>
        </g>

        <!-- Apartment building (center-bottom) -->
        <g filter="url(#hos612-sh)" transform="translate(196,196)">
          <rect x="0" y="28" width="128" height="96" rx="4" fill="url(#hos612-brick)" stroke="#64748b" stroke-width="1.2"/>
          <polygon points="64,8 122,30 6,30" fill="#475569"/>
          <rect x="14" y="42" width="22" height="18" rx="2" fill="#bae6fd" stroke="#0369a1" stroke-width="0.8"/>
          <rect x="42" y="42" width="22" height="18" rx="2" fill="#bae6fd" stroke="#0369a1" stroke-width="0.8"/>
          <rect x="70" y="42" width="22" height="18" rx="2" fill="#bae6fd" stroke="#0369a1" stroke-width="0.8"/>
          <rect x="98" y="42" width="16" height="18" rx="2" fill="#bae6fd" stroke="#0369a1" stroke-width="0.8"/>
          <rect x="14" y="68" width="22" height="18" rx="2" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="0.8"/>
          <rect x="42" y="68" width="22" height="18" rx="2" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="0.8"/>
          <rect x="70" y="68" width="22" height="18" rx="2" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="0.8"/>
          <rect x="98" y="68" width="16" height="18" rx="2" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="0.8"/>
          <rect x="52" y="94" width="24" height="30" rx="2" fill="#334155"/>
          <text x="64" y="22" text-anchor="middle" fill="#f8fafc" font-size="5.5" font-weight="700">КВАРТИРА</text>
        </g>

        <!-- Left: DKP document stack -->
        <g filter="url(#hos612-sh)" transform="translate(22,188)">
          <rect x="8" y="6" width="108" height="88" rx="6" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
          <rect x="0" y="0" width="108" height="88" rx="6" fill="url(#hos612-paper)" stroke="#0369a1" stroke-width="1.3"/>
          <rect x="0" y="0" width="108" height="16" rx="6" fill="url(#hos612-sky)"/>
          <rect y="10" width="108" height="6" fill="url(#hos612-sky)"/>
          <text x="54" y="11" text-anchor="middle" fill="#e0f2fe" font-size="5.5" font-weight="800">ДКП КВАРТИРЫ</text>
          <text x="54" y="28" text-anchor="middle" fill="#334155" font-size="5">цена в договоре</text>
          <text x="54" y="40" text-anchor="middle" fill="#0369a1" font-size="6.5" font-weight="800">5 000 000 ₽</text>
          <text x="54" y="52" text-anchor="middle" fill="#64748b" font-size="5">кадастр · экспертиза</text>
          <text x="54" y="64" text-anchor="middle" fill="#64748b" font-size="5">банковская ячейка</text>
          <rect x="10" y="70" width="88" height="11" rx="3" fill="#f0f9ff"/>
          <text x="54" y="78" text-anchor="middle" fill="#0369a1" font-size="4.8" font-weight="600">заверения продавца</text>
        </g>

        <!-- Right: gift deed -->
        <g filter="url(#hos612-sh)" transform="translate(390,188)">
          <rect x="6" y="4" width="108" height="88" rx="6" fill="#e2e8f0" stroke="#94a3b8" stroke-width="1"/>
          <rect x="0" y="0" width="108" height="88" rx="6" fill="url(#hos612-paper)" stroke="#1e3a8a" stroke-width="1.3"/>
          <rect x="0" y="0" width="108" height="16" rx="6" fill="url(#hos612-navy)"/>
          <rect y="10" width="108" height="6" fill="url(#hos612-navy)"/>
          <text x="54" y="11" text-anchor="middle" fill="#bfdbfe" font-size="5.5" font-weight="800">ДАРСТВЕННАЯ</text>
          <text x="54" y="28" text-anchor="middle" fill="#334155" font-size="5">п. 2 ст. 61.2</text>
          <text x="54" y="40" text-anchor="middle" fill="#1e3a8a" font-size="5.5" font-weight="700">цель вреда кредиторам</text>
          <text x="54" y="52" text-anchor="middle" fill="#64748b" font-size="5">look-back 3 года</text>
          <text x="54" y="64" text-anchor="middle" fill="#64748b" font-size="5">возврат в массу</text>
          <rect x="10" y="70" width="88" height="11" rx="3" fill="#eff6ff"/>
          <text x="54" y="78" text-anchor="middle" fill="#1e3a8a" font-size="4.8" font-weight="600">поз. 13 обзора</text>
        </g>

        <!-- st. 61.2 central tag -->
        <g filter="url(#hos612-sh)" transform="translate(214,308)">
          <rect width="92" height="36" rx="8" fill="url(#hos612-sky)"/>
          <text x="46" y="14" text-anchor="middle" fill="#e0f2fe" font-size="5.5" font-weight="700">ЗАКОН О БАНКРОТСТВЕ</text>
          <text x="46" y="27" text-anchor="middle" fill="#fff" font-size="8" font-weight="800">ст. 61.2</text>
        </g>

        <!-- Bottom info boxes -->
        <g filter="url(#hos612-sh)" transform="translate(18,358)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#1e3a8a" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="800">20 ПОЗИЦИЙ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">гражданское + банкротное</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">дарение · цена · мнимость</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">реституция ст. 167 ГК</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#eff6ff"/>
          <text x="77" y="63" text-anchor="middle" fill="#1e3a8a" font-size="5" font-weight="600">обзор 01.07.2026</text>
        </g>
        <g filter="url(#hos612-sh)" transform="translate(183,358)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#dc2626" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#dc2626" font-size="6" font-weight="800">&gt;20% НЕ ДОСТАТОЧНО</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">п. 1 ст. 61.2 · цена</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">контекст отношений сторон</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">совокупная оценка ВС</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#fef2f2"/>
          <text x="77" y="63" text-anchor="middle" fill="#dc2626" font-size="5" font-weight="600">поз. 14 · Чигарчакова</text>
        </g>
        <g filter="url(#hos612-sh)" transform="translate(348,358)">
          <rect width="154" height="66" rx="8" fill="#fff" stroke="#059669" stroke-width="1.2"/>
          <text x="77" y="17" text-anchor="middle" fill="#059669" font-size="6" font-weight="800">ДОБРОСОВЕСТНЫЙ</text>
          <text x="77" y="29" text-anchor="middle" fill="#64748b" font-size="5">покупатель · ст. 61.4</text>
          <text x="77" y="40" text-anchor="middle" fill="#334155" font-size="5">ЕГРН · заверения · ячейка</text>
          <text x="77" y="51" text-anchor="middle" fill="#334155" font-size="5">защита в арбитраже</text>
          <rect x="10" y="55" width="134" height="11" rx="3" fill="#ecfdf5"/>
          <text x="77" y="63" text-anchor="middle" fill="#059669" font-size="5" font-weight="600">поз. 15 обзора</text>
        </g>

        <text x="260" y="432" text-anchor="middle" fill="#94a3b8" font-size="6.5" font-weight="600">ARB · ст. 61.2 · жильё · ФУ · покупатель · обзор ВС 2026</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе

SLUG: vs-osparivanie-sdelok-zhiloe-bankrotstvo-2026
H1_для_hero: Обзор ВС 2026: оспаривание сделок с жильём в банкротстве — дарение, цена, мнимость
ПОДЗАГОЛОВОК_HERO: 20 позиций после «эффекта Долиной»: когда ФУ оспорит продажу квартиры, а покупатель защитит сделку
ТИП_СТАТЬИ: ARB — арбитраж при банкротстве
СЛЕДУЮЩИЙ_ШАГ: Наташа (сборка + публикация)
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>`.
