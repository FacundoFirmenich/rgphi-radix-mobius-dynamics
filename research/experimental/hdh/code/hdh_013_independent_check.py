#!/usr/bin/env python3
"""Independent compact checker for the HDH-013 receipt."""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"


def main() -> None:
    result = json.loads((ROOT / "HDH_013_RESULTS.json").read_text(encoding="utf-8"))
    assert result["status"]["exact_full_kernel_rg"] == "PASS"
    assert result["status"]["spectral_function_closure_on_defects"] == "FAIL_EXACT"
    assert result["exact_kernel_flow"]["maximum_composition_relative_error"] < 1e-12
    assert result["exact_kernel_flow"]["maximum_green_restriction_relative_error"] < 1e-12
    assert result["exact_kernel_flow"]["maximum_one_by_one_elimination_error"] < 1e-11
    assert result["exact_kernel_flow"]["maximum_permutation_covariance_error"] < 1e-12
    assert result["candidate_class"]["minimum_defect_arbitrary_spectral_residual"] > 1e-3
    assert result["candidate_class"]["maximum_nonlocal_mass_beyond_one_hop"] > 0.1
    assert result["causal_benchmark"]["flat_benchmark_pass"]

    with (ROOT / "HDH_013_CAUSAL_BENCHMARK.csv").open(
        encoding="utf-8", newline=""
    ) as stream:
        rows = list(csv.DictReader(stream))
    assert rows
    assert all(row["verdict"] != "FAIL" for row in rows)
    print("PASS_HDH013_COMPACT_RECEIPT")


if __name__ == "__main__":
    main()
