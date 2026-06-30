#!/usr/bin/env python3
"""Assemble Natasha HTML for plenum-vs-48 UG article."""
import html as H
import re
from pathlib import Path

SLUG = "plenum-vs-48-moshennichestvo-kriptovalyuta-zashchita"
OUT = Path(".cursor/page-content-natasha-plenum48.html")

H1 = "Пленум ВС № 48 о мошенничестве: криптовалюта, цифровые рубли и защита по ст. 159"
SUB = "ВС готовит разъяснения по цифровым активам; Госдума вводит ст. 171.6 за майнинг — что важно обвиняемому в 2026 году"
DESC = (
    "Верховный суд готовит изменения Пленума № 48 из‑за криптовалюты и цифровых рублей. "
    "Ст. 159 УК, изъятие крипто, майнинг 171.6 — защита по уголовному делу в 2026 году."
)

md = Path(".cursor/zhenya-longread-plenum48.md").read_text(encoding="utf-8")
sections = []
for m in re.finditer(r"^## (.+)$\n\n((?:.|\n)*?)(?=^## |\Z)", md, re.M):
    title, body = m.group(1), m.group(2).strip()
    if title in ("Мета", "Текст"):
        continue
    sections.append((title, body))


def md_body(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>', text)
    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    out = []
    for p in parts:
        if p.startswith("- "):
            items = re.findall(r"^- (.+)$", p, re.M)
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
        elif re.match(r"^\d+\. ", p):
            items = re.findall(r"^\d+\. (.+)$", p, re.M)
            out.append("<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>")
        else:
            out.append(f"<p>{p}</p>")
    return "\n".join(out)


def slugify(title: str) -> str:
    t = title.lower().replace("ё", "е")
    t = re.sub(r"[^a-z0-9а-я]+", "-", t)
    return t.strip("-")[:60]


cta_tpl = """<aside class="ym-cta" role="complementary">
<p class="ym-cta__text">{t}</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/">{b}</a></p>
</aside>"""
BORIS = r"""
<section id="l24-boris-plenum48-timeline" class="l24-boris-plenum48" aria-label="Хронология: Пленум № 48, цифровые активы и ст. 171.6 УК">
<style>
.l24-boris-plenum48{margin:48px 0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.l24-boris-plenum48__shell{background:linear-gradient(148deg,#0f2744 0%,#152a45 52%,#1a365d 100%);border:1px solid rgba(236,201,75,.24);border-radius:14px;padding:32px 28px 26px;color:#e2e8f0;box-shadow:0 18px 48px rgba(15,39,68,.28)}
.l24-boris-plenum48__eyebrow{margin:0 0 8px;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#ecc94b}
.l24-boris-plenum48__title{margin:0 0 10px;font-size:clamp(1.15rem,2.4vw,1.42rem);line-height:1.25;color:#fff;font-weight:700}
.l24-boris-plenum48__lead{margin:0 0 24px;font-size:.95rem;line-height:1.55;color:#a0aec0;max-width:68ch}
.l24-boris-plenum48__lead strong{color:#fff}
.l24-boris-plenum48__grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.l24-boris-plenum48__node{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:14px 12px;text-align:center}
.l24-boris-plenum48__year{display:block;font-size:.7rem;font-weight:700;color:#ecc94b;margin-bottom:6px}
.l24-boris-plenum48__label{font-size:.78rem;line-height:1.35;color:#cbd5e1}
@media(max-width:800px){.l24-boris-plenum48__grid{grid-template-columns:1fr 1fr}}
</style>
<div class="l24-boris-plenum48__shell">
<p class="l24-boris-plenum48__eyebrow">UG · маршрут 2026</p>
<h3 class="l24-boris-plenum48__title">От Пленума № 48 к цифровым активам и ст. 171.6</h3>
<p class="l24-boris-plenum48__lead"><strong>22.05.2026</strong> — Тимошин о подготовке изменений; <strong>28.05.2026</strong> — I чтение ст. 171.6; изъятие крипто по ст. 104.1 УК уже действует.</p>
<div class="l24-boris-plenum48__grid" role="list">
<div class="l24-boris-plenum48__node" role="listitem"><span class="l24-boris-plenum48__year">2017</span><span class="l24-boris-plenum48__label">Пленум № 48 · мошенничество</span></div>
<div class="l24-boris-plenum48__node" role="listitem"><span class="l24-boris-plenum48__year">2025–26</span><span class="l24-boris-plenum48__label">Изъятие криптовалюты · ст. 104.1</span></div>
<div class="l24-boris-plenum48__node" role="listitem"><span class="l24-boris-plenum48__year">22.05.26</span><span class="l24-boris-plenum48__label">ВС готовит разъяснения · CBDC</span></div>
<div class="l24-boris-plenum48__node" role="listitem"><span class="l24-boris-plenum48__year">28.05.26</span><span class="l24-boris-plenum48__label">Законопроект · ст. 171.6 майнинг</span></div>
</div>
</div>
</section>
"""

ctas = [
    (
        "После вызова в СК или полицию по «крипто» или P2P-сделке не откладывайте оценку риска по ст. 159 — первые протоколы задают рамку всего дела.",
        "Записаться на консультацию",
    ),
    (
        "Разграничьте гражданский спор и мошенничество до возбуждения дела: хронология договоров и переписки — ваш главный инструмент.",
        "Обсудить защиту по ст. 159",
    ),
    (
        "Если угрожают арестом кошельков или изъятием криптовалюты — нужен адвокат на стадии проверки.",
        "Получить помощь адвоката",
    ),
    (
        "Майнинг без реестра и крупный доход — зона будущей ст. 171.6 УК: проверьте статус до претензий следствия.",
        "Оценить уголовные риски",
    ),
]

toc = "\n".join(
    f'<li><a href="#{slugify(t)}">{H.escape(t[:52] + ("…" if len(t) > 52 else ""))}</a></li>'
    for t, _ in sections
)

FAQ = [
    (
        "Когда вступит в силу новый Пленум ВС № 48 о мошенничестве?",
        "На июнь 2026 года Верховный суд только готовит проект изменений. До официальной публикации действует постановление от 30.11.2017 № 48; защита должна опираться на текущие разъяснения и кассационную практику.",
    ),
    (
        "Можно ли привлечь к ст. 159 УК за невозврат криптовалюты по P2P?",
        "Не автоматически. Нужны доказательства обмана или злоупотребления доверием и умысла на хищение до получения актива. Иначе спор может оставаться гражданско-правовым.",
    ),
    (
        "Что такое ст. 171.6 УК о майнинге?",
        "Это проект (№ 1193493-8, I чтение 28.05.2026): уголовная ответственность за незаконный майнинг или работу оператором инфраструктуры без реестра при крупном доходе или ущербе (свыше 3,5 млн ₽).",
    ),
    (
        "Изымают ли криптовалюту по уголовному делу?",
        "Да: закон признаёт криминально полученную криптовалюту имуществом для изъятия по ст. 104.1 УК РФ. Важно документировать легальное происхождение активов.",
    ),
    (
        "Когда нужен адвокат по ст. 159?",
        "При первом вызове, аресте счетов/кошельков, уведомлении о подозрении или угрозе ужесточения наказания в кассации — до дачи показаний и подписания протоколов.",
    ),
]

faq_html = '<section class="l24-faq-ug" id="l24-faq-plenum48" aria-label="Частые вопросы о Пленуме № 48 и защите по ст. 159">\n<h2>Частые вопросы</h2>\n'
for q, a in FAQ:
    faq_html += f'<div class="l24-faq-ug__item"><p class="l24-faq-ug__q">{H.escape(q)}</p><p class="l24-faq-ug__a">{H.escape(a)}</p></div>\n'
faq_html += "</section>"

jsonld = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ],
}
import json

