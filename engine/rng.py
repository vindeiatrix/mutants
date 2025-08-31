"""Random number helpers for Mutants.

The original game relied heavily on dice rolls.  This module provides a small
wrapper around :mod:`random` that allows deterministic testing by seeding the
underlying PRNG.
"""

from __future__ import annotations

from dataclasses import dataclass
import random
from typing import Iterable


@dataclass
class RNG:
    """Helper class for rolling dice.

    Parameters
    ----------
    seed:
        Optional seed used to initialise the underlying random generator.
    """

    seed: int | None = None

    def __post_init__(self) -> None:
        self._random = random.Random(self.seed)

    def die(self, sides: int) -> int:
        """Roll a single die with ``sides`` sides.

        Returns an integer in the inclusive range ``1..sides``.
        """

        if sides < 1:
            raise ValueError("sides must be >= 1")
        return self._random.randint(1, sides)

    def roll(self, count: int, sides: int) -> int:
        """Roll ``count`` dice with ``sides`` sides and return the total."""

        if count < 0:
            raise ValueError("count must be >= 0")
        return sum(self.die(sides) for _ in range(count))


def roll_sequence(rng: RNG, spec: Iterable[tuple[int, int]]) -> list[int]:
    """Roll a sequence of dice and return individual results.

    ``spec`` is an iterable of ``(count, sides)`` tuples.
    """

    results: list[int] = []
    for count, sides in spec:
        for _ in range(count):
            results.append(rng.die(sides))
    return results
