"""Command line interface for a placeholder encounter."""

from __future__ import annotations

import click

from engine.rng import RNG


@click.command()
def main() -> None:
    """Run a tiny demo encounter.

    For now the CLI simply rolls a six-sided die and prints the result to show
    that the project is wired up correctly.
    """

    rng = RNG()
    roll = rng.die(6)
    click.echo(f"A mutant appears! You roll a {roll}.")


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
