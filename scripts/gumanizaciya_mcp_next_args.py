#!/usr/bin/env python3
"""Print arguments JSON for gumanizaciya blob step N."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-vs-gumanizaciya.html")
CHUNK_SIZE = 8000


def build_chunks() -> list[str]:
    html = HTML.read_text(encoding="utf-8")
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.S | re.I)
    return [html[i : i + CHUNK_SIZE] for i in range(0, len(html), CHUNK_SIZE)]


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: gumanizaciya_mcp_next_args.py <step> [blob_id]", file=sys.stderr)
        return 2
    idx = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    chunks = build_chunks()
    if idx < 0 or idx >= len(chunks):
        return 1
    args: dict = {"chunk": chunks[idx]}
    if idx == 0:
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
    if idx == len(chunks) - 1:
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
