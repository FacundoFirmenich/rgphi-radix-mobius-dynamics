module

import Mathlib

open Matrix

/-!
HDH-026 machine-checked finite block-Schur identities.
The statements are proved first in an arbitrary noncommutative ring.
Finite square matrix rings are then immediate instances.
-/

theorem schur_factorization_generic
    {R : Type*} [Ring R]
    (a b c d e : R) (hed : e * d = 1) :
    !![1, b * e; 0, 1] *
        !![a - b * e * c, 0; c, d] =
      !![a, b; c, d] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, hed, mul_assoc]

theorem block_inverse_left_generic
    {R : Type*} [Ring R]
    (a b c d e f : R)
    (hed : e * d = 1)
    (hde : d * e = 1)
    (hfs : f * (a - b * e * c) = 1)
    (hsf : (a - b * e * c) * f = 1) :
    !![f, -(f * b * e); -(e * c * f), e + e * c * f * b * e] *
        !![a, b; c, d] =
      !![1, 0; 0, 1] := by
  have h00 : f * a - f * b * e * c = 1 := by
    calc
      f * a - f * b * e * c = f * (a - b * e * c) := by noncomm_ring
      _ = 1 := hfs
  have h01 : f * b - f * b * e * d = 0 := by
    calc
      f * b - f * b * e * d = f * b - f * b * (e * d) := by noncomm_ring
      _ = 0 := by rw [hed]; noncomm_ring
  have h10 : -(e * c * f) * a + (e + e * c * f * b * e) * c = 0 := by
    calc
      -(e * c * f) * a + (e + e * c * f * b * e) * c =
          -(e * c) * (f * (a - b * e * c)) + e * c := by noncomm_ring
      _ = 0 := by rw [hfs]; noncomm_ring
  have h11 : -(e * c * f) * b + (e + e * c * f * b * e) * d = 1 := by
    calc
      -(e * c * f) * b + (e + e * c * f * b * e) * d =
          -(e * c * f * b) + e * d + e * c * f * b * (e * d) := by noncomm_ring
      _ = 1 := by rw [hed]; noncomm_ring
  ext i j
  fin_cases i <;> fin_cases j
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h00
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h01
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h10
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h11

theorem block_inverse_right_generic
    {R : Type*} [Ring R]
    (a b c d e f : R)
    (hed : e * d = 1)
    (hde : d * e = 1)
    (hfs : f * (a - b * e * c) = 1)
    (hsf : (a - b * e * c) * f = 1) :
    !![a, b; c, d] *
        !![f, -(f * b * e); -(e * c * f), e + e * c * f * b * e] =
      !![1, 0; 0, 1] := by
  have h00 : a * f - b * e * c * f = 1 := by
    calc
      a * f - b * e * c * f = (a - b * e * c) * f := by noncomm_ring
      _ = 1 := hsf
  have h01 : a * (-(f * b * e)) + b * (e + e * c * f * b * e) = 0 := by
    calc
      a * (-(f * b * e)) + b * (e + e * c * f * b * e) =
          -((a - b * e * c) * f) * b * e + b * e := by noncomm_ring
      _ = 0 := by rw [hsf]; noncomm_ring
  have h10 : c * f + d * (-(e * c * f)) = 0 := by
    calc
      c * f + d * (-(e * c * f)) = c * f - (d * e) * c * f := by noncomm_ring
      _ = 0 := by rw [hde]; noncomm_ring
  have h11 : c * (-(f * b * e)) + d * (e + e * c * f * b * e) = 1 := by
    calc
      c * (-(f * b * e)) + d * (e + e * c * f * b * e) =
          -(c * f * b * e) + d * e + (d * e) * c * f * b * e := by noncomm_ring
      _ = 1 := by rw [hde]; noncomm_ring
  ext i j
  fin_cases i <;> fin_cases j
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h00
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h01
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h10
  · simpa [Matrix.mul_apply, Fin.sum_univ_two, sub_eq_add_neg, mul_assoc] using h11

theorem finite_block_inverse_left
    {K : Type*} [Field K]
    {n : Type*} [Fintype n] [DecidableEq n]
    (A B C D E F : Matrix n n K)
    (hED : E * D = 1)
    (hDE : D * E = 1)
    (hFS : F * (A - B * E * C) = 1)
    (hSF : (A - B * E * C) * F = 1) :
    !![F, -(F * B * E); -(E * C * F), E + E * C * F * B * E] *
        !![A, B; C, D] =
      !![1, 0; 0, 1] :=
  block_inverse_left_generic A B C D E F hED hDE hFS hSF

theorem finite_block_inverse_right
    {K : Type*} [Field K]
    {n : Type*} [Fintype n] [DecidableEq n]
    (A B C D E F : Matrix n n K)
    (hED : E * D = 1)
    (hDE : D * E = 1)
    (hFS : F * (A - B * E * C) = 1)
    (hSF : (A - B * E * C) * F = 1) :
    !![A, B; C, D] *
        !![F, -(F * B * E); -(E * C * F), E + E * C * F * B * E] =
      !![1, 0; 0, 1] :=
  block_inverse_right_generic A B C D E F hED hDE hFS hSF
