# Validation status — pre-DOI gate

**Canonical date:** 27 October 2026  
**Archival decision:** **HOLD** until all three gates exceed 9/10.

| gate | target | current | status |
|---|---:|---:|---|
| A — archival readiness | >= 9.2 | **9.25** | PASS, pre-DOI |
| B — literature positioning | >= 9.2 | **9.20** | PASS, external priority check still required for 9.5+ |
| C — external mathematical validation | >= 9.0 | **4.0** | HOLD — independent reports/replication not yet received |

## Why Gate C is only 4.0

The repository currently has:

- adversarial internal referee simulation;
- exact CI and deterministic verification;
- complete referee packet;
- clean-room replication specification;
- reviewer scorecard;
- public issues tracking the validation campaign.

These make the project **review-ready**, not externally validated.

The following do not count as external validation:

- author self-review;
- AI-assisted critique;
- GitHub CI;
- independent implementations written by the same research workflow;
- literature searches performed by the authoring team.

## Gate-C upgrade path

### +2.0 — independent dynamics/continued-fractions review
Requires a written report pinned to a repository commit.

### +1.5 — independent arithmetic-dynamics/number-theory review
Requires a second written report by a different person.

### +1.5 — clean-room replication
Requires an independently written implementation reproducing the finite theorem stack.

These increments are not automatic. A report that finds an unresolved critical issue can reduce the score.

## Gate-C passing condition

\[
C\ge9.0
\]

only when:

1. two independent mathematical reports exist;
2. neither leaves a critical issue unresolved;
3. one independent implementation reproduces the core exact outputs;
4. all major criticisms are resolved, answered with evidence, or cause the affected claim to be removed.

## Current operational trackers

- Issue #4 — archival readiness
- Issue #5 — literature/priority closure
- Issue #6 — two independent referee reports
- Issue #7 — clean-room replication

## DOI condition

The archival release is authorized only if:

\[
\boxed{
A\ge9.2,\quad B\ge9.2,\quad C\ge9.0.
}
\]

At present:

\[
\boxed{\text{DOI status: HOLD}}
\]

for a scientifically legitimate reason: external validation has not yet occurred.
