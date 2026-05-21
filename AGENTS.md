# AGENTS.md

## Cursor Cloud specific instructions

This repository ("MyFirstProject") is currently an empty project with only a `README.md`. There are no applications, services, dependencies, or build systems to run.

### Environment

- No package manager or dependency files exist yet.
- No lint, test, or build tooling is configured.
- The update script is a no-op: it exits successfully since there is nothing to install.

### When code is added

Once application code and dependency files are added (e.g. `package.json`, `requirements.txt`, `pyproject.toml`), update this file and the VM update script accordingly with:
- The correct install command (e.g. `npm install`, `pip install -r requirements.txt`)
- Instructions for running lint, tests, build, and dev server
- Any required environment variables or secrets
