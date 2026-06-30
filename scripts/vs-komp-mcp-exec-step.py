#!/usr/bin/env python3
"""Load MCP append args for step N and print as JSON (for agent mcp_call_tool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "eR4nq755BCTfxtyeEP33kF52"
BASE = Path("/workspace/.cursor/vs-komp-blob-mcp")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs-komp-mcp-exec-step.py STEP", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    path = Path(f"/tmp/mcp-call-step{step}.json")
    if path.is_file():
        args = json.loads(path.read_text(encoding="utf-8"))
    else:
        args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
        if step > 0:
            args["blob_id"] = BLOB
            args.pop("reset", None)
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
