#!/usr/bin/env python3
"""Queue/state helper for a9c blob upload to page 346."""
from __future__ import annotations

import json
import sys
from pathlib import Path

CHUNK_DIR = Path("/workspace/.cursor")
STATE = Path("/tmp/a9c_blob_state.json")


def build_state() -> int:
    chunks = []
    for i in range(11):
        p = CHUNK_DIR / f"a9c{i}.txt"
        if not p.is_file():
            print(json.dumps({"error": f"missing {p}"}), file=sys.stderr)
            return 1
        chunks.append(str(p))
    STATE.write_text(
        json.dumps({"index": 0, "blob_id": None, "chunks": chunks, "total": 11}),
        encoding="utf-8",
    )
    print(json.dumps({"ok": True, "total": 11}))
    return 0


def next_args() -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    i = st["index"]
    if i >= st["total"]:
        print(json.dumps({"done": True, "blob_id": st.get("blob_id")}))
        return 0
    chunk = Path(st["chunks"][i]).read_text(encoding="utf-8")
    payload: dict = {"chunk": chunk}
    if i == 0:
        payload["reset"] = True
    elif st.get("blob_id"):
        payload["blob_id"] = st["blob_id"]
    if i == st["total"] - 1:
        payload["finalize"] = True
    print(
        json.dumps(
            {"index": i, "total": st["total"], "chunk_len": len(chunk), "arguments": payload},
            ensure_ascii=False,
        )
    )
    return 0


def advance(blob_id: str, bytes_total: int | None = None) -> int:
    st = json.loads(STATE.read_text(encoding="utf-8"))
    st["blob_id"] = blob_id
    if bytes_total is not None:
        st["bytes_total"] = bytes_total
    st["index"] = st.get("index", 0) + 1
    STATE.write_text(json.dumps(st), encoding="utf-8")
    print(json.dumps({"advanced": st["index"], "blob_id": blob_id, "bytes_total": bytes_total}))
    return 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    if cmd == "build":
        raise SystemExit(build_state())
    if cmd == "next":
        raise SystemExit(next_args())
    if cmd == "advance" and len(sys.argv) >= 3:
        bid = sys.argv[2]
        bt = int(sys.argv[3]) if len(sys.argv) > 3 else None
        raise SystemExit(advance(bid, bt))
    print("Usage: build | next | advance BLOB_ID [bytes]", file=sys.stderr)
    raise SystemExit(2)
