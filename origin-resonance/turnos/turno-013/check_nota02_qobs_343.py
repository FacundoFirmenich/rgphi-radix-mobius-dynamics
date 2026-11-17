#!/usr/bin/env python3
import mpmath as mp

mp.mp.dps = 80

assert 18**2 + 18 + 1 == 343 == 7**3
assert (18**3 - 1) // (18 - 1) == 343
assert 343 == 9 * 36 + 19 == 10 * 36 - 17
assert 17 + 19 == 36
assert 343 % 36 == 19
assert pow(343, 2, 36) == 1

H = mp.nsum(
    lambda f: (342**2) * f * mp.log(f, 2) / (343 ** (f + 1)),
    [2, mp.inf],
)
expected = mp.mpf("0.005837332402614633262170598195")
assert abs(H - expected) < mp.mpf("1e-30")

print("PASS_NOTA02_QOBS_005837_343")
print("cyclotomic_ladder=Phi1(18)=17,Phi2(18)=19,Phi3(18)=343=7^3")
print("base18_repunit=111_18")
print("phase_involution=343^2 mod36 = 1")
print("entropy_identity=H_infinity=E(343)")
