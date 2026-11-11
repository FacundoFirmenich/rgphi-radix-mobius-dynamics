# Simulated referee report B — number theory / computer-assisted proof

## Recommendation after RC1

**MINOR REVISION / artifact review required.**

This is a simulated adversarial report, not an independent external certification.

## Major questions resolved

1. Article and machine-readable artifacts now use the same labelled five-state object:
   `T=[1,0,3,2,4]`, `S=[4,2,1,0,0]`, strict edge `S3:x3->x0`.
2. The non-substantive finite-type toy checker was removed.
3. The five-state replay no longer claims minimality by itself.
4. The 37-row nonsquare certificate was recomputed exactly; each row is excluded by a nonresidue modulo `68`, `55` or `71`.
5. The infinite counterfamily is proved by generalized CRT; the 1,001-base Python/C++ replay is regression evidence only.

## Additional checks

- strict-`T` descent recomputed;
- strict-`S` quotient bounds recomputed;
- gcd/parity arguments added;
- universal CRT theorem checks exact gcd conditions;
- spectral JSON reconstructs the branch product exactly.

## Build audit

A fresh-directory internal simulation ran `make verify` and `make pdf`: all checkers and C++ compilation passed; both PDFs compiled without undefined references, overfull boxes or bibliography warnings; extracted text matched the primary build.

## Remaining requests

- confirm author metadata;
- obtain an independent clean-room replay;
- deposit immutable hashes at release;
- rerun priority search in closed bibliographic databases.

## Recommendation

No unresolved fatal or major issue remains within scope. Independent external artifact review is still mandatory.
