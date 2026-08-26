#!/usr/bin/env python3
"""Kreditor page 581 blob upload state machine (4 chunks).

Agent loop:
  python3 scripts/kreditor_mcp_upload.py pending
  # CallDynamicTool Kovcheg wordpress_content_blob_append json.load(pending path)
  python3 scripts/kreditor_mcp_upload.py advance '<mcp response>'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/kreditor-upload-state.json")
PENDING = Path("/workspace/.cursor/kreditor-mcp-pending.json")
STEPS = Path("/tmp")
TOTAL = 4


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 0, "blob_id": None, "sha256": None, "bytes_total": None}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_blob(resp: str) -> tuple[str | None, int | None, str | None]:
    bid = sha = None
    bt = None
    if m := re.search(r"blob_id[:\s]+(\S+)", resp):
        bid = m.group(1).strip("`")
    if m2 := re.search(r"bytes_total[:\s]+(\d+)", resp):
        bt = int(m2.group(1))
    if m3 := re.search(r"sha256[:\s]+([a-f0-9]{64})", resp, re.I):
        sha = m3.group(1)
    return bid, bt, sha


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    st = load_state()

    if cmd == "pending":
        step = st["index"]
        if step >= TOTAL:
            print(json.dumps({"done": True, "total": TOTAL, **st}, ensure_ascii=False))
            return 0
        args = json.loads((STEPS / f"kreditor-blob-step-{step}.json").read_text(encoding="utf-8"))
        if step > 0 and st.get("blob_id"):
            args["blob_id"] = st["blob_id"]
            args.pop("reset", None)
        PENDING.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(
            json.dumps(
                {
                    "step": step,
                    "total": TOTAL,
                    "args_path": str(PENDING),
                    "chunk_len": len(args["chunk"]),
                    "finalize": bool(args.get("finalize")),
                    "reset": bool(args.get("reset")),
                },
                ensure_ascii=False,
            )
        )
        return 0

    if cmd == "advance":
        resp = sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read()
        bid, bt, sha = parse_blob(resp)
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

    if cmd == "status":
        print(json.dumps({"total": TOTAL, **st}, ensure_ascii=False))
        return 0

    print(f"unknown cmd: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
