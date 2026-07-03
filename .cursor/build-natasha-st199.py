#!/usr/bin/env python3
"""Assemble Natasha HTML for vs-st-199-uklonenie-nalogov article."""
import re
from pathlib import Path

SLUG = "vs-st-199-uklonenie-nalogov-75-dnej-zashchita-2026"
PAGE_CLASS = f"{SLUG}-page"
ROOT = Path("/workspace/.cursor")
MD = ROOT / "zhenya-longread-st199.md"
OUT = ROOT / "page-content-natasha-st199.html"

TITLE = "ВС 2026: отмена приговора по ст. 199 — 75 дней после ФНС"
DESC = (
    "ВС отменил приговор за уклонение от уплаты налогов: УД до 75 дней после решения ФНС — нарушение. "
    "Защита директора, ст. 199 и граница с налоговым спором."
)
H1 = "ВС 2026: отмена приговора по ст. 199 — 75 дней после решения ФНС и защита директора"
SUB = "Строительная фирма, 14 млн ₽ недоимки: почему ВС вернул дело и что проверить до возбуждения УД"

H2_IDS = {
    "Позиция Верховного суда: отмена приговора по ст. 199 и суть дела": "vs-st-199-poziciya",
    "Уклонение от уплаты налогов по ст. 199 УК РФ: состав и размеры": "st-199-sostav",
    "75 дней после решения ФНС: п. 3 ст. 32 НК и законность возбуждения УД": "75-dnej-fns",
    "Уклонение от уплаты налогов организацией и ответственность директора": "otvetstvennost-direktora",
    "Ответственность за уклонение от уплаты налогов: уголовная, административная, налоговая": "otvetstvennost-vidy",
    "Налоговый спор и уголовное преследование: когда ФНС не должна «перепрыгивать» в УК": "nalogovyj-spor-uk",
    "Ст. 159 vs ст. 199: мошенничество и уклонение от налогов (без дубля статей про 159/177)": "st-159-vs-199",
    "Защита по уголовному делу на новом рассмотрении: тактика для директора и бизнеса": "zashchita-novoe-rassmotrenie",
    "Консультация по уголовным рискам при проверке ФНС": "konsultaciya-fns",
}


def slugify_heading(title: str) -> str:
    return H2_IDS.get(title.strip(), re.sub(r"[^a-z0-9а-яё]+", "-", title.lower())[:48].strip("-"))


def inline_md(text: str) -> str:
    text = re.sub(
        r"\[([^\]]+)\]\((https?://[^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        text,
    )
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    return text


def md_link_to_cta(line: str) -> str:
    if "advokat-vsem.ru" not in line:
        return None
    m = re.search(r"\[([^\]]+)\]\((https://advokat-vsem\.ru/[^)]*)\)", line)
    if m:
        label = m.group(1)
        url = m.group(2)
        return f"""<aside class="ym-cta ym-cta--legis24" role="complementary">
<p class="ym-cta__text">{inline_md(label)}</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="{url}">Записаться на консультацию</a></p>
</aside>"""
    return None


def md_to_html(md: str, boris_html: str) -> str:
    lines = md.split("\n")
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# ") or line.startswith("**Title:") or line.startswith("**Description:"):
            i += 1
            continue
        if line.strip() == "BORIS_PLACEHOLDER":
            out.append(boris_html)
            i += 1
            continue
        cta = md_link_to_cta(line)
        if cta:
            out.append(cta)
            i += 1
            continue
        if line.startswith("## "):
            title = line[3:].strip()
            if title == "FAQ":
                i += 1
                while i < len(lines):
                    i += 1
                break
            hid = slugify_heading(title)
            out.append(f'<h2 id="{hid}">{inline_md(title)}</h2>')
            i += 1
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline_md(line[4:].strip())}</h3>")
            i += 1
            continue
        if line.strip() == "---":
            i += 1
            continue
        if line.strip().startswith("**") and "?" in line:
            i += 1
            continue
        if re.match(r"^\d+\.\s", line.strip()):
            out.append("<ol>")
            while i < len(lines) and re.match(r"^\d+\.\s", lines[i].strip()):
                item = re.sub(r"^\d+\.\s+", "", lines[i].strip())
                out.append(f"<li>{inline_md(item)}</li>")
                i += 1
            out.append("</ol>")
            continue
        if line.strip():
            para = [line]
            i += 1
            while i < len(lines) and lines[i].strip() and not lines[i].startswith("#") and lines[i].strip() != "---" and not re.match(r"^\d+\.\s", lines[i].strip()) and lines[i].strip() != "BORIS_PLACEHOLDER":
                if "advokat-vsem.ru" in lines[i] and lines[i].strip().startswith("["):
                    break
                para.append(lines[i])
                i += 1
            out.append(f"<p>{inline_md(' '.join(para))}</p>")
            continue
        i += 1
    return "\n".join(out)


