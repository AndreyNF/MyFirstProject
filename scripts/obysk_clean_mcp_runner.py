#!/usr/bin/env python3
"""State machine for clean obysk blob upload (5k chunks, reset on step 0).

Usage:
  python3 scripts/obysk_clean_mcp_runner.py init BLOB_ID
  python3 scripts/obysk_clean_mcp_runner.py next
  python3 scripts/obysk_clean_mcp_runner.py advance 'MCP response text'
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

STATE = Path("/workspace/.cursor/obysk-clean-upload-state.json")
BLOB_PREFIX = "/tmp/obysk-clean-mcp-"


def main() -> int:
    if len(sys.argv) < 2:
        print("init BLOB | next | advance RESP", file=sys.stderr)
        return 2
    cmd = sys.argv[1]

    if cmd == "init":
        blob = sys.argv[2]
        st = {"index": 1, "blob_id": blob, "total": 18, "sha256": None}
        STATE.write_text(json.dumps(st, indent=2), encoding="utf-8")
        print(json.dumps(st))
        return 0

    st = json.loads(STATE.read_text(encoding="utf-8"))
    idx = st["index"]

    if cmd == "next":
        if idx >= st["total"]:
            print(json.dumps({"done": True, "blob_id": st["blob_id"], "sha256": st.get("sha256")}))
            return 0
        path = Path(f"{BLOB_PREFIX}{idx:02d}.json")
        args = json.loads(path.read_text(encoding="utf-8"))
        out = Path("/workspace/.cursor/obysk-mcp-active-args.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": idx, "args_path": str(out), "chunk_len": len(args["chunk"]), "finalize": args["finalize"]}))
        return 0

    if cmd == "advance":
        resp = sys.argv[2] if len(sys.argv) > 2 else ""
        m = re.search(r"sha256:\s*(\S+)", resp)
        if m:
            st["sha256"] = m.group(1)
        st["index"] = idx + 1
        STATE.write_text(json.dumps(st, indent=2, ensure_ascii=False), encoding="utf-8")
        print(json.dumps(st))
        return 0

    return 2


if __name__ == "__main__":
    raise SystemExit(main())
