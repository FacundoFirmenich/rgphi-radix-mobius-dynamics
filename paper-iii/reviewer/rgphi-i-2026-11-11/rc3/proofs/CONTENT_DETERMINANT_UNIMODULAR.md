# Determinant-controlled content and unimodular invariance

Let `M` be an integer `2 x 2` matrix with nonzero determinant and let `v` be a primitive integer vector.

## Theorem

`cont(Mv)` divides `|det M|`.

If `U in GL_2(Z)`, then `cont(Uw)=cont(w)` for every integer vector `w`. Therefore primitive content defects are invariant under integral projective changes of coordinates and under unimodular conjugacy of branch families.

## Proof

If `d=cont(Mv)`, then `d` divides both coordinates of `adj(M)Mv=(det M)v`. Since the coordinates of `v` are coprime, Bezout gives `d | det M`. Apply the same statement to `U` and `U^{-1}` to obtain equality of contents.

## Role in the paper

This places the local gcd laws inside a general degree-one projective-arithmetic fact. The novelty claim is not the determinant lemma itself; it is the use of exact content loss to control finite closed rational subdynamics.
