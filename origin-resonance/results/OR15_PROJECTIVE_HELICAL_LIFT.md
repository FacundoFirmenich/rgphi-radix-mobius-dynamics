# OR-15 — exact projective helical lift from the content cocycle

Round 022 defines the primitive projective lift

\[
\widehat g(v)=\operatorname{prim}(M_gv),
\qquad
\delta_g(v)=\operatorname{cont}(M_gv),
\]

and proves for every admissible word

\[
w=g_m\cdots g_1
\]

that

\[
M_wv_0=\Delta_wv_m,
\qquad
\Delta_w=\prod_{i=1}^m\delta_{g_i}(v_{i-1}).
\]

## Log-radial lift

Define

\[
\widetilde\Lambda^+=\Lambda^+\times\mathbb R
\]

and

\[
\widetilde g(v,\rho)
=
\bigl(\widehat g(v),\rho+\log\delta_g(v)\bigr).
\]

Then

\[
\widetilde w(v_0,\rho)
=
\bigl(v_m,\rho+\log\Delta_w\bigr).
\]

If the projective word is periodic,

\[
v_m=v_0,
\]

then

\[
\widetilde w^k(v_0,\rho)
=
\bigl(v_0,\rho+k\log\Delta_w\bigr).
\]

Thus:

- `Delta_w=1`: the lift closes;
- `Delta_w>1`: the projective phase closes while the log-radial coordinate advances by a fixed amount.

This is an exact discrete screw / helical lift: periodicity in the base coordinate plus translation in the fibre.

## Content-access receipt

Define

\[
\mathcal I(w)=\log\Delta_w.
\]

Then

\[
\mathcal I(uv)=\mathcal I(u)+\mathcal I(v)
\]

for concatenable admissible words. It is zero exactly when all branch reductions are unreduced.

For a word of length `m`, define the normalized content share

\[
\alpha(w)=\frac{\log\Delta_w}{m\log B}\in[0,1].
\]

On a cycle, the spectral theorem gives eigenvalues

\[
\lambda_1=B^{m\alpha},
\qquad
\lambda_2=B^{m(1-\alpha)}.
\]

Hence the two normalized log-spectral shares are exactly

\[
\boxed{\alpha,\ 1-\alpha}.
\]

## Authority boundary

The helical lift is a theorem about the augmented projective-content system.

The identification of `I` or `alpha` with the user's broader hyperaccess programme is **not** proved. They are, however, the first exact operational candidates because they are:

- representation-aware;
- additive or normalized-additive;
- zero exactly in the absence of content reduction;
- measurable from the lifted dynamics;
- invisible in the closed projective endpoint alone.

Status: `CLOSED_SYMBOLIC_HELICAL_LIFT / FORMAL_HYPERACCESS_CANDIDATE`.
