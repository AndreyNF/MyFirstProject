#!/usr/bin/env python3
"""Generate Legis24 longread HTML for VS obzor #3/2026 (ARB slot)."""
from __future__ import annotations

from pathlib import Path

SLUG = "vs-obzor-3-2026-nalogovye-spory-ens-fns"
PREFIX = SLUG
OUT = Path("/workspace/.cursor/page-content-natasha-vs-obzor-3.html")

TITLE = "Обзор ВС № 3/2026: налоговые споры с ФНС — ЕНС, безнадёжная задолженность и защита"
DESC = (
    "28 позиций обзора ВС № 3/2026 о налоговых спорах: ЕНС, одно требование, "
    "безнадёжная задолженность, пени, НДФЛ. Как оспорить ФНС в суде — сроки, стратегия, доказательства."
)
H1 = TITLE
SUB = "Единый налоговый счёт, судебные приказы и НДФЛ — практический разбор позиций Верховного Суда для налогоплательщиков и бизнеса"

LONGREAD = """
<h2 id="obzor-vs3">Тематический обзор ВС № 3/2026: зачем он нужен налогоплательщику</h2>

<h3>Постановление Президиума от 25.03.2026 № 4А/2026 и охват практики 2020–2025</h3>

<p>25 марта 2026 года Президиум Верховного Суда РФ утвердил Тематический обзор № 3/2026 «О рассмотрении судами общей юрисдикции споров, связанных с применением отдельных положений законодательства о налогах и сборах» (постановление № 4А/2026). Документ обобщает практику за 2020–2025 годы и содержит <strong>28 правовых позиций</strong> — от институтов Единого налогового счёта (ЕНС) до споров по НДФЛ, транспортному налогу и страховым взносам ИП.</p>

<p>Для предпринимателей и компаний обзор важен не меньше, чем арбитражные обзоры по налогу на имущество: многие споры с ФНС по пеням, взносам и административному взысканию проходят в судах общей юрисдикции, а позиции ВС напрямую влияют на аргументы при <strong>досудебном обжаловании</strong> и в связанных экономических спорах.</p>

<h3>Чем обзор № 3/2026 отличается от обзора № 4/2026 по имуществу организаций</h3>

<p>Если <a href="/vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns">обзор ВС № 4/2026</a> касается арбитражных споров по налогу на имущество организаций (глава 30 НК РФ), то обзор № 3/2026 охватывает <strong>налоговые споры физических лиц и ИП</strong> в судах общей юрисдикции: ЕНС, судебные приказы, НДФЛ при продаже недвижимости, транспортный налог, банкротство гражданина. Для юридической стратегии эти документы дополняют друг друга: директор, ИП и учредитель должны учитывать оба обзора при защите от ФНС.</p>

<h2 id="ens">ЕНС: одно требование, распределение платежей и споры с ФНС</h2>

<h3>Пункт 2 обзора — одно требование при отрицательном сальдо ЕНС</h3>

<p>С 1 января 2023 года налоговый орган направляет <strong>одно требование</strong> об уплате задолженности в размере отрицательного сальдо ЕНС. При увеличении долга (например, появились новые страховые взносы за 2023 год при уже существующем долге по транспортному налогу) <strong>новое требование не выставляется</strong>. Инспекция вправе сразу обратиться в суд — и суды поддерживают эту позицию (п. 2 обзора).</p>

<p><strong>Практический вывод:</strong> нельзя ссылаться на то, что «старое требование касалось другого налога». ЕНС объединяет обязательства; при росте отрицательного сальдо действует первоначальное требование.</p>

<h3>Пункт 5 — единый налоговый платёж и очерёдность погашения</h3>

<p>Любой платёж после 1 января 2023 года учитывается как единый налоговый платёж. ФНС распределяет его по правилам статьи 45 НК РФ: <strong>сначала на более ранние долги</strong>, независимо от назначения платежа, указанного плательщиком в платёжке. Спорить с таким распределением крайне сложно — важно контролировать сальдо ЕНС в личном кабинете и фиксировать дату каждого платежа.</p>

<h3>Пункт 3 — расхождение суммы в иске и в требовании</h3>

<p>Несовпадение суммы, заявленной налоговым органом в административном исковом заявлении, и суммы в требовании об уплате <strong>не является основанием для возврата заявления</strong>. Суд рассматривает спор по существу. Налогоплательщику следует готовить возражения по сути долга, а не по формальным расхождениям в цифрах.</p>

<div class="ym-cta ym-cta--legis24">
<p class="ym-cta__text">Получили требование по ЕНС или иск ФНС? Разберём сальдо, сроки обжалования и линию защиты до суда.</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по налоговому спору</a></p>
</div>

<h2 id="beznadezhnaya">Безнадёжная задолженность и судебные приказы: пункты 6–7 обзора</h2>

<h3>Трёхлетний срок предъявления приказа приставам</h3>

<p>Если мировой судья вынес судебный приказ о взыскании налога, приказ вступил в силу, но инспекция <strong>не направила его приставам в течение трёх лет</strong> и не восстановила срок, задолженность признаётся <strong>безнадёжной к взысканию</strong> (п. 6 обзора). Верховный Суд отменил позиции нижестоящих судов, которые отказывали налогоплательщику со ссылкой на «обязанность приставов».</p>

<h3>Пени при утрате права взыскать основной долг</h3>

<p>Пени — способ обеспечения основного обязательства. Если налоговый орган утратил возможность принудительно взыскать сам налог (истёк срок предъявления исполнительного листа), <strong>начислять и взыскивать пени нельзя</strong> (п. 7 обзора). Типичная ситуация: инспекция выиграла суд по страховым взносам в 2016 году, не передала лист приставам, срок истёк — но продолжала начислять пени. ВС отменил взыскание пеней.</p>

<p>Для бизнеса это критично при спорах с ФНС о «хвостах» задолженности: проверьте, не истёк ли срок принудительного взыскания по каждому исполнительному документу.</p>

<h2 id="uvedomlenie">Уведомления ФНС: не получил — всё равно плати (п. 1)</h2>

<p>Неполучение налогового уведомления или требования, направленного по адресу из базы ФНС, <strong>не освобождает от обязанности уплатить налог</strong>. В деле из обзора собственник автомобиля не получал документы по адресу регистрации; суд взыскал транспортный налог, поскольку сведения о смене адреса в инспекцию не поступали, а налогоплательщик сам не сообщил о неполучении уведомлений.</p>

<p><strong>Рекомендация:</strong> актуализируйте адрес в ФНС, подключите личный кабинет налогоплательщика, фиксируйте обращения о неполучении корреспонденции.</p>

<h2 id="bankrotstvo-ip">Банкротство, ИП и НДС без регистрации: п. 9–10</h2>

<h3>Прекращение статуса ИП с момента банкротства</h3>

<p>Признание гражданина банкротом освобождает от уплаты взносов на обязательное страхование в качестве ИП <strong>с момента решения о банкротстве</strong>, даже если запись в ЕГРИП прекращена позже (п. 9). Суды трёх инстанций ошибочно начисляли взносы за период после банкротства — ВС указал на прекращение статуса вместе с делом о банкротстве.</p>

<h3>Предпринимательская деятельность без регистрации ИП</h3>

<p>Отсутствие статуса ИП не освобождает от НДС, если деятельность по сути предпринимательская: систематическая сдача коммерческой недвижимости, продажа нежилых объектов (п. 10). ФНС вправе доначислить НДС по итогам выездной проверки — суды, включая ВС, поддерживают инспекцию.</p>

<h2 id="ndfl">НДФЛ: ключевые позиции обзора для физлиц и собственников бизнеса</h2>

<h3>Недействительные сделки и сохранение дохода (п. 11–12)</h3>

<p>Если суд признал договор дарения недействительным и стороны вернулись в первоначальное положение — <strong>объекта налогообложения по НДФЛ нет</strong> (п. 11). Обратная ситуация: договор купли-продажи признан недействительным, но реституция невозможна (покупатель снёс здание) — доход и обязанность уплатить НДФЛ <strong>сохраняются</strong> (п. 12).</p>

<h3>Возмещение реального ущерба — не доход (п. 14)</h3>

<p>Суммы возмещения реального ущерба (разница между вложенными средствами и стоимостью аналогичной квартиры при расторжении ДДУ) не облагаются НДФЛ. Суды трёх инстанций поддержали застройщика против инспекции — позиция закреплена в обзоре.</p>

<h3>Минимальный срок владения: незавершёнка и маткапитал (п. 17–18, 20)</h3>

<ul>
<li><strong>Незавершённое строительство:</strong> срок владения для льготы по НДФЛ исчисляется с даты регистрации <em>готового</em> объекта, а не исходной «незавершёнки» (п. 18).</li>
<li><strong>Кадастровая стоимость:</strong> применять её можно только если сведения внесены в ЕГРН на 1 января года регистрации права; иначе — расчёт от рыночной стоимости (п. 17).</li>
<li><strong>Материнский капитал:</strong> срок владения долей ребёнка в квартире — с даты направления маткапитала на погашение кредита, а не с даты оформления доли в ЕГРН (п. 20).</li>
</ul>

<h3>НДФЛ и место постановки на учёт (раздел II обзора)</h3>

<p>Для исчисления НДФЛ определяющим является <strong>место постановки налогоплательщика на учёт</strong>, а не место нахождения проданного имущества — это связано с перераспределением налоговых доходов между бюджетами.</p>

<h2 id="transport">Транспортный налог и регистрация ТС (п. 25)</h2>

<p>Обязанность по уплате транспортного налога связана с <strong>фактом регистрации</strong>, а не с правом собственности. Передача автомобиля по мировому соглашению без снятия с учёта не освобождает от налога — суды взыскали его с прежнего владельца, числящегося в ГИБДД.</p>

<h2 id="lgoty">Льготы без заявления и ремонт в предпринимательских целях (п. 26–27)</h2>

<p>Налог на имущество физлиц: если у инспекции есть сведения о праве на льготу (заявление о переходе на УСН, декларация об использовании помещения в бизнесе), льготу предоставляют <strong>беззаявительно</strong> (п. 27). Подготовительные работы (ремонт цеха под производство) — часть предпринимательской деятельности; имущество на этапе подготовки может освобождаться от налога (п. 26).</p>

<h2 id="strategiya">Стратегия защиты при налоговом споре с ФНС в 2026 году</h2>

<h3>Досудебный порядок и выбор подсудности</h3>

<p>До суда обжалуйте акты и решения в вышестоящей инспекции или УФНС в установленные сроки. Часть споров — в суде общей юрисдикции (административные иски ФНС, оспаривание безнадёжной задолженности), часть связанных вопросов — в арбитраже (доначисления организациям). Сопоставьте позиции обзора № 3/2026 с <a href="/vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns">обзором № 4/2026</a> и <a href="/vs-st-199-uklonenie-nalogov-75-dnej-zashchita-2026">уголовными рисками по ст. 199 УК</a> при крупных суммах.</p>

<h3>Чек-лист доказательств</h3>

<table>
<thead><tr><th>Ситуация</th><th>Что собрать</th><th>Пункт обзора</th></tr></thead>
<tbody>
<tr><td>Спор по ЕНС</td><td>Выписка сальдо, требование, платёжки, даты зачёта</td><td>п. 2, 4, 5</td></tr>
<tr><td>Безнадёжный долг</td><td>Судебный приказ, дата вступления, доказательства непредъявления приставам</td><td>п. 6</td></tr>
<tr><td>Пени на «мёртвый» долг</td><td>Исполнительный лист, срок предъявления, постановление об окончании ИП</td><td>п. 7</td></tr>
<tr><td>НДФЛ с продажи жилья</td><td>ЕГРН, даты прав, кадастровая на 01.01, документы о расходах</td><td>п. 17–18, 24</td></tr>
<tr><td>Транспортный налог</td><td>Данные ГИБДД, договор передачи, снятие с учёта</td><td>п. 25</td></tr>
</tbody>
</table>

<h3>Сроки: не пропустить окно</h3>

<p>Трёхлетний срок предъявления судебного приказа, сроки обжалования решений ФНС, сроки административного искового производства — ошибка в сроке часто дороже, чем слабая позиция по существу. Фиксируйте даты получения документов (заказные письма, личный кабинет).</p>

<div class="ym-cta">
<p class="ym-cta__text">Нужна стратегия в споре с ФНС: ЕНС, приказ, НДФЛ или взносы ИП? Подготовим возражения и представительство в суде.</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Записаться на консультацию</a></p>
</div>

<section class="l24-faq" id="faq">
<h2>Частые вопросы</h2>
<div class="l24-faq__item">
<p class="l24-faq__q">Можно ли не платить налог, если не пришло уведомление от ФНС?</p>
<p class="l24-faq__a">Нет. По п. 1 обзора № 3/2026 неполучение уведомления или требования, направленного по адресу из базы ФНС, не освобождает от уплаты. Сообщите инспекции о неполучении и проверьте актуальность адреса в личном кабинете.</p>
</div>
<div class="l24-faq__item">
<p class="l24-faq__q">ФНС выставила новое требование при росте долга на ЕНС — законно ли это?</p>
<p class="l24-faq__a">После 01.01.2023 при росте отрицательного сальдо ЕНС новое требование не направляется — действует первоначальное (п. 2 обзора). Инспекция может сразу идти в суд.</p>
</div>
<div class="l24-faq__item">
<p class="l24-faq__q">Истёк срок передачи судебного приказа приставам — можно списать долг?</p>
<p class="l24-faq__a">Да, при истечении трёхлетнего срока предъявления приказа без восстановления задолженность признаётся безнадёжной (п. 6). Подайте заявление в суд с доказательствами непредъявления.</p>
</div>
<div class="l24-faq__item">
<p class="l24-faq__q">Может ли ФНС взыскать пени, если основной налог уже нельзя взыскать?</p>
<p class="l24-faq__a">Нет. П. 7 обзора: утрата права принудительного взыскания основного долга исключает взыскание пеней на эту сумму.</p>
</div>
<div class="l24-faq__item">
<p class="l24-faq__q">Обзор № 3/2026 применим к спорам организаций в арбитраже?</p>
<p class="l24-faq__a">Обзор обобщает практику судов общей юрисдикции, но позиции по ЕНС, срокам и пеням релевантны и при досудебной защите бизнеса. Споры по налогу на имущество организаций — в <a href="/vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns">обзоре № 4/2026</a>.</p>
</div>
</section>
"""

