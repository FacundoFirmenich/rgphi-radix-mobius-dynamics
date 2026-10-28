#!/usr/bin/env python3
"""Validate the internal consistency of the RGΦ research object."""

from __future__ import annotations

import argparse
import json
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict:
    with (ROOT / path).open("rb") as handle:
        return json.load(handle)


def normalize_version(value: str) -> str:
    return re.sub(r"[^0-9a-z]", "", value.lower())


def validate() -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    with (ROOT / "pyproject.toml").open("rb") as handle:
        pyproject = tomllib.load(handle)

    zenodo = load_json(".zenodo.json")
    codemeta = load_json("codemeta.json")
    datacite = load_json("metadata/DATACITE_METADATA_DRAFT.json")
    registry = load_json("metadata/ARTIFACT_REGISTRY.json")
    targets = load_json("metadata/VALIDATION_TARGETS.json")

    versions = {
        "VERSION": version,
        "pyproject": pyproject["project"]["version"],
        "zenodo": zenodo["version"],
        "codemeta": codemeta["version"],
        "datacite": datacite["version"],
    }
    normalized = {name: normalize_version(value) for name, value in versions.items()}
    if len(set(normalized.values())) != 1:
        errors.append(f"version mismatch: {versions}")

    artifact_ids: set[str] = set()
    artifact_paths: set[str] = set()
    for artifact in registry["artifacts"]:
        artifact_id = artifact["id"]
        path = artifact["path"]
        if artifact_id in artifact_ids:
            errors.append(f"duplicate artifact id: {artifact_id}")
        if path in artifact_paths:
            errors.append(f"duplicate artifact path: {path}")
        artifact_ids.add(artifact_id)
        artifact_paths.add(path)
        if not (ROOT / path).is_file():
            errors.append(f"missing registered artifact: {path}")

    target_ids: set[str] = set()
    for target in targets["targets"]:
        target_id = target["id"]
        if target_id in target_ids:
            errors.append(f"duplicate validation target id: {target_id}")
        target_ids.add(target_id)
        for path in target.get("evidence", []):
            if not (ROOT / path).is_file():
                errors.append(f"missing target evidence {target_id}: {path}")

    creator = datacite["creators"][0]
    identifiers = creator.get("nameIdentifiers", [])
    if not any(item.get("nameIdentifierScheme") == "ORCID" for item in identifiers):
        errors.append("DataCite draft lacks creator ORCID")

    if datacite.get("draft") is not True:
        warnings.append("DataCite record is not marked as draft")
    if datacite["identifier"]["identifier"] != "PENDING":
        warnings.append("DataCite identifier is no longer PENDING; review DOI propagation")

    required_navigation = [
        "docs/START_HERE.md",
        "docs/ARTIFACT_CATALOG.md",
        "docs/FAIR_AND_ARCHIVAL_RICHNESS.md",
        "docs/validation/README.md",
    ]
    for path in required_navigation:
        if not (ROOT / path).is_file():
            errors.append(f"missing navigation artifact: {path}")

    return {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "version_records": versions,
        "artifact_count": len(artifact_ids),
        "validation_target_count": len(target_ids),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    report = validate()
    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    print(rendered)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
