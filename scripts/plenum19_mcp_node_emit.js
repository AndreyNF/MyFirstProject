#!/usr/bin/env node
/**
 * Load MCP args JSON and print envelope for wordpress_content_blob_append.
 * Agent must call mcp_call_tool with parsed arguments (chunk may be large).
 */
const fs = require('fs');

const argsPath = process.argv[2];
if (!argsPath) {
  console.error('usage: plenum19_mcp_node_emit.js ARGS.json');
  process.exit(2);
}
const args = JSON.parse(fs.readFileSync(argsPath, 'utf8'));
if ((args.chunk || '').includes('PLACEHOLDER')) {
  console.error('refusing PLACEHOLDER chunk');
  process.exit(1);
}
const envelope = {
  server: 'Kovcheg',
  toolName: 'wordpress_content_blob_append',
  arguments: args,
};
console.log(JSON.stringify({
  chunk_len: args.chunk.length,
  reset: !!args.reset,
  finalize: !!args.finalize,
  latin_st158: (args.chunk.match(/st\. 158/g) || []).length,
  cyr_st158: (args.chunk.match(/ст\. 158/g) || []).length,
  args_path: argsPath,
}));