HERO_SVG = """<svg viewBox="0 0 500 420" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:500px" role="img" aria-label="Единый налоговый счёт и весы правосудия: обзор ВС № 3/2026 о налоговых спорах с ФНС">
  <defs>
    <linearGradient id="h3-bg" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e8eef5"/></linearGradient>
    <linearGradient id="h3-vs" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="#1e40af"/><stop offset="100%" stop-color="#0f2744"/></linearGradient>
    <linearGradient id="h3-ens" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#fef3c7"/><stop offset="100%" stop-color="#fde68a"/></linearGradient>
    <filter id="h3-sh"><feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.12"/></filter>
  </defs>
  <rect x="10" y="12" width="480" height="396" rx="16" fill="url(#h3-bg)" stroke="#cbd5e1"/>
  <g filter="url(#h3-sh)" transform="translate(168, 20)">
    <rect x="0" y="32" width="164" height="44" rx="4" fill="url(#h3-vs)"/>
    <polygon points="82,0 164,32 0,32" fill="#1e40af"/>
    <text x="82" y="48" text-anchor="middle" fill="#e2e8f0" font-size="6.5" font-weight="800">ОБЗОР ВС № 3/2026</text>
    <text x="82" y="62" text-anchor="middle" fill="#93c5fd" font-size="5.5">налоговые споры · ЕНС</text>
    <text x="82" y="82" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="700">25.03.2026 · 4А/2026</text>
  </g>
  <g filter="url(#h3-sh)" transform="translate(40, 110)">
    <rect width="180" height="100" rx="10" fill="#fff" stroke="#cbd5e1"/>
    <rect width="180" height="22" rx="10" fill="url(#h3-ens)"/>
    <text x="90" y="15" text-anchor="middle" fill="#92400e" font-size="7" font-weight="800">ЕНС · единый счёт</text>
    <text x="20" y="42" fill="#64748b" font-size="5.5">Сальдо:</text>
    <text x="60" y="42" fill="#dc2626" font-size="6" font-weight="700">− 284 500 ₽</text>
    <rect x="16" y="52" width="148" height="6" rx="2" fill="#fee2e2"/>
    <text x="20" y="72" fill="#475569" font-size="5">Требование № 1 (единственное)</text>
    <text x="20" y="86" fill="#64748b" font-size="5">транспортный налог + взносы 2023</text>
    <text x="20" y="100" fill="#0369a1" font-size="5" font-weight="600">п. 2 обзора · без нового требования</text>
  </g>
  <g filter="url(#h3-sh)" transform="translate(280, 100)">
    <rect x="148" y="0" width="24" height="90" rx="3" fill="#64748b"/>
    <rect x="132" y="-8" width="56" height="10" rx="3" fill="#64748b"/>
    <line x1="160" y1="0" x2="160" y2="-24" stroke="#475569" stroke-width="3"/>
    <line x1="80" y1="-24" x2="240" y2="-24" stroke="#475569" stroke-width="3"/>
    <line x1="100" y1="-24" x2="100" y2="20" stroke="#64748b" stroke-width="2"/>
    <rect x="68" y="20" width="64" height="36" rx="4" fill="#fef2f2" stroke="#f87171"/>
    <text x="100" y="36" text-anchor="middle" fill="#991b1b" font-size="5" font-weight="700">ФНС</text>
    <text x="100" y="48" text-anchor="middle" fill="#64748b" font-size="4.5">иск / приказ</text>
    <line x1="220" y1="-24" x2="220" y2="16" stroke="#64748b" stroke-width="2"/>
    <rect x="188" y="16" width="64" height="36" rx="4" fill="#f0fdf4" stroke="#4ade80"/>
    <text x="220" y="32" text-anchor="middle" fill="#166534" font-size="5" font-weight="700">защита</text>
    <text x="220" y="44" text-anchor="middle" fill="#64748b" font-size="4.5">п. 6–7</text>
    <text x="160" y="108" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="700">безнадёжный долг · пени</text>
  </g>
  <g filter="url(#h3-sh)" transform="translate(48, 250)">
    <rect width="110" height="70" rx="8" fill="#fff" stroke="#e2e8f0"/>
    <text x="55" y="18" text-anchor="middle" fill="#334155" font-size="6" font-weight="800">судебный приказ</text>
    <text x="55" y="34" text-anchor="middle" fill="#64748b" font-size="5">3 года → приставы</text>
    <text x="55" y="50" text-anchor="middle" fill="#dc2626" font-size="5" font-weight="700">срок истёк</text>
    <text x="55" y="64" text-anchor="middle" fill="#166534" font-size="5" font-weight="600">долг списан</text>
  </g>
  <g filter="url(#h3-sh)" transform="translate(190, 248)">
    <rect width="120" height="72" rx="8" fill="#fff" stroke="#93c5fd"/>
    <text x="60" y="18" text-anchor="middle" fill="#1e3a8a" font-size="6" font-weight="800">НДФЛ · 28 позиций</text>
    <text x="60" y="34" text-anchor="middle" fill="#64748b" font-size="5">незавершёнка · маткапитал</text>
    <text x="60" y="50" text-anchor="middle" fill="#64748b" font-size="5">кадастр · льготы</text>
    <text x="60" y="66" text-anchor="middle" fill="#0369a1" font-size="5" font-weight="600">2020–2025 практика</text>
  </g>
  <g filter="url(#h3-sh)" transform="translate(340, 250)">
    <rect width="100" height="70" rx="8" fill="#fff" stroke="#fecaca"/>
    <text x="50" y="18" text-anchor="middle" fill="#991b1b" font-size="6" font-weight="800">п. 1</text>
    <text x="50" y="34" text-anchor="middle" fill="#475569" font-size="5">не получил</text>
    <text x="50" y="48" text-anchor="middle" fill="#475569" font-size="5">уведомление</text>
    <text x="50" y="62" text-anchor="middle" fill="#a31830" font-size="5" font-weight="700">всё равно плати</text>
  </g>
  <text x="250" y="408" text-anchor="middle" fill="#64748b" font-size="7" font-weight="600">ЕНС · единое требование · безнадёжная задолженность · НДФЛ · спор с ФНС</text>
</svg>"""

