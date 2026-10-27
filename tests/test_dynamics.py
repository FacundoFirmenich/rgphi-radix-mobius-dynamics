from fractions import Fraction

from rgphi import S, T, apply_branch, branch_matrix, complement, portal_height, seed_family_successor


def test_foundational_bridge() -> None:
    assert complement(Fraction(17, 20)) == T(complement(Fraction(17, 19)))
    assert S(Fraction(17, 19)) == Fraction(17, 20)


def test_noncommutativity() -> None:
    x = Fraction(17, 19)
    assert T(S(x)) == Fraction(1, 2)
    assert S(T(x)) == Fraction(9, 14)
    assert T(S(x)) != S(T(x))


def test_branch_determinants_base_family() -> None:
    for base in range(2, 31):
        for digit in range(base):
            assert branch_matrix("T", digit, base=base).determinant == base
            assert branch_matrix("S", digit, base=base).determinant == base


def test_seed_family_identity() -> None:
    for base in range(2, 16):
        for N in range(2, 35):
            for r in range(1, N):
                assert seed_family_successor(N, r, base=base) == Fraction(N, N + ((base * r) % N))


def test_portal_height() -> None:
    assert portal_height(Fraction(128, 129)) == 129
    assert portal_height(Fraction(1202, 1203)) == 1203


def test_exact_reduction_factors() -> None:
    result = apply_branch(Fraction(17, 19), "T")
    assert result is not None
    assert result.digit == 8
    assert result.state == Fraction(18, 19)
    assert result.reduction == 1
