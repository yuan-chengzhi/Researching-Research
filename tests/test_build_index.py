"""Regression tests for metadata boundaries and deterministic README generation."""
from __future__ import annotations

from copy import deepcopy
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stderr
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "build_index.py"
spec = importlib.util.spec_from_file_location("build_index", SCRIPT)
assert spec and spec.loader
atlas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(atlas)


class AtlasTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "projects").mkdir()
        self.project = dict(
            id="example", title="Example: a bounded result", theme="feedback",
            status="design", visibility="internal", ownership="direct",
            repository="internal:example", card="projects/example.md",
            last_reviewed="2026-10-14", evidence=["Author's design note"],
            evidence_status="author-report", claims_supported=["A design exists"],
            claims_not_supported=["Effectiveness is established"],
            next_question="Does it help?",
            relations=[dict(type="informs", to="hub:researching-research", why="A question", layer="problem")],
            changed_by=[dict(evidence="Design note", change="Makes the question testable")],
        )
        self.question = dict(
            id="Q0", title="Does it help?", status="open", role="current",
            source="current-questions.md#q0", description="Compare outcomes.",
            links=[dict(id="project:example", role="informs", why="A testable design")],
        )
        (self.root / "current-questions.md").write_text('<a id="q0"></a>\n## Q0\n', encoding="utf-8")
        self.write_card()

    def write_card(self):
        p = self.project
        (self.root / p["card"]).write_text(
            f'---\nid: {p["id"]}\ntitle: {json.dumps(p["title"])}\nstatus: {p["status"]}\n---\n\n# Example\n',
            encoding="utf-8",
        )

    def validate(self):
        atlas.validate([self.project], [self.question], self.root)

    def test_valid_design_and_quoted_title(self):
        self.validate()

    def test_legacy_card_may_omit_optional_front_matter(self):
        (self.root / self.project["card"]).write_text('---\nid: example\n---\n\n# Example\n', encoding="utf-8")
        self.validate()

    def test_invalid_enum_rejected(self):
        for field in ("ownership", "status", "visibility", "evidence_status"):
            with self.subTest(field=field):
                original = self.project[field]
                self.project[field] = "typo"
                with self.assertRaises(ValueError):
                    self.validate()
                self.project[field] = original

    def test_duplicate_project_id_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate project id"):
            atlas.validate([self.project, deepcopy(self.project)], [self.question], self.root)

    def test_duplicate_card_path_rejected(self):
        other = deepcopy(self.project)
        other["id"] = "other"
        with self.assertRaisesRegex(ValueError, "duplicate card path"):
            atlas.validate([self.project, other], [self.question], self.root)

    def test_invalid_calendar_date_rejected(self):
        self.project["last_reviewed"] = "2026-02-30"
        with self.assertRaises(ValueError):
            self.validate()

    def test_card_index_disagreement_rejected(self):
        self.project["title"] = "Different"
        with self.assertRaisesRegex(ValueError, "card/index title mismatch"):
            self.validate()

    def test_missing_front_matter_rejected(self):
        (self.root / self.project["card"]).write_text("# Example\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "front matter"):
            self.validate()

    def test_out_of_repository_path_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            path = Path(outside) / "card.md"
            path.write_text("content", encoding="utf-8")
            (self.root / "escape.md").symlink_to(path)
            for value in (str(path), "escape.md", "../missing.md"):
                with self.subTest(path=value), self.assertRaises(ValueError):
                    atlas.local_file(value, self.root)

    def test_fixed_commit_requires_full_immutable_reference(self):
        self.project["evidence_status"] = "fixed-commit"
        with self.assertRaises(ValueError):
            self.validate()
        self.project["evidence"] = ["https://github.com/owner/repo/blob/" + "a" * 40 + "/README.md"]
        self.validate()

    def test_short_commit_sha_rejected(self):
        self.project["evidence"] = ["https://github.com/owner/repo/commit/abc123"]
        with self.assertRaisesRegex(ValueError, "full SHA"):
            self.validate()

    def test_collaborative_entry_requires_personal_scope(self):
        self.project["ownership"] = "collaborative"
        with self.assertRaises(ValueError):
            self.validate()
        self.project.update(role_scope="analysis", contribution_scope=["Trace analysis"], not_my_contribution=["System implementation"])
        self.validate()

    def test_reference_entry_cannot_claim_repository_contribution(self):
        self.project.update(ownership="reference", status="reference-only", contribution_scope=[],
                            role_scope="reference-only-no-repository-contribution", not_my_contribution=["Repository implementation"])
        self.write_card()
        self.validate()
        self.project["contribution_scope"] = ["Implementation"]
        with self.assertRaisesRegex(ValueError, "empty contribution_scope"):
            self.validate()

    def test_reference_only_cannot_be_direct_work(self):
        self.project["status"] = "reference-only"
        with self.assertRaisesRegex(ValueError, "reference ownership"):
            self.validate()

    def test_unknown_relation_rejected(self):
        self.project["relations"][0]["to"] = "missing-project"
        with self.assertRaisesRegex(ValueError, "unknown relation"):
            self.validate()

    def test_malformed_change_record_rejected(self):
        self.project["changed_by"] = ["not an object"]
        with self.assertRaisesRegex(ValueError, "changed_by"):
            self.validate()

    def test_missing_question_anchor_rejected(self):
        self.question["source"] = "current-questions.md#missing"
        with self.assertRaisesRegex(ValueError, "anchor"):
            self.validate()

    def test_unknown_question_target_rejected(self):
        self.question["links"][0]["id"] = "project:missing"
        with self.assertRaisesRegex(ValueError, "target unknown"):
            self.validate()

    def test_duplicate_question_id_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate or invalid question"):
            atlas.validate([self.project], [self.question, deepcopy(self.question)], self.root)

    def test_registry_rejects_nonobject_entries(self):
        path = self.root / "bad.json"
        path.write_text(json.dumps(dict(schema_version=2, projects=["bad"])), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "must be an object"):
            atlas.load_registry(path, "projects")

    def test_bilingual_table_and_safe_labels(self):
        p = deepcopy(self.project)
        p["title"] = "A | [B] <C>\\D\nnext"
        en, zh = atlas.render([p], False), atlas.render([p], True)
        self.assertIn("Research design", en)
        self.assertIn("研究设计", zh)
        self.assertIn("&#124;", en)
        self.assertIn("&#91;B&#93;", en)
        self.assertIn("&lt;C&gt;&#92;D next", en)
        self.assertEqual(len(en.splitlines()), 5)

    def test_markers_must_be_unique_and_ordered(self):
        for text in ("none", atlas.END + atlas.START, atlas.START + atlas.START + atlas.END):
            with self.subTest(text=text), self.assertRaises(ValueError):
                atlas.replace_block(text, "replacement")

    def test_replacement_preserves_literal_backslash_and_other_text(self):
        original = "before\n" + atlas.START + "old" + atlas.END + "\nafter"
        block = atlas.START + r"\g<1>" + atlas.END
        self.assertEqual(atlas.replace_block(original, block), "before\n" + block + "\nafter")

    def test_cli_modes_are_exclusive(self):
        with redirect_stderr(io.StringIO()):
            for args in ([], ["--write", "--check"]):
                with self.subTest(args=args), self.assertRaises(SystemExit):
                    atlas.main(args)

    def test_write_then_check_is_idempotent(self):
        for filename, key, records in (("project-index.json", "projects", [self.project]),
                                       ("question-index.json", "questions", [self.question])):
            (self.root / filename).write_text(json.dumps({"schema_version": 2, key: records}), encoding="utf-8")
        for name in ("README.md", "README.zh-CN.md"):
            (self.root / name).write_text("intro\n" + atlas.START + "stale" + atlas.END + "\noutro\n", encoding="utf-8")
        with patch.object(atlas, "ROOT", self.root), redirect_stderr(io.StringIO()):
            self.assertEqual(atlas.main(["--check"]), 1)
            self.assertEqual(atlas.main(["--write"]), 0)
            before = (self.root / "README.md").read_bytes()
            self.assertEqual(atlas.main(["--check"]), 0)
            self.assertEqual(atlas.main(["--write"]), 0)
            self.assertEqual(before, (self.root / "README.md").read_bytes())


if __name__ == "__main__":
    unittest.main()
