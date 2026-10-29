module

import Mathlib

open Matrix

/-!
HDH-027 typed rectangular Schur factorization.
The retained and eliminated index types may differ.
-/

theorem rectangular_schur_factorization
    {K : Type*} [Field K]
    {m n : Type*}
    [Fintype m] [DecidableEq m]
    [Fintype n] [DecidableEq n]
    (A : Matrix m m K)
    (B : Matrix m n K)
    (C : Matrix n m K)
    (D E : Matrix n n K)
    (hED : E * D = 1) :
    Matrix.fromBlocks (1 : Matrix m m K) (B * E) 0 1 *
        Matrix.fromBlocks (A - B * E * C) 0 C D =
      Matrix.fromBlocks A B C D := by
  have hBED : B * E * D = B := by
    calc
      B * E * D = B * (E * D) := by rw [mul_assoc]
      _ = B := by rw [hED, mul_one]
  rw [Matrix.fromBlocks_multiply]
  simp [hBED, mul_assoc]
