# RGΦ architecture

This document separates the mathematical system, the evidence pipeline, and the publication objects.

## 1. Mathematical architecture

```mermaid
flowchart LR
    A[Integer-radix map T_B] --> C[Rational partial semigroup]
    B[Möbius-conjugate branch S_B] --> C
    C --> D[Primitive rational reduction]
    D --> E[Farey / prime-wise arithmetic context]
    E --> F[Exact state graph]
    F --> G[Extremal first-hit targets]
    F --> H[Finite recurrent components]
    G --> I[Escape / Bellman value]
    H --> J[Modular traps / infinite hitting distance]
```

The system is not presented as a direct golden-ratio digit correlation. The Fibonacci/golden-ratio structure enters through the projective chart \(H(x)=(1+x)^{-1}\) and its matrix identity.

## 2. Evidence architecture

```mermaid
flowchart TD
    S[Symbolic definitions and proofs] --> R[Reference exact implementation]
    R --> T[Theorem-level tests]
    R --> F[Finite exhaustive searches]
    R --> C[Large computer-assisted searches]
    F --> M[Machine-readable evidence tables]
    C --> K[Checkpoints, hashes, independent kernels]
    S --> Q[Claim-evidence registry]
    M --> Q
    K --> Q
    Q --> P[Paper and public scientific status]
    P --> V[Independent referee review]
    P --> X[Clean-room replication]
    V --> A[Archival v1.0.0]
    X --> A
```

Internal CI establishes deterministic consistency. It does not replace independent mathematical review or external replication.

## 3. Research-object architecture

```mermaid
flowchart LR
    P[Paper I] --- E[Exact evidence data]
    E --- W[Reference software]
    W --- T[Tests and workflows]
    T --- R[Reproducibility protocol]
    R --- L[Literature and priority audit]
    L --- M[Archival metadata]
    M --- P
```

The archival object is designed to be interpretable even when any single component is read independently.

## 4. Publication architecture

- **Paper I:** robust nonnested extremal targets.
- **Paper II:** hidden Farey / \(p\)-adic control, after a general theorem is established.
- **Paper III:** finite modular traps and basin structure, after a family theorem is established.
- **Computational companion:** exact search and certificate architecture.

The repository is broader than any one manuscript. The manuscripts must remain narrower than the repository.

## 5. Validation boundary

The project currently has:

- strong internal exact verification;
- strong research-object and archival infrastructure;
- a specialist-ready literature audit;
- a commit-pinned reviewer bundle.

It does not yet have:

- two independent mathematical referee reports;
- an external clean-room replication;
- a closed historical-priority assessment.

Those are the remaining pre-DOI scientific gates.
