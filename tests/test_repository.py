from pathlib import Path

from rgphi.verification import verify_repository


def test_repository_evidence() -> None:
    root = Path(__file__).resolve().parents[1]
    result = verify_repository(root)
    assert result["status"] == "PASS"
