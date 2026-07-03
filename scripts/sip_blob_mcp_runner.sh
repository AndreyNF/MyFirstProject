#!/usr/bin/env bash
# Print MCP args JSON path for step N (agent calls mcp_call_tool with json.load)
set -euo pipefail
STEP="${1:?step 0-9}"
BLOB_ID="${2:-}"
python3 /workspace/scripts/sip_prekrashchenie_mcp_upload.py "$STEP" $BLOB_ID > "/tmp/sip-mcp-step${STEP}.json"
python3 -c "import json; d=json.load(open('/tmp/sip-mcp-step${STEP}.json')); print(json.dumps({'step':${STEP},'chunk_len':len(d['chunk']),'blob_id':d.get('blob_id'),'finalize':d.get('finalize',False),'path':'/tmp/sip-mcp-step${STEP}.json'}))"