def hero() -> str:
    return f"""
<section id="l24-hero-{SLUG}" class="hero-ug-st199" aria-label="{H1}">
<style>
.hero-ug-st199{{position:relative;min-height:88vh;display:flex;align-items:center;padding:112px 24px 72px;background:linear-gradient(165deg,#f8fafc 0%,#eef2f7 45%,#e8eef6 100%);font-family:system-ui,sans-serif;overflow:hidden}}
.hero-ug-st199__inner{{max-width:1200px;margin:0 auto;width:100%;display:grid;grid-template-columns:1.05fr .95fr;gap:44px;align-items:center}}
.hero-ug-st199__badge{{display:inline-flex;align-items:center;gap:10px;margin:0 0 18px;padding:8px 14px;border-radius:999px;background:rgba(255,255,255,.9);border:1px solid rgba(15,23,42,.12);font-size:.82rem;font-weight:600;color:#334155}}
.hero-ug-st199__dot{{width:8px;height:8px;border-radius:50%;background:#0f2744}}
.hero-ug-st199__h1{{margin:0 0 18px;font-size:clamp(1.5rem,3.5vw,2.35rem);line-height:1.2;font-weight:800;color:#0f172a}}
.hero-ug-st199__accent{{color:#1e3a8a}}
.hero-ug-st199__sub{{margin:0 0 24px;max-width:40em;font-size:1.05rem;line-height:1.55;color:#475569}}
.hero-ug-st199__facts{{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 26px;padding:0;list-style:none}}
.hero-ug-st199__fact{{font-size:.78rem;font-weight:700;padding:7px 12px;border-radius:8px;background:#fff;border:1px solid #e2e8f0;color:#334155}}
.hero-ug-st199__cta{{display:inline-block;background:#a31830;color:#fff!important;padding:14px 28px;border-radius:8px;font-weight:700;text-decoration:none}}
@media(max-width:900px){{.hero-ug-st199__inner{{grid-template-columns:1fr}}.hero-ug-st199{{min-height:auto}}}}
</style>
<div class="hero-ug-st199__inner">
<div>
<div class="hero-ug-st199__badge"><span class="hero-ug-st199__dot" aria-hidden="true"></span> UG · ст. 199 · ВС 28.05.2026</div>
<h1 class="hero-ug-st199__h1"><span class="hero-ug-st199__accent">ВС 2026:</span> отмена приговора по ст. 199 — 75 дней после ФНС</h1>
<p class="hero-ug-st199__sub">{SUB}</p>
<ul class="hero-ug-st199__facts">
<li class="hero-ug-st199__fact">14 млн ₽ · строительство</li>
<li class="hero-ug-st199__fact">ст. 199 УК</li>
<li class="hero-ug-st199__fact">п. 3 ст. 32 НК</li>
<li class="hero-ug-st199__fact">новое рассмотрение</li>
</ul>
<a class="hero-ug-st199__cta" href="https://advokat-vsem.ru/" target="_blank" rel="noopener noreferrer">Консультация по уголовным рискам</a>
</div>
<div aria-hidden="true">
<svg viewBox="0 0 440 380" xmlns="http://www.w3.org/2000/svg" width="100%" style="max-width:440px" role="img" aria-label="ст. 199 УК: 75 дней после ФНС">
<rect x="8" y="8" width="424" height="364" rx="14" fill="#f8fafc" stroke="#cbd5e1"/>
<rect x="140" y="24" width="160" height="44" rx="6" fill="#1e3a8a"/><text x="220" y="52" text-anchor="middle" fill="#fff" font-size="11" font-weight="700" font-family="system-ui,sans-serif">ВС · ст. 199</text>
<rect x="48" y="100" width="100" height="56" rx="8" fill="#fff" stroke="#94a3b8"/><text x="98" y="128" text-anchor="middle" fill="#0f2744" font-size="9" font-family="system-ui,sans-serif">решение ФНС</text>
<rect x="170" y="100" width="100" height="56" rx="8" fill="#fff" stroke="#1e40af"/><text x="220" y="128" text-anchor="middle" fill="#1e40af" font-size="9" font-weight="600" font-family="system-ui,sans-serif">75 дней</text>
<rect x="292" y="100" width="100" height="56" rx="8" fill="#fff" stroke="#a31830"/><text x="342" y="128" text-anchor="middle" fill="#a31830" font-size="9" font-weight="600" font-family="system-ui,sans-serif">УД · ст. 199</text>
<path d="M98 156 L98 200 L220 200 L220 156" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4 3"/>
<rect x="120" y="220" width="200" height="64" rx="10" fill="#fef2f2" stroke="#a31830" stroke-width="1.2"/>
<text x="220" y="248" text-anchor="middle" fill="#a31830" font-size="10" font-weight="700" font-family="system-ui,sans-serif">отмена приговора</text>
<text x="220" y="264" text-anchor="middle" fill="#475569" font-size="8" font-family="system-ui,sans-serif">новое рассмотрение</text>
<text x="220" y="330" text-anchor="middle" fill="#64748b" font-size="8" font-family="system-ui,sans-serif">28.05.2026 · vsrf.ru</text>
</svg>
</div>
</div>
</section>
"""


