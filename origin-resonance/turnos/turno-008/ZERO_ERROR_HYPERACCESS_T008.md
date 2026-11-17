# Zero-error hyperaccess and the completion-phase threshold

Let `O_N:X_N->Y_N` be an observation map and put `m_N=max_y |O_N^{-1}(y)|`. A fixed-length zero-error key makes `x -> (O_N(x),K_N(x))` injective.

## Exact key theorem

The minimum key alphabet size is exactly

\[
M_N^*=m_N,
\]

and the minimum binary length is

\[
c_N^*=\lceil\log_2m_N\rceil.
\]

Necessity follows because states in one observation fibre require distinct keys; sufficiency follows by independently indexing each fibre.

For internal span `L_N`, define `kappa_N=log_2(m_N)/L_N`. A hyperaccess family has

\[
\log m_N=o(L_N)
\]

and distinct completions in a fibre remain macroscopically separated, in the strong form by a gain `Gamma_N -> infinity`. The key changes the representation from noninjective to injective without reconstructing the hidden subsystem.

For the coherent RGΦ paths

\[
W_N^{(0)}=(TTTT)^N,\qquad W_N^{(1)}=(TSTS)^N,
\]

the observation fibre has size two, the optimal key is one bit, its normalized rate is `1/(4N)`, and the log-radial separation is `N log 3`.

Thus superaccess recovers hidden contents, whereas hyperaccess selects the completion phase.

Status: `CLOSED_SYMBOLIC_T008`.
