import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from click.testing import CliRunner

from drivers.cli import cli


def test_demo_command_has_no_hit_or_miss() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["demo"])

    assert result.exit_code == 0
    output_lower = result.output.lower()
    assert output_lower.strip()  # some output exists
    assert "hit" not in output_lower
    assert "miss" not in output_lower
