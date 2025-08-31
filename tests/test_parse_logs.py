import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tools.parse_logs import parse_file


def test_parse_first_event():
    path = Path("references/logs/2100wiz")
    events = parse_file(path)
    assert events, "no events parsed"
    first = events[0]
    assert first["cmd"] == "look"
    assert first["output"][0] == "You feel a cold breeze."
