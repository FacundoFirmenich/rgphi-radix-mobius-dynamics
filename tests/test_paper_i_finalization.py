from pathlib import Path


def test_paper_i_finalization_markers() -> None:
    root = Path(__file__).resolve().parents[1]
    manuscript = (root / "paper" / "main.tex").read_text(encoding="utf-8")
    assert "% P1-FINALIZATION-2026-10-29" in manuscript
    assert "% P1-PAPER-GRAPH" in manuscript
    assert "Exactness of the layer recursion" in manuscript
    assert "Primary 37E05; Secondary 11A55, 11A63, 49L20" in manuscript
    assert "complete $329{,}106{,}757$-state depth-$162$ payload" in manuscript

    supplement = (root / "paper" / "supplement.md").read_text(encoding="utf-8")
    assert "## S10. Formal layer recursion and reviewer replay" in supplement
    assert "PASS_PAPER_I_FULL_EXACT_REPLAY" in supplement

    claims = (root / "paper" / "claim-evidence-matrix.csv").read_text(encoding="utf-8")
    assert "P15,the recursive exact layers equal the nonterminal reachable sets" in claims

    workflow = (root / ".github" / "workflows" / "reviewer-bundle.yml").read_text(encoding="utf-8")
    assert "paper/supplement.md" in workflow
    assert "data/thresholds/exact-bfs-depth-0-162.csv" in workflow
    assert "scripts/paper_i/replay_exact.sh" in workflow
