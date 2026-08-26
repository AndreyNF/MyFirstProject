#!/usr/bin/env python3
"""Load blob append args from JSON file path; print compact metadata for agent MCP call."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: obysk_mcp_upload_from_file.py ARGS_JSON", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    args = json.loads(path.read_text(encoding="utf-8"))
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit("refusing PLACEHOLDER chunk")
    out = Path("/workspace/.cursor/obysk-mcp-active-args.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(
        json.dumps(
            {
                "args_path": str(out),
                "blob_id": args.get("blob_id"),
                "chunk_len": len(args["chunk"]),
                "finalize": bool(args.get("finalize")),
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
