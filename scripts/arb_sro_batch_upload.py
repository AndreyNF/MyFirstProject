#!/usr/bin/env python3
"""State machine for arb-sro 2k blob upload (page 566).

Agent loop:
  python3 scripts/arb_sro_batch_upload.py status
  # mcp_call_tool Kovcheg wordpress_content_blob_append json.load(/tmp/arb-sro-mcp-next.json)
  python3 scripts/arb_sro_batch_upload.py advance 'MCP_RESPONSE'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/arb-sro-2k-state.json")
CHUNKS = Path("/tmp/arb-sro-2k")
NEXT = Path("/tmp/arb-sro-mcp-next.json")
BLOB = "9GPJWFouleTtzarVf3xgZwnY"


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 0, "blob_id": BLOB, "sha256": None, "bytes_total": 0}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_resp(text: str) -> tuple[str | None, int | None, str | None]:
    bid = sha = None
    bt = None
    if m := re.search(r"blob_id:\s*(\S+)", text):
        bid = m.group(1)
    if m2 := re.search(r"bytes_total:\s*(\d+)", text):
        bt = int(m2.group(1))
    if m3 := re.search(r"sha256:\s*(\S+)", text):
        sha = m3.group(1)
    return bid, bt, sha


def build_args(idx: int, blob_id: str) -> dict:
    d = json.loads((CHUNKS / f"{idx:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": d["chunk"]}
    if idx == 0:
        args["reset"] = True
    else:
        args["blob_id"] = blob_id
    if d.get("finalize"):
        args["finalize"] = True
    else:
        args["finalize"] = False
    return args


def cmd_status() -> int:
    st = load_state()
    idx = st["index"]
    if idx > 43:
        print(json.dumps({"done": True, **st}, ensure_ascii=False))
        return 0
    args = build_args(idx, st.get("blob_id", BLOB))
    NEXT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "index": idx,
                "chunk_len": len(args["chunk"]),
                "finalize": bool(args.get("finalize")),
                "args_path": str(NEXT),
                "blob_id": st.get("blob_id", BLOB),
                "bytes_total": st.get("bytes_total"),
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_advance(resp: str) -> int:
    st = load_state()
    bid, bt, sha = parse_resp(resp)
    if bid:
        st["blob_id"] = bid
    if bt is not None:
        st["bytes_total"] = bt
    if sha:
        st["sha256"] = sha
    st["index"] = st.get("index", 0) + 1
    save_state(st)
    print(json.dumps(st, ensure_ascii=False))
    return 0


def cmd_init_at(n: int) -> int:
    st = {"index": n, "blob_id": BLOB, "sha256": None, "bytes_total": 20974}
    save_state(st)
    print(json.dumps(st, ensure_ascii=False))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    if sys.argv[1] == "status":
        return cmd_status()
    if sys.argv[1] == "advance" and len(sys.argv) >= 3:
        return cmd_advance(sys.argv[2])
    if sys.argv[1] == "init_at" and len(sys.argv) >= 3:
        return cmd_init_at(int(sys.argv[2]))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