def boris() -> str:
    return """
<section id="l24-boris-st199-timeline" class="l24-boris-st199" aria-label="Хронология: от проверки ФНС к возбуждению УД">
<style>
.l24-boris-st199{margin:48px 0;font-family:system-ui,sans-serif}
.l24-boris-st199__shell{background:linear-gradient(148deg,#0f2744 0%,#152a45 52%,#1a365d 100%);border:1px solid rgba(236,201,75,.24);border-radius:14px;padding:32px 28px 26px;color:#e2e8f0}
.l24-boris-st199__eyebrow{margin:0 0 8px;font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#ecc94b}
.l24-boris-st199__title{margin:0 0 10px;font-size:clamp(1.15rem,2.4vw,1.42rem);line-height:1.25;color:#fff;font-weight:700}
.l24-boris-st199__lead{margin:0 0 24px;font-size:.95rem;line-height:1.55;color:#a0aec0;max-width:68ch}
.l24-boris-st199__grid{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
.l24-boris-st199__node{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:12px 10px;text-align:center}
.l24-boris-st199__year{display:block;font-size:.68rem;font-weight:700;color:#ecc94b;margin-bottom:6px}
.l24-boris-st199__label{font-size:.72rem;line-height:1.35;color:#cbd5e1}
@media(max-width:800px){.l24-boris-st199__grid{grid-template-columns:1fr 1fr}}
</style>
<div class="l24-boris-st199__shell">
<p class="l24-boris-st199__eyebrow">UG · процедура 2022–2026</p>
<h3 class="l24-boris-st199__title">Законный маршрут: ФНС → 75 дней → СК → ст. 199</h3>
<p class="l24-boris-st199__lead">В деле строительной фирмы УД возбудили <strong>06.10.2022</strong> — до вступления решения ФНС в силу. ВС <strong>26.05.2026</strong> отменил приговор.</p>
<div class="l24-boris-st199__grid" role="list">
<div class="l24-boris-st199__node" role="listitem"><span class="l24-boris-st199__year">01.2022</span><span class="l24-boris-st199__label">акт ВНП</span></div>
<div class="l24-boris-st199__node" role="listitem"><span class="l24-boris-st199__year">05–06.22</span><span class="l24-boris-st199__label">материалы в СК</span></div>
<div class="l24-boris-st199__node" role="listitem"><span class="l24-boris-st199__year">10.2022</span><span class="l24-boris-st199__label">возбуждение УД</span></div>
<div class="l24-boris-st199__node" role="listitem"><span class="l24-boris-st199__year">09.2022</span><span class="l24-boris-st199__label">решение ФНС</span></div>
<div class="l24-boris-st199__node" role="listitem"><span class="l24-boris-st199__year">05.2026</span><span class="l24-boris-st199__label">отмена ВС</span></div>
</div>
</div>
</section>
"""


