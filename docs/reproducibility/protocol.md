# External replication and certification protocol

## 1. Principle

Publishing source code is not sufficient to claim independent reproducibility.

A computational mathematical result should preserve:

- mathematical specification;
- source code;
- environment;
- inputs;
- exact outputs;
- provenance;
- claim-to-evidence mapping;
- a verifier smaller than the discovery system when possible.

## 2. Replication levels

### Level A — repository reproduction

Run the reference implementation and reproduce its declared outputs.

### Level B — independent engine

Reimplement the transition system independently and compare exact states, counts, intervals, and hashes.

### Level C — proof/certificate checking

Verify a compact proof artifact without trusting the original search engine.

RGΦ currently supports Level A strongly, contains partial Level B historical cross-checks, and treats stronger Level C certification as an active engineering goal.

## 3. Clean-room implementation specification

A clean-room implementation should use only the mathematical definitions, not the reference source structure.

Required objects:

1. reduced rational state \(a/b\);
2. \(T_B\);
3. admissible \(S_B\);
4. declared terminal set;
5. portal-height predicate;
6. exact per-level set semantics;
7. optional pruning only after a separate mathematical proof.

## 4. First replication targets

A new implementation should reproduce, in order:

1. benchmark first-hit times \(45,85,120,162\);
2. continuation times \(87,139,168\);
3. exact robustness intervals;
4. \(C_8\) forward invariance;
5. denominator-\(\le500\) trap-atlas counts.

Only after these small/medium targets agree should a replicator attempt depth-five large searches.

## 5. Large-search reporting

Every proof-relevant large run should record:

- exact source state and global time;
- target predicate;
- terminal convention;
- pruning theorem;
- visited states;
- raw child events;
- pruning counts;
- maximum frontier;
- final frontier;
- canonical hash;
- hardware/software environment;
- wall time and memory.

## 6. Persistent identity

For an archival release record:

- Git tag;
- Git commit SHA;
- Zenodo version DOI;
- Zenodo concept DOI;
- Software Heritage identifier when available;
- container digest when published;
- SHA-256 manifest;
- claim-registry version.

Identifiers not yet assigned must be reported as pending, never fabricated.

## 7. Environment

The current public release includes Python environment descriptors, a Dockerfile, CI workflows, and exact source.

Future high-cost campaigns should additionally publish a pinned OCI image or equivalent container digest.

## 8. Certificate architecture

The long-term preferred architecture separates:

\[
\text{search engine}
\rightarrow
\text{certificate writer}
\rightarrow
\text{small trusted checker}.
\]

The checker should verify mathematical validity without reproducing the full search strategy.

## 9. External replication report

An independent report should state:

- repository release/tag;
- whether the implementation was clean-room;
- all deviations from the reference environment;
- exact matching and nonmatching outputs;
- checksums;
- unresolved discrepancies.

## 10. Scientific boundary

Until a genuinely independent external group has reproduced the central computations, the repository should say:

> **internally reproducible and independently checkable in parts; external clean-room replication pending.**
