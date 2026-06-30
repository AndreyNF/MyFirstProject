#!/usr/bin/env python3
"""List A11 blob MCP steps (≤6000 chars per append). Usage: a11_blob_mcp_steps.py [step_index]"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path("/workspace/.cursor")
SUB = 6000


def build_steps() -> list[dict]:
    steps: list[dict] = []
    for fi in range(4):
        text = (ROOT / f"a11-chunk-{fi}.txt").read_text(encoding="utf-8")
        for j in range(0, len(text), SUB):
            steps.append({"file": fi, "part": j // SUB, "chunk": text[j : j + SUB]})
    return steps


def main() -> int:
    steps = build_steps()
    if len(sys.argv) < 2:
        print(json.dumps({"total": len(steps)}, ensure_ascii=False))
        return 0
    idx = int(sys.argv[1])
    if idx < 0 or idx >= len(steps):
        return 1
    st = steps[idx]
    args: dict = {"chunk": st["chunk"]}
    if idx == 0:
        args["reset"] = True
    if idx == len(steps) - 1:
        args["finalize"] = True
    print(json.dumps({"index": idx, "total": len(steps), "arguments": args}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
