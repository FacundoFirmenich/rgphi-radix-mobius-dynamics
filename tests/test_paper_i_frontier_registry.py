import json
from pathlib import Path


ALLOWED = {
    "CLOSED_SCOPED",
    "READY_FOR_EXTERNAL_ACTION",
    "ACTIVE_PARTIAL",
    "BLOCKED_SPECIFIC",
    "DEPENDENCY_BLOCKED",
    "REFUTED_SCOPED",
    "SUPERSEDED",
}


def test_paper_i_frontier_registry_is_typed_and_specific() -> None:
    root = Path(__file__).resolve().parents[1]
    registry = json.loads((root / "metadata" / "PAPER_I_FRONTIERS.json").read_text(encoding="utf-8"))

    assert registry["authority"] == "PUBLICATION_TRACK_P1_EXCLUSIVE"
    assert set(registry["status_vocabulary"]) == ALLOWED
    assert len(registry["frontiers"]) == 7

    ids = [item["id"] for item in registry["frontiers"]]
    assert len(ids) == len(set(ids))

    for item in registry["frontiers"]:
        assert item["status"] in ALLOWED
        assert item["operation_or_requirement"].strip()
        assert item["scope"].strip()
        assert item["reopening_condition"].strip()
        assert item["next_action"].strip()
        assert isinstance(item["alternatives"], list)
        assert isinstance(item["evidence"], list) and item["evidence"]
        if item["status"] == "BLOCKED_SPECIFIC":
            assert item["obstacle_evidence"].strip()
            assert item["alternatives"]

    by_id = {item["id"]: item for item in registry["frontiers"]}
    assert by_id["P1-G0-INTERNAL-CANDIDATE"]["status"] == "CLOSED_SCOPED"
    assert by_id["P1-G1-SPECIALIST-REVIEWS"]["status"] == "READY_FOR_EXTERNAL_ACTION"
    assert by_id["P1-G3-CLEAN-ROOM-REPLICATION"]["status"] == "READY_FOR_EXTERNAL_ACTION"
    assert by_id["P1-G4-FULL-CERTIFICATE-ARCHIVE"]["status"] == "BLOCKED_SPECIFIC"


def test_cross_project_audit_does_not_promote_scientific_claims() -> None:
    root = Path(__file__).resolve().parents[1]
    audit = json.loads((root / "metadata" / "PI_GENESIS_R2_P1_AUDIT.json").read_text(encoding="utf-8"))
    effect = audit["paper_i_scientific_effect"]
    assert effect == {
        "theorem_changed": False,
        "numerical_claim_changed": False,
        "evidence_changed": False,
        "novelty_claim_changed": False,
        "governance_hardened": True,
    }
    assert audit["pi_genesis_integrity"]["source_authority"] == "SHADOW"
