"""Parse legacy Mutants log files into structured JSON.

Log files capture interactive sessions from the classic BBS game.  The format is
fairly free-form, but most commands follow a pattern::

    >
    command here
    ***
    game output...

This script extracts a list of events with ``{"cmd": str, "output": [str, ...]}``
shapes that are later consumed by replay tests.
"""

from __future__ import annotations

import json
from pathlib import Path

import click


def parse_file(path: Path | str) -> list[dict[str, object]]:
    """Return a list of events parsed from ``path``.

    Only a tiny subset of the log format is recognised.  Lines occurring before
    the first ``>`` prompt are ignored.  Each event begins with ``>`` followed by
    the command on the next line; subsequent lines until the next ``>`` are
    collected as the event's output with ``***`` separators removed.
    """

    path = Path(path)
    events: list[dict[str, object]] = []
    current_cmd: str | None = None
    current_out: list[str] = []
    expecting_cmd = False
    started = False
    with path.open("r", encoding="utf8") as fh:
        for raw in fh:
            line = raw.rstrip("\n")
            if line == ">":
                started = True
                if current_cmd is not None or current_out:
                    events.append({"cmd": current_cmd, "output": current_out})
                    current_out = []
                expecting_cmd = True
                continue
            if not started:
                # Skip preamble before first prompt.
                continue
            if expecting_cmd:
                current_cmd = line.strip()
                expecting_cmd = False
                continue
            if line.startswith("***"):
                # log separator, ignore
                continue
            current_out.append(line)
    if current_cmd is not None or current_out:
        events.append({"cmd": current_cmd, "output": current_out})
    return events


@click.command()
@click.argument(
    "log_path", type=click.Path(exists=True, dir_okay=False, path_type=Path)
)
def main(log_path: Path) -> None:
    """Parse ``LOG_PATH`` and dump JSON events to stdout."""

    events = parse_file(log_path)
    json.dump(events, click.get_text_stream("stdout"), indent=2)


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()
