# MyFirstProject

## Cursor Cloud specific instructions

### What this repository is
This is a **content-only repository**, not a software project. It contains Markdown
deliverables (marketing/ad copy) and has **no application code, no dependency
manifests, no build system, and no runnable services**.

Current contents:
- `README.md` — placeholder title.
- `avito/seriya-novyh-obyavleniy-petrovich.md` — a Russian-language Avito ad series
  for the "Legis24" legal-services brand (titles, prices, descriptions, Wordstat data).

### Setup / build / test / run
- There is **nothing to install, build, or test** — the update script is intentionally
  a no-op. Do not add language toolchains or service-startup logic for the current state.
- There is no lint configuration. If you want to sanity-check Markdown, you can lint
  ad hoc with `npx markdownlint-cli '**/*.md'` (node 22 is available), but this is not
  part of the repo and not required.

### Previewing the content (the practical "run" for this repo)
The closest thing to "running the app" is rendering the Markdown to view it:
```bash
pip3 install --quiet markdown   # one-off, not part of the repo
python3 - <<'PY'
import markdown, pathlib
src = pathlib.Path("avito/seriya-novyh-obyavleniy-petrovich.md").read_text(encoding="utf-8")
html = markdown.markdown(src, extensions=["tables","fenced_code","sane_lists"])
pathlib.Path("/tmp/preview.html").write_text(
    "<!doctype html><meta charset='utf-8'>"+html, encoding="utf-8")
print("wrote /tmp/preview.html")
PY
python3 -m http.server 8765 --directory /tmp   # then open http://localhost:8765/preview.html
```

### Notes
- Content is in Russian (Cyrillic) and uses Markdown tables — make sure any tooling
  handles UTF-8 and GFM tables.
- The document explicitly states API publication was not performed; treat the file as
  editorial copy intended for manual upload to Avito.
- An MCP server ("Kovcheg") with WordPress/Wordstat/Telegram/image/VK tools may be
  available in the chat environment for publishing workflows, but it is **external** to
  this repo and not required to work with the files here.
