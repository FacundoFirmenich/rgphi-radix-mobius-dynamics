from rgphi.traps import C8, audit_finite_trap, multiplicative_order


def test_C8_is_exact_finite_trap() -> None:
    result = audit_finite_trap(C8)
    assert result["size"] == 8
    assert result["max_q"] == "13"
    assert all(edge["status"] in {"inside", "terminal"} for edge in result["edges"])


def test_modular_orders_underlying_C8() -> None:
    assert multiplicative_order(10, 13) == 6
    assert multiplicative_order(10, 11) == 2
