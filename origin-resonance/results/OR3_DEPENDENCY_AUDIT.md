# OR-3 dependency audit — `17/19` versus nineteen curves

## Formal chain currently inspected

The current Paper III derivation of the nineteen curves is:

1. form `DF015-0015`;
2. variables `A,z,w,C,D` with `A>5z>w>0`;
3. quotients `h=f/D`, `j=g/C`;
4. linear quantity `L=j-h+5w+85z`;
5. divisibility `A|L`;
6. sharpened bound `0<L/A<20`;
7. integer index `n=L/A in {1,...,19}`;
8. cubic family `F_n=0`.

The benchmark `17/19` does not occur as a variable, coefficient, modulus, initial condition or lemma in this formal chain.

## Adjudication

\[
\boxed{\text{No direct formal dependency is present in the current theorem DAG.}}
\]

This supports the label `CURRENT_FORMAL_INDEPENDENCE`.

It does **not** prove complete historical independence, because the full archive of informal discovery choices has not been reconstructed in this branch. The datum `17/19` is user-declared historical provenance.

The recurrence is scientifically eligible for prospective study, but it is not evidence of causation or of an ontological identification.
