#!/usr/bin/env python3
"""Upload steps START..END via Kovcheg MCP using subprocess curl to internal bridge.

Fallback: prints args path per step for agent mcp_call_tool.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def load_state() -> dict:
    if STATE.is_file():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {"next": 0, "blob_id": ""}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def parse_blob(resp: str) -> str:
    m = re.search(r"blob_id:\s*(\S+)", resp)
    return m.group(1) if m else ""


def mcp_append(args: dict) -> str:
    """Invoke MCP via agent tool bridge env if set."""
    fd = os.environ.get("CURSOR_MCP_FD")
    if not fd:
        raise RuntimeError("no MCP bridge")
    req = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": "wordpress_content_blob_append", "arguments": args},
    }
    os.write(int(fd), (json.dumps(req) + "\n").encode())
    return os.read(int(fd), 10_000_000).decode()


def main() -> int:
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 13
    s = load_state()
    blob_id = s.get("blob_id", "")
    results = []
    for step in range(start, end + 1):
        args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
        if step > 0:
            args["blob_id"] = blob_id
            args.pop("reset", None)
        out = Path(f"/workspace/.cursor/vs-mcp-step{step:02d}-args.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        results.append({"step": step, "path": str(out), "len": len(args["chunk"]), "finalize": bool(args.get("finalize"))})
    print(json.dumps({"blob_id": blob_id, "steps": results}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
