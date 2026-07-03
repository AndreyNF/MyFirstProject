#!/usr/bin/env python3
"""Print wordpress_content_blob_append arguments JSON for NIDO step (agent → mcp_call_tool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

DIR = Path("/workspace/.cursor/nido-blob-calls")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: nido_mcp_call_append.py STEP [BLOB_ID]", file=sys.stderr)
        return 2
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else ""
    args = json.loads((DIR / f"call-{step:02d}.json").read_text(encoding="utf-8"))
    if step > 0 and blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing placeholder chunk")
    sys.stdout.write(json.dumps(args, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
