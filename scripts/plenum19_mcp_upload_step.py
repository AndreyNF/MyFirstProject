#!/usr/bin/env python3
"""Upload plenum19 blob step via stdin JSON to stdout MCP bridge (agent loop).

Usage:
  python3 plenum19_mcp_upload_step.py STEP [BLOB_ID]

Prints one JSON object with keys: mcp_server, mcp_tool, mcp_arguments
Agent must call mcp_call_tool with mcp_arguments (may be large).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path("/workspace/scripts/publish_plenum19_mcp_step.py")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: plenum19_mcp_upload_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    cmd = ["python3", str(SCRIPT), str(step)]
    if step > 0:
        if len(sys.argv) < 3:
            print("blob_id required", file=sys.stderr)
            return 2
        cmd.append(sys.argv[2])
    args = json.loads(subprocess.check_output(cmd, text=True))
    out = {
        "mcp_server": "Kovcheg",
        "mcp_tool": "wordpress_content_blob_append",
        "mcp_arguments": args,
        "meta": {
            "step": step,
            "chunk_len": len(args["chunk"]),
            "reset": bool(args.get("reset")),
            "finalize": bool(args.get("finalize")),
            "latin_st158": args["chunk"].count("st. 158"),
            "cyr_st158": args["chunk"].count("ст. 158"),
        },
    }
    path = Path(f"/tmp/plenum19_upload_step_{step}.json")
    path.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "envelope_path": str(path), **out["meta"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
