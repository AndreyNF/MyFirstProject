=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Цифровой кошелёк под весами ВС» — платёжная среда 2026: цифровой рубль на счёте, тайное списание vs добровольный перевод; Пленум № 19 разводит кражу и мошенничество |
| **Центральная метафора** | Смартфон-кошелёк с цифровым рублём (₽) в центре; весы правосудия ВС сверху; развилка «ст. 158 — кража» / «ст. 159 — мошенничество»; критерий «обман только для доступа → тайное списание» |
| **Пространство** | Светлый холодный градиент «утро в зале суда / цифровой банкинг»; SVG — фасад ВС, весы, кошелёк, стрелки развилки, бейдж ст. 158.1 |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#0f172a` текст, `#1e3a5f` ВС/суд, `#0d9488` кража/ст. 158, `#b91c1c` мошенничество/ст. 159, `#0369a1` цифровой рубль, `#475569` подзаголовок, `#fefefe`–`#f0f9ff` фон |
| **Аудитория** | Обвиняемые и потерпевшие по хищениям; дропперы; владельцы цифровых кошельков; адвокаты по переквалификации 158/159 |

## Чеклист отличий от других hero

- [x] **Не Пленум № 48**: не мошенничество/крипто — угол **кража, гл. 21 УК, граница 158/159**
- [x] **Не КС № 43-П**: не госдоля в юрлице — **цифровой рубль как предмет кражи**
- [x] **Не СИП/ВПР**: не IP — тип статьи **UG, уголовное право**
- [x] **Не обзор ВС № 8**: не арбитраж/спецмеры — **Пленум ВС № 19 от 16.06.2026**
- [x] Уникальная сцена: цифровой кошелёк + весы ВС + развилка 158/159 + критерий тайного списания
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA в hero **не вставлять**

