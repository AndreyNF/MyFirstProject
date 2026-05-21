
import json, subprocess, sys
args = json.loads(open("/workspace/.cursor/MCP_ARGS_NOW.json", encoding="utf-8").read())
print("READY", len(args["chunk"]), list(k for k in args if k != "chunk"))
