#!/usr/bin/env python3
"""Upload UG blob chunks 00-04 via Kovcheg MCP stdio bridge (if available) or emit steps.

For cloud agent: prints one JSON line per step with args_path.
Agent calls mcp_call_tool Kovcheg wordpress_content_blob_append with json.load(path).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

STEPS = [
    ("/workspace/.cursor/ug-blob-calls/call-00.json", None),
    ("/workspace/.cursor/ug-mcp-args-01.json", "medKEIrb9e27rCp9Lc99w5E"),
    ("/workspace/.cursor/ug-mcp-args-02.json", "medKEIrb9e27rCp9Lc99w5E"),
    ("/workspace/.cursor/ug-mcp-args-03.json", "medKEIrb9e27rCp9Lc99w5E"),
    ("/workspace/.cursor/ug-mcp-args-04.json", "medKEIrb9e27rCp9Lc99w5E"),
]


def load_step(path: str, blob_id: str | None) -> dict:
    args = json.loads(Path(path).read_text(encoding="utf-8"))
    if blob_id:
        args["blob_id"] = blob_id
        args.pop("reset", None)
    if "PLACEHOLDER" in args.get("chunk", ""):
        raise SystemExit(f"refusing PLACEHOLDER in {path}")
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: ug_mcp_emit_steps.py prepare|step N [out_path]", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "prepare":
        out_dir = Path("/tmp/ug-mcp-steps")
        out_dir.mkdir(exist_ok=True)
        meta = []
        for i, (src, bid) in enumerate(STEPS):
            args = load_step(src, bid)
            out = out_dir / f"step-{i:02d}.json"
            out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
            meta.append(
                {
                    "step": i,
                    "args_path": str(out),
                    "chunk_len": len(args["chunk"]),
                    "reset": bool(args.get("reset")),
                    "finalize": bool(args.get("finalize")),
                    "blob_id": args.get("blob_id"),
                }
            )
        print(json.dumps({"steps": meta}, ensure_ascii=False, indent=2))
        return 0
    if cmd == "step" and len(sys.argv) >= 3:
        i = int(sys.argv[2])
        src, bid = STEPS[i]
        args = load_step(src, bid)
        out = Path(sys.argv[3]) if len(sys.argv) > 3 else Path(f"/tmp/ug-mcp-steps/step-{i:02d}.json")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"args_path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
        return 0
    print(f"unknown: {cmd}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
