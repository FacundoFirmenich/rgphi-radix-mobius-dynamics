# Paper I

## Nonnested extremal targets in a rational radix–Möbius semigroup

This directory contains the current submission-oriented manuscript and its immediate evidence map.

## Files

- main.tex — canonical manuscript source;
- main.pdf — rendered reference copy;
- supplement.md — supplementary notes and exact evidence pointers;
- claim-evidence-matrix.csv — manuscript claim to repository artifact map;
- references.bib — bibliography;
- cover-letter-jmd.md — working cover letter for Journal of Modern Dynamics.

## Scientific scope

Paper I is intentionally restricted to claims that are already mature:

- exact rational radix–Möbius system;
- benchmark first-hit chronology through depth four;
- three consecutive nonnesting counterexamples;
- exact threshold robustness;
- exact finite/computer-assisted methodology.

It does not require a solution of the depth-five optimum or a global theory of hidden arithmetic context.

## Build

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The GitHub paper workflow performs the same build in a clean environment.

## Evidence discipline

Every headline numerical statement should have an entry in claim-evidence-matrix.csv.

If a result is modified, update the matrix and the repository verifier before changing the manuscript prose.
