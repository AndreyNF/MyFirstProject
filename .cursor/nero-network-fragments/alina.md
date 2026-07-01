=== АЛИНА (HERO) ===
Статус: ✅ ГОТОВО

**Hero id / class:** `l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026`

## Паспорт мира

| Параметр | Значение |
|----------|----------|
| **Мир** | «Весы субсидиарной ответственности» — банкротная среда 2025–2026: КДЛ под давлением кредиторов и ФНС, Пленум № 42 меняет правила расчёта размера СО, щит защиты директора и учредителя |
| **Центральная метафора** | Здание Верховного суда с бейджем «42» (Пленум); весы правосудия (долги vs защита); три колонки КДЛ (директор, учредитель, наследники); щит с инструментами защиты; три факт-блока внизу |
| **Пространство** | Тёплый кремово-янтарный градиент «правовой документ / арбитражный зал»; SVG — фасад ВС, весы, три КДЛ-карточки, бирюзовый щит защиты, блоки фактов |
| **Движение** | Полностью static — без `<canvas>`, `<script>` и CSS-анимаций |
| **Палитра** | `#0f172a` текст, `#1e3a5f` ВС/суд, `#b45309`/`#92400e` банкротство/долги, `#0d9488` защита/щит, `#0369a1` учредитель, `#7c3aed` наследники, `#dc2626` исключения, `#fefefe`–`#fff7ed` фон |
| **Аудитория** | Директора и учредители под угрозой субсидиарки; бенефициары ООО; адвокаты по банкротству; арбитражные управляющие; кредиторы по банкротным делам |

## Чеклист отличий от других hero

- [x] **Не Пленум № 19**: не цифровой рубль/кража — угол **ARB, субсидиарная ответственность при банкротстве**
- [x] **Не Пленум № 53**: это hero к статье о **Пленуме № 42 (23.12.2025)** — первом системном обновлении Пленума 53 за 8 лет
- [x] **Не СИП/ВПР**: не IP — тип статьи **ARB, арбитраж при банкротстве**
- [x] **Не обзор ВС № 8**: не спецмеры — **Пленум ВС № 42 от 23.12.2025**
- [x] Уникальная сцена: суд с бейджем «42» + весы СО + три КДЛ-карточки + щит защиты + блоки фактов (размер СО, штрафы ФНС, наследники)
- [x] Тёплый янтарный фон — отличается от холодного синего UG-hero Пленума № 19
- [x] Без `<canvas>` и `<script>` — только inline CSS + static SVG
- [x] CTA в hero **не вставлять**

