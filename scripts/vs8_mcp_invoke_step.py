#!/usr/bin/env python3
"""Load vs8 blob append args for step N (1-4). Prints JSON to stdout for mcp_call_tool."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "PDBvIlPEeP73qtNQ0bAemyb"
DIR = Path("/workspace/.cursor")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: vs8_mcp_invoke_step.py STEP", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    p = DIR / f"_vs8_mcp_step{step}.json"
    if not p.is_file():
        p = DIR / "vs8-mcp-steps" / f"step{step}.json"
        args = json.loads(p.read_text(encoding="utf-8"))
        if step > 0:
            args["blob_id"] = BLOB
    else:
        args = json.loads(p.read_text(encoding="utf-8"))
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
