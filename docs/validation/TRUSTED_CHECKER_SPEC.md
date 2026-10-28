# Trusted checker specification v0.1

The checker must be smaller and logically weaker than the generator. It accepts immutable receipts and verifies:

1. canonical state encoding and primitive reduction;
2. exact branch semantics and admissibility;
3. target test before pruning;
4. terminal/trap closure certificates;
5. layer ordering, uniqueness and hashes;
6. witness replay for `HIT`;
7. complete frontier coverage for `NO_HIT`;
8. the claim-evidence boundary recorded in the canon.

The current implementation covers items 1–3 and the compact Paper I continuation receipts. The full Stage B2 no-hit checker remains open because the canonical checkpoint payload is absent.
