# Conflict-of-interest and independence policy

## Purpose

The external-validation gate is intended to measure independent mathematical scrutiny, not social support or informal endorsement.

## Reviewer independence

A mathematical report is considered independent when the reviewer:

- is not an author or contributor to RGΦ;
- did not design the reference implementation or discover the reported theorem;
- is not financially dependent on the project;
- has not been promised authorship, payment contingent on outcome, or reciprocal review;
- discloses recent close collaboration, institutional dependence, family relationship, or other material conflict;
- is free to recommend rejection, major revision, or withdrawal of a claim.

A reviewer may know the author personally. Personal acquaintance must be disclosed but does not automatically invalidate the report.

## Replicator independence

A clean-room replication counts only when:

- the implementation is independently designed;
- source structure is not copied from `src/rgphi` or the historical search engines;
- exact definitions and expected outputs are supplied, but no hidden correction is made to force agreement;
- all discrepancies are reported;
- the environment, code, commit, and result summary are archived.

## Role separation

The preferred panel has three distinct roles:

1. dynamics / continued-fractions reviewer;
2. arithmetic-dynamics / number-theory reviewer;
3. computational replicator.

One person should not fill all three roles.

## Public and private reports

A report may be public or private. A private report counts only if:

- its existence and review scope can be recorded;
- the reviewer consents to the level of attribution used;
- the author records how every critical and major point was resolved.

## Severity and resolution

- **Critical:** invalid theorem, false exact count, invalid state-space definition, or equivalent prior theorem destroying the main novelty claim.
- **Major:** missing hypothesis, incomplete proof boundary, serious reproducibility gap, or substantial literature collision.
- **Minor:** local clarification, notation, citation, or presentation issue.
- **Editorial:** venue and exposition advice.

The gate cannot pass with an unresolved critical issue. Major issues must be corrected, evidenced, or removed from the claim set.
