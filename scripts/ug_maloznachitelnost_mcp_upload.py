#!/usr/bin/env python3
"""Upload UG maloznachitelnost blob chunks 0-4 via Kovcheg MCP state machine.

Agent loop:
  python3 scripts/ug_maloznachitelnost_mcp_upload.py pending
  # mcp_call_tool Kovcheg wordpress_content_blob_append with json.load(args_path)
  python3 scripts/ug_maloznachitelnost_mcp_upload.py advance '<mcp response text>'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/ug-maloznachitelnost-upload-state.json")
PENDING = Path("/workspace/.cursor/ug-maloznachitelnost-mcp-pending.json")
ARGS_DIR = Path("/workspace/.cursor")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 0, "blob_id": None, "sha256": None, "bytes_total": None}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def get_args(step: int, blob_id: str | None) -> dict:
    args = json.loads((ARGS_DIR / f"ug-maloznachitelnost-mcp-args-{step}.json").read_text(encoding="utf-8"))
    if blob_id:
        args["blob_id"] = blob_id
    return args


def parse_blob(resp: str) -> tuple[str, int | None, str | None]:
    bid = ""
    m = re.search(r"blob_id[:\s]+(\S+)", resp)
    if m:
        bid = m.group(1).strip("`")
    bt = None
    m2 = re.search(r"bytes_total[:\s]+(\d+)", resp)
    if m2:
        bt = int(m2.group(1))
    sha = None
    m3 = re.search(r"sha256[:\s]+([a-f0-9]{64})", resp, re.I)
    if m3:
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
        if step >= 5:
            print(json.dumps({"done": True, **st}, ensure_ascii=False))
            return 0
        args = get_args(step, st.get("blob_id"))
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

    if cmd == "advance":
        resp = sys.argv[2] if len(sys.argv) > 2 else ""
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
        print(json.dumps(st, ensure_ascii=False))
        return 0

    print(f"unknown cmd: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
