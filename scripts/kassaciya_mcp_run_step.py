#!/usr/bin/env python3
"""Run kassaciya blob upload loop: pending -> print args path -> wait for MCP response file -> advance."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

UPLOAD = Path("/workspace/scripts/kassaciya_mcp_upload.py")
RESP = Path("/tmp/kassaciya-mcp-last-response.txt")


def pending_meta() -> dict:
    r = subprocess.run(
        ["python3", str(UPLOAD), "pending"],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(r.stdout.strip())


def advance(resp: str) -> dict:
    r = subprocess.run(
        ["python3", str(UPLOAD), "advance", resp],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(r.stdout.strip())


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: kassaciya_mcp_run_step.py emit|done|advance", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "emit":
        meta = pending_meta()
        if meta.get("done") or meta.get("step", 0) >= meta.get("total", 0):
            print(json.dumps({"done": True}))
            return 0
        args = json.loads(Path(meta["args_path"]).read_text(encoding="utf-8"))
        print(json.dumps({"step": meta["step"], "total": meta["total"], "args": args}, ensure_ascii=False))
        return 0
    if cmd == "done":
        meta = pending_meta()
        print(json.dumps(meta, ensure_ascii=False))
        return 0
    if cmd == "advance":
        resp = RESP.read_text(encoding="utf-8") if RESP.is_file() else sys.stdin.read()
        st = advance(resp)
        print(json.dumps(st, ensure_ascii=False))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
