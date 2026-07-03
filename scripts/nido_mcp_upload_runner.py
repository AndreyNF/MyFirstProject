#!/usr/bin/env python3
"""NIDO blob upload state machine for agent MCP loop.

Usage:
  python3 scripts/nido_mcp_upload_runner.py prepare     # build queue + pending args
  python3 scripts/nido_mcp_upload_runner.py pending     # print current step args path
  python3 scripts/nido_mcp_upload_runner.py advance BLOB_ID [bytes_total]  # after MCP success
  python3 scripts/nido_mcp_upload_runner.py status

Agent: pending → json.load(args_path) → mcp_call_tool Kovcheg wordpress_content_blob_append
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/nido-upload-state.json")
PENDING = Path("/workspace/.cursor/nido-mcp-pending-args.json")
QUEUE = Path("/workspace/.cursor/nido-upload-queue.jsonl")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"index": 0, "blob_id": None, "sha256": None}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def build_queue() -> None:
    lines = []
    for step in range(5):
        out = subprocess.check_output(
            ["python3", "/workspace/scripts/nido_mcp_call_append.py", str(step)],
            text=True,
        )
        lines.append(out.strip())
    QUEUE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    save_state({"index": 0, "blob_id": None, "sha256": None})


def write_pending(step: int, blob_id: str = "") -> dict:
    cmd = ["python3", "/workspace/scripts/nido_mcp_call_append.py", str(step)]
    if blob_id:
        cmd.append(blob_id)
    args = json.loads(subprocess.check_output(cmd, text=True))
    PENDING.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    return args


def parse_blob(resp: str) -> tuple[str, int | None, str | None]:
    bid = ""
    m = re.search(r"blob_id:\s*(\S+)", resp)
    if m:
        bid = m.group(1)
    bt = None
    m2 = re.search(r"bytes_total:\s*(\d+)", resp)
    if m2:
        bt = int(m2.group(1))
    sha = None
    m3 = re.search(r"sha256:\s*(\S+)", resp)
    if m3:
        sha = m3.group(1)
    return bid, bt, sha


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    st = load_state()

    if cmd == "prepare":
        build_queue()
        args = write_pending(0)
        print(json.dumps({"ok": True, "step": 0, "args_path": str(PENDING), "chunk_len": len(args["chunk"])}))
        return 0

    if cmd == "pending":
        step = st["index"]
        if step >= 5:
            print(json.dumps({"done": True, "blob_id": st.get("blob_id"), "sha256": st.get("sha256")}))
            return 0
        args = write_pending(step, st.get("blob_id") or "")
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
