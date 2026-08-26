#!/usr/bin/env python3
"""Prepare 2k chunks for ARB SRO blob upload."""
from __future__ import annotations

import json
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-vs-sro-sozidanie.html")
OUT = Path("/tmp/arb-sro-2k")
CHUNK = 2000


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for start in range(0, len(html), CHUNK):
        chunk = html[start : start + CHUNK]
        finalize = start + CHUNK >= len(html)
        args: dict = {"chunk": chunk, "finalize": finalize}
        (OUT / f"{n:02d}.json").write_text(
            json.dumps(args, ensure_ascii=False), encoding="utf-8"
        )
        n += 1
    print(json.dumps({"chunks": n, "bytes": len(html)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
