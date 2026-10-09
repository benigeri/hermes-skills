#!/usr/bin/env python3
"""Read-only structural verification for the installed DFU skill package."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FILES = {
    "LICENSE",
    "SKILL.md",
    "references/hermes-options.md",
    "references/recommended-policies.md",
    "scripts/verify_package.py",
    "templates/review-output.md",
}
TRIGGERS = ("DFU", "don't fuck up", "don't fuck it up")
REQUIRED_LINKS = (
    "references/hermes-options.md",
    "references/recommended-policies.md",
    "templates/review-output.md",
)
REQUIRED_FRONTMATTER = {
    "name": "dfu",
    "version": "1.0.0",
    "author": "benigeri",
    "license": "MIT",
}
REQUIRED_TAGS = {
    "hermes",
    "architecture",
    "review",
    "skills",
    "profiles",
    "configuration",
    "plugins",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def package_files(failures: list[str]) -> set[str]:
    found: set[str] = set()
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if "__pycache__" in relative.parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            failures.append(f"symbolic links are not allowed: {relative}")
        elif path.is_file():
            found.add(relative.as_posix())
        elif not path.is_dir():
            failures.append(f"non-regular package entry: {relative}")
    return found


def main() -> int:
    failures: list[str] = []
    hashes: dict[str, str] = {}
    found = package_files(failures)

    for relative in sorted(EXPECTED_FILES - found):
        failures.append(f"missing required file: {relative}")
    for relative in sorted(found - EXPECTED_FILES):
        failures.append(f"unexpected package file: {relative}")
    for relative in sorted(found & EXPECTED_FILES):
        hashes[relative] = sha256(ROOT / relative)

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        skill = skill_path.read_text(encoding="utf-8")
        lowered = skill.lower()
        frontmatter_match = re.match(r"\A---\n(.*?)\n---\n", skill, re.DOTALL)
        if not frontmatter_match:
            failures.append("SKILL.md must begin with YAML frontmatter")
        else:
            try:
                frontmatter = json.loads(frontmatter_match.group(1))
            except json.JSONDecodeError as exc:
                failures.append(f"SKILL.md frontmatter must be valid JSON, a strict YAML subset: {exc}")
                frontmatter = None

            if not isinstance(frontmatter, dict):
                failures.append("SKILL.md frontmatter must parse to a mapping")
            else:
                for key, value in REQUIRED_FRONTMATTER.items():
                    if frontmatter.get(key) != value:
                        failures.append(f"SKILL.md frontmatter must contain {key}: {value}")

                description = frontmatter.get("description")
                if not isinstance(description, str) or not description.strip():
                    failures.append("SKILL.md frontmatter must contain a description")
                elif len(description) > 60:
                    failures.append("SKILL.md description must be at most 60 characters")

                metadata = frontmatter.get("metadata")
                hermes_metadata = metadata.get("hermes") if isinstance(metadata, dict) else None
                if not isinstance(hermes_metadata, dict):
                    failures.append("SKILL.md frontmatter must contain metadata.hermes")
                else:
                    tags = hermes_metadata.get("tags")
                    if not isinstance(tags, list) or set(tags) != REQUIRED_TAGS:
                        failures.append("SKILL.md metadata.hermes.tags must match the required tags")

        for trigger in TRIGGERS:
            if trigger.lower() not in lowered:
                failures.append(f"SKILL.md missing trigger: {trigger}")

        headings = re.findall(r"(?m)^###\s+([1-7])\.\s+", skill)
        if headings != [str(number) for number in range(1, 8)]:
            failures.append("SKILL.md must contain exactly the seven numbered DFU rules in order")

        for link in REQUIRED_LINKS:
            if link not in skill:
                failures.append(f"SKILL.md missing support-file link: {link}")

    result = {
        "status": "pass" if not failures else "fail",
        "root": str(ROOT),
        "failed_checks": sorted(set(failures)),
        "files": {name: hashes[name] for name in sorted(hashes)},
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
