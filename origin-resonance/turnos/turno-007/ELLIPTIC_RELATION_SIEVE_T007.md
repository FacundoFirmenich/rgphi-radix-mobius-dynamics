# Local relation sieve for the Mordell–Weil pair P,R

Any global relation

\[
aP+bR=O
\]

reduces to a relation at every good prime. At a prime with `Rbar=k_p Pbar` and `ord(Pbar)=n_p`, it must satisfy

\[
a+k_pb\equiv0\pmod{n_p}.
\]

Using all 29 certified primes `p<=199` for which the discrete logarithm exists, the simultaneous congruence lattice has basis

\[
(N,0),\qquad(a_0,L),
\]

where

\[
N=486350841114209042571600,
\]

\[
L=581981400,
\]

\[
a_0=397929094518522627660600.
\]

Exact Gauss reduction gives

\[
(-6721598835151200,-8984879105202000),
\]

\[
(21459192394840200,-13425212699098200).
\]

Therefore every nonzero global relation must satisfy

\[
a^2+b^2\ge125907943435801460896187665440000,
\]

so its Euclidean coefficient norm is at least

\[
11220870885800329.
\]

This is a rigorous local sieve, not a proof that `P,R` are Mordell–Weil independent.
