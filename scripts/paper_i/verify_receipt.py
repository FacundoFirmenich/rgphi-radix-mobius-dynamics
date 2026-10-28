#!/usr/bin/env python3
"""Small independent checker for the compact Paper I continuation receipt."""
from __future__ import annotations

import csv
import json
import zipfile
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "data" / "certificates" / "paper-I"


def T(x: Fraction, base: int = 10) -> Fraction:
    y = base * x
    return y - (y.numerator // y.denominator)


def S(x: Fraction, base: int = 10) -> Fraction | None:
    if x == 0 or 2 * x < 1:
        return None
    u = Fraction(1, 1) / x - 1
    y = base * u
    return Fraction(1, 1) / (1 + y - (y.numerator // y.denominator))


def height(x: Fraction) -> Fraction:
    return Fraction(x.denominator, x.denominator - x.numerator)


def fraction(value: str) -> Fraction:
    a, b = map(int, value.split("/"))
    return Fraction(a, b)


def load_last_rows() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    with zipfile.ZipFile(CERT / "paper-I-profiles.zip") as archive:
        for name in archive.namelist():
            if not name.endswith(".csv"):
                continue
            text = archive.read(name).decode("utf-8").splitlines()
            rows = list(csv.DictReader(text))
            if not rows:
                raise AssertionError(f"empty certificate table: {name}")
            result[Path(name).stem] = rows[-1]
    return result


def main() -> None:
    receipt = json.loads((CERT / "benchmark_receipt.json").read_text(encoding="utf-8"))

    terminal = {fraction(value) for value in receipt["system"]["terminal_states"]}
    for state in terminal:
        for child in (T(state), S(state)):
            if child is not None and child not in terminal:
                raise AssertionError(f"terminal escape {state}->{child}")

    seed = Fraction(17, 19)
    assert S(seed) == Fraction(17, 20)
    assert T(S(seed)) == Fraction(1, 2)  # type: ignore[arg-type]
    assert S(T(seed)) == Fraction(9, 14)

    tau = {int(k): value for k, value in receipt["global_first_hits"]["tau"].items()}
    assert tau == {1: 45, 2: 85, 3: 120, 4: 162}
    for depth, states in receipt["global_first_hits"]["states"].items():
        for value in states:
            assert height(fraction(value)) > 11 * 10 ** int(depth)

    last_rows = load_last_rows()
    for certificate in receipt["continuation_searches"]:
        row = last_rows[certificate["label"]]
        assert int(row["seen_size"]) == certificate["seen_states"]
        if certificate.get("result") == "NO_HIT":
            assert int(row["local_depth"]) == certificate["local_horizon"]
            assert int(row["hit_count"]) == 0
        else:
            assert int(row["local_depth"]) == certificate["local_cost"]
            assert row["first_hit_state"] == certificate["endpoint"]
            assert int(row["hit_count"]) >= 1
            assert height(fraction(certificate["endpoint"])) > 11 * 10 ** certificate["target_m"]
            assert certificate["source_global_time"] + certificate["local_cost"] == certificate["arrival_global_time"]

    chronology = tuple(fraction(x) for x in receipt["robustness"]["chronology_interval"])
    nonnesting = tuple(fraction(x) for x in receipt["robustness"]["nonnesting_interval"])
    assert chronology == (Fraction(106197, 10000), Fraction(11643, 1000))
    assert nonnesting == (Fraction(106197, 10000), Fraction(1101, 100))
    assert receipt["current_tau5_interval"] == [186, 212]

    paper = (ROOT / "paper" / "main.tex").read_text(encoding="utf-8")
    assert r"186\le \tau_5\le212" in paper
    assert r"179\le \tau_5\le212" not in paper

    print("PASS_PAPER_I_RECEIPT")
    print("PASS_TERMINAL_SET")
    print("PASS_CONTINUATION_CERTIFICATES")
    print("PASS_THRESHOLD_INTERVALS")


if __name__ == "__main__":
    main()
