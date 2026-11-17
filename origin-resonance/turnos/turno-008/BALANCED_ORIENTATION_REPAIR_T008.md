# Repair of the six-state balanced orientation jurisdiction

There are four cyclic rotation classes of six-letter words with three `T` and three `S` symbols:

\[
TTTSSS,\quad TTSTSS,\quad TTSSTS,\quad TSTSTS.
\]

The middle pair are reflections, not rotations. Under the marked strict-source, back-edge and lollipop conditions, exact enumeration leaves one functional map per oriented word.

The previously omitted `TTSSTS` class has fibre form

\[
P/(dQ),\ C/Q,\ A/Q,\ A/D,\ A/E,\ P/E.
\]

For `d>=4`, highness of the strict source gives `P>dQ/2>=2Q`. The state `A/Q<1` gives `A<Q`, while highness of `A/E` gives `E<2A<2Q`. But `P/E<1` requires `P<E`, contradiction.

Thus, after the earlier exclusions of `TTTSSS` and `TTSTSS`,

\[
\boxed{TSTSTS\text{ is the unique surviving oriented word}}
\]

within the declared high-defect lollipop jurisdiction.

With a marked source and tagged witness word there are `4*720=2880` formal completions and `11520` after decoration by `d=4,5,6,7`. These are tagged profile counts, not a claim that different witness tags always give distinct untagged maps.

Status: `CLOSED_SYMBOLIC_ORIENTATION_REPAIR_T008`.
