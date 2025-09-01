.PHONY: setup test lint run

setup:
	python -m venv .venv
	./.venv/bin/pip install -e '.[dev]'

test:
	./.venv/bin/pytest -q

lint:
	./.venv/bin/ruff format .
	./.venv/bin/ruff check .

run:
	./.venv/bin/python -m drivers.cli
