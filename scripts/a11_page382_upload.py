#!/usr/bin/env python3
"""Upload page 382 HTML via Kovcheg blob (12×6k parts from a11-chunk files).

Agent loop:
  python3 scripts/a11_page382_upload.py build
  python3 scripts/a11_page382_upload.py next   # → JSON with arguments for mcp_call_tool
  # mcp_call_tool wordpress_content_blob_append
  python3 scripts/a11_page382_upload.py advance BLOB_ID [bytes_total]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/.cursor")
STATE = Path("/tmp/a11_page382_state.json")
PAGE_ID = 382
PARTS_DIR = Path("/tmp")
EXCERPT = (
    "Когда арбитражный управляющий оспаривает сделки должника в банкротстве: "
    "сроки по ст. 61.1–61.5, подозрительные и с предпочтением сделки, "
    "заявление в арбитражный суд и последствия для должника. Консультация по защите."
)


def build_payloads() -> int:
    parts = sorted(PARTS_DIR.glob("a11_part_*.txt"))
    if len(parts) != 12:
        # build parts from 4×18k chunks
        SUB = 6000
        parts = []
        texts = []
        for fi in range(4):
            texts.append((CHUNK_DIR / f"a11-chunk-{fi}.txt").read_text(encoding="utf-8"))
        flat = []
        for text in texts:
            for j in range(0, len(text), SUB):
                flat.append(text[j : j + SUB])
        for i, ch in enumerate(flat):
            (PARTS_DIR / f"a11_part_{i:02d}.txt").write_text(ch, encoding="utf-8")
        parts = sorted(PARTS_DIR.glob("a11_part_*.txt"))
    total = 0
    for i, p in enumerate(parts):
        chunk = p.read_text(encoding="utf-8")
        total += len(chunk)
        args: dict = {"chunk": chunk}
        if i == 0:
            args["reset"] = True
        if i == len(parts) - 1:
            args["finalize"] = True
        out = Path(f"/tmp/a11_mcp_{i}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    STATE.write_text(
        json.dumps({"index": 0, "blob_id": None, "total": len(parts), "chars": total}),
        encoding="utf-8",
    )
    print(json.dumps({"ok": True, "chunks": len(parts), "total_chars": total, "page_id": PAGE_ID}))
    return 0


def next_call() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    i = st["index"]
    if i >= st["total"]:
        print(json.dumps({"done": True, "blob_id": st.get("blob_id"), "bytes_total": st.get("bytes_total")}))
        return 0
    args = json.loads(Path(f"/tmp/a11_mcp_{i}.json").read_text(encoding="utf-8"))
    if st.get("blob_id"):
        args["blob_id"] = st["blob_id"]
        args.pop("reset", None)
    print(json.dumps({"index": i, "arguments": args}, ensure_ascii=False))
    return 0


def advance(blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["index"] = st.get("index", 0) + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps({"advanced": st["index"], "blob_id": blob_id}))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        raise SystemExit(build_payloads())
    if cmd == "next":
        raise SystemExit(next_call())
    if cmd == "advance" and len(sys.argv) >= 3:
        bid = sys.argv[2]
        bt = int(sys.argv[3]) if len(sys.argv) > 3 else None
        raise SystemExit(advance(bid, bt))
    print("Usage: build | next | advance BLOB_ID [bytes]", file=sys.stderr)
    raise SystemExit(2)
