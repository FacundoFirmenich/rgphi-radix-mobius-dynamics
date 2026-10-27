from fractions import Fraction
from pathlib import Path

from rgphi.thresholds import intersect, load_benchmark_intervals, load_nonnesting_intervals

ROOT = Path(__file__).resolve().parents[1]


def test_benchmark_robustness_interval() -> None:
    rows = load_benchmark_intervals(ROOT / "data/thresholds/benchmark-robustness.csv")
    assert [(row.depth, row.first_time) for row in rows] == [(1, 45), (2, 85), (3, 120), (4, 162)]
    assert intersect(rows) == (Fraction(106197, 10000), Fraction(11643, 1000))


def test_robust_nonnesting_interval() -> None:
    rows = load_nonnesting_intervals(ROOT / "data/thresholds/nonnesting-robustness.csv")
    assert len(rows) == 3
    lower = max(row[1] for row in rows)
    upper = min(row[2] for row in rows)
    assert (lower, upper) == (Fraction(106197, 10000), Fraction(1101, 100))
