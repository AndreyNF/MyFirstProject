#!/bin/bash
# Prepare next MCP args after advance. Usage: arb_sro_next_chunk.sh 'MCP_RESPONSE'
set -euo pipefail
python3 /workspace/scripts/arb_sro_batch_upload.py advance "$1" >/dev/null
python3 /workspace/scripts/arb_sro_batch_upload.py status
python3 -c "import json; a=json.load(open('/tmp/arb-sro-mcp-next.json')); json.dump({'blob_id':a['blob_id'],'finalize':a['finalize'],'chunk':a['chunk']}, open('/tmp/current-mcp.json','w'), ensure_ascii=False)"
python3 -c "import json; s=json.load(open('/workspace/.cursor/arb-sro-2k-state.json')); print('READY', s['index'], s.get('bytes_total'))"
