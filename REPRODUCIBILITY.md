# Reproducibility and independent verification

RGΦ separates **quick repository verification** from **independent scientific replication**.

## 1. Quick repository verification

Requirements:

- Python 3.11 or 3.12;
- a POSIX-like shell for the commands below.

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev]'

ruff check src tests
pytest
rgphi verify
~~~

Expected result: all checks pass.

GitHub Actions executes the same core verification on Python 3.11 and 3.12.

## 2. What rgphi verify checks

The repository verifier checks:

- the foundational conjugacy identity;
- noncommutativity at the benchmark seed;
- a parameterized seed-family identity over a finite audit grid;
- exact threshold intervals;
- the canonical \(C_8\) trap;
- modular orders underlying \(C_8\);
- reference finite-trap atlas counts;
- presence of the manuscript and archival metadata.

It is a **small verifier**, not the historical discovery engine.

## 3. Evidence tiers

### Tier S — symbolic

Reproduce from equations and exact unit tests.

### Tier F — finite exhaustive

Regenerate the finite search/atlas and compare exact states, counts, and intervals.

### Tier C — large computer-assisted

Use the independent C++/Python artifacts and compare canonical checkpoint counts and hashes. Large searches should report hardware, compiler, runtime, pruning theorem, and search horizon.

## 4. Clean-room replication protocol

A genuine clean-room replicator should implement independently:

1. reduced rational states;
2. \(T_B\) and admissible \(S_B\);
3. primitive reduction;
4. the declared terminal set;
5. exact portal membership;
6. per-level exact deduplication.

The replicator should then compare outputs, not source code structure.

Priority checks:

- \(\tau_1,\ldots,\tau_4\);
- the three continuation delays;
- threshold robustness intervals;
- \(C_8\) closure;
- denominator-\(\le500\) atlas counts.

## 5. Determinism

The reference finite computations are deterministic.

No stochastic seed, learned model, or approximate numerical solver enters the theorem-critical pipeline.

## 6. Floating-point boundary

Decimals may appear in reports for readability.

Logical decisions use:

- Python integers;
- fractions.Fraction;
- exact integer comparisons;
- exact reduced rational encodings.

## 7. Container and environment

The repository includes:

- Dockerfile;
- environment.yml;
- requirements.txt;
- requirements-dev.txt;
- pyproject.toml.

The Python package is intentionally small enough to inspect independently.

## 8. Manuscript reproduction

~~~bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The GitHub paper workflow performs the same build in a clean runner.

## 9. Archival reproducibility

Before the DOI is minted, the release checklist requires:

- green CI;
- green paper build;
- frozen manuscript;
- frozen data summaries;
- consistent version metadata;
- generated manifest/checksums;
- archival metadata review.

## 10. Known limitation

Internal reproducibility is strong; **external independent replication remains pending**. This is stated as a limitation rather than treated as completed validation.
