# External mathematical validation protocol

## Purpose

Obtain independent evidence that the main RGΦ claims are:

1. mathematically well-defined;
2. correctly proved or correctly certified;
3. positioned responsibly against prior literature;
4. reproducible independently of the discovery workflow.

The author’s own review, AI-assisted review, and CI do **not** count as external validation.

## Review roles

### Reviewer A — dynamics / continued fractions

Ideal expertise:

- interval dynamics;
- continued fractions;
- Farey/Gauss systems;
- projective or Möbius dynamics;
- natural extensions.

Questions:

1. Is the partial-transformation semigroup defined unambiguously?
2. Is the nonnesting result mathematically meaningful beyond terminology?
3. Are the robustness intervals stated with the correct endpoint conventions?
4. Is there known prior art that substantially anticipates the theorem?
5. Is the manuscript suitable for a journal such as Journal of Modern Dynamics or Experimental Mathematics?

### Reviewer B — number theory / arithmetic dynamics

Ideal expertise:

- arithmetic dynamics;
- multiplicative order / rational orbits;
- Diophantine or continued-fraction arithmetic;
- exact computation.

Questions:

1. Are branch-reduction and denominator arguments correct?
2. Is the trap mechanism genuinely structural?
3. Are general base-\(B\) claims scoped correctly?
4. Are any number-theoretic novelty claims overstated?
5. What theorem would most increase the project’s mathematical significance?

### Replicator C — independent computational verification

The replicator should not copy the implementation architecture.

They receive:

- mathematical definitions;
- terminal set;
- exact expected outputs;
- claim/evidence table.

They independently implement the maps and state enumeration.

## Minimum replication targets

| target | expected result |
|---|---|
| terminal states | 23 |
| attempted T/S branch checks | 46 |
| admissible terminal escapes | 0 |
| \(\tau_1\) | 45 |
| \(\tau_2\) | 85 |
| \(\tau_3\) | 120 |
| \(\tau_4\) | 162 |
| continuation from 128/129 | total time 87 |
| continuation from 1202/1203 | total time 139 |
| continuation from 11156/11157 | total time 168 |
| common chronology interval | [10.6197, 11.643) |
| robust nonnesting interval | [10.6197, 11.01) |
| \(C_8\) size | 8 |
| \(C_8\) max portal height | 13 |
| D<=500 states | 76,094 |
| D<=500 edges | 109,254 |
| D<=500 SCCs | 23,176 |
| closed SCCs modulo terminal | 153 |
| finite forward closures | 1,502 |

## Severity model

### Critical

Invalid theorem, wrong exact count, invalid state-space definition, or directly anticipated main theorem.

### Major

Missing hypothesis, incomplete proof boundary, weak reproducibility, or literature collision requiring substantial reframing.

### Minor

Presentation, notation, missing citation, local clarification.

### Editorial

Style or journal-fit recommendation.

## Passing criterion

The validation gate passes only when:

- zero unresolved critical issues;
- all major issues are resolved or explicitly remove a claim;
- two independent mathematical reviewers recommend at least “publishable after minor revision”;
- one independent implementation reproduces the core finite theorem stack.

## Version pinning

Each report must identify:

- repository commit SHA;
- manuscript PDF hash or commit;
- date;
- role of reviewer;
- whether the review included code execution.

Anonymous or private reviews may be summarized publicly only with reviewer consent.