```html
<section id="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026" class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026" aria-label="Пленум ВС № 42 — новые правила субсидиарной ответственности в банкротстве 2025–2026: защита директора и учредителя">
  <style>
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026 {
      position: relative;
      min-height: 88vh;
      min-height: 88dvh;
      box-sizing: border-box;
      display: flex;
      align-items: center;
      padding: 112px 24px 72px;
      background: linear-gradient(158deg, #fefefe 0%, #fffbf5 42%, #fff7ed 100%);
      color: #0f172a;
      font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
      overflow: hidden;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026::before {
      content: "";
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 44% 36% at 88% 10%, rgba(180, 83, 9, 0.07) 0%, transparent 55%),
        radial-gradient(ellipse 38% 32% at 8% 88%, rgba(13, 148, 136, 0.06) 0%, transparent 52%);
      pointer-events: none;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__inner {
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
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__badge {
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
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__badge-mark {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #b45309;
      flex-shrink: 0;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__h1 {
      margin: 0 0 18px;
      font-size: clamp(1.38rem, 3vw, 2.1rem);
      line-height: 1.24;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__h1-accent {
      color: #1e3a5f;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__sub {
      margin: 0 0 26px;
      max-width: 42em;
      font-size: clamp(0.98rem, 1.48vw, 1.1rem);
      line-height: 1.58;
      color: #475569;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__facts {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin: 0;
      padding: 0;
      list-style: none;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact {
      font-size: 0.76rem;
      font-weight: 700;
      padding: 7px 12px;
      border-radius: 8px;
      background: #fff;
      border: 1px solid #e2e8f0;
      color: #334155;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--court {
      border-color: #93c5fd;
      color: #1e3a5f;
      background: #eff6ff;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--dir {
      border-color: #fcd34d;
      color: #78350f;
      background: #fffbeb;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--found {
      border-color: #fca5a5;
      color: #b91c1c;
      background: #fef2f2;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--fns {
      border-color: #5eead4;
      color: #0f766e;
      background: #f0fdfa;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--heirs {
      border-color: #c4b5fd;
      color: #5b21b6;
      background: #f5f3ff;
    }
    .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__visual {
      display: flex;
      justify-content: center;
      align-items: center;
    }
    @media (max-width: 900px) {
      .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026 {
        min-height: auto;
        padding: 96px 20px 56px;
      }
      .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__inner {
        grid-template-columns: 1fr;
        gap: 30px;
      }
      .l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__visual {
        order: -1;
        max-height: 320px;
      }
    }
  </style>

  <div class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__inner">

    <!-- Текстовый блок -->
    <div class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__content">
      <div class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__badge">
        <span class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__badge-mark" aria-hidden="true"></span>
        ARB · Пленум ВС № 42 · 23.12.2025 · субсидиарная ответственность при банкротстве
      </div>
      <h1 class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__h1">
        <span class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__h1-accent">Пленум ВС&nbsp;№&nbsp;42 (2025–2026): новые правила субсидиарной ответственности в&nbsp;банкротстве — защита директора и&nbsp;учредителя</span>
      </h1>
      <p class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__sub">
        Размер ответственности, штрафы ФНС, презумпции вины и тактика в арбитраже
      </p>
      <ul class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__facts">
        <li class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--court">Пленум ВС&nbsp;№&nbsp;42 · 23.12.2025</li>
        <li class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--dir">субсидиарная ответственность директора</li>
        <li class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--found">субсидиарная ответственность учредителя</li>
        <li class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--fns">штрафы ФНС исключены · КС&nbsp;50-П</li>
        <li class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__fact--heirs">наследники КДЛ · пп.&nbsp;37¹–37⁵</li>
      </ul>
    </div>

    <!-- SVG визуализация -->
    <div class="l24-hero-plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026__visual" aria-hidden="true">
      <svg viewBox="0 0 500 450" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Пленум ВС № 42 по субсидиарной ответственности: здание суда с бейджем 42, весы баланса долгов и защиты, три категории КДЛ и бирюзовый щит с инструментами защиты директора">

        <defs>
          <linearGradient id="arb42-bg" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#fffdf8"/>
            <stop offset="100%" stop-color="#fff7ed"/>
          </linearGradient>
          <linearGradient id="arb42-court" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#1e3a5f"/>
            <stop offset="100%" stop-color="#0f172a"/>
          </linearGradient>
          <linearGradient id="arb42-debt" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#fef3c7"/>
            <stop offset="100%" stop-color="#fde68a"/>
          </linearGradient>
          <linearGradient id="arb42-prot" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="#ccfbf1"/>
            <stop offset="100%" stop-color="#99f6e4"/>
          </linearGradient>
          <linearGradient id="arb42-shield-g" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%" stop-color="#0d9488"/>
            <stop offset="100%" stop-color="#0f766e"/>
          </linearGradient>
          <pattern id="arb42-grid" width="20" height="20" patternUnits="userSpaceOnUse">
            <rect width="20" height="20" fill="#fffdf8"/>
            <path d="M20 0 L0 0 0 20" fill="none" stroke="#fde68a" stroke-width="0.35" opacity="0.45"/>
          </pattern>
          <filter id="arb42-shadow" x="-10%" y="-10%" width="120%" height="120%">
            <feDropShadow dx="0" dy="3" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.09"/>
          </filter>
          <marker id="arb42-arr-amber" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0 0 L6 3 L0 6 Z" fill="#b45309"/>
          </marker>
          <marker id="arb42-arr-teal" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
            <path d="M0 0 L6 3 L0 6 Z" fill="#0d9488"/>
          </marker>
        </defs>

        <!-- Фон SVG -->
        <rect x="8" y="8" width="484" height="434" rx="18" fill="url(#arb42-bg)" stroke="#e8dfc0" stroke-width="1.2"/>
        <rect x="8" y="8" width="484" height="434" rx="18" fill="url(#arb42-grid)" opacity="0.55"/>

        <!-- ЗДАНИЕ ВЕРХОВНОГО СУДА -->
        <g filter="url(#arb42-shadow)" transform="translate(157,5)">
          <!-- Фронтон (треугольная крыша) -->
          <polygon points="93,0 186,42 0,42" fill="#1e3a5f"/>
          <!-- Бейдж «42» на фронтоне -->
          <circle cx="93" cy="18" r="14" fill="#b45309"/>
          <text x="93" y="23" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="900">42</text>
          <!-- Корпус здания -->
          <rect x="0" y="42" width="186" height="50" rx="3" fill="url(#arb42-court)"/>
          <!-- Колонны -->
          <rect x="12" y="46" width="10" height="36" rx="1" fill="#334155" opacity="0.55"/>
          <rect x="30" y="46" width="10" height="36" rx="1" fill="#334155" opacity="0.55"/>
          <rect x="50" y="46" width="16" height="40" rx="1" fill="#475569" opacity="0.60"/>
          <rect x="80" y="48" width="10" height="38" rx="1" fill="#475569" opacity="0.65"/>
          <rect x="96" y="48" width="10" height="38" rx="1" fill="#475569" opacity="0.65"/>
          <rect x="120" y="46" width="16" height="40" rx="1" fill="#475569" opacity="0.60"/>
          <rect x="148" y="46" width="10" height="36" rx="1" fill="#334155" opacity="0.55"/>
          <rect x="166" y="46" width="10" height="36" rx="1" fill="#334155" opacity="0.55"/>
          <!-- Надписи в здании -->
          <text x="93" y="57" text-anchor="middle" fill="#e0f2fe" font-size="5.8" font-weight="800" letter-spacing="0.04em">ВЕРХОВНЫЙ СУД РФ</text>
          <text x="93" y="69" text-anchor="middle" fill="#93c5fd" font-size="5">Пленум № 42 · 23.12.2025</text>
          <text x="93" y="81" text-anchor="middle" fill="#7dd3fc" font-size="4.5">первое системное обновление Пленума № 53 за 8 лет</text>
        </g>

        <!-- ВЕСЫ ПРАВОСУДИЯ / БАЛАНС СО -->
        <g transform="translate(175,105)">
          <!-- Заголовок весов -->
          <text x="75" y="0" text-anchor="middle" fill="#1e3a5f" font-size="5.2" font-weight="800" letter-spacing="0.02em">ВЕСЫ БАЛАНСА · РАЗМЕР ОТВЕТСТВЕННОСТИ</text>
          <!-- Центральная стойка весов -->
          <line x1="75" y1="8" x2="75" y2="44" stroke="#1e3a5f" stroke-width="2.5"/>
          <!-- Поворотный шарнир -->
          <circle cx="75" cy="44" r="4" fill="#b45309"/>
          <!-- Горизонтальная балка -->
          <line x1="10" y1="14" x2="140" y2="14" stroke="#1e3a5f" stroke-width="2.8"/>
          <!-- Левое плечо: ДОЛГИ (янтарный) -->
          <line x1="10" y1="14" x2="10" y2="32" stroke="#92400e" stroke-width="1.6"/>
          <rect x="-16" y="32" width="52" height="30" rx="5" fill="url(#arb42-debt)" stroke="#b45309" stroke-width="1.5"/>
          <text x="10" y="44" text-anchor="middle" fill="#78350f" font-size="4.8" font-weight="800">ДОЛГИ</text>
          <text x="10" y="54" text-anchor="middle" fill="#92400e" font-size="4.2">реестр кредиторов</text>
          <!-- Правое плечо: ЗАЩИТА (бирюзовый) -->
          <line x1="140" y1="14" x2="140" y2="32" stroke="#0d9488" stroke-width="1.6"/>
          <rect x="116" y="32" width="52" height="30" rx="5" fill="url(#arb42-prot)" stroke="#0d9488" stroke-width="1.5"/>
          <text x="140" y="44" text-anchor="middle" fill="#065f46" font-size="4.8" font-weight="800">ЗАЩИТА</text>
          <text x="140" y="54" text-anchor="middle" fill="#0f766e" font-size="4.2">аргументы КДЛ</text>
        </g>

        <!-- КДЛ: три категории (левая колонка) -->
        <g filter="url(#arb42-shadow)" transform="translate(18,172)">
          <text x="74" y="0" text-anchor="middle" fill="#1e3a5f" font-size="5.5" font-weight="800">КТО НЕСЁТ СУБСИДИАРКУ</text>

          <!-- Карточка 1: Директор (янтарный) -->
          <rect x="0" y="8" width="144" height="38" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.5"/>
          <circle cx="15" cy="27" r="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.2"/>
          <text x="15" y="31" text-anchor="middle" fill="#b45309" font-size="9" font-weight="800">Д</text>
          <text x="82" y="22" text-anchor="middle" fill="#0f172a" font-size="5.2" font-weight="700">ДИРЕКТОР ООО</text>
          <text x="82" y="32" text-anchor="middle" fill="#64748b" font-size="4.2">ст. 61.11 · доведение до банкротства</text>
          <text x="82" y="42" text-anchor="middle" fill="#b45309" font-size="4" font-weight="600">молчание = перенос бремени (п. 56¹)</text>

          <!-- Карточка 2: Учредитель (синий) -->
          <rect x="0" y="54" width="144" height="38" rx="8" fill="#ffffff" stroke="#0369a1" stroke-width="1.5"/>
          <circle cx="15" cy="73" r="10" fill="#e0f2fe" stroke="#0369a1" stroke-width="1.2"/>
          <text x="15" y="77" text-anchor="middle" fill="#0369a1" font-size="9" font-weight="800">У</text>
          <text x="82" y="68" text-anchor="middle" fill="#0f172a" font-size="5.2" font-weight="700">УЧРЕДИТЕЛЬ (УЧАСТНИК)</text>
          <text x="82" y="78" text-anchor="middle" fill="#64748b" font-size="4.2">одобрял сделки · пп. 22¹–22² — индив.</text>
          <text x="82" y="88" text-anchor="middle" fill="#0369a1" font-size="4" font-weight="600">снижение с 40 млн до 8 млн (практика)</text>

          <!-- Карточка 3: Наследники / Номинал (фиолетовый) -->
          <rect x="0" y="100" width="144" height="38" rx="8" fill="#ffffff" stroke="#7c3aed" stroke-width="1.5"/>
          <circle cx="15" cy="119" r="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.2"/>
          <text x="15" y="123" text-anchor="middle" fill="#7c3aed" font-size="8" font-weight="800">Н</text>
          <text x="82" y="114" text-anchor="middle" fill="#0f172a" font-size="5.2" font-weight="700">НАСЛЕДНИКИ / НОМИНАЛ</text>
          <text x="82" y="124" text-anchor="middle" fill="#64748b" font-size="4.2">пп. 37¹–37⁵ · в пределах наследства</text>
          <text x="82" y="134" text-anchor="middle" fill="#7c3aed" font-size="4" font-weight="600">раскрытие бенефициара снижает СО</text>
        </g>

        <!-- ЩИТ ЗАЩИТЫ КДЛ (правая колонка) -->
        <g filter="url(#arb42-shadow)" transform="translate(336,170)">
          <!-- Форма щита (геральдический пятиугольник) -->
          <path d="M72 0 L144 28 L144 88 L72 132 L0 88 L0 28 Z" fill="url(#arb42-shield-g)" stroke="#0f766e" stroke-width="1.5" opacity="0.97"/>
          <!-- Внутренний контур блика -->
          <path d="M72 6 L138 32 L138 85 L72 126 L6 85 L6 32 Z" fill="none" stroke="rgba(255,255,255,0.16)" stroke-width="1"/>
          <!-- Заголовок щита -->
          <text x="72" y="30" text-anchor="middle" fill="#ffffff" font-size="6.2" font-weight="900" letter-spacing="0.04em">ЗАЩИТА КДЛ</text>
          <text x="72" y="42" text-anchor="middle" fill="#ccfbf1" font-size="5.2" font-weight="700">Пленум № 42 · 2026</text>
          <line x1="16" y1="48" x2="128" y2="48" stroke="rgba(255,255,255,0.25)" stroke-width="0.8"/>
          <!-- Инструменты защиты -->
          <text x="72" y="60" text-anchor="middle" fill="#e0fdf4" font-size="4.2">✓ предпринимат. риск (п. 1)</text>
          <text x="72" y="71" text-anchor="middle" fill="#e0fdf4" font-size="4.2">✓ штрафы ФНС исключены (п. 26¹)</text>
          <text x="72" y="82" text-anchor="middle" fill="#e0fdf4" font-size="4.2">✓ инд-ия вины органа (пп. 22¹–22²)</text>
          <text x="72" y="93" text-anchor="middle" fill="#e0fdf4" font-size="4.2">✓ ранний вход в дело (п. 26¹⁰)</text>
          <text x="72" y="104" text-anchor="middle" fill="#e0fdf4" font-size="4.2">✓ обеспечит. меры (п. 36¹)</text>
        </g>

        <!-- НИЖНИЕ ФАКТ-БЛОКИ (три в ряд) -->

        <!-- Блок А: Размер СО -->
        <g filter="url(#arb42-shadow)" transform="translate(18,316)">
          <rect x="0" y="0" width="149" height="70" rx="8" fill="#ffffff" stroke="#1e3a5f" stroke-width="1.2"/>
          <rect x="0" y="0" width="149" height="20" rx="8" fill="#1e3a5f"/>
          <rect x="0" y="12" width="149" height="8" fill="#1e3a5f"/>
          <text x="74" y="14" text-anchor="middle" fill="#e0f2fe" font-size="5" font-weight="800">РАЗМЕР СО · пп. 26¹–26¹¹</text>
          <text x="74" y="30" text-anchor="middle" fill="#334155" font-size="4.3">включается: реестр + текущие</text>
          <text x="74" y="40" text-anchor="middle" fill="#334155" font-size="4.3">+ зареестровые + мораторные %</text>
          <text x="74" y="52" text-anchor="middle" fill="#dc2626" font-size="4.2">исключения: аффил. лица,</text>
          <text x="74" y="62" text-anchor="middle" fill="#dc2626" font-size="4.2">«осведомлённые» кредиторы</text>
        </g>

        <!-- Блок Б: Штрафы ФНС исключены -->
        <g filter="url(#arb42-shadow)" transform="translate(175,316)">
          <rect x="0" y="0" width="150" height="70" rx="8" fill="#ffffff" stroke="#b45309" stroke-width="1.2"/>
          <rect x="0" y="0" width="150" height="20" rx="8" fill="#b45309"/>
          <rect x="0" y="12" width="150" height="8" fill="#b45309"/>
          <text x="75" y="14" text-anchor="middle" fill="#ffffff" font-size="5" font-weight="800">ФНС: ШТРАФЫ ИСКЛЮЧЕНЫ</text>
          <text x="75" y="30" text-anchor="middle" fill="#334155" font-size="4.3">п. 26¹ прямо закрепил:</text>
          <text x="75" y="40" text-anchor="middle" fill="#92400e" font-size="4.5" font-weight="700">штрафы за нал. правонарушения</text>
          <text x="75" y="50" text-anchor="middle" fill="#92400e" font-size="4.5" font-weight="700">НЕ входят в размер СО</text>
          <text x="75" y="62" text-anchor="middle" fill="#64748b" font-size="4.2">КС РФ № 50-П · 30.10.2023</text>
        </g>

        <!-- Блок В: Наследники КДЛ -->
        <g filter="url(#arb42-shadow)" transform="translate(333,316)">
          <rect x="0" y="0" width="149" height="70" rx="8" fill="#ffffff" stroke="#0d9488" stroke-width="1.2"/>
          <rect x="0" y="0" width="149" height="20" rx="8" fill="#0d9488"/>
          <rect x="0" y="12" width="149" height="8" fill="#0d9488"/>
          <text x="74" y="14" text-anchor="middle" fill="#ffffff" font-size="5" font-weight="800">НАСЛЕДНИКИ КДЛ</text>
          <text x="74" y="30" text-anchor="middle" fill="#334155" font-size="4.3">пп. 37¹–37⁵ Пленума 42:</text>
          <text x="74" y="40" text-anchor="middle" fill="#0f172a" font-size="4.5">ответственность только</text>
          <text x="74" y="50" text-anchor="middle" fill="#0f172a" font-size="4.5">в пределах стоимости наследства</text>
          <text x="74" y="62" text-anchor="middle" fill="#64748b" font-size="4.2">А41-29270/2021 · АСМО · янв. 2026</text>
        </g>

        <!-- ЦИТАТА ЭКСПЕРТА -->
        <g transform="translate(18,398)">
          <rect x="0" y="0" width="462" height="40" rx="8" fill="rgba(30,58,95,0.05)" stroke="#1e3a5f" stroke-width="0.8" stroke-dasharray="4 2"/>
          <text x="231" y="14" text-anchor="middle" fill="#1e3a5f" font-size="4.8" font-weight="700">«Это первое системное обновление разъяснений по субсидиарной ответственности КДЛ за восемь лет.»</text>
          <text x="231" y="26" text-anchor="middle" fill="#475569" font-size="4.5">— Антон Пуляев, ADVOLAW (ГАРАНТ, 29.05.2026)</text>
          <text x="231" y="37" text-anchor="middle" fill="#94a3b8" font-size="4">ARB · арбитраж при банкротстве · субсидиарная ответственность директора и учредителя · Legis24</text>
        </g>

        <!-- ПОДПИСЬ ВНИЗУ SVG -->
        <text x="250" y="446" text-anchor="middle" fill="#b8a487" font-size="6.5" font-weight="600">Пленум № 42 · Пленум № 53 · КДЛ · субсидиарная ответственность · банкротство 2025–2026</text>

      </svg>
    </div>
  </div>
</section>
```

## Передача пайплайну

SLUG: plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026
H1_для_hero: Пленум ВС № 42 (2025–2026): новые правила субсидиарной ответственности в банкротстве — защита директора и учредителя
ПОДЗАГОЛОВОК_HERO: Размер ответственности, штрафы ФНС, презумпции вины и тактика в арбитраже
ТИП_СТАТЬИ: ARB — арбитраж при банкротстве
СЛЕДУЮЩИЙ_ШАГ: Наташа (сборка + публикация)
ВНИМАНИЕ: hero — static SVG + inline CSS, без `<canvas>`, `<script>` и CTA в hero.
