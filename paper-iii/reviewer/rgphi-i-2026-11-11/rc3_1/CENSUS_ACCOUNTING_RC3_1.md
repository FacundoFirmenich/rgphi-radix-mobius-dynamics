# Exact census accounting — RC3.1

For bases `2 <= B <= 60` and cardinality at most five:

- all 19 bases with `gcd(B,6)=1` are ruled out symbolically by the cycle budget;
- 40 bases remain after that disjoint symbolic partition;
- the archived computation nevertheless performs 47 exact divisor-universe runs;
- seven of those runs (`5,7,11,13,17,19,25`) redundantly recheck bases already ruled out symbolically;
- the remaining 12 coprime-to-six bases are handled by the budget alone;
- the 47 exact runs examine 2,210,941 candidate states and find 14 closed SCCs, all permutational.

Thus both identities are correct but count different things:

```text
19 symbolic + 40 remaining = 59 bases        (disjoint mathematical partition)
47 exact runs + 12 budget-only = 59 bases    (actual method used per base)
```

The checker `src/rmr/check_census_B2_60.py` verifies the overlap explicitly.
