"""RGΦ exact rational radix–Möbius dynamics."""
from .dynamics import (
    DEFAULT_TERMINAL,
    S,
    T,
    apply_branch,
    branch_matrix,
    chart,
    children,
    complement,
    in_portal,
    iterate_word,
    portal_height,
    seed_family_state,
    seed_family_successor,
)

__all__ = [
    "DEFAULT_TERMINAL", "S", "T", "apply_branch", "branch_matrix",
    "chart", "children", "complement", "in_portal", "iterate_word",
    "portal_height", "seed_family_state", "seed_family_successor",
]
__version__ = "1.0.0rc1"
