module

import Mathlib

open Matrix

/-!
HDH-030 machine-checked hidden-union block inverse and its connection to the
Schur quotient formula.  The inverse theorem is first proved over an arbitrary
noncommutative ring.  A typed rectangular contraction theorem then permits
different retained and hidden index types.
-/

def hiddenUnionInverse2 {R : Type*} [Ring R]
    (f h k l : R) : Matrix (Fin 2) (Fin 2) R :=
  !![l, -(l * f * k); -(k * h * l), k + k * h * l * f * k]

theorem hidden_union_inverse_left_generic
    {R : Type*} [Ring R]
    (e f h j k l : R)
    (hKJ : k * j = 1)
    (_hJK : j * k = 1)
    (hLS : l * (e - f * k * h) = 1)
    (_hSL : (e - f * k * h) * l = 1) :
    hiddenUnionInverse2 f h k l * !![e, f; h, j] = 1 := by
  have h00 : l * e - l * f * k * h = 1 := by
    calc
      l * e - l * f * k * h = l * (e - f * k * h) := by noncomm_ring
      _ = 1 := hLS
  have h01 : l * f - l * f * k * j = 0 := by
    calc
      l * f - l * f * k * j = l * f - l * f * (k * j) := by noncomm_ring
      _ = 0 := by rw [hKJ]; noncomm_ring
  have h10 : -(k * h * l) * e + (k + k * h * l * f * k) * h = 0 := by
    calc
      -(k * h * l) * e + (k + k * h * l * f * k) * h =
          -(k * h) * (l * (e - f * k * h)) + k * h := by noncomm_ring
      _ = 0 := by rw [hLS]; noncomm_ring
  have h11 : -(k * h * l) * f + (k + k * h * l * f * k) * j = 1 := by
    calc
      -(k * h * l) * f + (k + k * h * l * f * k) * j =
          -(k * h * l * f) + k * j + k * h * l * f * (k * j) := by noncomm_ring
      _ = 1 := by rw [hKJ]; noncomm_ring
  ext i q
  fin_cases i <;> fin_cases q
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h00
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h01
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h10
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h11

theorem hidden_union_inverse_right_generic
    {R : Type*} [Ring R]
    (e f h j k l : R)
    (_hKJ : k * j = 1)
    (hJK : j * k = 1)
    (_hLS : l * (e - f * k * h) = 1)
    (hSL : (e - f * k * h) * l = 1) :
    !![e, f; h, j] * hiddenUnionInverse2 f h k l = 1 := by
  have h00 : e * l - f * k * h * l = 1 := by
    calc
      e * l - f * k * h * l = (e - f * k * h) * l := by noncomm_ring
      _ = 1 := hSL
  have h01 : e * (-(l * f * k)) + f * (k + k * h * l * f * k) = 0 := by
    calc
      e * (-(l * f * k)) + f * (k + k * h * l * f * k) =
          -((e - f * k * h) * l) * f * k + f * k := by noncomm_ring
      _ = 0 := by rw [hSL]; noncomm_ring
  have h10 : h * l + j * (-(k * h * l)) = 0 := by
    calc
      h * l + j * (-(k * h * l)) = h * l - (j * k) * h * l := by noncomm_ring
      _ = 0 := by rw [hJK]; noncomm_ring
  have h11 : h * (-(l * f * k)) + j * (k + k * h * l * f * k) = 1 := by
    calc
      h * (-(l * f * k)) + j * (k + k * h * l * f * k) =
          -(h * l * f * k) + j * k + (j * k) * h * l * f * k := by noncomm_ring
      _ = 1 := by rw [hJK]; noncomm_ring
  ext i q
  fin_cases i <;> fin_cases q
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h00
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h01
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h10
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h11

theorem hidden_union_inverse_two_sided_generic
    {R : Type*} [Ring R]
    (e f h j k l : R)
    (hKJ : k * j = 1) (hJK : j * k = 1)
    (hLS : l * (e - f * k * h) = 1)
    (hSL : (e - f * k * h) * l = 1) :
    hiddenUnionInverse2 f h k l * !![e, f; h, j] = 1 ∧
      !![e, f; h, j] * hiddenUnionInverse2 f h k l = 1 := by
  exact ⟨hidden_union_inverse_left_generic e f h j k l hKJ hJK hLS hSL,
    hidden_union_inverse_right_generic e f h j k l hKJ hJK hLS hSL⟩

theorem hidden_union_contraction_rectangular
    {K : Type*} [Field K]
    {m n p : Type*}
    [Fintype m] [DecidableEq m]
    [Fintype n] [DecidableEq n]
    [Fintype p] [DecidableEq p]
    (A : Matrix m m K)
    (B : Matrix m n K) (C : Matrix m p K)
    (D : Matrix n m K) (G : Matrix p m K)
    (F : Matrix n p K) (H : Matrix p n K)
    (Kinv : Matrix p p K) (L : Matrix n n K) :
    A - (B * L * D + B * (-(L * F * Kinv)) * G +
      C * (-(Kinv * H * L)) * D +
      C * (Kinv + Kinv * H * L * F * Kinv) * G) =
    A - C * Kinv * G -
      (B - C * Kinv * H) * L * (D - F * Kinv * G) := by
  simp only [Matrix.mul_assoc, Matrix.mul_add, Matrix.add_mul,
    Matrix.mul_sub, Matrix.sub_mul]
  abel
