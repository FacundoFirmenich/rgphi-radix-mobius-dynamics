# Corrected noncommutative energy-norm bound (HDH-033)

Let `D_J = diag(1,...,J)`, `S_J` positive definite and
`S_J >= c D_J`, with `c>0` independent of `h,J`. Assume the
modewise error entries satisfy `|E_jk| <= C h^2 (j k)^(3/2)`.

Set `B=D_J^{-1/2} E D_J^{-1/2}`. Then
`|B_jk|<=C h^2 j k` and

```text
||B||_2 <= ||B||_F <= C h^2 sum(j^2, j=1..J) = O(h^2 J^3).
```

Inverse order of the Löwner inequality gives
`S_J^{-1} <= c^{-1} D_J^{-1}`, hence

```text
||S_J^{-1/2} D_J^{1/2}||_2^2
    = ||D_J^{1/2} S_J^{-1} D_J^{1/2}||_2 <= c^{-1}.
```

Using the exact factorization

```text
S_J^{-1/2} E S_J^{-1/2}
  = (S_J^{-1/2} D_J^{1/2}) B (D_J^{1/2} S_J^{-1/2}),
```

we obtain `||S_J^{-1/2} E S_J^{-1/2}||_2 <= c^{-1}
||B||_2=O(h^2 J^3)`. This does **not** assume `S_J` and `D_J`
commute or that `S_J^{-1/2}` acts entrywise.

Raw is `O(h^2J^4)`. Thus `J_h = O(h^{-alpha})` gives raw decay for
`alpha<1/2` and energy decay for `alpha<2/3`. At
`alpha=1/2`, the raw theorem is critical and yields no decay guarantee,
not asymptotic divergence.

**Scope:** pure conditional matrix/norm theorem. The PDE/FEM modewise
estimate is not established by this lemma. No RGΦ/Paper I authority.
