#!/usr/bin/env python3
"""Fanta blob upload state machine — agent calls MCP with pending args JSON."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/fanta-upload-state.json")
PENDING = Path("/workspace/.cursor/fanta-mcp-pending.json")
CHUNKS = Path("/workspace/.cursor/fanta-blob-calls")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 0, "blob_id": None, "sha256": None, "bytes_total": 0}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def build_args(step: int, blob_id: str = "") -> dict:
    data = json.loads((CHUNKS / f"call-{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": data["chunk"], "finalize": bool(data.get("finalize"))}
    if step == 0:
        args["reset"] = True
    elif blob_id:
        args["blob_id"] = blob_id
    return args


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


def cmd_pending() -> int:
    st = load_state()
    step = st["index"]
    if step > 23:
        print(json.dumps({"done": True, **st}, ensure_ascii=False))
        return 0
    args = build_args(step, st.get("blob_id") or "")
    PENDING.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "args_path": str(PENDING),
                "chunk_len": len(args["chunk"]),
                "reset": bool(args.get("reset")),
                "finalize": bool(args.get("finalize")),
                "blob_id": args.get("blob_id"),
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


def cmd_init(step: int, blob_id: str, bytes_total: int = 0) -> int:
    st = {"index": step, "blob_id": blob_id, "sha256": None, "bytes_total": bytes_total}
    save_state(st)
    print(json.dumps(st, ensure_ascii=False))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "pending":
        return cmd_pending()
    if cmd == "advance" and len(sys.argv) >= 3:
        return cmd_advance(sys.argv[2])
    if cmd == "init" and len(sys.argv) >= 4:
        bt = int(sys.argv[4]) if len(sys.argv) > 4 else 0
        return cmd_init(int(sys.argv[2]), sys.argv[3], bt)
    if cmd == "status":
        print(json.dumps(load_state(), ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
