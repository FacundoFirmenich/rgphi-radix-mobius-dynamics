# Contributing

Contributions are welcome when they preserve the repository's evidence
boundaries and exact-arithmetic discipline.

## Required for mathematical changes

1. State the claim precisely and mark it as symbolic, finite-computational, or conjectural.
2. Add or update an exact verifier.
3. Add a regression test that fails before the change.
4. Do not use floating-point comparisons for reachability or portal membership.
5. Record any changed canonical count or hash in the claim-evidence matrix.
6. Keep superseded results when they remain locally valid; relabel rather than erase.

## Development setup

```bash
python -m pip install -e '.[dev]'
pytest
ruff check .
rgphi verify
```

## Pull requests

A pull request should include:

- scientific motivation;
- exact statement affected;
- evidence and verifier;
- computational cost and boundary;
- literature impact when novelty claims change.
