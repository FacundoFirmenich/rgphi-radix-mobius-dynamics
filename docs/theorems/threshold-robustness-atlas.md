# RGΦ Threshold Robustness Atlas v1.0

## Exact result

For

\[
P_m(10,\kappa)=\{x:q(x)>\kappa 10^m\},
\]

the benchmark first-hit vector

\[
(\tau_1,\tau_2,\tau_3,\tau_4)=(45,85,120,162)
\]

is simultaneously unchanged for

\[
\boxed{\kappa\in[106197/10000,11643/1000)}
=
\boxed{\kappa\in[10.6197,11.643)}.
\]

The lower endpoint is included and the upper endpoint excluded because portal
membership is strict.

## Robustness of nonnesting

The three exact continuation failures persist simultaneously for

\[
\boxed{\kappa\in[106197/10000,1101/100)}
=
\boxed{\kappa\in[10.6197,11.01)}.
\]

Throughout this interval:

1. the first m1 portal at time 45 reaches m2 only at time 87, whereas the global m2 time is 85;
2. the first m2 portal at time 85 reaches m3 only at time 139, whereas the global m3 time is 120;
3. the m3 optimum 11156/11157 reaches m4 only at 168, whereas the global m4 time is 162;
4. the other two m3-optimal states have no m4 hit by 162 throughout this same interval.

Hence the nonnested-portal phenomenon is not a single-threshold accident at
\(\kappa=11\). It occupies an exact interval of positive width.

## Benchmark intervals

| m | tau | exact kappa interval |
|---:|---:|---|
| 1 | 45 | [93/10, 129/10) |
| 2 | 85 | [903/100, 1203/100) |
| 3 | 120 | [10019/1000, 11643/1000) |
| 4 | 162 | [106197/10000, 124853/10000) |


## Evidence boundary

The full piecewise atlas is exact through global depth 162. Statements beyond
that horizon require additional layer maxima. The nonnesting intervals use
independent exact continuation searches from the relevant optimal portal
states.
