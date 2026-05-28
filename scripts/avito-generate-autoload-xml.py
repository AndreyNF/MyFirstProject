#!/usr/bin/env python3
"""Generate Avito Autoload XML (formatVersion 3) for Legis24 service ads.

Canonical field values: shared/legis24-avito-xml-rules.md
Validated via autoload.avito.ru/format/xmlcheck/
"""

from __future__ import annotations

import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

ADS = [
    {
        "id": "legis24-vozrazhenie-fns-001",
        "title": "Возражение на акт ФНС — за 24 часа Legis24",
        "price": 70000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961233_f22a669e05774c3e85e1d4f8f5d3349f.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961371_c5a0d7fbe20f41aa84422d7d74a2c8d2.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961502_ec5cfae180104270bc4a366c3758620f.png",
        ],
        "description": """Пришёл акт налоговой проверки или решение ФНС — срок на возражение ограничен.

Legis24 готовит возражение на акт камеральной или выездной проверки за 24 часа:
• разбор акта и материалов;
• правовая позиция с судебной практикой;
• документ, готовый к подаче.

70 000 ₽. Кейс: 150 млн → 43 млн после возражений.
По всей РФ, удалённо. Без НДС (УСН).

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-otvet-trebovanie-fns-002",
        "title": "Ответ на требование ФНС — от 10 000 ₽ за 24 ч",
        "price": 10000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961631430-trcjuqdovy.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961687_f8d140203f62407ba8c9402ee936f6ae.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961728873-evdgp0bm23f.png",
        ],
        "description": """ФНС запросила пояснения, документы или прислала уведомление?

Подготовим за 24 часа:
• ответ на требование о документах;
• пояснения по НДС, прибыли, УСН, НДФЛ;
• письмо в инспекцию с обоснованной позицией.

От 10 000 ₽. Legis24 — не шаблон, а позиция под вашу ситуацию.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-analiz-spor-003",
        "title": "Анализ налогового спора — заключение за 24 ч",
        "price": 25000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961780_d2741f7302354bf4bc7cd6571c3c021a.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961849_3e7b4040d36e43709f534c9a0e7e5ed9.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961904_fc088a27a05e4db8bf6abb6bfc01f42a.png",
        ],
        "description": """Нужно понять перспективы до суда или возражения?

Правовое заключение Legis24 за 24 часа:
• оценка позиции ФНС и ваших документов;
• прогноз рисков;
• рекомендации: возражение, иск, допрос.

25 000 ₽. Для собственника, финдиректора, юриста.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-isk-nalog-arbitr-004",
        "title": "Иск в арбитраж по налогу — за 24 часа",
        "price": 45000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779961958_17e37c77c20649049d078bc16f276829.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962029_34ccb6e90e624775933267a803400842.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962125_533cce6651ad4faa9291c696c6dc9fd7.png",
        ],
        "description": """УФНС отказала, срок обжалования на исходе?

Иск в арбитражный суд за 24 часа:
• исковое заявление по налоговому спору;
• расчёт требований;
• процессуальная стратегия.

45 000 ₽. Кейс: иск подан за 26 часов, дело принято.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-paket-akt-isk-005",
        "title": "Акт ФНС + иск в арбитраж — пакет 60 000 ₽",
        "price": 60000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962201_3da51964987c46a6ba36ced57b29dd72.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962261_e57e1885cd734adca06bc50401d2874c.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962308_708a301841c344d99f470ab8b2f5d4b1.png",
        ],
        "description": """Одна правовая позиция от акта до суда.

Пакет Legis24:
1. анализ акта ФНС;
2. возражение при необходимости;
3. иск в арбитраж.

60 000 ₽ (экономия 10 000 ₽). От 24 часов на ключевые документы.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-otzyv-isk-006",
        "title": "Отзыв на иск в арбитраж — за 24 часа",
        "price": 30000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962362151-bpqxnuryivq.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962432_8f529bb5e5d64691ac4524ba46e6014c.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962501177-o2p7ga3jni.png",
        ],
        "description": """Иск от контрагента, заседание через несколько дней?

Отзыв на иск за 24 часа:
• разбор иска и приложений;
• правовая позиция;
• ходатайства при необходимости.

