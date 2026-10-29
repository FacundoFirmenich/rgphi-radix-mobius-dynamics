# External reviewer packet

## What to read

A focused mathematical review should not require reading the entire repository.

Recommended sequence:

1. `paper/main.pdf`
2. `paper/supplement.md`
3. `paper/claim-evidence-matrix.csv`
4. `paper/CLAIM_FREEZE.md`
5. `paper/PAPER_I_FINALIZATION_STATUS.md`
6. `docs/SCIENTIFIC_STATUS.md`
7. `docs/literature/CLAIM_BY_CLAIM_POSITIONING.md`
8. `data/certificates/terminal-set-audit.json`
9. `data/certificates/paper-I/benchmark_receipt.json`
10. `data/thresholds/exact-bfs-depth-0-162.csv`
11. `data/thresholds/portal-continuation-costs.csv`
12. `data/thresholds/nonnesting-robustness.csv`
13. `docs/theorems/threshold-robustness-atlas.md`

The logical dependency graph is Figure 1 of the manuscript. Proposition 8.1
states the exact layer-recursion invariant used by the computer-assisted proof.

## Five mathematical questions

1. Do you see a mathematical error in the formal setup, the layer-recursion proposition, or the main theorem?
2. Is the term “nonnested extremal targets” a defensible description of the exact phenomenon?
3. Do you know a theorem or system that makes the main result non-novel or essentially equivalent to known work?
4. Is the benchmark theorem significant enough without a family-level generalization?
5. What is the strongest plausible venue after revision?

## Five computer-assisted-proof questions

1. Is the evidence boundary between compact receipts and the external depth-162 payload stated adequately?
2. Are the continuation receipts independently replayable and sufficiently separated from the checker?
3. What minimal certificate would make the depth-162 no-hit claim checker-complete?
4. Is the target-before-pruning and terminal-set protocol sufficient?
5. What additional adversarial test should precede submission?

## What is *not* being claimed

- `tau_5=212`;
- universality across all bases or seeds;
- invention of Farey or Möbius dynamics;
- invention of state augmentation;
- complete global trap classification;
- a proved global orthomodular lattice;
- physical, quantum, cosmological or ontological implications.

## Prohibited review shortcut

Do not treat closure of `tau_5` as a prerequisite for Paper I. Its theorems are
independent of the open interval.

## Review output

Use `REVIEW_SCORECARD.md` or provide free-form comments classified as critical /
major / minor / editorial. Every review must identify the pinned commit and say
whether the reviewer executed code or used an independent implementation.
