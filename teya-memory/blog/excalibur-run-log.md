# Excalibur run log

## 2026-09-15 — B03 dosudebnoe-obzhalovanie-resheniya-fns

| Поле | Значение |
|---|---|
| topic_id | B03 |
| slug | dosudebnoe-obzhalovanie-resheniya-fns |
| h1 | Досудебное обжалование решения ФНС: жалоба в УФНС — сроки, порядок, образец |
| primary_query | жалоба в УФНС на решение налоговой |
| char_count | 8683 |
| article-qa | PASS |
| wp_status | **published** |
| wp_post_id | 620 |
| wp_url | https://advokat-vsem.online/?p=620 |
| wp_media_id | 619 |
| published_at | 2026-09-15T09:43:06Z |

### Gates

- research-notes-gate: PASS (Wordstat 403 — warning в notes)
- html-linter: PASS
- slop-detector: PASS (Flesch RU 44.3)
- fact-checker: PASS (9/9 verified vs fact-bank D01-D15)
- link-verify: PASS
- utility-gate: PASS
- human-voice-gate: PASS
- cannibalization: PASS

### Cover

- Path: `teya-memory/blog/articles/B03-dosudebnoe-obzhalovanie-resheniya-fns/cover/cover.png`
- Prompt (AURA): prefix + `official complaint envelope to tax authority...` + suffix
- MCP gpt-image-2: **FAILED** (5× Request timed out -32001)
- Fallback: локальный PNG 1200×675, палитра AURA (#FAFAF7, #E85D4C, #1A1A2E)

### Факты

Только fact-bank D01-D15 + L05/L12 (CTA 24 ч, самостоятельная подача).

### Файлы пакета

```
research-context.json
research-serp.json
research-notes.md
research-notes-gate.json
article.html
article.meta.json
article-qa.md
schema.jsonld
cover/cover.png
html-linter-report.json
slop-detector-report.json
fact-check-report.json
link-verify.json
utility-gate-report.json
human-voice-report.json
cannibalization-report.json
```
