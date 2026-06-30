#!/usr/bin/env python3
"""Print MCP append args for A10 chunks (agent calls mcp_call_tool per line)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

DIR = Path("/workspace/.cursor/a10-blob-calls")
STATE = Path("/tmp/a10_blob_state.json")


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "init"
    if cmd == "init":
        STATE.write_text(json.dumps({"index": 0, "blob_id": None}), encoding="utf-8")
        print(json.dumps({"ok": True, "state": str(STATE)}))
        return 0
    if cmd == "next":
        st = json.loads(STATE.read_text(encoding="utf-8"))
        i = st["index"]
        if i > 3:
            print(json.dumps({"done": True, "blob_id": st.get("blob_id")}))
            return 0
        args = json.loads((DIR / f"{i:02d}.json").read_text(encoding="utf-8"))
        if st.get("blob_id"):
            args["blob_id"] = st["blob_id"]
            args.pop("reset", None)
        print(json.dumps({"index": i, "arguments": args}, ensure_ascii=False))
        return 0
    if cmd == "advance" and len(sys.argv) >= 3:
        st = json.loads(STATE.read_text(encoding="utf-8"))
        st["blob_id"] = sys.argv[2]
        if len(sys.argv) > 3:
            st["bytes_total"] = int(sys.argv[3])
        if len(sys.argv) > 4:
            st["sha256"] = sys.argv[4]
        st["index"] = st.get("index", 0) + 1
        STATE.write_text(json.dumps(st), encoding="utf-8")
        print(json.dumps(st))
        return 0
    print("Usage: init | next | advance BLOB_ID [bytes] [sha256]", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
