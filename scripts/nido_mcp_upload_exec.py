#!/usr/bin/env python3
"""Load NIDO blob append args for step N; write MCP-ready envelope to stdout path meta only.

Usage:
  python3 scripts/nido_mcp_upload_exec.py STEP [BLOB_ID]

Writes /workspace/.cursor/nido-mcp-active.json and prints metadata JSON.
Agent must call mcp_call_tool Kovcheg wordpress_content_blob_append with arguments
from that file (json.load).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

OUT = Path("/workspace/.cursor/nido-mcp-active.json")
STATE = Path("/workspace/.cursor/nido-upload-state.json")


def load_step(step: int, blob_id: str = "") -> dict:
    cmd = ["python3", "/workspace/scripts/nido_mcp_call_append.py", str(step)]
    if blob_id:
        cmd.append(blob_id)
    out = subprocess.check_output(cmd, text=True)
    args = json.loads(out)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit(f"refusing PLACEHOLDER in step {step}")
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: nido_mcp_upload_exec.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = load_step(step, blob_id)
    OUT.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    meta = {
        "step": step,
        "args_path": str(OUT),
        "chunk_len": len(args["chunk"]),
        "reset": bool(args.get("reset")),
        "finalize": bool(args.get("finalize")),
        "blob_id": args.get("blob_id"),
    }
    print(json.dumps(meta, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
