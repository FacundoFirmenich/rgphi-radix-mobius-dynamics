# OR-13 — direct orbital adjudication of `44 -> 48` and `88 -> 96`

The integer triples satisfy

\[
(44,4,48)\times2=(88,8,96).
\]

Round 021 makes 44 non-arbitrary within the inspected orbit:

- among `P,2P,...,50P`, only `P` and `44P` lie in the strict chamber;
- `44P` reaches the universal boundary point modulo 83;
- `44=(89-1)/2` in the prime-order reduction group.

However, the defect four is not specific to 44: it follows from the odd-index parity theorem whenever `A` is even.

Exact group-law computation gives:

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

What survives is an exact post-hoc integer homothety and an independently exact finite-field selection of 44 and 88. The proposed orbital completion is refuted.
