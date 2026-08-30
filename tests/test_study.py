import tempfile
import unittest
from pathlib import Path

from oakx_study.study import WORLDS, ResearchLockError, build_oakx_repo, grade_episode, safe_path, validate_config


class StudyTests(unittest.TestCase):
    def base_config(self):
        return {
            "research_mode": True,
            "endpoint": "http://127.0.0.1:11434",
            "model": "fixed:model",
            "model_digest": "abc",
            "concurrency": 1,
            "conditions": ["baseline", "placebo", "oakx"],
        }

    def test_research_lock_rejects_remote_endpoint(self):
        config = self.base_config()
        config["endpoint"] = "https://example.com"
        with self.assertRaises(ResearchLockError):
            validate_config(config)

    def test_research_lock_rejects_parallelism(self):
        config = self.base_config()
        config["concurrency"] = 2
        with self.assertRaises(ResearchLockError):
            validate_config(config)

    def test_safe_path_rejects_escape(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                safe_path(Path(directory), "../outside")

    def test_grade_requires_actual_authoritative_read(self):
        world = WORLDS[0]
        result = {
            "submission": {
                "root_cause": world.root_cause,
                "recommended_value": world.recommended_value,
                "evidence_paths": [world.source_path],
            },
            "tool_transcript": [],
        }
        grade = grade_episode(result, world)
        self.assertFalse(grade["strict_success"])
        self.assertTrue(grade["evidence_ok"])
        self.assertFalse(grade["authoritative_source_read"])

    def test_grade_accepts_exact_verified_answer(self):
        world = WORLDS[0]
        result = {
            "submission": {
                "root_cause": world.root_cause,
                "recommended_value": 58,
                "evidence_paths": [world.source_path],
            },
            "tool_transcript": [{
                "tool": "read_file",
                "arguments": {"repo": "ops", "path": world.source_path.removeprefix("ops/")},
            }],
        }
        self.assertTrue(grade_episode(result, world)["strict_success"])

    def test_placebo_does_not_contain_task_signatures_or_rules(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "placebo"
            build_oakx_repo(root, WORLDS, placebo=True)
            corpus = "\n".join(
                path.read_text(encoding="utf-8")
                for path in (root / "knowledge").glob("*.md")
            )
            for world in WORLDS:
                self.assertNotIn(world.error_code, corpus)
                self.assertNotIn(world.root_cause, corpus)
                self.assertNotIn(world.recommended_value, corpus)


if __name__ == "__main__":
    unittest.main()