jsonld_pre = (
    f'<pre class="l24-jsonld-plenum48" hidden aria-hidden="true">{H.escape(json.dumps(jsonld, ensure_ascii=False))}</pre>'
)

lr = []
ci = 0
for i, (title, body) in enumerate(sections):
    aid = slugify(title)
    lr.append(f'<h2 id="{aid}">{H.escape(title)}</h2>')
    lr.append(md_body(body))
    if title.startswith("Статья 171.6"):
        lr.append(BORIS)
    if i in (1, 3, 5, 7) and ci < len(ctas):
        t, b = ctas[ci]
        lr.append(cta_tpl.format(t=t, b=b))
        ci += 1
lr.append(
    cta_tpl.format(
        t="Комплексная консультация по уголовным рискам при работе с цифровыми активами и защите по уголовному делу — до суда и на кассации.",
        b="Консультация по уголовному делу",
    )
)
lr.append(
    """<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
<p class="ym-cta__text">Юридическая помощь по уголовным делам: мошенничество, цифровые активы, защита на проверке и в суде.</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/">Оставить заявку</a></p>
</aside>"""
)
longread = "\n".join(lr)

pc = SLUG + "-page"
hero_svg = r'''<svg viewBox="0 0 440 380" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:440px" role="img" aria-label="Пленум ВС № 48, ст. 159 УК и цифровые активы: схема защиты">
<defs><linearGradient id="hg" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e8eef6"/></linearGradient>
<linearGradient id="hn" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#1e3a8a"/><stop offset="100%" stop-color="#0f2744"/></linearGradient></defs>
<rect x="8" y="8" width="424" height="364" rx="14" fill="url(#hg)" stroke="#cbd5e1"/>
<rect x="140" y="24" width="160" height="44" rx="6" fill="url(#hn)"/><text x="220" y="52" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="system-ui,sans-serif">Пленум ВС № 48</text>
<rect x="48" y="100" width="100" height="56" rx="8" fill="#fff" stroke="#94a3b8"/><text x="98" y="128" text-anchor="middle" fill="#0f2744" font-size="9" font-family="system-ui,sans-serif">ст. 159</text><text x="98" y="142" text-anchor="middle" fill="#64748b" font-size="8" font-family="system-ui,sans-serif">мошенничество</text>
<rect x="170" y="100" width="100" height="56" rx="8" fill="#fff" stroke="#1e40af"/><text x="220" y="128" text-anchor="middle" fill="#1e40af" font-size="9" font-weight="600" font-family="system-ui,sans-serif">крипто</text><text x="220" y="142" text-anchor="middle" fill="#64748b" font-size="8" font-family="system-ui,sans-serif">CBDC · токены</text>
<rect x="292" y="100" width="100" height="56" rx="8" fill="#fff" stroke="#a31830"/><text x="342" y="128" text-anchor="middle" fill="#a31830" font-size="9" font-weight="600" font-family="system-ui,sans-serif">ст. 171.6</text><text x="342" y="142" text-anchor="middle" fill="#64748b" font-size="8" font-family="system-ui,sans-serif">майнинг</text>
<path d="M98 156 L98 200 L220 200 L220 156" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<path d="M220 156 L220 200" fill="none" stroke="#64748b" stroke-width="1.5"/>
<path d="M342 156 L342 200 L220 200" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<rect x="120" y="220" width="200" height="64" rx="10" fill="#fef2f2" stroke="#a31830" stroke-width="1.2"/>
<text x="220" y="248" text-anchor="middle" fill="#a31830" font-size="10" font-weight="700" font-family="system-ui,sans-serif">защита по УД</text>
<text x="220" y="264" text-anchor="middle" fill="#475569" font-size="8" font-family="system-ui,sans-serif">умысел · гражданский спор · кассация</text>
<text x="220" y="330" text-anchor="middle" fill="#64748b" font-size="8" font-family="system-ui,sans-serif">Тимошин · 22.05.2026 · законопроект 28.05.2026</text>
</svg>'''

