#!/usr/bin/env python3
"""Print MCP append args for obysk 5k step N (agent CallDynamicTool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB = "6k97VtvlREclZgKuM9HLouz"
BASE = Path("/workspace/.cursor/obysk-mcp-5k")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_mcp_print_step.py STEP", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    args = json.loads((BASE / f"step_{step:02d}.json").read_text(encoding="utf-8"))
    if step == 0:
        args["reset"] = True
    else:
        args["blob_id"] = BLOB
    if step == 17:
        args["finalize"] = True
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
