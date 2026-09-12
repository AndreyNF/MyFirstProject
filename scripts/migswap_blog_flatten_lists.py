#!/usr/bin/env python3
"""Flatten nested lists in MigSwap article HTML for WordPress."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


def flatten_lists(html: str) -> str:
    """Remove nested ul/ol by flattening to single-level lists."""
    prev = None
    while prev != html:
        prev = html
        html = re.sub(
            r"<li>([^<]*)<ul>(.*?)</ul>",
            lambda m: "".join(f"<li>{item.strip()}</li>" for item in re.findall(r"<li>(.*?)</li>", m.group(2), re.DOTALL)),
            html,
            flags=re.DOTALL,
        )
        html = re.sub(
            r"<li>([^<]*)<ol>(.*?)</ol>",
            lambda m: "".join(f"<li>{item.strip()}</li>" for item in re.findall(r"<li>(.*?)</li>", m.group(2), re.DOTALL)),
            html,
            flags=re.DOTALL,
        )
    return html


def main() -> int:
    parser = argparse.ArgumentParser(description="Flatten lists in MigSwap article HTML")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    args = parser.parse_args()

    html = args.input.read_text(encoding="utf-8")
    result = flatten_lists(html)
    args.output.write_text(result, encoding="utf-8")
    print(f"Wrote {args.output} ({len(result)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
