#!/usr/bin/env python3
"""Validate MigSwap BLOG article.html against writing contract."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MIN_CHARS = 8500
MAX_CHARS = 9500
MIN_BOT_LINKS = 6
MAX_BOT_LINKS = 10
MIN_SITE_LINKS = 2
MAX_SITE_LINKS = 4

BOT_URL = "https://t.me/MigSwap_bot"
SITE_URL = "https://migswap.com"

FORBIDDEN_PATTERNS = [
    r"купить\s+usdt",
    r"курс\s+btc",
    r"доходност",
    r"прогноз\s+курса",
    r"лицензия\s+цб",
    r"обход\s+115",
]

ALLOWED_TAGS = {"h2", "h3", "p", "b", "i", "a", "ul", "ol", "li", "blockquote", "table", "tr", "td", "th", "thead", "tbody", "strong", "em", "br"}

DISCLAIMER_MARKERS = ["риск", "282", "migswap.com"]


def strip_tags(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    return re.sub(r"\s+", " ", text).strip()


def count_links(html: str, url: str) -> int:
    return len(re.findall(rf'href=["\']{re.escape(url)}[^"\']*["\']', html, re.I))


def check_forbidden_in_headers_and_lead(html: str) -> list[str]:
    errors = []
    lead_match = re.search(r"<p>(.*?)</p>", html, re.DOTALL | re.I)
    lead = lead_match.group(1) if lead_match else ""
    headers = re.findall(r"<h[23]>(.*?)</h[23]>", html, re.DOTALL | re.I)
    title_zone = lead + " " + " ".join(headers)
    for pat in FORBIDDEN_PATTERNS:
        if re.search(pat, title_zone, re.I):
            errors.append(f"Forbidden pattern in lead/H2/H3: {pat}")
    return errors


def check_tags(html: str) -> list[str]:
    errors = []
    for tag in re.findall(r"</?([a-z][a-z0-9]*)", html, re.I):
        if tag.lower() not in ALLOWED_TAGS:
            errors.append(f"Disallowed tag: {tag}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("article_html", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    html = args.article_html.read_text(encoding="utf-8")
    plain = strip_tags(html)
    char_count = len(plain)

    errors: list[str] = []
    warnings: list[str] = []

    if char_count < MIN_CHARS:
        errors.append(f"Too short: {char_count} < {MIN_CHARS}")
    if char_count > MAX_CHARS:
        errors.append(f"Too long: {char_count} > {MAX_CHARS}")

    bot_links = count_links(html, BOT_URL)
    site_links = count_links(html, SITE_URL)

    if bot_links < MIN_BOT_LINKS:
        errors.append(f"Bot links: {bot_links} < {MIN_BOT_LINKS}")
    if bot_links > MAX_BOT_LINKS:
        warnings.append(f"Bot links: {bot_links} > {MAX_BOT_LINKS}")
    if site_links < MIN_SITE_LINKS:
        errors.append(f"Site links: {site_links} < {MIN_SITE_LINKS}")
    if site_links > MAX_SITE_LINKS:
        warnings.append(f"Site links: {site_links} > {MAX_SITE_LINKS}")

    errors.extend(check_forbidden_in_headers_and_lead(html))
    errors.extend(check_tags(html))

    disclaimer_lower = html.lower()
    for marker in DISCLAIMER_MARKERS:
        if marker not in disclaimer_lower:
            errors.append(f"Missing disclaimer marker: {marker}")

    if "<h2>" not in html.lower():
        errors.append("Missing h2 sections")

    result = {
        "status": "OK" if not errors else "FAIL",
        "char_count": char_count,
        "bot_links": bot_links,
        "site_links": site_links,
        "errors": errors,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"QA: {result['status']}")
        print(f"Chars: {char_count}, bot: {bot_links}, site: {site_links}")
        for e in errors:
            print(f"ERROR: {e}")
        for w in warnings:
            print(f"WARN: {w}")

    return 0 if result["status"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
