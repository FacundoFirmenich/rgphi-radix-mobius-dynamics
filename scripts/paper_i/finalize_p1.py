#!/usr/bin/env python3
"""Deterministically harden Paper I for specialist review.

The transformation is intentionally narrow and idempotent. It strengthens the
manuscript's theorem-first structure, makes the computer-assisted proof
obligation explicit, adds a compact paper graph, and assembles submission and
review documentation without importing any P2/P3 or experimental claim.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "paper" / "main.tex"
SUPPLEMENT = ROOT / "paper" / "supplement.md"
CLAIM_FREEZE = ROOT / "paper" / "CLAIM_FREEZE.md"
CLAIM_MATRIX = ROOT / "paper" / "claim-evidence-matrix.csv"
REFEREE_PACKET = ROOT / "docs" / "validation" / "REFEREE_PACKET.md"
REVIEWER_WORKFLOW = ROOT / ".github" / "workflows" / "reviewer-bundle.yml"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one anchor, found {count}")
    return text.replace(old, new, 1)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def update_manuscript() -> None:
    text = PAPER.read_text(encoding="utf-8")
    if "% P1-FINALIZATION-2026-10-29" in text:
        return

    text = replace_once(
        text,
        "\\usepackage{amsmath,amssymb,amsthm,booktabs,array,hyperref,mathtools}\n"
        "\\usepackage[margin=1in]{geometry}",
        "\\usepackage{amsmath,amssymb,amsthm,booktabs,array,hyperref,mathtools}\n"
        "\\usepackage{tikz}\n"
        "\\usetikzlibrary{arrows.meta,positioning,calc}\n"
        "\\usepackage[margin=1in]{geometry}",
        "packages",
    )
    text = replace_once(text, "\\date{27 October 2026}", "\\date{29 October 2026}", "date")
    text = replace_once(
        text,
        "\\date{29 October 2026}\n\n\\begin{document}",
        "\\date{29 October 2026}\n"
        "% P1-FINALIZATION-2026-10-29\n"
        "\\subjclass[2020]{Primary 37E05; Secondary 11A55, 11A63, 49L20}\n"
        "\\keywords{arithmetic dynamics, radix transformations, M\\\"obius semigroups, first-hit times, dynamic programming, computer-assisted proof}\n\n"
        "\\begin{document}",
        "metadata",
    )

    contribution_anchor = (
        "\\end{enumerate}\n\n"
        "The depth-five hitting time is not needed here.  Its current exact interval is $186\\le \\tau_5\\le212$, but none of the claims below depends on closing that interval."
    )
    graph = r"""\end{enumerate}

