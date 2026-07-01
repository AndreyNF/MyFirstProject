=== БОРИС (БЛОК СТАТЬИ, НЕ HERO) ===
Статус: ✅ ГОТОВО
ЯКОРЬ: l24-boris-plenum42-size

## Паспорт блока

| Параметр | Значение |
|----------|----------|
| **Статья** | Пленум ВС № 42 — субсидиарная ответственность при банкротстве |
| **SLUG** | `plenum-vs-42-subsidiarnaya-otvetstvennost-bankrotstvo-2026` |
| **Якорь** | `l24-boris-plenum42-size` |
| **Тема** | Схема «Размер СО»: что включается / не включается (штрафы ФНС, реестр, текущие платежи) |
| **Размещение** | В теле статьи под H2 «Как определяется размер субсидиарной ответственности» |
| **Режим** | MCP-only: только inline CSS + SVG, без `<canvas>` и `<script>` |
| **Палитра** | Тёмный navy `#060f1e`–`#0f2244`; включено: emerald `#059669`; исключено: crimson `#dc2626`; штрафы ФНС: orange `#ea580c`; центр: amber `#d97706` |

```html
<section id="l24-boris-plenum42-size" class="bsp42" aria-label="Схема: размер субсидиарной ответственности — что включается и что нет, Пленум ВС № 42">
<style>
.bsp42{
  --bg0:#060f1e;--bg1:#0b1c36;--bg2:#0f2244;
  --inc:#059669;--incs:#6ee7b7;--incp:rgba(5,150,105,.14);
  --exc:#dc2626;--excs:#fca5a5;--excp:rgba(220,38,38,.14);
  --acc:#d97706;--acc2:#f59e0b;--accs:#fde68a;
  --ks:#ea580c;--ks2:#f97316;--kss:#fdba74;--ksp:rgba(234,88,12,.15);
  --txt:#e2e8f0;--mut:#94a3b8;--brd:rgba(255,255,255,.1);
  margin:48px 0;
  font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
}
.bsp42__shell{
  background:linear-gradient(145deg,var(--bg0) 0%,var(--bg1) 52%,var(--bg2) 100%);
  border:1px solid rgba(15,34,68,.8);
  border-radius:16px;
  padding:32px 28px 24px;
  box-shadow:0 20px 54px rgba(6,15,30,.52);
  color:var(--txt);
}
.bsp42__ew{
  margin:0 0 8px;
  font-size:.69rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--acc2);
}
.bsp42__h3{
  margin:0 0 10px;
  font-size:clamp(1.08rem,2.2vw,1.36rem);line-height:1.22;
  color:#fff;font-weight:700;
}
.bsp42__lead{
  margin:0 0 24px;
  font-size:.92rem;line-height:1.56;color:var(--mut);max-width:82ch;
}
.bsp42__lead strong{color:#fff;}
.bsp42__svg{display:block;width:100%;height:auto;margin-bottom:22px;}
.bsp42__cols{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:18px;}
.bsp42__col{border-radius:10px;padding:18px 16px;}
.bsp42__col--in{background:var(--incp);border:1px solid rgba(5,150,105,.32);}
.bsp42__col--out{background:var(--excp);border:1px solid rgba(220,38,38,.32);}
.bsp42__col-hd{
  margin:0 0 12px;
  font-size:.71rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase;
}
.bsp42__col--in .bsp42__col-hd{color:var(--incs);}
.bsp42__col--out .bsp42__col-hd{color:var(--excs);}
.bsp42__ul{margin:0;padding:0;list-style:none;display:flex;flex-direction:column;gap:9px;}
.bsp42__ul>li{font-size:.78rem;line-height:1.44;color:var(--mut);}
.bsp42__ul>li:not(.bsp42__li-ks){padding-left:16px;position:relative;}
.bsp42__ul>li:not(.bsp42__li-ks)::before{position:absolute;left:0;font-weight:800;}
.bsp42__col--in .bsp42__ul>li:not(.bsp42__li-ks)::before{content:"✓";color:var(--incs);}
.bsp42__col--out .bsp42__ul>li:not(.bsp42__li-ks)::before{content:"✕";color:var(--excs);}
.bsp42__ul>li strong{color:var(--txt);}
.bsp42__ul>li small{display:block;font-size:.67rem;margin-top:3px;font-weight:600;opacity:.85;}
.bsp42__li-ks{
  background:var(--ksp);
  border:1px solid rgba(234,88,12,.38);
  border-radius:8px;
  padding:10px 12px;
}
.bsp42__ks-ico{color:var(--kss);font-weight:800;margin-right:4px;}
.bsp42__ks-tag{
  display:inline-block;font-size:.62rem;font-weight:800;
  text-transform:uppercase;letter-spacing:.05em;
  background:rgba(234,88,12,.3);border:1px solid var(--ks2);color:var(--kss);
  border-radius:4px;padding:2px 6px;margin-right:5px;
}
.bsp42__ks-box{
  display:flex;flex-wrap:wrap;gap:14px;align-items:flex-start;
  background:var(--ksp);border:1px solid rgba(234,88,12,.38);
  border-radius:10px;padding:16px 18px;margin-bottom:16px;
}
.bsp42__ks-lbl{
  display:inline-block;white-space:nowrap;
  font-size:.67rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;
  background:rgba(234,88,12,.25);border:1px solid var(--ks2);color:var(--kss);
  border-radius:6px;padding:5px 10px;flex-shrink:0;
}
.bsp42__ks-p{margin:0;font-size:.79rem;line-height:1.53;color:var(--mut);flex:1;min-width:180px;}
.bsp42__ks-p strong{color:var(--kss);}
.bsp42__foot{
  display:flex;flex-wrap:wrap;gap:7px;
  margin-top:14px;padding-top:14px;border-top:1px solid var(--brd);
}
.bsp42__tag{
  font-size:.7rem;font-weight:600;padding:5px 10px;border-radius:999px;
  background:rgba(255,255,255,.05);color:var(--txt);border:1px solid rgba(255,255,255,.13);
}
.bsp42__tag--a{border-color:rgba(217,119,6,.5);color:var(--accs);}
.bsp42__tag--i{border-color:rgba(5,150,105,.5);color:var(--incs);}
.bsp42__tag--e{border-color:rgba(220,38,38,.5);color:var(--excs);}
.bsp42__tag--k{border-color:rgba(234,88,12,.5);color:var(--kss);}
@media(max-width:740px){
  .bsp42__cols{grid-template-columns:1fr;}
  .bsp42__shell{padding:24px 18px 20px;}
}
</style>

<div class="bsp42__shell">
  <p class="bsp42__ew">ARB · Пленум ВС № 42 · 23.12.2025 · пп. 26¹–26¹¹ Пленума ВС № 53</p>
  <h3 class="bsp42__h3">Размер субсидиарной ответственности: что включается и что нет — схема по п. 26¹</h3>
  <p class="bsp42__lead">Пленум № 42 создал единый раздел «Размер СО» (пп. 26¹–26¹¹). Главное правило: <strong>штрафы ФНС за налоговые правонарушения прямо исключены</strong> — позиция КС РФ № 50-П стала обязательной нормой для всех судов с 23.12.2025.</p>

  <svg class="bsp42__svg" viewBox="0 0 720 232" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="b42t b42d">
    <title id="b42t">Схема: размер субсидиарной ответственности по Пленуму ВС № 42</title>
    <desc id="b42d">Что включается (реестровые, зареестровые, текущие платежи, санкции без штрафов ФНС, мораторные проценты) и что не включается (штрафы ФНС — КС 50-П, аффилированные, осведомлённые кредиторы, без причинно-следственной связи) в размер субсидиарной ответственности — пп. 26¹–26¹¹ Пленума ВС № 53 в редакции Пленума № 42</desc>
    <defs>
      <linearGradient id="b42gctr" x1="0" y1="0" x2="1" y2="1" gradientUnits="objectBoundingBox">
        <stop offset="0%" stop-color="#0c1e42"/>
        <stop offset="100%" stop-color="#07121f"/>
      </linearGradient>
      <marker id="b42mg" markerWidth="8" markerHeight="7" refX="7" refY="3.5" orient="auto">
        <polygon points="0 0, 8 3.5, 0 7" fill="#10b981"/>
      </marker>
    </defs>

    <!-- ===== ЛЕВАЯ ЧАСТЬ: ВКЛЮЧАЕТСЯ (x=8–226) ===== -->
    <rect x="8" y="16" width="218" height="33" rx="7" fill="rgba(5,150,105,.17)" stroke="#10b981" stroke-width="1.3"/>
    <text x="19" y="29" fill="#6ee7b7" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✓</text>
    <text x="31" y="29" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Реестровые требования кредиторов</text>
    <text x="31" y="42" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">1–3 очередь · основная база СО</text>

    <rect x="8" y="58" width="218" height="33" rx="7" fill="rgba(5,150,105,.17)" stroke="#10b981" stroke-width="1.3"/>
    <text x="19" y="71" fill="#6ee7b7" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✓</text>
    <text x="31" y="71" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Зареестровые требования</text>
    <text x="31" y="84" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">заявленные после закрытия реестра</text>

    <rect x="8" y="100" width="218" height="33" rx="7" fill="rgba(5,150,105,.17)" stroke="#10b981" stroke-width="1.3"/>
    <text x="19" y="113" fill="#6ee7b7" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✓</text>
    <text x="31" y="113" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Текущие платежи</text>
    <text x="31" y="126" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">ст. 5 Закона о банкротстве</text>

    <rect x="8" y="142" width="218" height="33" rx="7" fill="rgba(5,150,105,.17)" stroke="#10b981" stroke-width="1.3"/>
    <text x="19" y="155" fill="#6ee7b7" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✓</text>
    <text x="31" y="155" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Санкции за публичные нарушения</text>
    <text x="31" y="168" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">кроме штрафов ФНС · п. 26¹</text>

    <rect x="8" y="184" width="218" height="33" rx="7" fill="rgba(5,150,105,.17)" stroke="#10b981" stroke-width="1.3"/>
    <text x="19" y="197" fill="#6ee7b7" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✓</text>
    <text x="31" y="197" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Мораторные проценты</text>
    <text x="31" y="210" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">пп. 4 ст. 63, 2 ст. 81, 2¹ ст. 126</text>

    <!-- Стрелки к центральному блоку (x=268) -->
    <line x1="226" y1="32"  x2="268" y2="90"  stroke="#10b981" stroke-width="1.3" marker-end="url(#b42mg)" opacity="0.75"/>
    <line x1="226" y1="74"  x2="268" y2="104" stroke="#10b981" stroke-width="1.3" marker-end="url(#b42mg)" opacity="0.85"/>
    <line x1="226" y1="116" x2="268" y2="118" stroke="#10b981" stroke-width="1.6" marker-end="url(#b42mg)"/>
    <line x1="226" y1="158" x2="268" y2="132" stroke="#10b981" stroke-width="1.3" marker-end="url(#b42mg)" opacity="0.85"/>
    <line x1="226" y1="200" x2="268" y2="146" stroke="#10b981" stroke-width="1.3" marker-end="url(#b42mg)" opacity="0.75"/>

    <!-- ===== ЦЕНТРАЛЬНЫЙ БЛОК: РАЗМЕР СО (x=268–438, y=58–174) ===== -->
    <rect x="268" y="58" width="170" height="116" rx="12" fill="url(#b42gctr)" stroke="#d97706" stroke-width="2"/>
    <rect x="268" y="58" width="170" height="116" rx="12" fill="none" stroke="rgba(217,119,6,.18)" stroke-width="7"/>
    <text x="353" y="90"  text-anchor="middle" fill="#fde68a" font-size="9"   font-weight="800" font-family="system-ui,sans-serif" letter-spacing=".04em">РАЗМЕР</text>
    <text x="353" y="106" text-anchor="middle" fill="#fde68a" font-size="7.8" font-weight="800" font-family="system-ui,sans-serif" letter-spacing=".03em">СУБСИДИАРНОЙ</text>
    <text x="353" y="120" text-anchor="middle" fill="#fde68a" font-size="7.8" font-weight="800" font-family="system-ui,sans-serif" letter-spacing=".03em">ОТВЕТСТВЕННОСТИ</text>
    <line x1="282" y1="127" x2="424" y2="127" stroke="rgba(217,119,6,.28)" stroke-width="1"/>
    <text x="353" y="140" text-anchor="middle" fill="#94a3b8" font-size="6.2" font-family="system-ui,sans-serif">= Σ включённых требований</text>
    <text x="353" y="153" text-anchor="middle" fill="#64748b" font-size="5.8" font-family="system-ui,sans-serif">п. 26¹ Пленума ВС № 53</text>
    <text x="353" y="165" text-anchor="middle" fill="#64748b" font-size="5.8" font-family="system-ui,sans-serif">(ред. Пленума № 42 · 23.12.2025)</text>

    <!-- ===== ПРАВАЯ ЧАСТЬ: НЕ ВКЛЮЧАЕТСЯ (x=450–712) ===== -->
    <line x1="445" y1="14" x2="445" y2="220" stroke="rgba(220,38,38,.22)" stroke-width="1.5" stroke-dasharray="5,4"/>

    <!-- R1: Штрафы ФНС — особо выделено -->
    <rect x="450" y="14" width="262" height="62" rx="9" fill="rgba(234,88,12,.18)" stroke="#ea580c" stroke-width="2"/>
    <rect x="450" y="14" width="262" height="62" rx="9" fill="none" stroke="rgba(234,88,12,.35)" stroke-width="5" stroke-dasharray="4,3"/>
    <text x="465" y="32" fill="#fdba74" font-size="7.8" font-weight="800" font-family="system-ui,sans-serif">✕  Штрафы ФНС за налоговые</text>
    <text x="465" y="46" fill="#fdba74" font-size="7.8" font-weight="800" font-family="system-ui,sans-serif">     правонарушения должника</text>
    <rect x="465" y="52" width="92" height="16" rx="4" fill="rgba(234,88,12,.4)"/>
    <text x="511" y="63" text-anchor="middle" fill="#fff" font-size="6" font-weight="800" font-family="system-ui,sans-serif">КС РФ № 50-П · п. 26¹</text>

    <!-- R2: Аффилированные -->
    <rect x="450" y="86" width="262" height="33" rx="7" fill="rgba(220,38,38,.12)" stroke="#ef4444" stroke-width="1.2"/>
    <text x="463" y="99"  fill="#fca5a5" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✕</text>
    <text x="475" y="99"  fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Требования аффилированных лиц</text>
    <text x="475" y="112" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">контролирующих / подконтрольных КДЛ · п. 26²</text>

    <!-- R3: Осведомлённые кредиторы -->
    <rect x="450" y="129" width="262" height="33" rx="7" fill="rgba(220,38,38,.12)" stroke="#ef4444" stroke-width="1.2"/>
    <text x="463" y="142" fill="#fca5a5" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✕</text>
    <text x="475" y="142" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Требования «осведомлённых» кредиторов</text>
    <text x="475" y="155" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">знали о нарушениях при заключении договора · п. 26⁷</text>

    <!-- R4: Отсутствие причинно-следственной связи -->
    <rect x="450" y="172" width="262" height="33" rx="7" fill="rgba(220,38,38,.12)" stroke="#ef4444" stroke-width="1.2"/>
    <text x="463" y="185" fill="#fca5a5" font-size="7.2" font-weight="800" font-family="system-ui,sans-serif">✕</text>
    <text x="475" y="185" fill="#e2e8f0" font-size="6.8" font-weight="700" font-family="system-ui,sans-serif">Требования без причинно-след. связи</text>
    <text x="475" y="198" fill="#94a3b8" font-size="5.9" font-family="system-ui,sans-serif">КДЛ доказало отсутствие влияния · п. 26⁶</text>

    <!-- Подписи колонок -->
    <text x="117" y="224" text-anchor="middle" fill="#6ee7b7" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif" letter-spacing=".05em">ВКЛЮЧАЕТСЯ В РАЗМЕР СО (п. 26¹)</text>
    <text x="581" y="224" text-anchor="middle" fill="#fca5a5" font-size="6.5" font-weight="700" font-family="system-ui,sans-serif" letter-spacing=".04em">НЕ ВКЛЮЧАЕТСЯ / СНИЖАЕТ РАЗМЕР СО</text>
  </svg>

  <!-- Детальный разбор: HTML-колонки -->
  <div class="bsp42__cols">
    <div class="bsp42__col bsp42__col--in">
      <p class="bsp42__col-hd">✓ Что включается в размер СО</p>
      <ul class="bsp42__ul">
        <li><strong>Реестровые требования кредиторов</strong> — все три очереди (основная база)</li>
        <li><strong>Зареестровые требования</strong> — заявленные после закрытия реестра</li>
        <li><strong>Текущие платежи</strong> — ст. 5 Закона о банкротстве</li>
        <li><strong>Санкции за публичные правонарушения</strong> — кроме штрафов ФНС<small>пени ФНС и санкции за иные нарушения — включаются; штрафы за налоговые — нет</small></li>
        <li><strong>Мораторные проценты</strong> — пп. 4 ст. 63, 2 ст. 81, абз. 4 п. 2 ст. 95, п. 2¹ ст. 126 Закона о банкротстве</li>
      </ul>
    </div>
    <div class="bsp42__col bsp42__col--out">
      <p class="bsp42__col-hd">✕ Что не включается / снижает размер</p>
      <ul class="bsp42__ul">
        <li class="bsp42__li-ks">
          <span class="bsp42__ks-ico">✕</span><span class="bsp42__ks-tag">КС 50-П · п. 26¹</span><strong>Штрафы ФНС</strong> за налоговые правонарушения должника
          <small>Карательная мера ≠ компенсационная СО · обязательно для всех судов с 23.12.2025</small>
        </li>
        <li><strong>Требования аффилированных лиц</strong> — контролирующих или подконтрольных КДЛ структур — п. 26²</li>
        <li><strong>Требования, уступленные заинтересованному лицу</strong> — п. 26², ст. 384 ГК РФ</li>
        <li><strong>Требования «осведомлённых» кредиторов</strong> — знали о нарушениях при заключении договора<small>исключение: недобровольные кредиторы (работники, обязательные платежи) защищены всегда — п. 26⁷</small></li>
        <li><strong>Требования без причинно-следственной связи</strong> — КДЛ доказало, что конкретное требование не связано с его действиями — п. 26⁶</li>
      </ul>
    </div>
  </div>

  <!-- Блок КС РФ № 50-П -->
  <div class="bsp42__ks-box">
    <span class="bsp42__ks-lbl">КС РФ № 50-П · 30.10.2023 → п. 26¹ Пленума № 42</span>
    <p class="bsp42__ks-p"><strong>Субсидиарная ответственность — компенсационная, а не карательная.</strong> Налоговый штраф — персональная санкция за конкретное правонарушение должника; перенос её на КДЛ нарушает принцип персонализации публичного наказания. До Пленума № 42 часть судов включала штрафы ФНС в базу СО. С 23.12.2025 это прямо запрещено: <strong>если ФНС заявила штрафы в составе требований о привлечении к СО — это прямое основание для снижения заявленной суммы.</strong></p>
  </div>

  <!-- Теги -->
  <div class="bsp42__foot" aria-label="Нормативная база блока">
    <span class="bsp42__tag bsp42__tag--a">Пленум ВС № 42 · 23.12.2025</span>
    <span class="bsp42__tag bsp42__tag--a">пп. 26¹–26¹¹ Пленума ВС № 53</span>
    <span class="bsp42__tag bsp42__tag--i">реестр · зареестровые · текущие платежи</span>
    <span class="bsp42__tag bsp42__tag--e">штрафы ФНС — исключаются</span>
    <span class="bsp42__tag bsp42__tag--k">КС РФ № 50-П · 30.10.2023</span>
    <span class="bsp42__tag bsp42__tag--e">аффилированные · осведомлённые · п. 26², 26⁶, 26⁷</span>
  </div>
</div>
</section>
```

## Передача Наташе

- **Якорь:** `l24-boris-plenum42-size`
- **После H3:** «Что входит в размер: реестровые и зареестровые требования кредиторов»
- **Перед:** H3 «Штрафы и санкции ФНС: почему они не включаются (позиция КС РФ № 50-П)»
- **MCP-only:** без `<canvas>` и `<script>` — только inline CSS + SVG
