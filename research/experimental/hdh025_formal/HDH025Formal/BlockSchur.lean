import Mathlib.Data.Matrix.Notation
import Mathlib.Tactic

open Matrix

/-!
Machine-checked finite block-Schur factorization used by HDH-025.
The generic theorem is noncommutative.  Instantiating the coefficient ring
with a finite square matrix ring yields the finite block identity.
-/

theorem schur_factorization_generic
    {R : Type*} [Ring R]
    (a b c d e : R) (hed : e * d = 1) :
    !![1, b * e; 0, 1] *
        !![a - b * e * c, 0; c, d] =
      !![a, b; c, d] := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [Matrix.mul_apply, Fin.sum_univ_two, hed, mul_assoc] <;>
    noncomm_ring

theorem finite_block_schur_factorization
    {K : Type*} [Field K]
    {n : Type*} [Fintype n] [DecidableEq n]
    (A B C D E : Matrix n n K) (hED : E * D = 1) :
    !![1, B * E; 0, 1] *
        !![A - B * E * C, 0; C, D] =
      !![A, B; C, D] :=
  schur_factorization_generic A B C D E hED
