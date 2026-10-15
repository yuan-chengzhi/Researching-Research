#!/usr/bin/env python3
"""Validate atlas metadata and render compact, bilingual README indexes.

Uses only the standard library. It does not audit scientific claims or check
remote access; those require a separate, dated human review.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- project-index:start -->"
END = "<!-- project-index:end -->"
RELATION_LAYERS = {"temporal", "problem", "constructive", "evidence", "collaborative", "parallel", "future", "adjacent"}
QUESTION_STATUSES = {"hypothesis", "active", "open", "adjacent"}
OWNERSHIP = {
    "direct": ("Direct work", "个人工作"),
    "collaborative": ("Team contribution", "团队中的贡献"),
    "reference": ("Reference only; no repository contribution", "关联参考；无该仓库贡献"),
}
STATUSES = {
    "design": ("Research design", "研究设计"),
    "prototype": ("Prototype", "原型"),
    "implemented": ("Implemented", "已有实现"),
    "experimentally-observed": ("Experiment recorded", "已有实验记录"),
    "collaborative-research": ("Collaborative research", "合作研究"),
    "submitted": ("Submitted", "已投稿"),
    "analysis": ("Analysis", "分析"),
    "adjacent-work": ("Adjacent creative work", "相邻创作"),
    "research-thread": ("Research thread", "研究线索"),
    "archived": ("Archived", "历史存档"),
    "reference-only": ("Associated component", "关联组件"),
}
VISIBILITY = {
    "public": ("Public source", "公开来源"),
    "private": ("Private source", "私有来源"),
    "internal": ("Internal material", "内部材料"),
}
EVIDENCE_STATUSES = {"fixed-commit", "branch-pinned", "branch-unpinned", "internal-thread", "internal-artifact", "author-report"}
REQUIRED = {
    "id", "title", "theme", "status", "visibility", "repository", "card",
    "last_reviewed", "evidence", "evidence_status", "relations", "changed_by", "ownership",
    "claims_supported", "claims_not_supported", "next_question",
}


def load_registry(path: Path, key: str) -> list[dict]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("schema_version") != 2:
        raise ValueError(f"{path.name} must declare schema_version 2")
    records = payload.get(key)
    if not isinstance(records, list) or not records:
        raise ValueError(f"{path.name} must contain a non-empty {key} list")
    if not all(isinstance(record, dict) for record in records):
        raise ValueError(f"{path.name}: every {key} entry must be an object")
    return records


def local_file(value: str, root: Path) -> Path:
    if not isinstance(value, str) or not value or Path(value).is_absolute():
        raise ValueError(f"invalid relative file path: {value!r}")
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        raise ValueError(f"missing or out-of-repository file: {value}")
    return path


def nonempty_list(record: dict, field: str) -> None:
    value = record.get(field)
    if not isinstance(value, list) or not value:
        raise ValueError(f"{record.get('id', '<unknown>')}.{field} must be a non-empty list")


def validate(projects: list[dict], questions: list[dict], root: Path = ROOT) -> None:
    ids: set[str] = set()
    cards: set[Path] = set()
    for project in projects:
        if not isinstance(project, dict):
            raise ValueError("project must be an object")
        missing = REQUIRED - project.keys()
        if missing:
            raise ValueError(f"{project.get('id', '<unknown>')} missing {sorted(missing)}")
        pid = project["id"]
        if not isinstance(pid, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", pid):
            raise ValueError(f"invalid project id: {pid!r}")
        if pid in ids:
            raise ValueError(f"duplicate project id: {pid}")
        ids.add(pid)
        for field, allowed in (("ownership", OWNERSHIP), ("status", STATUSES), ("visibility", VISIBILITY), ("evidence_status", EVIDENCE_STATUSES)):
            if not isinstance(project[field], str) or project[field] not in allowed:
                raise ValueError(f"invalid {field} for {pid}")
        for field in ("title", "theme", "repository", "next_question"):
            if not isinstance(project[field], str) or not project[field].strip():
                raise ValueError(f"{pid}.{field} must be non-empty text")
        if project["ownership"] == "collaborative":
            if not project.get("role_scope"):
                raise ValueError(f"collaborative project missing role_scope: {pid}")
            for field in ("contribution_scope", "not_my_contribution"):
                nonempty_list(project, field)
        if project["ownership"] == "reference":
            if project["status"] != "reference-only" or project.get("contribution_scope") != []:
                raise ValueError(f"reference must be reference-only with empty contribution_scope: {pid}")
            if project.get("role_scope") != "reference-only-no-repository-contribution":
                raise ValueError(f"reference must explicitly disclaim repository contribution: {pid}")
            nonempty_list(project, "not_my_contribution")
        elif project["status"] == "reference-only":
            raise ValueError(f"reference-only status requires reference ownership: {pid}")
        card = local_file(project["card"], root)
        if card in cards:
            raise ValueError(f"duplicate card path: {project['card']}")
        cards.add(card)
        # Legacy cards may omit optional metadata, but must not contradict it.
        text = card.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            raise ValueError(f"card missing front matter: {pid}")
        front = text[4:].split("\n---\n", 1)[0]
        for field in ("id", "title", "theme", "status", "visibility", "ownership", "repository", "last_reviewed"):
            match = re.search(rf"^{field}:\s*(.+)$", front, re.MULTILINE)
            if match:
                value = match.group(1).strip()
                if value.startswith('"'):
                    value = json.loads(value)
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1].replace("''", "'")
                if value != project[field]:
                    raise ValueError(f"card/index {field} mismatch: {pid}")
            if field == "id" and not match:
                raise ValueError(f"card missing id: {pid}")
        stamp = project["last_reviewed"]
        if not isinstance(stamp, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", stamp):
            raise ValueError(f"invalid review date for {pid}")
        date.fromisoformat(stamp)
        if not (project["repository"].startswith("https://github.com/") or project["repository"].startswith("internal:")):
            raise ValueError(f"repository must be a GitHub or internal reference: {pid}")
        for field in ("evidence", "claims_supported", "claims_not_supported", "relations", "changed_by"):
            nonempty_list(project, field)
        for field in ("evidence", "claims_supported", "claims_not_supported"):
            if not all(isinstance(item, str) and item.strip() for item in project[field]):
                raise ValueError(f"{pid}.{field} must contain non-empty text")
        for evidence in project["evidence"]:
            if "/commit/" in evidence and not re.search(r"/commit/[0-9a-f]{40}(?:$|[/?#])", evidence):
                raise ValueError(f"commit evidence is not pinned to a full SHA: {pid}")
        if project["evidence_status"] == "fixed-commit" and not any(
            re.search(r"https://github\.com/[^/]+/[^/]+/(?:commit|blob|tree)/[0-9a-f]{40}(?:$|[/?#])", item)
            for item in project["evidence"]
        ):
            raise ValueError(f"fixed-commit needs an immutable GitHub reference: {pid}")
        for change in project["changed_by"]:
            if not isinstance(change, dict) or not all(isinstance(change.get(key), str) and change[key].strip() for key in ("evidence", "change")):
                raise ValueError(f"invalid changed_by entry: {pid}")

    for project in projects:
        for relation in project["relations"]:
            if not isinstance(relation, dict) or not {"type", "to", "why", "layer"} <= relation.keys():
                raise ValueError(f"invalid relation shape: {project['id']}")
            if not all(isinstance(relation[key], str) and relation[key].strip() for key in ("type", "to", "why", "layer")):
                raise ValueError(f"invalid relation values: {project['id']}")
            if relation["layer"] not in RELATION_LAYERS:
                raise ValueError(f"invalid relation layer: {project['id']}")
            if relation["to"] not in ids and not re.fullmatch(r"(?:hub|doc):[A-Za-z0-9._/-]+", relation["to"]):
                raise ValueError(f"unknown relation target: {relation['to']}")

    question_ids: set[str] = set()
    for question in questions:
        required = {"id", "title", "status", "role", "source", "description", "links"}
        if not isinstance(question, dict) or required - question.keys():
            raise ValueError("question missing required fields")
        qid = question["id"]
        if not isinstance(qid, str) or qid in question_ids:
            raise ValueError(f"duplicate or invalid question id: {qid!r}")
        question_ids.add(qid)
        if not isinstance(question["status"], str) or question["status"] not in QUESTION_STATUSES:
            raise ValueError(f"invalid question status: {qid}")
        if not all(isinstance(question[field], str) and question[field].strip() for field in ("title", "role", "source", "description")):
            raise ValueError(f"question missing text: {qid}")
        source_path, separator, anchor = question["source"].partition("#")
        source = local_file(source_path, root).read_text(encoding="utf-8")
        if not separator or not anchor or not re.search(rf'<a id="{re.escape(anchor)}"></a>\n## ', source):
            raise ValueError(f"question source anchor is not followed by a heading: {qid}")
        nonempty_list(question, "links")
        for link in question["links"]:
            if not isinstance(link, dict) or not all(isinstance(link.get(key), str) and link[key].strip() for key in ("id", "role", "why")):
                raise ValueError(f"invalid question link shape: {qid}")
            if link["id"] not in {f"project:{pid}" for pid in ids} and not re.fullmatch(r"(?:hub|doc):[A-Za-z0-9._/-]+", link["id"]):
                raise ValueError(f"question link target unknown {link['id']}: {qid}")


def cell(text: str) -> str:
    """Escape text that could break a Markdown table or link label."""
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("\\", "&#92;").replace("|", "&#124;").replace("[", "&#91;")
            .replace("]", "&#93;").replace("\r", " ").replace("\n", " "))


def render(projects: list[dict], chinese: bool) -> str:
    language = int(chinese)
    header = "| 条目 | 状态 | 我的角色 | 原始来源 |" if chinese else "| Entry | Status | My role | Original source |"
    lines = [START, header, "| --- | --- | --- | --- |"]
    for p in projects:
        lines.append(f"| [{cell(p['title'])}]({p['card']}) | {STATUSES[p['status']][language]} | {OWNERSHIP[p['ownership']][language]} | {VISIBILITY[p['visibility']][language]} |")
    return "\n".join(lines + [END])


def replace_block(text: str, block: str) -> str:
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) >= text.index(END):
        raise ValueError("README must contain exactly one ordered project-index marker pair")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    return pattern.sub(lambda _: block, text, count=1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="refresh generated README blocks")
    mode.add_argument("--check", action="store_true", help="fail if either generated block is stale")
    args = parser.parse_args(argv)
    try:
        projects = load_registry(ROOT / "project-index.json", "projects")
        questions = load_registry(ROOT / "question-index.json", "questions")
        validate(projects, questions, ROOT)
        updates = []
        for filename, chinese in (("README.md", False), ("README.zh-CN.md", True)):
            path = ROOT / filename
            current = path.read_text(encoding="utf-8")
            updated = replace_block(current, render(projects, chinese))
            if updated != current:
                updates.append((path, updated))
        # Validate both targets before writing either one.
        for path, updated in updates:
            if args.write:
                path.write_text(updated, encoding="utf-8")
            else:
                print(f"{path.name}: generated index is out of date", file=sys.stderr)
        return int(bool(updates) and args.check)
    except (OSError, ValueError, TypeError) as exc:
        print(f"Atlas validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
