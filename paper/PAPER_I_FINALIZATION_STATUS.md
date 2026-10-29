# Paper I finalization status — 30 October 2026

**Branch purpose:** Paper I only. P2/P3, Stage B2 and all experimental branches
remain outside the theorem dependency graph.

## Current internal scorecard

| Dimension | Score / 10 | Current assessment |
|---|---:|---|
| Formal definition and domain | 9.4 | Partial-semigroup domain and admissibility explicit |
| Main theorem clarity | 9.3 | Chronology, nonnesting and robustness stated exactly |
| Computer-assisted proof architecture | 9.1 | Exact layer recursion formalized; compact checker separated |
| Claim hygiene | 9.5 | Narrow freeze, explicit nonclaims and typed frontier protocol |
| Literature positioning | 8.4 | Adjacent hitting-depth and Farey-tree work cited; specialist closed-database check pending |
| Reproducibility | 8.7 | Compact replay strong; full depth-162 payload archival gate specifically blocked |
| Generality | 7.1 | Exact benchmark theorem; family theorem intentionally deferred |
| External validation | 4.0 | Review and clean-room packets ready for genuinely external actors |
| Editorial readiness | 8.9 | Submission package ready after external gates and venue selection |

## Material improvements in finalization

- added MSC2020 classifications and keywords;
- inserted a logical paper graph;
- proved exactness of the finite layer recursion by induction;
- made target-before-pruning semantics explicit;
- replaced approximate Bellman-height examples by an exact rational table;
- sharpened the evidence and payload boundary;
- expanded the supplement with exact replay commands;
- strengthened the referee packet;
- cited adjacent Gauss-map hitting-depth and generalized Farey-tree work;
- added venue-specific cover letters and a journal decision memo;
- expanded the reviewer bundle with supplement, replay scripts and compact exact data;
- typed every remaining gate in `metadata/PAPER_I_FRONTIERS.json`;
- adopted a five-field blocker rule, scoped impossibility and explicit reopening conditions.

## Remaining binding gates

| Gate | Typed status | Immediate next action |
|---|---|---|
| Two specialist reviews | `READY_FOR_EXTERNAL_ACTION` | send pinned reviewer bundle to two independent specialists |
| Closed-database priority chaining | `ACTIVE_PARTIAL` | complete MathSciNet/zbMATH or equivalent chaining |
| Clean-room replication | `READY_FOR_EXTERNAL_ACTION` | recruit an external implementation or replay actor |
| Full depth-162 certificate | `BLOCKED_SPECIFIC` | locate/deposit original payload or cleanly regenerate it |
| Journal and format | `DEPENDENCY_BLOCKED` | adjudicate specialist feedback, then choose venue |
| DOI/release | `DEPENDENCY_BLOCKED` | close predecessor gates and freeze the signed candidate |

The exact blocker records, alternatives and reopening conditions are in:

```text
metadata/PAPER_I_FRONTIERS.json
```

## Promotion rule

Paper I can be submitted before `tau_5` is resolved. It cannot be called
externally validated or archival-complete before the corresponding typed gates
close. Open, partial and unattempted gates are not described as inaccessible.
