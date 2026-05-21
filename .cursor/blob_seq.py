#!/usr/bin/env python3
"""Sequential blob upload via stdin protocol: prints next chunk index until done."""
import json
import sys
from pathlib import Path

STATE = Path('/workspace/.cursor/blob_seq_state.json')
BLOB = 'kRPycabFYb1A7EHwIfTNGtMe'
START = 4
END = 18

def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'next'
    if cmd == 'init':
        STATE.write_text(json.dumps({'next': START, 'blob_id': BLOB}), encoding='utf-8')
        print('init', START)
        return
    state = json.loads(STATE.read_text(encoding='utf-8'))
    if cmd == 'done':
        idx = int(sys.argv[2])
        state['next'] = idx + 1
        STATE.write_text(json.dumps(state), encoding='utf-8')
        print('advanced', state['next'])
        return
    idx = state['next']
    if idx > END:
        print('ALL_DONE')
        return
    args = json.loads(Path(f'/workspace/.cursor/_upload_{idx}.json').read_text(encoding='utf-8'))
    Path('/workspace/.cursor/MCP_NEXT.json').write_text(json.dumps(args, ensure_ascii=False), encoding='utf-8')
    print(json.dumps({'idx': idx, 'len': len(args['chunk']), 'finalize': bool(args.get('finalize'))}))

if __name__ == '__main__':
    main()
