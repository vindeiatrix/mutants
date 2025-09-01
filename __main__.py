"""Entry point for ``python -m mutants``."""

from __future__ import annotations

from .drivers.cli import cli


def main() -> None:  # pragma: no cover - thin wrapper
    """Execute the command line interface."""

    cli(standalone_mode=False)


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
