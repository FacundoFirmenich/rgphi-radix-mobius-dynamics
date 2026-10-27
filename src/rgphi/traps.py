"""Finite-trap construction and exact audits."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import Iterable

import networkx as nx

from .dynamics import DEFAULT_TERMINAL, children, portal_height


C8: frozenset[Fraction] = frozenset(
    {
        Fraction(1, 13), Fraction(3, 13), Fraction(4, 13),
        Fraction(5, 11), Fraction(6, 11), Fraction(9, 13),
        Fraction(10, 13), Fraction(12, 13),
    }
)


@dataclass(frozen=True, slots=True)
class TrapAtlasSummary:
    base: int
    denominator_bound: int
    states: int
    edges: int
    strongly_connected_components: int
    closed_sccs_modulo_terminal: int
    finite_forward_closures: int


def multiplicative_order(base: int, modulus: int) -> int | None:
    if modulus <= 1 or gcd(base, modulus) != 1:
        return None
    residue = 1
    for order in range(1, 10 * modulus + 1):
        residue = (residue * base) % modulus
        if residue == 1:
            return order
    raise ArithmeticError(f"order search exceeded safety bound: base={base}, modulus={modulus}")


def audit_finite_trap(
    trap: Iterable[Fraction],
    *,
    base: int = 10,
    terminal: frozenset[Fraction] | set[Fraction] = DEFAULT_TERMINAL,
) -> dict[str, object]:
    trap_set = frozenset(trap)
    if not trap_set:
        raise ValueError("trap cannot be empty")
    edges: list[dict[str, str]] = []
    for state in sorted(trap_set):
        for action in ("T", "S"):
            from .dynamics import apply_branch
            branch = apply_branch(state, action, base=base)  # type: ignore[arg-type]
            if branch is None:
                continue
            successor = branch.state
            status = "inside" if successor in trap_set else "terminal" if successor in terminal else "outside"
            edges.append({"state": str(state), "action": action, "successor": str(successor), "status": status})
            if status == "outside":
                raise AssertionError(f"trap leaks: {state} --{action}--> {successor}")
    return {
        "size": len(trap_set),
        "max_q": str(max(portal_height(state) for state in trap_set)),
        "edges": edges,
        "denominators": sorted({state.denominator for state in trap_set}),
    }


def build_atlas(
    *,
    denominator_bound: int = 500,
    base: int = 10,
    terminal: frozenset[Fraction] | set[Fraction] = DEFAULT_TERMINAL,
) -> tuple[TrapAtlasSummary, nx.DiGraph, list[set[Fraction]], list[frozenset[Fraction]]]:
    if denominator_bound < 2:
        raise ValueError("denominator_bound must be at least 2")
    states = [
        Fraction(a, b)
        for b in range(2, denominator_bound + 1)
        for a in range(1, b)
        if gcd(a, b) == 1 and Fraction(a, b) not in terminal
    ]
    state_set = set(states)
    graph = nx.DiGraph()
    graph.add_nodes_from(states)
    outside: dict[Fraction, list[Fraction]] = {state: [] for state in states}
    for state in states:
        for branch in children(state, base=base, terminal=None):
            successor = branch.state
            if successor in terminal:
                continue
            if successor in state_set:
                graph.add_edge(state, successor, action=branch.action)
            else:
                outside[state].append(successor)

    sccs = [set(component) for component in nx.strongly_connected_components(graph)]
    node_to_scc = {state: index for index, component in enumerate(sccs) for state in component}
    condensation = nx.DiGraph()
    condensation.add_nodes_from(range(len(sccs)))
    unsafe: set[int] = set()
    for state in states:
        source = node_to_scc[state]
        if outside[state]:
            unsafe.add(source)
        for successor in graph.successors(state):
            target = node_to_scc[successor]
            if source != target:
                condensation.add_edge(source, target)

    closed_sccs: list[set[Fraction]] = []
    for index, component in enumerate(sccs):
        if index in unsafe:
            continue
        if not tuple(condensation.successors(index)):
            closed_sccs.append(component)

    closures: set[frozenset[Fraction]] = set()
    for index in condensation.nodes:
        reachable = {index} | nx.descendants(condensation, index)
        if any(item in unsafe for item in reachable):
            continue
        closures.add(frozenset(state for item in reachable for state in sccs[item]))

    summary = TrapAtlasSummary(
        base=base,
        denominator_bound=denominator_bound,
        states=len(states),
        edges=graph.number_of_edges(),
        strongly_connected_components=len(sccs),
        closed_sccs_modulo_terminal=len(closed_sccs),
        finite_forward_closures=len(closures),
    )
    return summary, graph, closed_sccs, sorted(closures, key=lambda item: (len(item), tuple(sorted(item))))
