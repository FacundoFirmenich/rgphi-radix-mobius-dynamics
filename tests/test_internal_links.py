from pathlib import Path
import runpy


def test_canonical_markdown_has_no_broken_local_links() -> None:
    module = runpy.run_path(str(Path("tools/check_internal_links.py")))
    errors = module["check_all"]()
    assert errors == [], errors
