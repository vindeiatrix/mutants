import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from engine.rng import RNG


def test_die_deterministic():
    rng = RNG(seed=42)
    rolls = [rng.die(6) for _ in range(5)]
    assert rolls == [6, 1, 1, 6, 3]


def test_roll_totals():
    rng = RNG(seed=42)
    total = rng.roll(5, 6)
    assert total == 17
