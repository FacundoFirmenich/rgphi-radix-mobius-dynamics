from pathlib import Path
import runpy


def test_research_object_validator_passes() -> None:
    module = runpy.run_path(str(Path("tools/validate_research_object.py")))
    report = module["validate"]()
    assert report["status"] == "PASS", report
    assert report["artifact_count"] >= 15
    assert report["validation_target_count"] >= 19
