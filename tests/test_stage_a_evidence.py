from pathlib import Path
import subprocess
import sys


def test_stage_a_compact_evidence() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(root / "scripts" / "stage_a" / "verify_stage_a_evidence.py")],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    assert "PASS_STAGE_A_COMPACT_EVIDENCE" in result.stdout
