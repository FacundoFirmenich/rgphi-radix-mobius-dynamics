# OR-9 — 44P as a half-scale echo of the 88→96 differential

## Historical framing

The historical construction used

\[
q_O=\pi/18,
\qquad q_R=8q_O=4\pi/9,
\]

so that

\[
88q_O=11q_R,
\qquad
96q_O=12q_R.
\]

Hence `88 -> 96` is an `11 -> 12` completion with differential 8.

## Exact integer homothety

Round 021 certifies that the elliptic multiple `44P` is in the strict chamber and its cubic divisibility defect is exactly 4. Therefore

\[
44+4=48,
\]

and

\[
(44,4,48)\times2=(88,8,96).
\]

Equivalently,

\[
44=11\cdot4,
\qquad 48=12\cdot4,
\]

while

\[
88=11\cdot8,
\qquad96=12\cdot8.
\]

## Stronger selection of 44 and 88

Among multiples `1P,...,50P`, only `P` and `44P` lie in the strict chamber.

Moreover, modulo the boundary-collision prime 83,

\[
[44]P=R=[1:2:2].
\]

The smooth reduction has

\[
\#F_{17}(\mathbb F_{83})=89,
\]

so

\[
44=(89-1)/2,
\qquad88=89-1.
\]

Thus 44 and 88 are selected by an exact finite-field group relation rather than only by scaling the historical motif.

## Dynamic falsification

The defect 4 is not unique to 44: on every odd-index cubic it is forced whenever the primitive coordinate `A` is even.

Direct exact computation gives:

| multiple | strict chamber | cubic defect |
|---:|:---:|---:|
| `44P` | yes | 4 |
| `48P` | no | 4 |
| `88P` | no | 4 |
| `96P` | no | 4 |

Therefore neither

\[
44P\to48P
\]

nor

\[
88P\to96P
\]

is a chamber-completion law.

## Adjudication

- integer homothety: `POSTHOC_EXACT`;
- finite-field selection of 44 and 88: `CLOSED_EXACT`;
- orbital completion interpretation: `REFUTED`.

No identification of the elliptic point `P` with the historical quanta is claimed.
