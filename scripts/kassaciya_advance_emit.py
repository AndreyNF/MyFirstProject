#!/usr/bin/env python3
"""Advance state from MCP response file and emit next args (one line JSON)."""
import json
import subprocess
import sys
from pathlib import Path

UPLOAD = Path("/workspace/scripts/kassaciya_mcp_upload.py")
PENDING = Path("/workspace/.cursor/kassaciya-mcp-pending.json")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: kassaciya_advance_emit.py '<mcp response>'", file=sys.stderr)
        return 2
    resp = sys.argv[1]
    st = subprocess.check_output(["python3", str(UPLOAD), "advance", resp], text=True).strip()
    meta = subprocess.check_output(["python3", str(UPLOAD), "pending"], text=True).strip()
    m = json.loads(meta)
    if m.get("done"):
        print(json.dumps({"done": True, "state": json.loads(st)}, ensure_ascii=False))
        return 0
    args = json.loads(PENDING.read_text(encoding="utf-8"))
    print(json.dumps({"step": m["step"], "total": m["total"], "finalize": m.get("finalize"), "args": args, "state": json.loads(st)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
