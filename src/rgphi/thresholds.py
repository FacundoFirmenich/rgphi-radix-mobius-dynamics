"""Exact threshold-robustness utilities."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import csv
from typing import Iterable


@dataclass(frozen=True, slots=True)
class RobustnessInterval:
    depth: int
    first_time: int
    lower: Fraction
    upper: Fraction

    def contains(self, kappa: Fraction) -> bool:
        return self.lower <= kappa < self.upper


def interval_from_record_heights(
    *, depth: int, first_time: int, previous_record: Fraction, first_hit_record: Fraction, base: int = 10
) -> RobustnessInterval:
    scale = base**depth
    return RobustnessInterval(
        depth=depth,
        first_time=first_time,
        lower=previous_record / scale,
        upper=first_hit_record / scale,
    )


def intersect(intervals: Iterable[RobustnessInterval]) -> tuple[Fraction, Fraction]:
    intervals = tuple(intervals)
    if not intervals:
        raise ValueError("at least one interval is required")
    lower = max(item.lower for item in intervals)
    upper = min(item.upper for item in intervals)
    if lower >= upper:
        raise ValueError(f"empty intersection [{lower}, {upper})")
    return lower, upper


def load_benchmark_intervals(path: str | Path) -> list[RobustnessInterval]:
    result: list[RobustnessInterval] = []
    with Path(path).open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            result.append(
                RobustnessInterval(
                    depth=int(row["m"]),
                    first_time=int(row["tau"]),
                    lower=Fraction(row["kappa_lower_inclusive"]),
                    upper=Fraction(row["kappa_upper_exclusive"]),
                )
            )
    return result


def load_nonnesting_intervals(path: str | Path) -> list[tuple[str, Fraction, Fraction]]:
    result: list[tuple[str, Fraction, Fraction]] = []
    with Path(path).open(newline="", encoding="utf-8") as stream:
        for row in csv.DictReader(stream):
            result.append(
                (
                    row["transition"],
                    Fraction(row["nonnesting_kappa_lower_inclusive"]),
                    Fraction(row["nonnesting_kappa_upper_exclusive"]),
                )
            )
    return result