INTRO_ROUTE = """<svg class="l24-intro-vs__route-svg" viewBox="0 0 380 120" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Маршрут: обзор ВС → ЕНС → суд → защита">
  <defs><marker id="intro-h3-arr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,0 L7,3.5 L0,7Z" fill="#1e40af"/></marker></defs>
  <rect x="4" y="38" width="72" height="44" rx="6" fill="#eff6ff" stroke="#93c5fd"/><text x="40" y="58" text-anchor="middle" fill="#1e3a8a" font-size="7" font-weight="700">Обзор ВС</text><text x="40" y="72" text-anchor="middle" fill="#64748b" font-size="6">25.03.2026</text>
  <line x1="80" y1="60" x2="94" y2="60" stroke="#1e40af" stroke-width="1.5" marker-end="url(#intro-h3-arr)"/>
  <rect x="98" y="38" width="72" height="44" rx="6" fill="#fef9c3" stroke="#fde047"/><text x="134" y="58" text-anchor="middle" fill="#854d0e" font-size="7" font-weight="700">ЕНС</text><text x="134" y="72" text-anchor="middle" fill="#64748b" font-size="6">1 требование</text>
  <line x1="174" y1="60" x2="188" y2="60" stroke="#1e40af" stroke-width="1.5" marker-end="url(#intro-h3-arr)"/>
  <rect x="192" y="38" width="72" height="44" rx="6" fill="#fef2f2" stroke="#fecaca"/><text x="228" y="58" text-anchor="middle" fill="#991b1b" font-size="7" font-weight="700">Суд</text><text x="228" y="72" text-anchor="middle" fill="#64748b" font-size="6">приказ / иск</text>
  <line x1="268" y1="60" x2="282" y2="60" stroke="#1e40af" stroke-width="1.5" marker-end="url(#intro-h3-arr)"/>
  <rect x="286" y="38" width="88" height="44" rx="6" fill="#1e3a8a"/><text x="330" y="58" text-anchor="middle" fill="#e2e8f0" font-size="7" font-weight="700">Защита</text><text x="330" y="72" text-anchor="middle" fill="#93c5fd" font-size="6">п. 6–7 · НДФЛ</text>
</svg>"""


