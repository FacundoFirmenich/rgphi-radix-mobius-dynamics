from __future__ import annotations

import csv
import json
import zipfile
from fractions import Fraction
from pathlib import Path

from rgphi.dynamics import DEFAULT_TERMINAL, S, T, portal_height

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "data" / "certificates" / "paper-I"


def as_fraction(value: str) -> Fraction:
    a, b = map(int, value.split("/"))
    return Fraction(a, b)


def test_compact_receipt() -> None:
    receipt = json.loads((CERT / "benchmark_receipt.json").read_text(encoding="utf-8"))
    assert {as_fraction(x) for x in receipt["system"]["terminal_states"]} == set(DEFAULT_TERMINAL)
    for state in DEFAULT_TERMINAL:
        for child in (T(state), S(state)):
            assert child is None or child in DEFAULT_TERMINAL

    assert receipt["current_tau5_interval"] == [186, 212]
    assert receipt["global_first_hits"]["tau"] == {"1": 45, "2": 85, "3": 120, "4": 162}
    for depth, states in receipt["global_first_hits"]["states"].items():
        assert all(portal_height(as_fraction(value)) > 11 * 10 ** int(depth) for value in states)

    last_rows: dict[str, dict[str, str]] = {}
    with zipfile.ZipFile(CERT / "paper-I-profiles.zip") as archive:
        for name in archive.namelist():
            if name.endswith(".csv"):
                rows = list(csv.DictReader(archive.read(name).decode("utf-8").splitlines()))
                assert rows
                last_rows[Path(name).stem] = rows[-1]

    for certificate in receipt["continuation_searches"]:
        assert int(last_rows[certificate["label"]]["seen_size"]) == certificate["seen_states"]
