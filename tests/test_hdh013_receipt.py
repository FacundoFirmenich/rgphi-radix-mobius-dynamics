from pathlib import Path
import subprocess
import sys


def test_hdh013_independent_receipt() -> None:
    root = Path(__file__).resolve().parents[1]
    hdh = root / "research" / "experimental" / "hdh"
    result = subprocess.run(
        [sys.executable, str(hdh / "code" / "hdh_013_independent_check.py")],
        cwd=hdh / "data",
        check=True,
        capture_output=True,
        text=True,
    )
    assert "PASS_HDH013_COMPACT_RECEIPT" in result.stdout
