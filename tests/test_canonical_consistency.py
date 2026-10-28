from pathlib import Path

from rgphi.verification import verify_repository


def test_canonical_claims_are_synchronized() -> None:
    root = Path(__file__).resolve().parents[1]
    result = verify_repository(root)
    assert result["tau5_interval"] == [186, 212]
