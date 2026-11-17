# F17 local Mordell–Weil relation sieve through prime 1000

For every certified good prime with `Rbar=k_p Pbar` and `ord(Pbar)=n_p`, a global relation `aP+bR=O` must satisfy

\[
a+k_pb=0\pmod{n_p}.
\]

The exact checker retains 102 such primes at most 1000. Small characteristics `2,3,5` are excluded from this implementation and `619` is singular.

The simultaneous relation lattice has basis `(N,0),(a_0,L)` with

```text
N = 2351192158242633981543137402715976069817988808139961087355956724773220529926849717801730605200925470000
L = 121150487714207359895410823499600
a0= 2068621604368448552570469715883845443941485480438749617860584075153721313479230272742636022519452794400
```

Exact two-dimensional Gauss reduction proves that every nonzero global relation satisfies

\[
a^2+b^2\ge
73022226486547047350820807270502256563763194012005877593402140974959341002513077272519694176522565820967864659518028034447565672000000.
\]

Hence no nonzero relation has Euclidean coefficient norm at most

```text
8545304353067071849899288697544026718324675836661131573707357233455
```

This raises the certified exclusion from 17 to 67 decimal digits. It remains a local sieve, not an independence proof.

Status: `CLOSED_EXACT_LOCAL_SIEVE_P_LE_1000 / INDEPENDENCE_OPEN`.