def faq_section() -> str:
    return """
<section class="l24-faq-ug" id="l24-faq-st199" aria-label="Частые вопросы">
<h2>Частые вопросы</h2>
<div class="l24-faq-ug__item"><p class="l24-faq-ug__q">Можно ли осудить директора по ст. 199, если уголовное дело возбудили до истечения 75 дней после решения ФНС?</p><p class="l24-faq-ug__a">По позиции ВС от 26–28.05.2026 — нет: такое возбуждение — существенное нарушение порядка; при установлении дефекта суды отменяют приговор и направляют дело на новое рассмотрение.</p></div>
<div class="l24-faq-ug__item"><p class="l24-faq-ug__q">Чем отличается ответственность за налоговые правонарушения по НК от ст. 199 УК?</p><p class="l24-faq-ug__a">НК — доначисление, пени, штрафы. УК — умышленное уклонение после вступления решения в силу, 75 рабочих дней на уплату и передачи материалов по ст. 32 НК.</p></div>
<div class="l24-faq-ug__item"><p class="l24-faq-ug__q">Кого привлекают по уклонению от уплаты налогов организацией?</p><p class="l24-faq-ug__a">Генерального директора, лиц с правом подписи, главбуха — при доказанности участия и умысла.</p></div>
<div class="l24-faq-ug__item"><p class="l24-faq-ug__q">Помогает ли частичная уплата недоимки при защите по ст. 199?</p><p class="l24-faq-ug__a">Может смягчить наказание (ст. 61 УК), но не заменяет оспаривание преждевременного возбуждения. В деле 2026 года ВС отменил приговор несмотря на частичную уплату.</p></div>
<div class="l24-faq-ug__item"><p class="l24-faq-ug__q">Что делать после отмены приговора Верховным судом?</p><p class="l24-faq-ug__a">Готовить линию на новом рассмотрении: процесс (75 дней, ст. 32 НК), затем материальные доводы. Вести единый календарь с налоговым спором и платежами на ЕНП.</p></div>
</section>
<aside class="ym-cta ym-cta--legis24 ym-cta--bottom" role="complementary">
<p class="ym-cta__text">Юридическая помощь по уголовным делам: ст. 199, проверка ФНС, защита директора.</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/">Оставить заявку</a></p>
</aside>
"""


def page_css() -> str:
    return f"""
.breadcrumbs,.breadcrumb,.woocommerce-breadcrumb,.rank-math-breadcrumb,.yoast-breadcrumb,
.entry-header,.page-title-section,.entry-title,.main_title,h1.entry-title{{display:none!important}}
#primary,.site-main,.site-content,#content,.content-area{{padding-top:0!important;margin-top:0!important}}
#sidebar,.sidebar,#secondary{{display:none!important}}
.{PAGE_CLASS} .entry-content{{max-width:none!important;width:100%!important;padding:0!important}}
.{PAGE_CLASS} .l24-longread-wrap{{max-width:820px;margin:0 auto;padding:48px 24px 80px;font-size:1.05rem;line-height:1.65;color:#1a202c}}
.{PAGE_CLASS} h2{{margin-top:2.5em;color:#1a365d;font-size:1.45rem}}
.{PAGE_CLASS} h3{{margin-top:1.5em;color:#2c5282;font-size:1.15rem}}
.{PAGE_CLASS} a{{color:#1e40af}}
.l24-intro-ug{{max-width:1200px;margin:0 auto;padding:40px 24px 8px;font-family:system-ui,sans-serif}}
.l24-intro-ug__grid{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(260px,.9fr);gap:28px}}
.l24-intro-ug__text{{border-left:4px solid #0f2744;padding:4px 0 4px 22px}}
.l24-intro-ug__text p{{margin:0 0 14px;font-size:1.02rem;line-height:1.6;color:#334155}}
.l24-intro-ug__brief{{background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:16px 18px;margin-top:16px;font-size:.95rem}}
.l24-intro-ug__decor{{background:linear-gradient(160deg,#f1f5f9 0%,#fff 100%);border:1px solid #e2e8f0;border-radius:12px;padding:18px}}
.l24-intro-ug__chips{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 14px;padding:0;list-style:none}}
.l24-intro-ug__chip{{font-size:.72rem;font-weight:700;padding:6px 10px;border-radius:999px;background:#fff;border:1px solid #cbd5e1;color:#475569}}
.l24-intro-ug__chip--accent{{border-color:#1e40af;color:#1e40af}}
.l24-intro-ug__chip--warn{{border-color:#a31830;color:#a31830}}
.ym-toc{{max-width:820px;margin:24px auto 0;padding:0 24px 32px;text-align:center;font-family:system-ui,sans-serif}}
.ym-toc__title{{font-size:.8rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#64748b;margin:0 0 12px}}
.ym-toc__list{{list-style:none;padding:0;margin:0;display:flex;flex-wrap:wrap;justify-content:center;gap:8px}}
.ym-toc__list a{{display:inline-block;padding:8px 12px;border-radius:8px;background:#f1f5f9;color:#1e40af;text-decoration:none;font-size:.88rem;font-weight:600}}
.ym-cta{{margin:28px 0;padding:22px 24px;border-radius:10px;background:linear-gradient(135deg,#f8fafc,#edf2f7);border:1px solid #cbd5e1;border-left:4px solid #a31830}}
.ym-cta--legis24{{border-left-color:#1e3a8a;background:linear-gradient(135deg,#eff6ff,#f8fafc)}}
.ym-cta__text{{margin:0 0 14px;line-height:1.55;color:#334155}}
.ym-cta__btn{{display:inline-block;background:#a31830;color:#fff!important;padding:12px 22px;border-radius:8px;font-weight:700;text-decoration:none}}
.l24-faq-ug{{margin-top:2.5em;padding:28px 24px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px}}
.l24-faq-ug h2{{margin-top:0!important}}
.l24-faq-ug__item{{margin-bottom:18px;padding-bottom:18px;border-bottom:1px solid #e2e8f0}}
.l24-faq-ug__q{{margin:0 0 8px;font-size:1.05rem;color:#1a365d;font-weight:600}}
.l24-faq-ug__a{{margin:0;color:#334155}}
@media(max-width:900px){{.l24-intro-ug__grid{{grid-template-columns:1fr}}}}
"""


