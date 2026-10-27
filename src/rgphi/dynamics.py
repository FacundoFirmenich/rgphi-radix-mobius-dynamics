"""Exact rational dynamics for the RGΦ radix--Möbius semigroup.

All state transitions use :class:`fractions.Fraction`; no floating-point value
participates in reachability or target-membership decisions.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterator, Literal

Action = Literal["T", "S"]


DEFAULT_TERMINAL: frozenset[Fraction] = frozenset(
    {
        Fraction(2, 11), Fraction(9, 11), Fraction(0, 1), Fraction(1, 1),
        Fraction(1, 2), Fraction(1, 3), Fraction(2, 3), Fraction(3, 4),
        Fraction(4, 5), Fraction(5, 6), Fraction(7, 8), Fraction(7, 9),
        Fraction(7, 10), Fraction(4, 11), Fraction(7, 11), Fraction(7, 12),
        Fraction(2, 13), Fraction(5, 13), Fraction(6, 13), Fraction(7, 13),
        Fraction(8, 13), Fraction(11, 13), Fraction(11, 20),
    }
)


@dataclass(frozen=True, slots=True)
class BranchResult:
    action: Action
    digit: int
    state: Fraction
    raw_numerator: int
    raw_denominator: int
    reduction: int


@dataclass(frozen=True, slots=True)
class BranchMatrix:
    action: Action
    digit: int
    base: int
    entries: tuple[tuple[int, int], tuple[int, int]]

    @property
    def determinant(self) -> int:
        (a, b), (c, d) = self.entries
        return a * d - b * c


def complement(x: Fraction) -> Fraction:
    """Return C(x)=1/x-1 on positive rational states."""
    if x <= 0:
        raise ValueError("complement requires x>0")
    return Fraction(1, 1) / x - 1


def chart(x: Fraction) -> Fraction:
    """Return H(x)=1/(1+x)."""
    if x == -1:
        raise ZeroDivisionError("H is undefined at -1")
    return Fraction(1, 1) / (1 + x)


def T(x: Fraction, *, base: int = 10) -> Fraction:
    """Integer-radix transformation T_B(x)={B x}."""
    if base < 2:
        raise ValueError("base must be at least 2")
    y = base * x
    return y - (y.numerator // y.denominator)


def S(x: Fraction, *, base: int = 10) -> Fraction | None:
    """Möbius-conjugate branch S_B=H∘T_B∘H^{-1}.

    The branch is admissible only for x>=1/2 in the benchmark interval.
    """
    if base < 2:
        raise ValueError("base must be at least 2")
    if x == 0 or 2 * x < 1:
        return None
    u = Fraction(1, 1) / x - 1
    y = base * u
    return Fraction(1, 1) / (1 + y - (y.numerator // y.denominator))


def branch_matrix(action: Action, digit: int, *, base: int = 10) -> BranchMatrix:
    if base < 2:
        raise ValueError("base must be at least 2")
    if action == "T":
        entries = ((base, -digit), (0, 1))
    elif action == "S":
        entries = ((1, 0), (-(base - 1 + digit), base))
    else:  # pragma: no cover - protected by typing, kept for runtime users
        raise ValueError(f"unknown action {action!r}")
    result = BranchMatrix(action=action, digit=digit, base=base, entries=entries)
    if result.determinant != base:
        raise ArithmeticError("branch determinant invariant failed")
    return result


def apply_branch(x: Fraction, action: Action, *, base: int = 10) -> BranchResult | None:
    """Apply one exact branch and expose the primitive-reduction factor."""
    if base < 2:
        raise ValueError("base must be at least 2")
    a, b = x.numerator, x.denominator
    if action == "T":
        digit = (base * a) // b
        raw_a = base * a - digit * b
        raw_b = b
    elif action == "S":
        if a == 0 or 2 * a < b:
            return None
        digit = (base * (b - a)) // a
        raw_a = a
        raw_b = base * b - (base - 1 + digit) * a
    else:
        raise ValueError(f"unknown action {action!r}")
    reduction = gcd(abs(raw_a), abs(raw_b))
    if reduction <= 0:
        raise ArithmeticError("invalid primitive reduction")
    state = Fraction(raw_a // reduction, raw_b // reduction)
    return BranchResult(
        action=action,
        digit=digit,
        state=state,
        raw_numerator=raw_a,
        raw_denominator=raw_b,
        reduction=reduction,
    )


def children(
    x: Fraction,
    *,
    base: int = 10,
    terminal: frozenset[Fraction] | set[Fraction] | None = DEFAULT_TERMINAL,
) -> Iterator[BranchResult]:
    """Yield every admissible nonterminal child."""
    for action in ("T", "S"):
        result = apply_branch(x, action, base=base)
        if result is None:
            continue
        if terminal is not None and result.state in terminal:
            continue
        yield result


def portal_height(x: Fraction) -> Fraction:
    """Return q(x)=1/(1-x)=b/(b-a) for x<1."""
    if x >= 1:
        raise ValueError("portal height is defined here only for x<1")
    return Fraction(x.denominator, x.denominator - x.numerator)


def in_portal(x: Fraction, *, depth: int, kappa: Fraction, base: int = 10) -> bool:
    if depth < 1:
        raise ValueError("depth must be positive")
    if kappa <= 0:
        raise ValueError("kappa must be positive")
    return portal_height(x) > kappa * (base**depth)


def iterate_word(seed: Fraction, word: str, *, base: int = 10) -> list[Fraction]:
    """Return the complete exact state trace, including the seed."""
    states = [seed]
    x = seed
    for index, action in enumerate(word, 1):
        result = apply_branch(x, action, base=base)  # type: ignore[arg-type]
        if result is None:
            raise ValueError(f"inadmissible action {action!r} at step {index}, state={x}")
        x = result.state
        states.append(x)
    return states


def seed_family_state(N: int, r: int) -> Fraction:
    if N <= 1 or not (1 <= r < N):
        raise ValueError("require N>1 and 1<=r<N")
    return Fraction(N, N + r)


def seed_family_successor(N: int, r: int, *, base: int = 10) -> Fraction:
    """Closed form S_B(N/(N+r))=N/(N+(Br mod N))."""
    x = seed_family_state(N, r)
    expected = Fraction(N, N + ((base * r) % N))
    actual = S(x, base=base)
    if actual != expected:
        raise ArithmeticError("seed-family conjugacy invariant failed")
    return expected
