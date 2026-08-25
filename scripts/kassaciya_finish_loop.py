#!/usr/bin/env python3
"""Run remaining kassaciya blob steps: advance with response, emit next args JSON to stdout."""
import json
import subprocess
import sys
from pathlib import Path

UPLOAD = Path("/workspace/scripts/kassaciya_mcp_upload.py")
PENDING = Path("/workspace/.cursor/kassaciya-mcp-pending.json")


def advance(resp: str) -> dict:
    out = subprocess.check_output(["python3", str(UPLOAD), "advance", resp], text=True).strip()
    return json.loads(out)


def pending() -> dict:
    out = subprocess.check_output(["python3", str(UPLOAD), "pending"], text=True).strip()
    return json.loads(out)


def main() -> int:
    if len(sys.argv) < 2:
        meta = pending()
        if meta.get("done") or meta.get("step", 0) >= meta.get("total", 0):
            print(json.dumps({"done": True, "meta": meta}, ensure_ascii=False))
            return 0
        args = json.loads(PENDING.read_text(encoding="utf-8"))
        print(json.dumps({"step": meta["step"], "total": meta["total"], "finalize": meta.get("finalize"), "args": args}, ensure_ascii=False))
        return 0
    resp = sys.argv[1]
    st = advance(resp)
    meta = pending()
    if meta.get("done") or meta.get("step", 0) >= meta.get("total", 0):
        print(json.dumps({"done": True, "state": st, "meta": meta}, ensure_ascii=False))
        return 0
    args = json.loads(PENDING.read_text(encoding="utf-8"))
    print(json.dumps({"step": meta["step"], "total": meta["total"], "finalize": meta.get("finalize"), "args": args, "state": st}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
