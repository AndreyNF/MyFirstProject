#!/usr/bin/env python3
"""Upload one sub-chunk via Kovcheg by writing MCP request for agent bridge.

If KOVCHEG_MCP_HTTP_URL is set, POST directly. Otherwise prints args path.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.request
from pathlib import Path

SUB = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
STATE = Path("/workspace/.cursor/vs-uslovnyy-upload-state.json")


def load_state() -> dict:
    return json.loads(STATE.read_text(encoding="utf-8")) if STATE.is_file() else {"blob_id": "", "next": 0}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, indent=2), encoding="utf-8")


def load_args(step: int) -> dict:
    path = Path(f"/workspace/.cursor/vs-sub-mcp-{step:02d}.json")
    if path.is_file():
        return json.loads(path.read_text(encoding="utf-8"))
    s = load_state()
    args = json.loads((SUB / f"sub-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0:
        args["blob_id"] = s["blob_id"]
        args.pop("reset", None)
    return args


def main() -> int:
    step = int(sys.argv[1])
    args = load_args(step)
    url = os.environ.get("KOVCHEG_MCP_HTTP_URL")
    if url:
        body = json.dumps(
            {"jsonrpc": "2.0", "id": step, "method": "tools/call", "params": {"name": "wordpress_content_blob_append", "arguments": args}},
            ensure_ascii=False,
        ).encode()
        req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
        resp = urllib.request.urlopen(req).read().decode()
        print(resp)
        return 0
    out = Path(f"/tmp/vs-sub-upload-{step:02d}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "args_path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