def intro() -> str:
    return """
<section class="l24-intro-ug" aria-label="Кратко о теме">
<div class="l24-intro-ug__grid">
<div class="l24-intro-ug__text">
<p>Верховный суд <strong>28 мая 2026 года</strong> сообщил об отмене приговора по <strong>ст. 199 УК РФ</strong>: уголовное дело возбудили до истечения <strong>75 рабочих дней</strong> после вступления в силу решения ФНС.</p>
<p>Материал для руководителей и директоров при проверке и возбуждении дела по <strong>уклонению от уплаты налогов</strong>.</p>
<div class="l24-intro-ug__brief"><strong>Источник:</strong> <a href="https://vsrf.ru/press_center/news/35926/" target="_blank" rel="noopener noreferrer">пресс-релиз ВС от 28.05.2026</a>.</div>
</div>
<div class="l24-intro-ug__decor">
<ul class="l24-intro-ug__chips">
<li class="l24-intro-ug__chip l24-intro-ug__chip--accent">ст. 199 УК</li>
<li class="l24-intro-ug__chip">75 дней</li>
<li class="l24-intro-ug__chip l24-intro-ug__chip--warn">директор</li>
<li class="l24-intro-ug__chip">защита по УД</li>
</ul>
<p style="margin:0;font-size:.9rem;color:#475569">Wordstat: «уклонение от уплаты налогов» ~7 600; «защита по уголовному делу» ~4 900 показов/мес.</p>
</div>
</div>
</section>
"""


def main():
    raw = MD.read_text(encoding="utf-8")
    start = raw.find("## Полный текст")
    md_body = raw[start + len("## Полный текст") :].strip() if start >= 0 else raw
    md_body = re.sub(r"^## FAQ[\s\S]*$", "", md_body).strip()
    insert_at = md_body.find("## Налоговый спор и уголовное преследование")
    if insert_at > 0:
        md_body = md_body[:insert_at] + "BORIS_PLACEHOLDER\n\n" + md_body[insert_at:]

    content = md_to_html(md_body, boris())
    toc = """<nav class="ym-toc" aria-label="Содержание"><p class="ym-toc__title">Содержание</p><ol class="ym-toc__list">
<li><a href="#vs-st-199-poziciya">Позиция ВС</a></li>
<li><a href="#st-199-sostav">Ст. 199 УК</a></li>
<li><a href="#75-dnej-fns">75 дней после ФНС</a></li>
<li><a href="#otvetstvennost-direktora">Директор</a></li>
<li><a href="#nalogovyj-spor-uk">Налоговый спор</a></li>
<li><a href="#zashchita-novoe-rassmotrenie">Защита</a></li>
<li><a href="#l24-faq-st199">FAQ</a></li>
</ol></nav>"""

    html = f"""<!-- wp:html -->
<style>
{page_css()}
</style>
<main id="primary" class="site-main {PAGE_CLASS}" role="main" tabindex="-1" itemscope itemtype="https://schema.org/Article">
<meta itemprop="headline" content="{H1}">
<meta itemprop="description" content="{DESC}">
<meta itemprop="inLanguage" content="ru-RU">
{hero()}
{intro()}
{toc}
<div class="l24-longread-wrap" itemprop="articleBody">
{content}
<aside class="ym-cta" role="complementary">
<p class="ym-cta__text">После вызова по ст. 199 не откладывайте проверку календаря 75 дней — первые процессуальные ошибки следствия задают рамку дела.</p>
<p class="ym-cta__actions"><a class="ym-cta__btn" href="https://advokat-vsem.ru/">Записаться на консультацию</a></p>
</aside>
{faq_section()}
</div>
</main>
<!-- /wp:html -->
"""
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} ({len(html)} chars)")


if __name__ == "__main__":
    main()
