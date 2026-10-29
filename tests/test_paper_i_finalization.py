import json
from pathlib import Path


def test_paper_i_finalization_markers() -> None:
    root = Path(__file__).resolve().parents[1]
    manuscript = (root / "paper" / "main.tex").read_text(encoding="utf-8")
    assert "% P1-FINALIZATION-2026-10-29" in manuscript
    assert "% P1-PAPER-GRAPH" in manuscript
    assert "Exactness of the layer recursion" in manuscript
    assert "Primary 37E05; Secondary 11A55, 11A63, 49L20" in manuscript
    assert "complete $329{,}106{,}757$-state depth-$162$ payload" in manuscript
    assert "$103/131\\ (131/28)$" in manuscript
    assert "$11803/22160\\ (22160/10357)$" in manuscript

    supplement = (root / "paper" / "supplement.md").read_text(encoding="utf-8")
    assert "## S10. Formal layer recursion and reviewer replay" in supplement
    assert "PASS_PAPER_I_FULL_EXACT_REPLAY" in supplement

    claims = (root / "paper" / "claim-evidence-matrix.csv").read_text(encoding="utf-8")
    assert "P15,the recursive exact layers equal the nonterminal reachable sets" in claims

    state = json.loads((root / "metadata" / "PAPER_I_STATE.json").read_text(encoding="utf-8"))
    assert state["authority"] == "PUBLICATION_TRACK_P1_EXCLUSIVE"
    assert state["closed_claims"]["tau"] == {"1": 45, "2": 85, "3": 120, "4": 162}
    assert state["context_only"]["tau5_interval"] == [186, 212]
    assert state["status"] == "INTERNAL_FINALIZATION_COMPLETE_EXTERNAL_GATES_OPEN"

    charter = (root / "docs" / "validation" / "PAPER_I_BRANCH_CHARTER_2026-10-29.md").read_text(encoding="utf-8")
    assert "PUBLICATION_TRACK / P1_EXCLUSIVE" in charter
    assert "No out-of-scope result may enter the theorem dependency graph" in charter

    workflow = (root / ".github" / "workflows" / "reviewer-bundle.yml").read_text(encoding="utf-8")
    assert "paper/supplement.md" in workflow
    assert "paper/PAPER_I_ONE_PAGE_BRIEF.md" in workflow
    assert "metadata/PAPER_I_STATE.json" in workflow
    assert "data/thresholds/exact-bfs-depth-0-162.csv" in workflow
    assert "scripts/paper_i/replay_exact.sh" in workflow
