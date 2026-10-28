# External reviewer packet

## What to read

A focused mathematical review should not require reading the entire repository.

Recommended sequence:

1. `paper/main.pdf`
2. `paper/claim-evidence-matrix.csv`
3. `paper/CLAIM_FREEZE.md`
4. `docs/SCIENTIFIC_STATUS.md`
5. `docs/literature/CLAIM_BY_CLAIM_POSITIONING.md`
6. `data/certificates/terminal-set-audit.json`
7. `data/certificates/paper-I/benchmark_receipt.json`
8. `data/thresholds/portal-continuation-costs.csv`
9. `data/thresholds/nonnesting-robustness.csv`
10. `docs/theorems/threshold-robustness-atlas.md`

For the trap line additionally read:

11. `docs/theorems/trap-classification-theorem.md`
12. `data/traps/C8-exact-audit.csv`
13. `data/traps/trap-atlas-result-D500.json`

## Five mathematical questions

1. Do you see a mathematical error in the formal setup or the main theorem?
2. Is the term “nonnested extremal targets” a defensible description of the exact phenomenon?
3. Do you know a theorem or system that makes the main result non-novel or essentially equivalent to known work?
4. Are the computer-assisted claims documented at a level appropriate for publication?
5. What is the strongest journal tier you would regard as plausible after revision?

## Five computer-assisted-proof questions

1. Is the evidence boundary between compact receipts and the external depth-162 payload stated adequately?
2. Are the continuation receipts independently replayable and sufficiently separated from the checker?
3. What minimal certificate would make the depth-162 no-hit claim checker-complete?
4. Is the target-before-pruning and terminal-set protocol sufficient?
5. What additional adversarial test should precede submission?

## What is *not* being claimed

- \(\tau_5=212\);
- universality across all bases or seeds;
- invention of Farey or Möbius dynamics;
- invention of state augmentation;
- complete global trap classification;
- a proved global orthomodular lattice;
- physical or quantum implications.

## Prohibited review shortcut

Do not treat closure of \(\tau_5\) as a prerequisite for Paper I. Its theorems are independent of the open interval.

## Review output

Use `REVIEW_SCORECARD.md` or provide free-form comments classified as critical / major / minor / editorial.
