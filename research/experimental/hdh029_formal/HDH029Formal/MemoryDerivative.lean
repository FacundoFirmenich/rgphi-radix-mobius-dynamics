module

import Mathlib

open Matrix

/-!
HDH-029 machine-checked algebraic core:
* derivative of an inverse in a noncommutative ring;
* derivative of the Schur-memory response;
* quotient formula both as a nested Schur expression and as an explicit
  contraction with a 2 x 2 hidden-block inverse candidate.
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

def schur2 {R : Type*} [Ring R] (a b c e : R) : R :=
  a - b * e * c

def directUnionSchur {R : Type*} [Ring R]
    (a b c d f g h k l : R) : R :=
  a - (b * l * d - b * l * f * k * g - c * k * h * l * d +
    c * k * g + c * k * h * l * f * k * g)

def sequentialSchur {R : Type*} [Ring R]
    (a b c d _e f g h k l : R) : R :=
  schur2 (schur2 a c g k) (b - c * k * h) (d - f * k * g) l

def hiddenInverse2 {R : Type*} [Ring R]
    (f h k l : R) : Matrix (Fin 2) (Fin 2) R :=
  !![l, -(l * f * k); -(k * h * l), k + k * h * l * f * k]

def retainedRow2 {R : Type*} [Ring R]
    (b c : R) : Matrix (Fin 1) (Fin 2) R :=
  !![b, c]

def retainedCol2 {R : Type*} [Ring R]
    (d g : R) : Matrix (Fin 2) (Fin 1) R :=
  !![d; g]

theorem explicit_quotient_formula_generic
    {R : Type*} [Ring R]
    (a b c d e f g h k l : R) :
    sequentialSchur a b c d e f g h k l =
      directUnionSchur a b c d f g h k l := by
  simp [sequentialSchur, schur2, directUnionSchur]
  noncomm_ring

theorem quotient_formula_block_contraction_generic
    {R : Type*} [Ring R]
    (a b c d e f g h k l : R) :
    (!![a] : Matrix (Fin 1) (Fin 1) R) -
        retainedRow2 b c * hiddenInverse2 f h k l * retainedCol2 d g =
      !![sequentialSchur a b c d e f g h k l] := by
  ext i j
  fin_cases i <;> fin_cases j
  simp [retainedRow2, hiddenInverse2, retainedCol2,
    sequentialSchur, schur2, Matrix.mul_apply, Fin.sum_univ_two]
  noncomm_ring
