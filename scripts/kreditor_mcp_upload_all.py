#!/usr/bin/env python3
"""Emit MCP append args for kreditor blob chunks 1-3 (agent calls CallDynamicTool)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOB_ID = "AsjvgTB1Mq6cOie49LRl646"
BASE = Path("/workspace/.cursor")


def main() -> int:
    step = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if step < 1 or step > 3:
        print("usage: kreditor_mcp_upload_all.py <1|2|3>", file=sys.stderr)
        return 2
    args = json.loads((BASE / f"kreditor-blob-payload-{step}.json").read_text(encoding="utf-8"))
    args["blob_id"] = BLOB_ID
    args.pop("reset", None)
    out = Path(f"/tmp/kreditor-mcp-step-{step}.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "args_path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
