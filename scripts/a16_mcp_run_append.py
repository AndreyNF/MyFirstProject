#!/usr/bin/env python3
"""Load append args for step N (0-5) and print as JSON for mcp_call_tool."""
import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/a16-blob-mcp")
BLOB = sys.argv[2] if len(sys.argv) > 2 else ""


def main() -> int:
    step = int(sys.argv[1])
    if step == 0:
        d = json.loads((BASE / "00.json").read_text(encoding="utf-8"))
        args = {"chunk": d["chunk"], "reset": True, "finalize": False}
    else:
        d = json.loads((BASE / f"{step:02d}.json").read_text(encoding="utf-8"))
        args = {
            "blob_id": BLOB,
            "chunk": d["chunk"],
            "finalize": bool(d.get("finalize")),
        }
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