page = f"""<!-- wp:html -->
<style>
.breadcrumbs, .breadcrumb, .woocommerce-breadcrumb, .rank-math-breadcrumb, .yoast-breadcrumb,
.entry-header, .page-title-section, .entry-title, .main_title, h1.entry-title {{ display: none !important; }}
#primary, .site-main, .site-content, #content, .content-area {{ padding-top: 0 !important; margin-top: 0 !important; }}
#sidebar, .sidebar, #secondary, .et_pb_column_1_4 {{ display: none !important; }}
.{pc} .entry-content {{ max-width: none !important; width: 100% !important; padding: 0 !important; }}
.{pc} .l24-longread-wrap {{ max-width: 820px; margin: 0 auto; padding: 48px 24px 80px; font-size: 1.05rem; line-height: 1.65; color: #1a202c; }}
.{pc} h2 {{ margin-top: 2.5em; color: #1a365d; font-size: 1.45rem; }}
.{pc} h3 {{ margin-top: 1.5em; color: #2c5282; font-size: 1.15rem; }}
.{pc} table {{ width: 100%; border-collapse: collapse; margin: 1.5em 0; font-size: 0.95rem; }}
.{pc} th, .{pc} td {{ border: 1px solid #e2e8f0; padding: 10px 12px; text-align: left; }}
.{pc} th {{ background: #edf2f7; }}
.{pc} a {{ color: #1e40af; }}
.l24-intro-ug {{ max-width: 1200px; margin: 0 auto; padding: 40px 24px 8px; font-family: system-ui, sans-serif; }}
.l24-intro-ug__grid {{ display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(260px, 0.9fr); gap: 28px; }}
.l24-intro-ug__text {{ border-left: 4px solid #0f2744; padding: 4px 0 4px 22px; }}
.l24-intro-ug__text p {{ margin: 0 0 14px; font-size: 1.02rem; line-height: 1.6; color: #334155; }}
.l24-intro-ug__brief {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 18px; margin-top: 16px; font-size: 0.95rem; }}
.l24-intro-ug__decor {{ background: linear-gradient(160deg, #f1f5f9 0%, #fff 100%); border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; }}
.l24-intro-ug__chips {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }}
.l24-intro-ug__chip {{ font-size: 0.72rem; font-weight: 700; padding: 6px 10px; border-radius: 999px; background: #fff; border: 1px solid #cbd5e1; color: #475569; }}
.l24-intro-ug__chip--accent {{ border-color: #1e40af; color: #1e40af; }}
.l24-intro-ug__chip--warn {{ border-color: #a31830; color: #a31830; }}
.ym-toc {{ max-width: 820px; margin: 24px auto 0; padding: 0 24px 32px; text-align: center; font-family: system-ui, sans-serif; }}
.ym-toc__title {{ font-size: 0.8rem; font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; color: #64748b; margin: 0 0 12px; }}
.ym-toc__list {{ list-style: none; padding: 0; margin: 0; display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; }}
.ym-toc__list a {{ display: inline-block; padding: 8px 12px; border-radius: 8px; background: #f1f5f9; color: #1e40af; text-decoration: none; font-size: 0.88rem; font-weight: 600; }}
.ym-cta {{ margin: 28px 0; padding: 22px 24px; border-radius: 10px; background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%); border: 1px solid #cbd5e1; border-left: 4px solid #a31830; }}
.ym-cta--legis24 {{ border-left-color: #1e3a8a; background: linear-gradient(135deg, #eff6ff 0%, #f8fafc 100%); }}
.ym-cta__text {{ margin: 0 0 14px; line-height: 1.55; color: #334155; }}
.ym-cta__btn {{ display: inline-block; background: #a31830; color: #fff !important; padding: 12px 22px; border-radius: 8px; font-weight: 700; text-decoration: none; }}
.l24-faq-ug {{ margin-top: 2.5em; padding: 28px 24px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; }}
.l24-faq-ug h2 {{ margin-top: 0 !important; }}
.l24-faq-ug__item {{ margin-bottom: 18px; padding-bottom: 18px; border-bottom: 1px solid #e2e8f0; }}
.l24-faq-ug__q {{ margin: 0 0 8px; font-size: 1.05rem; color: #1a365d; font-weight: 600; }}
.l24-faq-ug__a {{ margin: 0; color: #334155; }}
.l24-jsonld-plenum48 {{ display: none !important; }}
@media (max-width: 900px) {{ .l24-intro-ug__grid {{ grid-template-columns: 1fr; }} }}
.hero-ug-plenum48 {{ position: relative; min-height: 88vh; display: flex; align-items: center; padding: 112px 24px 72px; background: linear-gradient(165deg, #f8fafc 0%, #eef2f7 45%, #e8eef6 100%); font-family: system-ui, sans-serif; overflow: hidden; }}
.hero-ug-plenum48__inner {{ max-width: 1200px; margin: 0 auto; width: 100%; display: grid; grid-template-columns: 1.05fr 0.95fr; gap: 44px; align-items: center; }}
.hero-ug-plenum48__badge {{ display: inline-flex; align-items: center; gap: 10px; margin: 0 0 18px; padding: 8px 14px; border-radius: 999px; background: rgba(255,255,255,.9); border: 1px solid rgba(15,23,42,.12); font-size: 0.82rem; font-weight: 600; color: #334155; }}
.hero-ug-plenum48__dot {{ width: 8px; height: 8px; border-radius: 50%; background: #0f2744; }}
.hero-ug-plenum48__h1 {{ margin: 0 0 18px; font-size: clamp(1.5rem, 3.5vw, 2.35rem); line-height: 1.2; font-weight: 800; color: #0f172a; }}
.hero-ug-plenum48__accent {{ color: #1e3a8a; }}
.hero-ug-plenum48__sub {{ margin: 0 0 24px; max-width: 40em; font-size: 1.05rem; line-height: 1.55; color: #475569; }}
.hero-ug-plenum48__facts {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 26px; padding: 0; list-style: none; }}
.hero-ug-plenum48__fact {{ font-size: 0.78rem; font-weight: 700; padding: 7px 12px; border-radius: 8px; background: #fff; border: 1px solid #e2e8f0; color: #334155; }}
.hero-ug-plenum48__cta {{ display: inline-block; background: #a31830; color: #fff !important; padding: 14px 28px; border-radius: 8px; font-weight: 700; text-decoration: none; }}
@media (max-width: 900px) {{ .hero-ug-plenum48__inner {{ grid-template-columns: 1fr; }} .hero-ug-plenum48 {{ min-height: auto; }} }}
</style>
<main id="primary" class="site-main {pc}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H.escape(H1)}">
<meta itemprop="description" content="{H.escape(DESC)}">
<meta itemprop="inLanguage" content="ru-RU">

<section id="l24-hero-plenum48" class="hero-ug-plenum48" aria-label="{H.escape(H1)}">
<div class="hero-ug-plenum48__inner">
<div>
<div class="hero-ug-plenum48__badge"><span class="hero-ug-plenum48__dot" aria-hidden="true"></span> UG · Пленум № 48 · ст. 159 · 2026</div>
<h1 class="hero-ug-plenum48__h1"><span class="hero-ug-plenum48__accent">Пленум ВС № 48:</span> мошенничество, криптовалюта и цифровые рубли</h1>
<p class="hero-ug-plenum48__sub">{H.escape(SUB)}</p>
<ul class="hero-ug-plenum48__facts">
<li class="hero-ug-plenum48__fact">22.05.2026 · Тимошин</li>
<li class="hero-ug-plenum48__fact">ст. 159 УК</li>
<li class="hero-ug-plenum48__fact">ст. 171.6 · майнинг</li>
<li class="hero-ug-plenum48__fact">изъятие крипто</li>
</ul>
<a class="hero-ug-plenum48__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по уголовным рискам</a>
</div>
<div aria-hidden="true">{hero_svg}</div>
</div>
</section>

<section class="l24-intro-ug" aria-label="Кратко о теме">
<div class="l24-intro-ug__grid">
<div class="l24-intro-ug__text">
<p>Верховный суд готовит обновление разъяснений по <strong>мошенничеству</strong> в связи с цифровыми рублями, криптовалютой и майнингом. Параллельно расширяется уголовное преследование за незаконный майнинг и изъятие цифровых активов.</p>
<p>Материал для тех, кому грозит или уже возбуждено дело по <strong>ст. 159 УК РФ</strong>, и для бизнеса, работающего с цифровой валютой.</p>
<div class="l24-intro-ug__brief"><strong>Источник новости:</strong> заявление Николая Тимошина (РАПСИ, 22.05.2026); законопроект № 1193493-8 (I чтение, 28.05.2026).</div>
</div>
<div class="l24-intro-ug__decor">
<ul class="l24-intro-ug__chips">
<li class="l24-intro-ug__chip l24-intro-ug__chip--accent">Пленум № 48</li>
<li class="l24-intro-ug__chip">ст. 159</li>
<li class="l24-intro-ug__chip l24-intro-ug__chip--warn">ст. 171.6</li>
<li class="l24-intro-ug__chip">защита по УД</li>
</ul>
<p style="margin:0;font-size:0.9rem;color:#475569;line-height:1.5">Спрос Wordstat: «мошенничество ст 159» ~8 300; «защита по уголовному делу» ~4 970 показов/мес.</p>
</div>
</div>
</section>

<nav class="ym-toc" aria-label="Содержание статьи">
<p class="ym-toc__title">Содержание</p>
<ol class="ym-toc__list">{toc}</ol>
</nav>

<div class="l24-longread-wrap" itemprop="articleBody">
{longread}
{faq_html}
{jsonld_pre}
</div>
</main>
<!-- /wp:html -->
"""

OUT.write_text(page, encoding="utf-8")
print(f"Wrote {OUT} ({len(page)} bytes, {len(page)} chars)")
assert "<script>" not in page.lower()
