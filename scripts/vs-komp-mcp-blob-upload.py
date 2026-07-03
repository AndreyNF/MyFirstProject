#!/usr/bin/env python3
"""Upload vs-komp blob chunks 0-4 via stdin JSON lines to agent MCP loop.

Prints one JSON object per line:
  {"tool":"wordpress_content_blob_append","arguments":{...}}

Agent: for each line, mcp_call_tool Kovcheg wordpress_content_blob_append.
After step 4 finalize, call wordpress_update_page_from_blob and wordpress_update_page.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BASE = Path("/workspace/.cursor/vs-komp-blob-mcp")
PAGE_ID = 443
EXCERPT = (
    "ВС разъяснил: при иске о компенсации за нарушение товарного знака суды проверяют "
    "Указ № 322. Как ИП на маркетплейсе оспорить иск иностранного правообладателя."
)


def load_step(step: int, blob_id: str = "") -> dict:
    args = json.loads((BASE / f"{step}.json").read_text(encoding="utf-8"))
    if step > 0:
        if not blob_id:
            raise SystemExit(f"blob_id required for step {step}")
        args["blob_id"] = blob_id
        args.pop("reset", None)
    return args


def main() -> int:
    if len(sys.argv) < 2:
        print("emit STEP [BLOB_ID] | meta", file=sys.stderr)
        return 2
    cmd = sys.argv[1]
    if cmd == "meta":
        print(json.dumps({"page_id": PAGE_ID, "excerpt": EXCERPT, "slug": "vs-kompensaciya-tovarnyj-znak-nedruzhestvennye-strany"}))
        return 0
    if cmd == "emit":
        step = int(sys.argv[2])
        blob_id = sys.argv[3] if len(sys.argv) > 3 else ""
        args = load_step(step, blob_id)
        out = Path(f"/tmp/vs-komp-emit-step{step}.json")
        out.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        print(json.dumps({"step": step, "path": str(out), "chunk_len": len(args["chunk"]), "finalize": bool(args.get("finalize"))}))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