% P1-PAPER-GRAPH
\begin{figure}[t]
\centering
\begin{tikzpicture}[
  box/.style={draw, rounded corners, align=center, inner sep=4pt,
              font=\small, text width=.29\textwidth},
  wide/.style={box, text width=.66\textwidth},
  arr/.style={-{Stealth[length=2mm]}, thick}
]
\node[wide] (system) {partial radix--M\"obius semigroup\\and forward-invariant terminal set};
\node[wide, below=4mm of system] (layers) {exact layer recursion on primitive rationals\\with admissibility and exact deduplication};
\node[box, below left=5mm and 5mm of layers] (chronology) {global first-hit chronology\\$45,85,120,162$};
\node[box, below right=5mm and 5mm of layers] (continuations) {independent continuation searches\\and no-hit certificates};
\node[box, below=5mm of chronology] (robustness) {record-height atlas\\and exact robustness intervals};
\node[box, below=5mm of continuations] (nonnesting) {three consecutive failures\\of nested optimality};
\node[wide, below=7mm of $(robustness)!0.5!(nonnesting)$] (bellman) {target depth and current height are not sufficient Bellman variables\\for the declared sequential portal objectives};
\draw[arr] (system) -- (layers);
\draw[arr] (layers) -- (chronology);
\draw[arr] (layers) -- (continuations);
\draw[arr] (chronology) -- (robustness);
\draw[arr] (continuations) -- (nonnesting);
\draw[arr] (robustness) -- (bellman);
\draw[arr] (nonnesting) -- (bellman);
\end{tikzpicture}
\caption{Logical dependency graph of Paper I.  Symbolic definitions and the certified terminal convention feed an exact finite recursion; global layers and independent continuation searches establish chronology, nonnesting and robustness before the Bellman consequences are drawn.}
\label{fig:paper-graph}
\end{figure}

The depth-five hitting time is not needed here.  Its current exact interval is $186\le \tau_5\le212$, but none of the claims below depends on closing that interval."""
    text = replace_once(text, contribution_anchor, graph, "paper graph")

    method_anchor = (
        "\\section{Certified computational method}\n\n"
        "All computations use reduced pairs of nonnegative integers.  No floating-point comparison decides target membership.  The proof stack contains:"
    )
    method = r"""\section{Certified computational method}

\begin{proposition}[Exactness of the layer recursion]\label{prop:layer-exactness}
Let $\mathcal L_0=\{x_0\}\setminus E$ and define recursively
\[
\mathcal L_{n+1}=\left\{A(x)\notin E:
 x\in\mathcal L_n,\ A\in\{T,S\},\ A\text{ is admissible at }x\right\},
\]
where every rational is reduced to primitive form and duplicate states are identified.  Then $\mathcal L_n$ is exactly the set of nonterminal states reachable from $x_0$ by an admissible word of length $n$.  Consequently,
\[
\tau_m(\kappa)=\min\{n:\mathcal L_n\cap P_m(10,\kappa)\ne\varnothing\}.
\]
\end{proposition}

\begin{proof}
The statement is immediate at $n=0$.  Assume it holds at time $n$.  Every admissible word of length $n+1$ has an admissible prefix of length $n$ and a final generator $A\in\{T,S\}$, hence its endpoint is generated by the displayed recursion.  Conversely, every state produced by the recursion extends an admissible length-$n$ word by one admissible generator.  Removing $E$ loses no later nonterminal trajectory because $E$ is forward invariant.  Primitive reduction and exact deduplication change only the representation and multiplicity of a rational state, not reachability.  Induction proves the equality of layers, and the first-hit formula follows.
\end{proof}

All computations use reduced pairs of nonnegative integers.  No floating-point comparison decides target membership.  Target membership is tested on every exact child before any certified terminal or viability pruning.  The proof stack contains:"""
    text = replace_once(text, method_anchor, method, "layer exactness")

    evidence_old = (
        "The global layer profile through depth $162$ and the five continuation profiles required by Theorems 5.1 and 7.4 accompany the manuscript.  The result is therefore a computer-assisted theorem with a finite, replayable evidence chain, rather than a numerical simulation."
    )
    evidence_new = (
        "The repository contains the exact layer-maxima ledger through depth $162$, the threshold atlas, a compact benchmark receipt, the complete terminal-set audit, five continuation profiles, replay source, an independent receipt checker, and cryptographic hashes.  The lightweight reviewer bundle includes the compact evidence needed to audit the headline claims.  The complete $329{,}106{,}757$-state depth-$162$ payload is not duplicated in ordinary Git; clean archival deposition or independent regeneration remains a pre-DOI gate.  The result is therefore a computer-assisted theorem with a finite and explicitly delimited evidence chain, rather than a numerical simulation."
    )
    text = replace_once(text, evidence_old, evidence_new, "evidence boundary")

    limitations_old = (
        "The exact threshold atlas in this paper is complete through depth $162$ for the benchmark seed, base, and terminal convention.  The robustness theorems are exact on their stated intervals, but no universality in $B$, seed, or $\\kappa$ is claimed.  The hidden-state interpretation is supported by exact counterexamples; minimality of any particular augmented coordinate system is not proved here.  The large layer enumeration is internally reproducible and accompanied by independent checking infrastructure, but an external clean-room replication has not yet been completed.  Finally, the priority claim remains provisional pending closed-database citation chaining and external specialist review."
    )
    limitations_new = (
        "The exact threshold atlas in this paper is complete through depth $162$ for the benchmark seed, base, and terminal convention.  The robustness theorems are exact on their stated intervals, but no universality in $B$, seed, or $\\kappa$ is claimed.  The hidden-state interpretation is supported by exact counterexamples; minimality of any particular augmented coordinate system is not proved here.  The compact theorem stack is internally replayable, while archival deposition or clean regeneration of the full depth-$162$ layer remains open.  No external clean-room implementation has yet reproduced the complete chronology.  Finally, the priority claim remains provisional pending closed-database citation chaining and external specialist review."
    )
    text = replace_once(text, limitations_old, limitations_new, "limitations")

    data_old = (
        "The submission package contains the global layer profile, exact continuation profiles, threshold-atlas generator, trap-independent verifiers, and SHA-256 manifests.  A public archival DOI and Software Heritage identifier will be assigned at release; no identifier is claimed before deposition."
    )
    data_new = (
        "The public research repository is available at \\url{https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics}.  The submission package contains the compact global layer profile, exact continuation profiles, threshold-atlas data and generator, terminal-set audit, independent receipt checker, and SHA-256 manifests.  The complete depth-$162$ state payload is outside the lightweight package and is an explicit archival/clean-regeneration gate.  A public archival DOI and Software Heritage identifier will be assigned only after the reviewed commit and evidence set are frozen; no identifier is claimed before deposition."
    )
    text = replace_once(text, data_old, data_new, "data availability")
    PAPER.write_text(text, encoding="utf-8")


def update_supplement() -> None:
    text = SUPPLEMENT.read_text(encoding="utf-8")
    if "## S10. Formal layer recursion and reviewer replay" in text:
        return
    addition = r"""

## S10. Formal layer recursion and reviewer replay

Let `L_0={x_0}\E` and recursively form `L_{n+1}` from every admissible exact
`T/S` child of `L_n`, remove the certified forward-invariant terminal set, reduce
every fraction primitively, and deduplicate exact rational pairs. Proposition
8.1 of the manuscript proves by induction that `L_n` is precisely the
nonterminal reachable set at time `n`. Thus first-hit absence and presence are
finite reachability statements, not heuristic properties of sampled paths.

Minimal compact verification:

```bash
python -m pip install -e '.[dev]'
rgphi verify
python scripts/paper_i/verify_receipt.py
```

Full exact replay of the five continuation searches:

```bash
scripts/paper_i/replay_exact.sh
```

The replay output must end in:

```text
PASS_PAPER_I_FULL_EXACT_REPLAY
```

## S11. Submission evidence boundary

The lightweight reviewer bundle contains the manuscript, supplement, claim
freeze, claim-evidence matrix, compact benchmark receipt, evidence boundary,
terminal-set audit, exact layer profile, robustness tables, continuation
profiles, replay scripts and independent checker. The complete depth-162 state
payload is intentionally not duplicated in ordinary Git. Before archival DOI
freeze it must either be deposited in an external research-data archive with a
cryptographic manifest or regenerated cleanly by an independent implementation.
This open archival item does not alter the exact finite theorems stated in the
manuscript, but it remains a submission-quality and long-term reproducibility
gate.
"""
    SUPPLEMENT.write_text(text.rstrip() + addition + "\n", encoding="utf-8")


def update_claims() -> None:
    freeze = """# Paper I claim freeze

## Allowed central claims

1. The radix and Möbius-conjugate branches define a noncommutative partial rational semigroup with determinant-`B` branch matrices.
2. In the declared decimal benchmark, `tau_1..tau_4 = 45,85,120,162`.
3. Three consecutive optimal target transitions are nonnested, with delays `2,19,6`.
4. The chronology is stable for `κ∈[10.6197,11.643)` and simultaneous nonnesting for `κ∈[10.6197,11.01)`.
5. Target depth and present height are not sufficient Bellman variables in this system.
6. The declared exact layer recursion enumerates precisely the nonterminal reachable set at every finite depth, conditional only on the independently certified forward invariance of the terminal set.

## Required demarcations

- `tau_5` is open in `[186,212]` and is not needed for Paper I.
- The full depth-162 payload is not duplicated in the compact deployment.
- No priority claim for a “new Farey map”, p-adic interpreters, global orthomodularity or digit correlation with `φ`.
- No U5-HD, HM, EO, ODT, BQ, OMNI or HDH claim enters Paper I.
- The compact receipt/checker stack does not substitute for external clean-room replication.

## Submission blockers

- Specialist literature review and citation chaining.
- Clean archival deposition or independent regeneration of the global layer certificate.
- One external replay of the compact continuation theorem stack.
- Final journal choice and format-specific submission audit.
"""
    write(CLAIM_FREEZE, freeze)

    matrix = CLAIM_MATRIX.read_text(encoding="utf-8").rstrip()
    if "P15," not in matrix:
        matrix += (
            "\nP15,the recursive exact layers equal the nonterminal reachable sets,"
            "symbolic induction plus independently audited terminal forward invariance,CLOSED,"
            "Proposition 8.1,Target checked before pruning; primitive reduction and deduplication preserve reachability"
        )
    write(CLAIM_MATRIX, matrix)


def update_referee_packet() -> None:
    content = """# External reviewer packet

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
"""
    write(REFEREE_PACKET, content)


def create_submission_docs() -> None:
    status = """# Paper I finalization status — 29 October 2026

**Branch purpose:** Paper I only. P2/P3, Stage B2 and all experimental branches
remain outside the theorem dependency graph.

## Current internal scorecard

| Dimension | Score / 10 | Current assessment |
|---|---:|---|
| Formal definition and domain | 9.4 | Partial-semigroup domain and admissibility explicit |
| Main theorem clarity | 9.3 | Chronology, nonnesting and robustness stated exactly |
| Computer-assisted proof architecture | 9.1 | Exact layer recursion now formalized; compact checker separated |
| Claim hygiene | 9.5 | Narrow freeze and explicit nonclaims |
| Literature positioning | 8.2 | Strong open-literature map; specialist closed-database check pending |
| Reproducibility | 8.7 | Compact replay strong; full depth-162 payload archival gate open |
| Generality | 7.1 | Exact benchmark theorem; family theorem intentionally deferred |
| External validation | 4.0 | Two specialist reviews and clean-room replay still open |
| Editorial readiness | 8.8 | Submission package ready after external gate and target selection |

## Material improvements in this finalization

- added MSC2020 classifications and keywords;
- inserted a logical paper graph;
- proved exactness of the finite layer recursion by induction;
- made target-before-pruning semantics explicit;
- sharpened the evidence and payload boundary;
- expanded the supplement with exact replay commands;
- strengthened the referee packet;
- added venue-specific cover letters and a journal decision memo;
- expanded the reviewer bundle with the supplement, replay scripts and compact exact data.

## Remaining binding gates

1. two independent specialist reviews pinned to one commit;
2. closed-database priority/citation chaining;
3. one external replay or clean-room implementation;
4. archival deposition or clean regeneration of the full depth-162 certificate;
5. final venue decision, formatting audit and signed release candidate.

## Promotion rule

Paper I can be submitted before `tau_5` is resolved. It cannot be called
externally validated or archival-complete before the five gates above pass.
"""
    write(ROOT / "paper" / "PAPER_I_FINALIZATION_STATUS.md", status)

    decision = """# Paper I journal decision memo — 29 October 2026

## Recommended strategy

### Ambitious first submission: Journal of Modern Dynamics

Best conceptual fit when the paper is framed as an interaction between rational
dynamics and number theory. Use only after two positive specialist reviews. The
principal editorial risk is benchmark specificity rather than correctness.

### Best artifact-aware alternative: Experimental Mathematics

Strongest fit for an exact theorem discovered and certified through large-scale
computer experimentation, with replayable evidence and transparent negative
boundaries. This is the safest venue if reviewers judge the benchmark too narrow
for JMD.

### Fast specialist alternative: Dynamical Systems

The current manuscript is close to the journal's preferred short-paper range.
Use a dynamics-first framing and explain why the counterexample exposes a real
state-sufficiency issue rather than a bespoke rational puzzle.

### Aspirational alternative: Ergodic Theory and Dynamical Systems

Plausible only if specialist review judges the theorem conceptually central or a
family-level extension is added. Do not delay Paper I indefinitely to chase this
ceiling.

## Binding decision rule

1. Send the frozen reviewer packet to two specialists.
2. If both regard the result as conceptually significant beyond the benchmark,
   submit to JMD.
3. If correctness is endorsed but benchmark specificity remains the dominant
   criticism, submit to Experimental Mathematics.
4. If a concise specialist dynamics paper is preferred, submit to Dynamical
   Systems.

No venue decision may broaden the frozen claims.
"""
    write(ROOT / "docs" / "validation" / "PAPER_I_JOURNAL_DECISION_2026-10-29.md", decision)

    cover_ds = """# Cover letter — Dynamical Systems

Dear Editors,

Please consider the manuscript **“Nonnested extremal targets in a rational
radix–Möbius semigroup”** by Facundo Firmenich.

The paper gives an exact arithmetic example in which states that first attain
three consecutive extremal targets fail to be optimal precursors of the next
target. For the declared decimal benchmark the first-hit times are 45, 85, 120
and 162, the continuation delays are 2, 19 and 6 actions, and the phenomenon
persists on the exact positive-width interval

\[
\kappa\in[10.6197,11.01).
\]

The result is presented as a theorem about a partial rational dynamical
semigroup, not as a novelty claim for Bellman's principle or Farey dynamics.
The computational component uses primitive integer arithmetic, a formally
specified exact layer recursion, independent continuation searches, compact
receipts, source code and checkers. The open depth-five problem is outside the
dependency graph of the manuscript.

We believe the manuscript fits *Dynamical Systems* because it isolates a clear
and robust dynamical obstruction to nested target optimality in a
noncommutative interval system, while remaining short and accessible beyond the
specific computation.

The manuscript is not under consideration elsewhere. The public research
repository is:

https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics

Sincerely,

Facundo Firmenich  
Barcelona, Spain
"""
    write(ROOT / "paper" / "cover-letter-dynamical-systems.md", cover_ds)

    cover_em = """# Cover letter — Experimental Mathematics

Dear Editors,

Please consider the manuscript **“Nonnested extremal targets in a rational
radix–Möbius semigroup”** by Facundo Firmenich.

The manuscript reports an exact theorem emerging from systematic computation
in a rational noncommutative dynamical system. It certifies four extremal
first-hit times, three consecutive failures of nested optimality, and a
positive exact parameter interval on which the phenomenon persists. The
computer is used neither for floating-point simulation nor as a black box: the
state recursion is exact, the terminal convention is independently audited,
target comparisons use integer arithmetic, and the principal continuation
searches are independently replayable.

The submission includes the mathematical proof architecture, compact exact
evidence, source, checkers, hashes and a precise account of what is not yet
archived or externally replicated. The unresolved depth-five optimum is
explicitly outside the paper's theorem dependency graph.

We believe the work fits *Experimental Mathematics* because experimentation,
formal theorem extraction and reproducibility are integral to the mathematical
contribution, while the final claims are exact and narrowly delimited.

The manuscript is not under consideration elsewhere. The public research
repository is:

https://github.com/FacundoFirmenich/rgphi-radix-mobius-dynamics

Sincerely,

Facundo Firmenich  
Barcelona, Spain
"""
    write(ROOT / "paper" / "cover-letter-experimental-mathematics.md", cover_em)

    prebuttal = """# Paper I referee prebuttal — concise response map

| Likely objection | Evidence-based answer | Remaining boundary |
|---|---|---|
| `S_B` is not a total interval map | Natural domain `[1/2,1]` and admissible-word semantics are explicit | none |
| terminal pruning may remove valid trajectories | 23 states and all 46 attempted branches independently audited; zero admissible escapes | convention is benchmark-specific |
| chronology may be threshold-fine-tuned | exact intervals `[10.6197,11.643)` and `[10.6197,11.01)` | no universality claim |
| “Bellman failure” overclaims a classical principle | claim is only insufficiency of two compressed observables in this exact system | minimal sufficient state open |
| computation is opaque | Proposition 8.1 formalizes recursion; compact receipt, replay source and independent checker supplied | full depth-162 payload archive/clean regeneration open |
| single benchmark limits significance | accepted and stated; base-`B` formalism is general but finite theorem is benchmark-only | family theorem belongs to later work |
| priority is uncertain | wording remains “we are not aware of”; recent projective, finite-orbit and semigroup literature is cited | specialist closed-database check open |
| `tau_5` remains open | no Paper I theorem depends on it | Stage B2 belongs to P2 |
"""
    write(ROOT / "docs" / "validation" / "PAPER_I_REFEREE_PREBUTTAL_2026-10-29.md", prebuttal)


def update_reviewer_workflow() -> None:
    text = REVIEWER_WORKFLOW.read_text(encoding="utf-8")
    if "paper/PAPER_I_FINALIZATION_STATUS.md" in text:
        return
    old_dirs = (
        'mkdir -p "$OUT/paper" "$OUT/data/certificates/paper-I" \\\n            "$OUT/docs/validation" "$OUT/docs/literature" "$OUT/metadata"'
    )
    new_dirs = (
        'mkdir -p "$OUT/paper" "$OUT/data/certificates/paper-I" "$OUT/data/certificates" \\\n            "$OUT/data/thresholds" "$OUT/scripts/paper_i" "$OUT/docs/theorems" \\\n            "$OUT/docs/validation" "$OUT/docs/literature" "$OUT/metadata"'
    )
    text = replace_once(text, old_dirs, new_dirs, "reviewer bundle directories")

    old_copy = (
        'cp paper/main.pdf paper/main.tex paper/claim-evidence-matrix.csv \\\n            paper/CLAIM_FREEZE.md "$OUT/paper/"'
    )
    new_copy = (
        'cp paper/main.pdf paper/main.tex paper/supplement.md \\\n            paper/claim-evidence-matrix.csv paper/CLAIM_FREEZE.md \\\n            paper/PAPER_I_FINALIZATION_STATUS.md "$OUT/paper/"'
    )
    text = replace_once(text, old_copy, new_copy, "reviewer paper files")

    anchor = (
        'cp data/certificates/paper-I/benchmark_receipt.json \\\n            data/certificates/paper-I/EVIDENCE_BOUNDARY.md \\\n            data/certificates/paper-I/paper-I-profiles.zip \\\n            data/certificates/paper-I/paper-I-profiles.zip.sha256 \\\n            "$OUT/data/certificates/paper-I/"'
    )
    expanded = anchor + r'''
          cp data/certificates/terminal-set-audit.json "$OUT/data/certificates/"
          cp data/thresholds/exact-bfs-depth-0-162.csv \
            data/thresholds/benchmark-robustness.csv \
            data/thresholds/portal-continuation-costs.csv \
            data/thresholds/nonnesting-robustness.csv \
            data/thresholds/robustness-result.json \
            "$OUT/data/thresholds/"
          cp scripts/paper_i/replay_exact.sh scripts/paper_i/verify_receipt.py \
            "$OUT/scripts/paper_i/"
          cp docs/theorems/threshold-robustness-atlas.md "$OUT/docs/theorems/"'''
    text = replace_once(text, anchor, expanded, "reviewer compact evidence")

    validation_anchor = (
        'cp docs/validation/REPLICATION_REPORT_TEMPLATE.md "$OUT/docs/validation/"'
    )
    validation_expanded = validation_anchor + r'''
          cp docs/validation/PAPER_I_JOURNAL_DECISION_2026-10-29.md \
            docs/validation/PAPER_I_REFEREE_PREBUTTAL_2026-10-29.md \
            "$OUT/docs/validation/"'''
    text = replace_once(text, validation_anchor, validation_expanded, "reviewer validation docs")
    REVIEWER_WORKFLOW.write_text(text, encoding="utf-8")


def add_regression_test() -> None:
    test = r'''from pathlib import Path


def test_paper_i_finalization_markers() -> None:
    root = Path(__file__).resolve().parents[1]
    manuscript = (root / "paper" / "main.tex").read_text(encoding="utf-8")
    assert "% P1-FINALIZATION-2026-10-29" in manuscript
    assert "% P1-PAPER-GRAPH" in manuscript
    assert "Exactness of the layer recursion" in manuscript
    assert "Primary 37E05; Secondary 11A55, 11A63, 49L20" in manuscript
    assert "complete $329{,}106{,}757$-state depth-$162$ payload" in manuscript

    supplement = (root / "paper" / "supplement.md").read_text(encoding="utf-8")
    assert "## S10. Formal layer recursion and reviewer replay" in supplement
    assert "PASS_PAPER_I_FULL_EXACT_REPLAY" in supplement

    claims = (root / "paper" / "claim-evidence-matrix.csv").read_text(encoding="utf-8")
    assert "P15,the recursive exact layers equal the nonterminal reachable sets" in claims

    workflow = (root / ".github" / "workflows" / "reviewer-bundle.yml").read_text(encoding="utf-8")
    assert "paper/supplement.md" in workflow
    assert "data/thresholds/exact-bfs-depth-0-162.csv" in workflow
    assert "scripts/paper_i/replay_exact.sh" in workflow
'''
    write(ROOT / "tests" / "test_paper_i_finalization.py", test)


def main() -> None:
    update_manuscript()
    update_supplement()
    update_claims()
    update_referee_packet()
    create_submission_docs()
    update_reviewer_workflow()
    add_regression_test()
    print("PASS_PAPER_I_FINALIZATION_GENERATION")


if __name__ == "__main__":
    main()