def css_block() -> str:
    p = PREFIX
    return f"""
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section,
.entry-title, .main_title, h1.entry-title {{ display: none !important; }}
#primary, .site-main, .site-content, #content, .content-area {{
  padding-top: 0 !important; margin-top: 0 !important;
}}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 {{ display: none !important; }}
.{p}-page .entry-content {{
  max-width: none !important; width: 100% !important; padding: 0 !important;
}}
.{p}-page .l24-longread-wrap {{
  max-width: 820px; margin: 0 auto; padding: 48px 24px 80px;
  font-size: 1.05rem; line-height: 1.65; color: #1a202c;
}}
.{p}-page h2 {{ margin-top: 2.5em; color: #1a365d; font-size: 1.45rem; }}
.{p}-page h3 {{ margin-top: 1.5em; color: #2c5282; font-size: 1.15rem; }}
.{p}-page table {{ width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem; }}
.{p}-page th, .{p}-page td {{ border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left; }}
.{p}-page th {{ background: #edf2f7; }}
.{p}-page a {{ color: #1e40af; }}
.{p}-page ol, .{p}-page ul {{ margin: 1em 0; padding-left: 1.4em; }}
.{p}-page li {{ margin-bottom: 0.45em; }}
.l24-intro-vs {{ max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px; font-family: system-ui, sans-serif; }}
.l24-intro-vs__grid {{ display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr); gap: 28px; }}
.l24-intro-vs__text {{ border-left: 4px solid #a31830; padding: 4px 0 4px 22px; text-align: left; }}
.l24-intro-vs__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-vs__brief {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; }}
.l24-intro-vs__decor {{ background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%); border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; }}
.l24-intro-vs__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-vs__chip {{ font-size: 0.72rem; font-weight: 700; padding: 6px 10px; border-radius: 999px; background: #fff; border: 1px solid #cbd5e1; color: #475569; }}
.l24-intro-vs__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-vs__chip--warn {{ border-color: #a31830; color: #a31830; }}
.ym-toc {{ max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px; text-align: center; }}
.ym-toc__title {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #64748b; }}
.ym-toc__list {{ list-style: none; padding: 0; margin: 12px 0 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; }}
.ym-toc__list a {{ display: inline-block; padding: 8px 12px; border-radius: 8px; background: #f1f5f9; color: #1e40af; text-decoration: none; font-size: 0.88rem; font-weight: 600; }}
.ym-cta {{ margin: 28px 0; padding: 22px 24px; border-radius: 10px; background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%); border: 1px solid #cbd5e1; border-left: 4px solid #a31830; }}
.ym-cta--legis24 {{ border-left-color: #1e3a8a; background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%); }}
.ym-cta__btn {{ display: inline-block; background: #a31830; color: #fff !important; padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; }}
.l24-faq {{ margin-top: 2.5em; padding: 28px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; }}
.l24-faq__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; font-weight: 700; }}
.l24-faq__a {{ margin: 0; color: #334155; }}
.l24-hero-{p} {{
  min-height: 85vh; display: flex; align-items: center; padding: 100px 24px 64px;
  background: linear-gradient(152deg, #fefefe 0%, #f3f6fa 50%, #eef2f8 100%);
  font-family: system-ui, sans-serif; color: #0f172a;
}}
.l24-hero-{p}__inner {{ max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; width: 100%; }}
.l24-hero-{p}__badge {{ display: inline-flex; align-items: center; gap: 8px; padding: 8px 14px; border-radius: 999px; background: #fff; border: 1px solid #e2e8f0; font-size: 0.78rem; font-weight: 600; text-transform: uppercase; color: #334155; margin-bottom: 16px; }}
.l24-hero-{p}__badge-mark {{ width: 8px; height: 8px; border-radius: 50%; background: #0369a1; }}
.l24-hero-{p}__h1 {{ margin: 0 0 16px; font-size: clamp(1.4rem, 3vw, 2.1rem); line-height: 1.22; font-weight: 800; }}
.l24-hero-{p}__h1-accent {{ color: #1e3a8a; }}
.l24-hero-{p}__sub {{ margin: 0 0 20px; color: #475569; line-height: 1.55; max-width: 40em; }}
.l24-hero-{p}__facts {{ display: flex; flex-wrap: wrap; gap: 8px; list-style: none; padding: 0; margin: 0 0 22px; }}
.l24-hero-{p}__fact {{ font-size: 0.76rem; font-weight: 700; padding: 6px 11px; border-radius: 8px; background: #fff; border: 1px solid #e2e8f0; color: #334155; }}
.l24-hero-{p}__cta {{ display: inline-block; background: #a31830; color: #fff !important; padding: 14px 26px; border-radius: 8px; font-weight: 700; text-decoration: none; }}
@media (max-width: 900px) {{
  .l24-hero-{p}__inner, .l24-intro-vs__grid {{ grid-template-columns: 1fr; }}
  .l24-hero-{p} {{ min-height: auto; padding: 88px 20px 48px; }}
}}
"""


