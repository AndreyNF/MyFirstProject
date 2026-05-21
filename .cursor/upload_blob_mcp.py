#!/usr/bin/env python3
"""Load MCP args for blob step — agent calls mcp_call_tool with MCP_ARGS_NOW.json."""
import json
import sys
from pathlib import Path


def main() -> None:
    step = int(sys.argv[1])
    blob_id = sys.argv[2] if len(sys.argv) > 2 else None
    chunk = Path(f"/workspace/.cursor/chunk_body_{step}.txt").read_text(encoding="utf-8")
    meta = json.loads(Path(f"/workspace/.cursor/chunk_meta_{step}.json").read_text(encoding="utf-8"))
    args = {"chunk": chunk, **meta}
    if blob_id and step > 0:
        args["blob_id"] = blob_id
    out = Path("/workspace/.cursor/MCP_ARGS_NOW.json")
    out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({"step": step, "chunk_len": len(chunk), "keys": list(args.keys())}))


if __name__ == "__main__":
    main()
