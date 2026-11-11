# OR-16 — latent golden/Fibonacci conjugacy

Round 022 makes the conjugating matrix explicit:

\[
H=
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix},
\qquad
C_k=HA_kH^{-1}.
\]

This matrix satisfies the exact polynomial identity

\[
\boxed{H^2=H+I}.
\]

Therefore its characteristic polynomial is

\[
\lambda^2-\lambda-1,
\]

with eigenvalues

\[
\boxed{\varphi,\ -\varphi^{-1}},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

Moreover, for `n>=1`,

\[
\boxed{
H^n=
\begin{pmatrix}
F_{n-1}&F_n\\
F_n&F_{n+1}
\end{pmatrix}
}
\]

where `F_n` are the Fibonacci numbers.

## Interpretation

The radix/Mobius duality is mediated by an exact Fibonacci matrix with:

- determinant `-1`;
- one positive and one negative eigenvalue;
- golden-ratio spectral scale;
- Fibonacci iterates.

This is structurally exact but not an independent late-stage recurrence: the map

\[
\Phi(x)=\frac1{1+x}
\]

already contains this golden fixed-point structure. Round 022 exposes it at the integral-matrix level.

Status: `CLOSED_SYMBOLIC / LATENT_BUILT_IN_STRUCTURE`, not independent evidence for a new origin hypothesis.
