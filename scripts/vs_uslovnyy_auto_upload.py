#!/usr/bin/env python3
"""Upload all vs-uslovnyy blob chunks via Kovcheg MCP using agent tool bridge file.

Writes /tmp/vs-mcp-next.json with next chunk args; agent calls mcp_call_tool and runs:
  python3 scripts/vs_uslovnyy_auto_upload.py record 'MCP_RESPONSE'

Or run full loop if CURSOR_MCP_FD is set.
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
NEXT = Path("/tmp/vs-mcp-next.json")
MODE = os.environ.get("VS_UPLOAD_MODE", "4c")  # 4c | sub


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
        else:
            args["blob_id"] = blob_id
            args.pop("reset", None)
        return args
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def total_steps() -> int:
    return 4 if MODE == "4c" else 14


def mcp_append(args: dict) -> str:
    fd = os.environ.get("CURSOR_MCP_FD")
    if not fd:
        raise RuntimeError("no MCP bridge")
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": "wordpress_content_blob_append", "arguments": args},
    }
    os.write(int(fd), (json.dumps(req, ensure_ascii=False) + "\n").encode())
    return os.read(int(fd), 20_000_000).decode()


def cmd_next() -> int:
    s = load_state()
    step = s["next"]
    total = total_steps()
    if step >= total:
        print(json.dumps({"done": True, "blob_id": s.get("blob_id")}))
        return 0
    args = load_args(step, s.get("blob_id", ""))
    NEXT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "step": step,
                "total": total,
                "args_path": str(NEXT),
                "chunk_len": len(args["chunk"]),
                "finalize": bool(args.get("finalize")),
                "blob_id": args.get("blob_id"),
            },
            ensure_ascii=False,
        )
    )
    return 0


def cmd_record(resp: str) -> int:
    s = load_state()
    step = s["next"]
    bid = parse_blob(resp)
    if bid:
        s["blob_id"] = bid
    s["next"] = step + 1
    save_state(s)
    print(json.dumps(s, ensure_ascii=False))
    return 0


def cmd_run_all() -> int:
    s = {"next": 0, "blob_id": ""}
    save_state(s)
    total = total_steps()
    for step in range(total):
        args = load_args(step, s.get("blob_id", ""))
        resp = mcp_append(args)
        print(resp)
        bid = parse_blob(resp)
        if bid:
            s["blob_id"] = bid
        s["next"] = step + 1
        save_state(s)
    print(json.dumps({"done": True, "blob_id": s["blob_id"]}))
    return 0


def main() -> int:
    if len(sys.argv) < 2:
        print("next | record 'RESP' | run-all", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "next":
        return cmd_next()
    if cmd == "record":
        return cmd_record(sys.argv[2] if len(sys.argv) > 2 else sys.stdin.read())
    if cmd == "run-all":
        return cmd_run_all()
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
