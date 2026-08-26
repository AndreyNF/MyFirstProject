#!/usr/bin/env python3
"""Print MCP append args JSON to stdout for agent CallDynamicTool."""
import json
import sys

step = int(sys.argv[1])
args = json.load(open(f"/tmp/kreditor-mcp-step-{step}.json", encoding="utf-8"))
print(json.dumps(args, ensure_ascii=False))
