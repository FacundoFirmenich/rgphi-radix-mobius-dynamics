# OR-5 — five-state defect-cell hypotheses

## Primary endpoint — SHORT_DEFECT_CYCLE

For every minimal finite all-high nonpermutation SCC, there exists a simple directed cycle satisfying:

- cycle length at most five;
- exactly one strict edge;
- every other cycle edge unreduced.

This is a direct graph predicate once exact strict-edge metadata are supplied.

## Secondary endpoint — FIVE_STATE_DEFECT_QUOTIENT

Contract maximal unreduced numerator-fibre and denominator-fibre cycles while preserving generator labels and strict-edge status. The resulting minimal defect quotient should:

- have exactly five vertices;
- be isomorphic, up to `T<->S`, to one of the twenty canonical five-state forms.

## Interpretation

A primary hit supports five as a universal local obstruction. A secondary hit would support five as a universal quotient cell. Failure of either endpoint must be retained; no looser `five-like` criterion may be substituted.
