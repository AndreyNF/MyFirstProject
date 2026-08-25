#!/usr/bin/env python3
"""Emit pending args JSON for one kassaciya blob step (stdout for CallDynamicTool)."""
import json
import subprocess
import sys


def main() -> int:
    r = subprocess.run(
        ["python3", "/workspace/scripts/kassaciya_mcp_upload.py", "pending"],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        print(r.stderr, file=sys.stderr)
        return r.returncode
    meta = json.loads(r.stdout.strip())
    if meta.get("done"):
        print(json.dumps({"done": True, **meta}, ensure_ascii=False))
        return 0
    args = json.load(open(meta["args_path"], encoding="utf-8"))
    print(json.dumps({"step": meta["step"], "args": args}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