30 000 ₽. Кейс: требования снижены на 2,1 млн ₽.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-buhgalteram-008",
        "title": "Бухгалтерам: акт ФНС — решение за 24 ч",
        "price": 25000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962550_c1d1204310d04942afa8d9cd40149153.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962597_22c790784dae4259b677775759c6b47d.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962658_ff9d47ddd0e44e3695d45979f38da180.png",
        ],
        "description": """Клиент получил акт ФНС или попал в арбитраж?

Передайте кейс Legis24 — стратегия за 24 часа, партнёрское вознаграждение до 30%.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
    {
        "id": "legis24-sk-poziciya-009",
        "title": "ФНС передала в СК — позиция за 24 часа",
        "price": 25000,
        "image_urls": [
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962715_fcb930a0acf448c796170bc5cdda75df.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962767_57e15a46d4724dd9a330c39b952ee96d.png",
            "https://advokat-vsem.online/wp-content/uploads/2026/05/1779962822_35ce5e2ba95447ceb775e754230020cd.png",
        ],
        "description": """Материалы в СКР, допрос через 2–3 дня?

За 24 часа: анализ документов, процессуальные нарушения, линия защиты до допроса.

25 000 ₽ (анализ). Не заменяем адвоката по УПК — даём правовую базу.

order@advokat-vsem.ru
https://advokat-vsem.ru""",
    },
]

CONTACT_PHONE = "79126994560"  # в кабинете может храниться; в карточке — только чат
CONTACT_METHOD = "В сообщениях"  # не «По телефону» / не «По телефону и в сообщениях»
ADDRESS = "Россия"
CATEGORY = "Предложение услуг"
# Иерархия Avito: Предложение услуг → Деловые услуги → Юридические услуги
SERVICE_TYPE = "Деловые услуги"
SERVICE_SUBTYPE = "Юридические услуги"  # обязательный «Тип услуги» (ServiceSubtype)
# Поля как в опубликованном объявлении id 8159283806 (Legis24)
SERVICE_SUBSPECIES = "Составление договоров, доверенностей, исков"
PREPAYMENT = "Нужна"
WORK_WITH_CONTRACT = "Да"
CONSULTATIONS = "Нет"
PLACE = "Удалённо"
WORK_EXPERIENCE = "4–7 лет"
DESCRIPTION_SUFFIX = "\n\nСвязь только в чате Avito, звонки не принимаем."


def _add_images(el: ET.Element, image_urls: str | list[str]) -> None:
    urls = [image_urls] if isinstance(image_urls, str) else image_urls
    images = ET.SubElement(el, "Images")
    for url in urls:
        ET.SubElement(images, "Image", url=url)


def _add_legal_service_fields(el: ET.Element) -> None:
    """Обязательные параметры категории «Юридические услуги» (по живому объявлению)."""
    ET.SubElement(el, "ServiceSubspecies").text = SERVICE_SUBSPECIES
    ET.SubElement(el, "WorkExperience").text = WORK_EXPERIENCE
    ET.SubElement(el, "Prepayment").text = PREPAYMENT
    ET.SubElement(el, "WorkWithContract").text = WORK_WITH_CONTRACT
    ET.SubElement(el, "Consultations").text = CONSULTATIONS
    ET.SubElement(el, "Place").text = PLACE


def build_xml() -> ET.Element:
    root = ET.Element("Ads", formatVersion="3", target="Avito.ru")
    today = date.today().isoformat()

    for ad in ADS:
        el = ET.SubElement(root, "Ad")
        ET.SubElement(el, "Id").text = ad["id"]
        ET.SubElement(el, "DateBegin").text = today
        ET.SubElement(el, "ListingFee").text = "Package"
        ET.SubElement(el, "AdStatus").text = "Free"
        ET.SubElement(el, "Category").text = CATEGORY
        ET.SubElement(el, "ServiceType").text = SERVICE_TYPE
        ET.SubElement(el, "ServiceSubtype").text = SERVICE_SUBTYPE
        _add_legal_service_fields(el)
        ET.SubElement(el, "Title").text = ad["title"]
        desc = ET.SubElement(el, "Description")
        desc.text = ad["description"].rstrip() + DESCRIPTION_SUFFIX
        _add_images(el, ad["image_urls"])
        ET.SubElement(el, "Price").text = str(ad["price"])
        ET.SubElement(el, "Address").text = ADDRESS
        ET.SubElement(el, "ContactPhone").text = CONTACT_PHONE
        ET.SubElement(el, "ContactMethod").text = CONTACT_METHOD
        ET.SubElement(el, "CompanyName").text = "Legis24"

    return root


def main() -> None:
    out = Path(__file__).resolve().parents[1] / "avito" / "autoload" / "legis24-new-ads.xml"
    out.parent.mkdir(parents=True, exist_ok=True)
    tree = ET.ElementTree(build_xml())
    ET.indent(tree, space="  ")
    tree.write(out, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {len(ADS)} ads to {out}")


if __name__ == "__main__":
    main()
