#!/usr/bin/env python3
"""Upload page 434 SIP HTML via Kovcheg blob (12×5k parts after initial 18k chunk).

Agent loop:
  python3 scripts/sip_page434_upload.py build [BLOB_ID]
  python3 scripts/sip_page434_upload.py next
  python3 scripts/sip_page434_upload.py advance BLOB_ID [bytes_total]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PARTS_DIR = Path("/workspace/.cursor/sip-blob-mcp/parts3k")
STATE = Path("/tmp/sip_page434_state.json")
PAGE_ID = 434
EXCERPT = (
    "Постановление СИП от 20.03.2026: кассация отменила взыскание 766 млн ₽ за слоган "
    "на упаковке. Смешение, компенсация по ст. 1515, злоупотребление правом — что важно "
    "ответчику при иске по товарному знаку."
)


def build_payloads(initial_blob: str | None = None) -> int:
    parts = sorted(PARTS_DIR.glob("part-*.json"))
    if not parts:
        raise SystemExit("missing parts in .cursor/sip-blob-mcp/parts — run split first")
    STATE.write_text(
        json.dumps(
            {
                "index": 0,
                "blob_id": initial_blob,
                "total": len(parts),
                "page_id": PAGE_ID,
                "excerpt": EXCERPT,
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(
        json.dumps(
            {"ok": True, "chunks": len(parts), "blob_id": initial_blob, "page_id": PAGE_ID},
            ensure_ascii=False,
        )
    )
    return 0


def next_call() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    i = st["index"]
    parts = sorted(PARTS_DIR.glob("part-*.json"))
    if i >= len(parts):
        print(json.dumps({"done": True, "blob_id": st.get("blob_id")}, ensure_ascii=False))
        return 0
    args = json.loads(parts[i].read_text(encoding="utf-8"))
    if st.get("blob_id"):
        args["blob_id"] = st["blob_id"]
    print(json.dumps({"index": i, "arguments": args}, ensure_ascii=False))
    return 0


def advance(blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["index"] = st.get("index", 0) + 1
    STATE.write_text(json.dumps(st, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"advanced": st["index"], "blob_id": blob_id}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        bid = sys.argv[2] if len(sys.argv) > 2 else None
        raise SystemExit(build_payloads(bid))
    if cmd == "next":
        raise SystemExit(next_call())
    if cmd == "advance" and len(sys.argv) >= 3:
        bt = int(sys.argv[3]) if len(sys.argv) > 3 else None
        raise SystemExit(advance(sys.argv[2], bt))
    print("Usage: build [BLOB_ID] | next | advance BLOB_ID [bytes]", file=sys.stderr)
    raise SystemExit(2)
