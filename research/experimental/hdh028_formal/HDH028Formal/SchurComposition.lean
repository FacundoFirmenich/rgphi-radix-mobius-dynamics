module

import Mathlib

open Matrix

/-!
HDH-028: sequential Schur elimination equals direct elimination of the
union hidden block.  The first theorem is the noncommutative algebraic core;
the second enforces rectangular block types explicitly.
-/

theorem schur_sequential_direct_generic
    {R : Type*} [Ring R]
    (a b c d f g h k l : R) :
    a - c * k * g - (b - c * k * h) * l * (d - f * k * g) =
      a - b * l * d + b * l * f * k * g + c * k * h * l * d -
        c * k * h * l * f * k * g - c * k * g := by
  noncomm_ring

theorem schur_sequential_direct_rectangular
    {K : Type*} [Field K]
    {m n p : Type*}
    [Fintype m] [DecidableEq m]
    [Fintype n] [DecidableEq n]
    [Fintype p] [DecidableEq p]
    (A : Matrix m m K)
    (B : Matrix m n K)
    (C : Matrix m p K)
    (D : Matrix n m K)
    (E : Matrix n n K)
    (F : Matrix n p K)
    (G : Matrix p m K)
    (H : Matrix p n K)
    (J Kinv : Matrix p p K)
    (Sinv : Matrix n n K)
    (_hKJ : Kinv * J = 1)
    (_hJK : J * Kinv = 1)
    (_hLS : Sinv * (E - F * Kinv * H) = 1)
    (_hSL : (E - F * Kinv * H) * Sinv = 1) :
    A - C * Kinv * G - (B - C * Kinv * H) * Sinv * (D - F * Kinv * G) =
      A - B * Sinv * D + B * Sinv * F * Kinv * G +
        C * Kinv * H * Sinv * D - C * Kinv * H * Sinv * F * Kinv * G -
        C * Kinv * G := by
  ext i j
  simp [Matrix.mul_apply, Finset.mul_sum, Finset.sum_mul]
  ring
