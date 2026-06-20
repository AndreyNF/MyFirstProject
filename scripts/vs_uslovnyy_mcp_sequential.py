#!/usr/bin/env python3
"""Sequential blob upload: loads JSON args and calls Kovcheg MCP append.

Uses CURSOR_MCP_FD if available; otherwise prints args path for agent.
Usage: vs_uslovnyy_mcp_sequential.py STEP
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

BASE_4C = Path("/workspace/.cursor/blob-args-vs-uslovnyy")
SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")
MODE = os.environ.get("VS_UPLOAD_MODE", "sub")  # sub | 4c


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 0, "blob_id": ""}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def parse_blob(resp: str) -> str:
    m = re.search(r"blob_id:\s*(\S+)", resp)
    return m.group(1) if m else ""


def load_args(step: int, blob_id: str = "") -> dict:
    if MODE == "4c":
        args = json.loads((BASE_4C / f"chunk-{step:02d}.json").read_text(encoding="utf-8"))
        if step == 0:
            args["reset"] = True
        elif blob_id:
            args["blob_id"] = blob_id
            args.pop("reset", None)
        return args
    path = Path(f"/workspace/.cursor/vs-sub-mcp-{step:02d}.json")
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    s = load_state()
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = s.get("blob_id") or blob_id
        args.pop("reset", None)
    return args


def mcp_append(args: dict) -> str:
    fd = os.environ.get("CURSOR_MCP_FD")
    if not fd:
        raise RuntimeError("CURSOR_MCP_FD not set")
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": "wordpress_content_blob_append", "arguments": args},
    }
    os.write(int(fd), (json.dumps(req, ensure_ascii=False) + "\n").encode())
    return os.read(int(fd), 20_000_000).decode()


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs_uslovnyy_mcp_sequential.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    s = load_state()
    blob_id = sys.argv[2] if len(sys.argv) > 2 else s.get("blob_id", "")
    args = load_args(step, blob_id)
    out = Path(f"/tmp/vs-mcp-append-{step:02d}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    if os.environ.get("CURSOR_MCP_FD"):
        resp = mcp_append(args)
        print(resp)
        bid = parse_blob(resp)
        if bid:
            s["blob_id"] = bid
        s["next"] = step + 1
        save_state(s)
        return 0
    print(json.dumps({"step": step, "args_path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
