module

import Mathlib

open Matrix

/-!
HDH-031 integrated machine-checked algebraic core.

* inverse differentiation in a noncommutative ring;
* Schur-memory differentiation;
* the hidden-union inverse on a 2 x 2 block ring;
* typed rectangular contraction connecting the inverse to the quotient formula.
-/

theorem inverse_derivative_generic
    {R : Type*} [Ring R]
    (a e da de : R)
    (hAE : a * e = 1)
    (hTangent : de * a + e * da = 0) :
    de = -(e * da * e) := by
  have hzero : de + e * da * e = 0 := by
    calc
      de + e * da * e = de * (a * e) + e * da * e := by rw [hAE, mul_one]
      _ = (de * a + e * da) * e := by noncomm_ring
      _ = 0 := by rw [hTangent, zero_mul]
  calc
    de = de + e * da * e - e * da * e := by noncomm_ring
    _ = -(e * da * e) := by rw [hzero]; noncomm_ring

theorem schur_memory_derivative_generic
    {R : Type*} [Ring R]
    (c e dc de da dm : R)
    (hCE : c * e = 1)
    (hInvTangent : de * c + e * dc = 0)
    (hMemoryTangent : dm = da - de) :
    dm = da + e * dc * e := by
  have hde : de = -(e * dc * e) :=
    inverse_derivative_generic c e dc de hCE hInvTangent
  rw [hMemoryTangent, hde]
  noncomm_ring

theorem finite_matrix_schur_memory_derivative
    {K : Type*} [Field K]
    {n : Type*} [Fintype n] [DecidableEq n]
    (C E dC dE dA dM : Matrix n n K)
    (hCE : C * E = 1)
    (hInvTangent : dE * C + E * dC = 0)
    (hMemoryTangent : dM = dA - dE) :
    dM = dA + E * dC * E :=
  schur_memory_derivative_generic C E dC dE dA dM
    hCE hInvTangent hMemoryTangent

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
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h00
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h01
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h10
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h11

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
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h00
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h01
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h10
  · simpa [hiddenUnionInverse2, Matrix.mul_apply, Fin.sum_univ_two,
      sub_eq_add_neg, mul_assoc] using h11

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
  have h1 : B * (-(L * F * Kinv)) * G = -(B * L * F * Kinv * G) := by
    simp [Matrix.mul_assoc]
  have h2 : C * (-(Kinv * H * L)) * D = -(C * Kinv * H * L * D) := by
    simp [Matrix.mul_assoc]
  have h3 : C * (Kinv + Kinv * H * L * F * Kinv) * G =
      C * Kinv * G + C * Kinv * H * L * F * Kinv * G := by
    simp [Matrix.mul_add, Matrix.add_mul, Matrix.mul_assoc]
  have h4 : (B - C * Kinv * H) * L * (D - F * Kinv * G) =
      B * L * D - B * L * F * Kinv * G - C * Kinv * H * L * D +
        C * Kinv * H * L * F * Kinv * G := by
    simp [Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_assoc]
    abel
  rw [h1, h2, h3, h4]
  abel
