"""Command line interface for the Mutants demo."""

from __future__ import annotations

import click

try:  # pragma: no cover - fallback for direct execution
    from ..engine.rng import RNG
except ImportError:  # pragma: no cover - when repository root on sys.path
    from engine.rng import RNG


@click.group()
def cli() -> None:
    """Mutants command line tools."""


@cli.command()
def demo() -> int:
    """Run a tiny deterministic demo encounter.

    The encounter rolls initiative using a fixed seed and then performs
    three placeholder rounds.  This command is mechanics-neutral and exists
    solely to smoke-test the CLI wiring.
    """

    rng = RNG(seed=42)

    click.echo("Rolling initiative...")
    player_init = rng.die(20)
    mutant_init = rng.die(20)
    click.echo(f"You roll {player_init} for initiative.")
    click.echo(f"The mutant rolls {mutant_init}.")

    if player_init >= mutant_init:
        click.echo("You act first!")
    else:
        click.echo("The mutant acts first!")

    for round_number in range(1, 4):
        click.echo(f"Round {round_number}: demo action.")

    return 0


def main() -> None:  # pragma: no cover - thin wrapper
    """Entrypoint used by console scripts."""

    cli(standalone_mode=False)


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
