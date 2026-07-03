#!/usr/bin/env python3
"""Load Fanta blob append args for step N (0-23). Agent: mcp_call_tool with printed JSON."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB_ID = "jv73pPUhDjAiEHe66uo8DbgA"
CHUNKS = Path("/tmp/fanta-blob-args")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: fanta_blob_mcp_step.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else BLOB_ID
    data = json.loads((CHUNKS / f"{step:02d}.json").read_text(encoding="utf-8"))
    args: dict = {"chunk": data["chunk"], "finalize": bool(data.get("finalize"))}
    if step == 0:
        args["reset"] = True
    else:
        args["blob_id"] = blob_id
    print(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
