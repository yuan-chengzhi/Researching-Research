#!/usr/bin/env python3
"""Validate and render the mechanical project indexes."""

from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "project-index.json"
README_PATH = ROOT / "README.md"
README_ZH_PATH = ROOT / "README.zh-CN.md"
START = "<!-- project-index:start -->"
END = "<!-- project-index:end -->"
REQUIRED = {
    "id", "title", "theme", "status", "visibility", "repository", "card",
    "last_reviewed", "evidence", "evidence_status", "relations", "changed_by", "ownership",
    "claims_supported", "claims_not_supported", "next_question",
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
        if project["ownership"] not in {"direct", "collaborative"}:
            raise ValueError(f"invalid ownership for {project_id}")
        if project["ownership"] == "collaborative":
            for field in ("role_scope", "contribution_scope", "not_my_contribution"):
                if not project.get(field):
                    raise ValueError(f"collaborative project missing {field}: {project_id}")
        if project_id in ids:
            raise ValueError(f"duplicate project id: {project_id}")
        ids.add(project_id)
        card = ROOT / project["card"]
        card_key = str(card)
        if card_key in cards:
            raise ValueError(f"duplicate card path: {project['card']}")
        cards.add(card_key)
        if not card.exists():
            raise ValueError(f"missing card: {project['card']}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", project["last_reviewed"]):
            raise ValueError(f"invalid review date for {project_id}")
        repository = project["repository"]
        if not (repository.startswith("https://github.com/") or repository.startswith("internal:")):
            raise ValueError(f"repository must be a GitHub or internal reference: {project_id}")
        for field in ("evidence", "claims_supported", "claims_not_supported", "relations", "changed_by"):
            if not isinstance(project[field], list) or not project[field]:
                raise ValueError(f"{project_id}.{field} must be a non-empty list")
        for evidence in project["evidence"]:
            if "/commit/" in evidence and not re.search(r"/commit/[0-9a-f]{40}(?:$|[/?#])", evidence):
                raise ValueError(f"commit evidence is not pinned to a full SHA: {project_id}")


def render(projects: list[dict], chinese: bool) -> str:
    if chinese:
        lines = [START, "| 项目 | 主题 | 状态 | 归属 | 可见性 | 证据 |", "| --- | --- | --- | --- | --- | --- |"]
    else:
        lines = [START, "| Project | Theme | Status | Ownership | Visibility | Evidence |", "| --- | --- | --- | --- | --- |"]
    for project in projects:
        evidence = "; ".join(project["evidence"])
        lines.append(f"| [{project['title']}]({project['card']}) | {project['theme']} | {project['status']} | {project['ownership']} | {project['visibility']} | {evidence} |")
    lines.append(END)
    return "\n".join(lines)


def replace_block(readme: str, block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        raise ValueError("README is missing project-index markers")
    return pattern.sub(block, readme, count=1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="write generated blocks")
    parser.add_argument("--check", action="store_true", help="fail if either README is out of date")
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("choose --write or --check")
    projects = load_index()
    validate(projects)
    targets = [(README_PATH, render(projects, False)), (README_ZH_PATH, render(projects, True))]
    changed = False
    for path, expected in targets:
        current = path.read_text(encoding="utf-8")
        updated = replace_block(current, expected)
        if args.write:
            if updated != current:
                path.write_text(updated, encoding="utf-8")
        elif updated != current:
            print(f"{path.name} project index is out of date", file=sys.stderr)
            changed = True
    return 1 if changed else 0


if __name__ == "__main__":
    raise SystemExit(main())
