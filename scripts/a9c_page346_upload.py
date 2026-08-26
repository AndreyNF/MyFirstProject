#!/usr/bin/env python3
"""Upload page 346 HTML via Kovcheg blob (11×a9c chunks).

Agent must call mcp_call_tool for each step:
  server=Kovcheg, toolName=wordpress_content_blob_append
  arguments from /tmp/a9c_mcp_{i}.json (add blob_id from previous response)

Then:
  wordpress_update_page_from_blob page_id=346, blob_id
  wordpress_update_page page_id=346, status=publish, excerpt=...
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/.cursor")
STATE = Path("/tmp/a9c_page346_state.json")
PAGE_ID = 346
EXCERPT = (
    "Что считается нарушением товарного знака, как собрать доказательства, "
    "взыскать компенсацию по ст. 1515 ГК РФ и защититься в арбитражном суде."
)


def build_payloads() -> int:
    total = 0
    for i in range(11):
        p = CHUNK_DIR / f"a9c{i}.txt"
        if not p.is_file():
            print(json.dumps({"error": f"missing {p}"}), file=sys.stderr)
            return 1
        chunk = p.read_text(encoding="utf-8")
        total += len(chunk)
        args: dict = {"chunk": chunk}
        if i == 0:
            args["reset"] = True
        if i == 10:
            args["finalize"] = True
        out = Path(f"/tmp/a9c_mcp_{i}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    STATE.write_text(json.dumps({"index": 0, "blob_id": None, "total": 11, "chars": total}), encoding="utf-8")
    print(json.dumps({"ok": True, "chunks": 11, "total_chars": total, "page_id": PAGE_ID}))
    return 0


def next_call() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    i = st["index"]
    if i >= st["total"]:
        print(json.dumps({"done": True, "blob_id": st.get("blob_id"), "bytes_total": st.get("bytes_total")}))
        return 0
    args = json.loads(Path(f"/tmp/a9c_mcp_{i}.json").read_text(encoding="utf-8"))
    if st.get("blob_id"):
        args["blob_id"] = st["blob_id"]
        args.pop("reset", None)
    print(json.dumps({"index": i, "tool": "wordpress_content_blob_append", "arguments": args}, ensure_ascii=False))
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
