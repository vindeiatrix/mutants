# AGENTS.md — Codex playbook for Mutants

## Goal
Recreate the BBS game “Mutants” as a modular Python project. For proof-of-concept, implement years: 2000, 2100, 2200, 2300, 2500, 2600. Use `/reference` (rules, logs, screenshots) as source of truth to infer mechanics, monsters, gear, AI, and messages. Where rules are unclear, choose the simplest consistent model and document assumptions in code comments and tests.

## Environment
- Python 3.11+
- Create a virtualenv `.venv` and install deps from `pyproject.toml` or `requirements-dev.txt`.

## Build & Test
- Run tests: `pytest -q`
- Format/lint: `ruff format .` and `ruff check .`

## Project Structure (target)
mutants/
  engine/          # rng, rules, statuses, effects, combat, ai, loot, serialization
  content/         # monsters.yaml, items.yaml, spells.yaml, years.yaml, messages.yaml
  drivers/         # cli.py (text UI), replay.py
  tools/           # parse_logs.py, diff_text.py
  tests/           # pytest: rules, spells, ai, replays

## First tasks for the agent
1) Scaffold the project structure with stubs and docstrings.
2) Add `pyproject.toml` (or `requirements-dev.txt`) with: pytest, ruff, pyyaml, rich, click.
3) Implement `engine/rng.py` (seedable dice helpers), and a minimal CLI that runs a single placeholder encounter.
4) Create `tools/parse_logs.py` that parses `/reference/logs/*` into structured JSON suitable for replay tests.
5) Add basic tests (`tests/test_rules.py` for dice; `tests/test_parse_logs.py` for one log).
6) Open a PR titled “Milestone 0 — Scaffolding & Harness”.

## Data to learn from
- `/reference/rules/*`
- `/reference/logs/*`
- `/reference/screenshots/*` (match message text & edge cases)