def hero_block() -> str:
    p = PREFIX
    return f"""
<section id="l24-hero-{p}" class="l24-hero-{p}" aria-label="{H1}">
  <div class="l24-hero-{p}__inner">
    <div>
      <div class="l24-hero-{p}__badge"><span class="l24-hero-{p}__badge-mark" aria-hidden="true"></span>ARB · обзор ВС № 3/2026 · ЕНС · март 2026</div>
      <h1 class="l24-hero-{p}__h1"><span class="l24-hero-{p}__h1-accent">{H1}</span></h1>
      <p class="l24-hero-{p}__sub">{SUB}</p>
      <ul class="l24-hero-{p}__facts">
        <li class="l24-hero-{p}__fact">28 позиций ВС</li>
        <li class="l24-hero-{p}__fact">ЕНС · 1 требование</li>
        <li class="l24-hero-{p}__fact">безнадёжный долг</li>
        <li class="l24-hero-{p}__fact">НДФЛ · пени</li>
      </ul>
      <a class="l24-hero-{p}__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по спору с ФНС</a>
    </div>
    <div aria-hidden="true">{HERO_SVG}</div>
  </div>
</section>
"""


def main() -> int:
    p = PREFIX
    html = f"""<!-- wp:html -->
<style>
{css_block()}
</style>
<main id="primary" class="site-main {p}-page" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{TITLE}">
<meta itemprop="description" content="{DESC}">
<meta itemprop="inLanguage" content="ru-RU">
{hero_block()}
<section class="l24-intro-vs">
  <div class="l24-intro-vs__grid">
    <div class="l24-intro-vs__text">
      <p>25 марта 2026 года Президиум Верховного Суда утвердил обзор № 3/2026 о налоговых спорах в судах общей юрисдикции. Документ систематизирует 28 позиций по ЕНС, судебным приказам, пеням, НДФЛ и взносам ИП — практика 2020–2025 годов.</p>
      <p>Для бизнеса и собственников компаний это практический навигатор: как отбиваться от ФНС при росте сальдо ЕНС, когда долг становится безнадёжным и какие аргументы по НДФЛ работают в суде.</p>
      <div class="l24-intro-vs__brief">Разбираем ключевые пункты обзора, чек-лист доказательств и стратегию защиты — с отсылками к <a href="/vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns">арбитражному обзору № 4/2026</a> по налогу на имущество организаций.</div>
    </div>
    <div class="l24-intro-vs__decor">
      <ul class="l24-intro-vs__chips">
        <li class="l24-intro-vs__chip l24-intro-vs__chip--accent">обзор № 3/2026</li>
        <li class="l24-intro-vs__chip">ЕНС</li>
        <li class="l24-intro-vs__chip">судебный приказ</li>
        <li class="l24-intro-vs__chip l24-intro-vs__chip--warn">пени</li>
        <li class="l24-intro-vs__chip">НДФЛ</li>
        <li class="l24-intro-vs__chip">транспортный налог</li>
        <li class="l24-intro-vs__chip">банкротство ИП</li>
        <li class="l24-intro-vs__chip">28 позиций</li>
      </ul>
      {INTRO_ROUTE}
    </div>
  </div>
</section>
<nav class="ym-toc" aria-label="Содержание">
  <p class="ym-toc__title">Содержание</p>
  <ul class="ym-toc__list">
    <li><a href="#obzor-vs3">Обзор ВС № 3/2026</a></li>
    <li><a href="#ens">ЕНС и одно требование</a></li>
    <li><a href="#beznadezhnaya">Безнадёжный долг</a></li>
    <li><a href="#uvedomlenie">Уведомления ФНС</a></li>
    <li><a href="#bankrotstvo-ip">Банкротство и ИП</a></li>
    <li><a href="#ndfl">НДФЛ</a></li>
    <li><a href="#transport">Транспортный налог</a></li>
    <li><a href="#strategiya">Стратегия защиты</a></li>
    <li><a href="#faq">FAQ</a></li>
  </ul>
</nav>
<div class="l24-longread-wrap">
<blockquote><p>Смежные материалы: <a href="/vs-obzor-4-2026-nalog-imushchestvo-organizacii-arbitrazh-fns">обзор ВС № 4/2026 в арбитраже</a>, <a href="/vs-obzor-5-2026-subsidiarnaya-otvetstvennost-kreditora">обзор № 5/2026 о субсидиарной ответственности</a>, <a href="/fns-strahovye-vznosy-vtoraya-ochered-bankrotstvo-vs">страховые взносы ФНС при банкротстве</a>.</p></blockquote>
{LONGREAD}
</div>
</main>
<!-- /wp:html -->
"""
    if "<script" in html.lower().replace("application/ld+json", ""):
        raise SystemExit("unexpected script tag")
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {len(html)} chars to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
