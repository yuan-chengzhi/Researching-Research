#!/usr/bin/env python3
"""Validate and render the mechanical project index.

The script intentionally has no third-party dependencies. It keeps the
human-written README outside the generated region untouched.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "project-index.json"
README_PATH = ROOT / "README.md"
START = "<!-- project-index:start -->"
END = "<!-- project-index:end -->"
REQUIRED = {
    "id",
    "title",
    "theme",
    "status",
    "visibility",
    "repository",
    "card",
    "last_reviewed",
    "evidence",
    "claims_supported",
    "claims_not_supported",
    "next_question",
}


def load_index() -> list[dict]:
    payload = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1:
        raise ValueError("project-index.json must declare schema_version 1")
    projects = payload.get("projects")
    if not isinstance(projects, list) or not projects:
        raise ValueError("project-index.json must contain a non-empty projects list")
    return projects


def validate(projects: list[dict]) -> None:
    ids: set[str] = set()
    cards: set[str] = set()
    for project in projects:
        missing = REQUIRED - project.keys()
        if missing:
            raise ValueError(f"{project.get('id', '<unknown>')} missing {sorted(missing)}")
        project_id = project["id"]
        if project_id in ids:
            raise ValueError(f"duplicate project id: {project_id}")
        ids.add(project_id)

        card = ROOT / project["card"]
        if str(card) in cards:
            raise ValueError(f"duplicate card path: {project['card']}")
        cards.add(str(card))
        if not card.exists():
            raise ValueError(f"missing card: {project['card']}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", project["last_reviewed"]):
            raise ValueError(f"invalid review date for {project_id}")
        repository = project["repository"]
        if not (
            repository.startswith("https://github.com/")
            or repository.startswith("internal:")
        ):
            raise ValueError(f"repository must be a GitHub or internal reference: {project_id}")
        for field in ("evidence", "claims_supported", "claims_not_supported"):
            if not isinstance(project[field], list) or not project[field]:
                raise ValueError(f"{project_id}.{field} must be a non-empty list")


def render(projects: list[dict]) -> str:
    lines = [
        START,
        "| Project | Theme | Status | Visibility | Evidence |",
        "| --- | --- | --- | --- | --- |",
    ]
    for project in projects:
        evidence = "; ".join(project["evidence"])
        lines.append(
            f"| [{project['title']}]({project['card']}) | "
            f"{project['theme']} | {project['status']} | "
            f"{project['visibility']} | {evidence} |"
        )
    lines.append(END)
    return "\n".join(lines)


def replace_block(readme: str, block: str) -> str:
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END), re.DOTALL
    )
    if not pattern.search(readme):
        raise ValueError("README.md is missing project-index markers")
    return pattern.sub(block, readme, count=1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write the generated block")
    parser.add_argument("--check", action="store_true", help="fail if README is out of date")
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("choose --write or --check")

    projects = load_index()
    validate(projects)
    expected = render(projects)
    current = README_PATH.read_text(encoding="utf-8")
    updated = replace_block(current, expected)
    if args.write:
        README_PATH.write_text(updated, encoding="utf-8")
        return 0
    if updated != current:
        print("README.md project index is out of date", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
