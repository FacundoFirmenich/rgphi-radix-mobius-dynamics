module

import Mathlib

open Matrix

/-!
HDH-032 machine-checked covariance of finite Schur memory under an invertible
change of retained basis.  The algebraic core is noncommutative; finite matrix
rings are immediate instances.
-/

theorem retained_inverse_covariance_generic
    {R : Type*} [Ring R]
    (q r c e : R)
    (hQR : q * r = 1)
    (hRQ : r * q = 1)
    (hCE : c * e = 1)
    (hEC : e * c = 1) :
    (r * c * q) * (r * e * q) = 1 ∧
      (r * e * q) * (r * c * q) = 1 := by
  constructor
  · calc
      (r * c * q) * (r * e * q) = r * c * (q * r) * e * q := by noncomm_ring
      _ = r * c * e * q := by rw [hQR, mul_one]
      _ = r * q := by rw [hCE, mul_one]
      _ = 1 := hRQ
  · calc
      (r * e * q) * (r * c * q) = r * e * (q * r) * c * q := by noncomm_ring
      _ = r * e * c * q := by rw [hQR, mul_one]
      _ = r * q := by rw [hEC, mul_one]
      _ = 1 := hRQ

theorem memory_derivative_covariance_generic
    {R : Type*} [Ring R]
    (q r e dc da : R)
    (hQR : q * r = 1) :
    r * (da + e * dc * e) * q =
      r * da * q + (r * e * q) * (r * dc * q) * (r * e * q) := by
  calc
    r * da * q + (r * e * q) * (r * dc * q) * (r * e * q) =
        r * da * q + r * e * (q * r) * dc * (q * r) * e * q := by noncomm_ring
    _ = r * da * q + r * e * dc * e * q := by rw [hQR, mul_one]
    _ = r * (da + e * dc * e) * q := by noncomm_ring

theorem finite_matrix_memory_derivative_covariance
    {K : Type*} [Field K]
    {n : Type*} [Fintype n] [DecidableEq n]
    (Q R E dC dA : Matrix n n K)
    (hQR : Q * R = 1) :
    R * (dA + E * dC * E) * Q =
      R * dA * Q + (R * E * Q) * (R * dC * Q) * (R * E * Q) :=
  memory_derivative_covariance_generic Q R E dC dA hQR

theorem finite_matrix_inverse_covariance
    {K : Type*} [Field K]
    {n : Type*} [Fintype n] [DecidableEq n]
    (Q R C E : Matrix n n K)
    (hQR : Q * R = 1)
    (hRQ : R * Q = 1)
    (hCE : C * E = 1)
    (hEC : E * C = 1) :
    (R * C * Q) * (R * E * Q) = 1 ∧
      (R * E * Q) * (R * C * Q) = 1 :=
  retained_inverse_covariance_generic Q R C E hQR hRQ hCE hEC