```html
<section id="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026" class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026" aria-label="Пленум ВС № 19 (2026): цифровой рубль как предмет кражи — когда обман это не мошенничество">
  <style>
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(158deg, #fefefe 0%, #f0f9ff 42%, #ecfeff 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 44% 36% at 88% 10%, rgba(3, 105, 161, 0.08) 0%, transparent 55%),
        radial-gradient(ellipse 38% 32% at 8% 88%, rgba(13, 148, 136, 0.07) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__inner {
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
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__badge {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      margin: 0 0 18px;
      padding: 8px 14px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.96);
      border: 1px solid rgba(15, 23, 42, 0.1);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: #334155;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #1e3a5f;
      flex-shrink: 0;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.38rem, 3vw, 2.1rem);
      line-height: 1.24;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__h1-accent {
      color: #1e3a5f;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--vs {
      border-color: #93c5fd;
      color: #1e3a5f;
      background: #eff6ff;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--theft {
      border-color: #5eead4;
      color: #0f766e;
      background: #f0fdfa;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--fraud {
      border-color: #fecaca;
      color: #991b1b;
      background: #fef2f2;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--ruble {
      border-color: #7dd3fc;
      color: #0369a1;
      background: #f0f9ff;
    }
    .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>
  <div class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__inner">
    <div class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__content">
      <div class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__badge">
        <span class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__badge-mark" aria-hidden="true"></span>
        UG · Пленум ВС № 19 · 16.06.2026 · цифровой рубль
      </div>
      <h1 class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__h1">
        <span class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__h1-accent">Пленум ВС № 19 (2026): цифровой рубль как предмет кражи — когда обман это не мошенничество</span>
      </h1>
      <p class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__sub">
        16 июня 2026: ВС РФ разъяснил квалификацию хищений цифровых активов, границу кражи и ст. 159, условия ст. 158.1
      </p>
      <ul class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__facts">
        <li class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--vs">Пленум ВС № 19 · 16.06.2026</li>
        <li class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--theft">ст. 158 — кража</li>
        <li class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--fraud">ст. 159 — мошенничество</li>
        <li class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__fact--ruble">цифровой рубль · ст. 158.1</li>
      </ul>
    </div>
    <div class="l24-hero-plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Цифровой кошелёк с рублём под весами Верховного суда: развилка квалификации — статья 158 кража или статья 159 мошенничество">
        <defs>
          <linearGradient id="hero-p19-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#f8fafc"/>
            <stop offset="100%" stop-color="#ecfeff"/>
          </linearGradient>
          <linearGradient id="hero-p19-vs" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a5f"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="hero-p19-wallet" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#e0f2fe"/>
            <stop offset="100%" stop-color="#cffafe"/>
          </linearGradient>
          <linearGradient id="hero-p19-ruble" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#0369a1"/>
            <stop offset="100%" stop-color="#0c4a6e"/>
          </linearGradient>
          <pattern id="hero-p19-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#f0f9ff"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#e0f2fe" stroke-width="0.5"/>
          </pattern>
          <filter id="hero-p19-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="4" stdDeviation="7" flood-color="#0f172a" flood-opacity="0.1"/>
          </filter>
          <marker id="hero-p19-arr-teal" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0 0 L6 3 L0 6 Z" fill="#0d9488"/>
          </marker>
          <marker id="hero-p19-arr-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0 0 L6 3 L0 6 Z" fill="#b91c1c"/>
          </marker>
        </defs>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-p19-bg)" stroke="#cbd5e1" stroke-width="1.2"/>
        <rect x="8" y="10" width="484" height="430" rx="18" fill="url(#hero-p19-grid)" opacity="0.4"/>
        <!-- фасад ВС -->
        <g filter="url(#hero-p19-shadow)" transform="translate(158, 6)">
          <rect x="0" y="38" width="184" height="50" rx="4" fill="url(#hero-p19-vs)"/>
          <polygon points="92,0 184,38 0,38" fill="#1e3a5f"/>
          <rect x="24" y="48" width="16" height="32" rx="1" fill="#334155" opacity="0.5"/>
          <rect x="52" y="48" width="16" height="32" rx="1" fill="#334155" opacity="0.5"/>
          <rect x="80" y="48" width="24" height="36" rx="1" fill="#475569" opacity="0.6"/>
          <rect x="116" y="48" width="16" height="32" rx="1" fill="#334155" opacity="0.5"/>
          <rect x="144" y="48" width="16" height="32" rx="1" fill="#334155" opacity="0.5"/>
          <text x="92" y="54" text-anchor="middle" fill="#e0f2fe" font-size="6" font-weight="800" letter-spacing="0.04em">ВЕРХОВНЫЙ СУД РФ</text>
          <text x="92" y="66" text-anchor="middle" fill="#93c5fd" font-size="5">Пленум № 19 · 16.06.2026</text>
          <text x="92" y="78" text-anchor="middle" fill="#7dd3fc" font-size="4.5">изменения в Пленум № 29 (2002)</text>
        </g>
        <!-- весы правосудия -->
        <g filter="url(#hero-p19-shadow)" transform="translate(206, 54)">
          <line x1="44" y1="10" x2="44" y2="30" stroke="#1e3a5f" stroke-width="2.2"/>
          <line x1="18" y1="14" x2="70" y2="14" stroke="#1e3a5f" stroke-width="2.4"/>
          <path d="M18 14 L10 28 L26 28 Z" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.2"/>
          <path d="M70 14 L62 28 L78 28 Z" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.2"/>
          <circle cx="10" cy="30" r="3.5" fill="#0d9488" opacity="0.9"/>
          <circle cx="26" cy="30" r="3.5" fill="#0d9488" opacity="0.9"/>
          <circle cx="62" cy="30" r="3.5" fill="#b91c1c" opacity="0.9"/>
          <circle cx="78" cy="30" r="3.5" fill="#b91c1c" opacity="0.9"/>
          <text x="18" y="38" text-anchor="middle" fill="#0f766e" font-size="4" font-weight="800">ст. 158</text>
          <text x="70" y="38" text-anchor="middle" fill="#991b1b" font-size="4" font-weight="800">ст. 159</text>
        </g>
        <!-- цифровой кошелёк -->
        <g filter="url(#hero-p19-shadow)" transform="translate(168, 118)">
          <rect width="164" height="108" rx="14" fill="url(#hero-p19-wallet)" stroke="#7dd3fc" stroke-width="1.5"/>
          <rect x="12" y="10" width="140" height="88" rx="10" fill="#fff" stroke="#e2e8f0" stroke-width="1"/>
          <!-- экран смартфона -->
          <rect x="20" y="18" width="124" height="72" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="0.8"/>
          <text x="82" y="30" text-anchor="middle" fill="#64748b" font-size="4.5" font-weight="700">ЦИФРОВОЙ КОШЕЛЁК</text>
          <!-- монета цифрового рубля -->
          <circle cx="82" cy="58" r="22" fill="url(#hero-p19-ruble)" stroke="#0369a1" stroke-width="1.5"/>
          <text x="82" y="64" text-anchor="middle" fill="#e0f2fe" font-size="18" font-weight="900">₽</text>
          <text x="82" y="78" text-anchor="middle" fill="#0369a1" font-size="4" font-weight="700">цифровой рубль</text>
          <!-- стрелка списания -->
          <path d="M108 52 L128 52" stroke="#b91c1c" stroke-width="1.5" stroke-dasharray="3 2" marker-end="url(#hero-p19-arr-red)"/>
          <text x="136" y="54" fill="#991b1b" font-size="3.5" font-weight="700">−</text>
        </g>
        <!-- развилка 158 / 159 -->
        <g filter="url(#hero-p19-shadow)" transform="translate(36, 248)">
          <text x="214" y="0" text-anchor="middle" fill="#1e3a5f" font-size="5.5" font-weight="800">КРИТЕРИЙ ПЛЕНУМА: ОБМАН ТОЛЬКО ДЛЯ ДОСТУПА</text>
          <!-- центральный столб -->
          <circle cx="214" cy="28" r="10" fill="#1e3a5f"/>
          <text x="214" y="31" text-anchor="middle" fill="#fff" font-size="5" font-weight="900">?</text>
          <!-- ветка влево — кража -->
          <path d="M204 34 L80 70" fill="none" stroke="#0d9488" stroke-width="2.2" marker-end="url(#hero-p19-arr-teal)"/>
          <rect x="8" y="62" width="128" height="58" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.2"/>
          <text x="72" y="78" text-anchor="middle" fill="#0f766e" font-size="5.5" font-weight="800">ст. 158 — КРАЖА</text>
          <text x="72" y="90" text-anchor="middle" fill="#334155" font-size="4">обман → доступ</text>
          <text x="72" y="100" text-anchor="middle" fill="#334155" font-size="4">тайное списание</text>
          <text x="72" y="112" text-anchor="middle" fill="#0d9488" font-size="3.5" font-weight="600">п. 2, п. 25.1 Пленума</text>
          <!-- ветка вправо — мошенничество -->
          <path d="M224 34 L348 70" fill="none" stroke="#b91c1c" stroke-width="2.2" marker-end="url(#hero-p19-arr-red)"/>
          <rect x="292" y="62" width="128" height="58" rx="8" fill="#fef2f2" stroke="#b91c1c" stroke-width="1.2"/>
          <text x="356" y="78" text-anchor="middle" fill="#991b1b" font-size="5.5" font-weight="800">ст. 159 — ОБМАН</text>
          <text x="356" y="90" text-anchor="middle" fill="#334155" font-size="4">потерпевший сам</text>
          <text x="356" y="100" text-anchor="middle" fill="#334155" font-size="4">передал деньги</text>
          <text x="356" y="112" text-anchor="middle" fill="#b91c1c" font-size="3.5" font-weight="600">обман = способ завладения</text>
        </g>
        <!-- блок цифровых активов -->
        <g filter="url(#hero-p19-shadow)" transform="translate(36, 338)">
          <rect width="200" height="56" rx="8" fill="#fff" stroke="#0369a1" stroke-width="1"/>
          <text x="100" y="16" text-anchor="middle" fill="#0369a1" font-size="5" font-weight="800">ПРЕДМЕТ ХИЩЕНИЯ (п. 11)</text>
          <text x="100" y="28" text-anchor="middle" fill="#334155" font-size="4">цифровой рубль · цифровые права</text>
          <text x="100" y="38" text-anchor="middle" fill="#64748b" font-size="3.8">безналичные ДС · цифровая валюта</text>
          <text x="100" y="48" text-anchor="middle" fill="#64748b" font-size="3.5">окончание = момент списания (п. 6)</text>
        </g>
        <!-- блок ст. 158.1 -->
        <g filter="url(#hero-p19-shadow)" transform="translate(256, 338)">
          <rect width="216" height="56" rx="8" fill="#fff" stroke="#0d9488" stroke-width="1"/>
          <text x="108" y="16" text-anchor="middle" fill="#0f766e" font-size="5" font-weight="800">ст. 158.1 — МЕЛКОЕ ХИЩЕНИЕ</text>
          <text x="108" y="28" text-anchor="middle" fill="#334155" font-size="4">≤ 2 500 ₽ · повтор после КоАП</text>
          <text x="108" y="38" text-anchor="middle" fill="#64748b" font-size="3.8">4 проверки суда (п. 17.1)</text>
          <text x="108" y="48" text-anchor="middle" fill="#64748b" font-size="3.5">адм. дело ≠ преюдиция для УК</text>
        </g>
        <text x="250" y="438" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">Пленум № 19 · цифровой кошелёк · весы 158/159 · тайное списание vs перевод</text>
      </svg>
    </div>
  </div>
</section>
```

## Передача Наташе
SLUG: plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>` и CTA в hero.
