# Reproducibility

## Fast verification

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'
pytest
rgphi verify
```

## Evidence classes

1. **Symbolic identities** are tested with exact `fractions.Fraction` arithmetic.
2. **Finite exhaustive results** ship with source data, machine-readable summaries,
   independent regression tests, and SHA-256 manifests.
3. **Large historical searches** remain separately labelled; their compact
   certificates and independent-engine hashes are not silently conflated with
   the small release tests.
4. **Open claims** remain explicitly marked open, including the exact value of
   the depth-five hitting time.

## Reference computational products

- exact first-hit chronology and threshold robustness data: `data/thresholds/`;
- finite trap atlas at denominator bound 500: `data/traps/`;
- manuscript claim-evidence matrix: `paper/claim-evidence-matrix.csv`;
- repository verifier: `src/rgphi/verification.py`.

## Clean-room replication

A replicator should implement `T`, `S`, primitive rational reduction, the
certified terminal convention, and target tests independently. Compare exact
counts, states, intervals, and hashes rather than floating-point summaries.
