# T006-B — observer-relative hyperaccess

## Exact correction

For fixed `B` and word length `m`,
\[
\boldsymbol\nu(w),\quad \Delta_w,\quad \log\Delta_w,\quad
\alpha(w)=\frac{\log\Delta_w}{m\log B}
\]
are mutually determining. Equality of the logarithmic receipts implies equality of the underlying integers and therefore equality of all prime valuations by unique factorization.

The prime vector is coordinate-resolved, but it is not more informative than the exact scalar receipt. The earlier wording suggesting exact information loss from vector to scalar is withdrawn.

## Observer-relative quantities

For a length-`m` path `W`, let
\[
\mathbf R(W)=(a_{e_1},\ldots,a_{e_m})
\]
be the local content history and
\[
N(W)=\sum_i a_{e_i}
\]
its terminal holonomy.

Given an observer map `O(W)` and path law `mu`, define
\[
\mathsf H^{\rm path}_\mu(O)=H_\mu(\mathbf R(W)\mid O(W)),
\]
\[
\mathsf H^{\rm term}_\mu(O)=H_\mu(N(W)\mid O(W)).
\]
Then
\[
\boxed{\mathsf H^{\rm path}_\mu(O)\ge\mathsf H^{\rm term}_\mu(O)\ge0.}
\]
The corresponding zero-error ambiguities are the logarithms of the maximal numbers of distinct histories or terminal receipts inside one observer fibre.

## Data processing

If `O_2` refines `O_1`, so `O_1=f(O_2)`, then both hidden-access quantities can only decrease. An observer supplied with the full content history has zero hidden content.

## Exact one-bit witness

Under the uniform law on
\[
w_0=TTTT,\qquad w_1=TSTS,
\]
from the same state, both words have length four and the same projective endpoint, while their receipts are `0` and `e_3`. Hence an endpoint-length observer has
\[
\boxed{\mathsf H^{\rm path}=\mathsf H^{\rm term}=\log2}
\]
—one bit—whereas the full-word observer has zero.

## Superior RGΦ profile

The system-specific object is the triple
\[
\boxed{
\mathfrak H_{F,\mu,O}=
(\mathcal A_F,\mathsf H^{\rm path}_\mu(O),\mathsf H^{\rm term}_\mu(O)),
}
\]
where `A_F` is the access-rate polytope. This is a formal RGΦ-relative hyperaccess notion, not an identification with a general theory outside this system.
