# Paper I frontier adjudication protocol — 30 October 2026

**Authority:** `PUBLICATION_TRACK / P1_EXCLUSIVE`  
**Scope:** governance of unresolved Paper I gates only.

## 1. Foundational rule

A frontier that is open, partial or not yet attempted is not thereby inaccessible.
No P1 document may use `blocked`, `impossible`, `inaccessible`, `cannot be done`
or an equivalent expression unless the declaration satisfies this protocol.

This protocol is a cross-project governance adaptation. It imports no theorem,
data, score, obligation list or scientific claim from the source program.

## 2. Allowed status vocabulary

### `CLOSED_SCOPED`

A defined question or capability is satisfied inside an explicit contract,
hypothesis class, jurisdiction and evidence boundary. It does not imply universal
closure.

### `READY_FOR_EXTERNAL_ACTION`

All internal preparation is complete and the remaining operation must be
performed by a genuine external actor, reviewer or implementation. The gate is
not scientifically blocked.

### `ACTIVE_PARTIAL`

A material attempt has produced progress, but the declared completion criterion
has not been met. The remaining operation and evidence are known.

### `BLOCKED_SPECIFIC`

A precise operation cannot currently proceed because a concrete resource,
permission, artifact or logical prerequisite is missing. The blockage is local
to that operation and must carry the five-field record below.

### `DEPENDENCY_BLOCKED`

The operation is internally feasible but must wait for another named gate. This
is a scheduling dependency, not evidence of scientific impossibility.

### `REFUTED_SCOPED`

A claim or route fails under a frozen contract, hypothesis class and evidence
jurisdiction. A reformulated contract is a new question and may not erase or
reinterpret the prior negative result.

### `SUPERSEDED`

A previously valid local state has been replaced by a stronger result. Its
historical validity and provenance remain preserved.

## 3. Mandatory record for `BLOCKED_SPECIFIC`

Every specific blocker must state:

1. **operation or requirement** — the exact action that cannot proceed;
2. **obstacle evidence** — the observed failure, missing resource or proved
   logical incompatibility, with provenance;
3. **scope** — what the blocker prevents and what it does not prevent;
4. **alternatives** — relevant routes considered, attempted or still available;
5. **reopening condition** — a checkable condition that changes the status.

A missing subscription, payload, account permission or external reviewer does
not automatically block theorem writing, local verification, alternative-source
search, packaging or preparation.

## 4. Conditional impossibility

An impossibility certificate is limited to the stated:

- contract;
- hypotheses;
- model or evidence class;
- target claim;
- jurisdiction.

Changing any of those terms defines a new experiment or theorem. The earlier
negative result remains valid under its original contract.

## 5. Scoped closure

Paper I may be complete as a publication unit without resolving `tau_5`, a
minimal hidden state, a global trap theorem, P2, P3 or any experimental branch.
Conversely, closure of Paper I does not close the wider RGΦ program.

## 6. Independence rule

A second run, implementation or audit controlled by the same research process
may strengthen internal verification, but it is not external independence.

The following require a genuinely external actor:

- specialist review;
- clean-room replication;
- independent preference or venue judgment;
- independent priority assessment when claimed as such.

Internal work may prepare those acts but may not simulate their completion.

## 7. Strategic revisions and score discipline

A strategic reframing may:

- clarify priorities;
- type open questions;
- specify attempts and completion criteria;
- reopen routes under a new declared contract.

It may not silently create:

- new experiments;
- new theorems;
- efficacy claims;
- external validation;
- score improvements.

Any such change requires its own evidence and claim update.

## 8. Exclusive P1 boundary

No P2/P3 or experimental result may be imported to rescue an open P1 gate or
inflate Paper I novelty. Cross-project material may contribute only governance,
software or validation method when the scientific dependency remains absent and
explicit.

## 9. Machine-readable registry

The active P1 frontiers are recorded in:

```text
metadata/PAPER_I_FRONTIERS.json
```

Every status change must update that registry, cite the supporting artifact and
preserve the previous negative or partial state in Git history.
