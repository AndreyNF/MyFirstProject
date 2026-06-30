#!/usr/bin/env python3
"""Prepare plenum-vs-19 page for MCP Kovcheg blob upload."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HTML_PATH = Path("/workspace/.cursor/page-content-natasha-plenum19.html")
OUT_DIR = Path("/workspace/.cursor/plenum19-blob-calls")
CHUNK = 18000

SLUG = "plenum-vs-19-cifrovoj-rubl-krazha-moshennichestvo-2026"
TITLE = "Пленум ВС № 19 (2026): цифровой рубль как предмет кражи — когда обман это не мошенничество"
EXCERPT = (
    "16.06.2026: Пленум ВС РФ № 19 разъяснил квалификацию хищений цифрового рубля "
    "и цифровых прав, отличие кражи от мошенничества и условия ст. 158.1 УК РФ. "
    "Защита при обвинении."
)


def strip_scripts(html: str) -> str:
    return re.sub(r"<script\b[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)


def main() -> int:
    text = strip_scripts(HTML_PATH.read_text(encoding="utf-8"))
    if "<script" in text.lower():
        print("ERROR: script tags remain", file=sys.stderr)
        return 1
    if not text.strip().startswith("<!-- wp:html -->"):
        text = "<!-- wp:html -->\n" + text
    if "<!-- /wp:html -->" not in text:
        text = text.rstrip() + "\n<!-- /wp:html -->\n"
    parts = [text[i : i + CHUNK] for i in range(0, len(text), CHUNK)]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for i, part in enumerate(parts):
        args: dict = {"chunk": part}
        if i == 0:
            args["reset"] = True
        if i == len(parts) - 1:
            args["finalize"] = True
        (OUT_DIR / f"{i:02d}.json").write_text(
            json.dumps(args, ensure_ascii=False), encoding="utf-8"
        )
    meta = {
        "slug": SLUG,
        "title": TITLE,
        "excerpt": EXCERPT,
        "parts": len(parts),
        "chars": len(text),
    }
    (OUT_DIR / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
