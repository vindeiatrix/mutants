# mutants

mutants text adventure game recreation

## Quickstart

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .[dev]
```

Run the demo CLI:

```bash
python -m drivers.cli
```

Run tests:

```bash
pytest -q
```

Lint and format:

```bash
ruff format .
ruff check .
```
