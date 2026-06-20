#!/usr/bin/env python3
"""Split vs-uslovnyy HTML into small MCP sub-chunks and print upload plan."""
from __future__ import annotations

import json
from pathlib import Path

HTML = Path("/workspace/.cursor/page-content-natasha-vs-uslovnyy-srok.html")
SUB = 5000


def main() -> int:
    text = HTML.read_text(encoding="utf-8")
    if "<script" in text.lower():
        raise SystemExit("script tags found")
    parts = [text[i : i + SUB] for i in range(0, len(text), SUB)]
    out_dir = Path("/workspace/.cursor/vs-uslovnyy-subchunks")
    out_dir.mkdir(exist_ok=True)
    plan = []
    for i, ch in enumerate(parts):
        args = {"chunk": ch}
        if i == 0:
            args["reset"] = True
        if i == len(parts) - 1:
            args["finalize"] = True
        p = out_dir / f"sub-{i:02d}.json"
        p.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        plan.append({"i": i, "len": len(ch), "reset": bool(args.get("reset")), "finalize": bool(args.get("finalize"))})
    meta = {"total": len(text), "parts": len(parts), "sub_size": SUB, "plan": plan}
    (out_dir / "meta.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(json.dumps(meta))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
