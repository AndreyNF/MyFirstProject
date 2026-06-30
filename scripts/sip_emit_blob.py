#!/usr/bin/env python3
"""Emit wordpress_content_blob_append args for sip page chunk step."""
from __future__ import annotations

import json
import sys
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-sip-sinergetik.html")
CHUNK_SIZE = 18000


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: sip_emit_blob.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    html = HTML.read_text(encoding="utf-8")
    chunks = [html[i : i + CHUNK_SIZE] for i in range(0, len(html), CHUNK_SIZE)]
    if step < 0 or step >= len(chunks):
        print(f"invalid step {step}, max {len(chunks) - 1}", file=sys.stderr)
        return 2
    args: dict = {"chunk": chunks[step]}
    if step == 0:
        args["reset"] = True
    else:
        if not blob_id:
            print("blob_id required for step > 0", file=sys.stderr)
            return 2
        args["blob_id"] = blob_id
    if step == len(chunks) - 1:
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
