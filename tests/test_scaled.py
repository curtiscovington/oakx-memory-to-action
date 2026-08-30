import tempfile
import unittest
from pathlib import Path

from oakx_study.scaled import BoundedTools, WORLDS
from oakx_study.study import build_oakx_repo


class ScaledStudyTests(unittest.TestCase):
    def test_task_bank_is_unique_and_frozen_size(self):
        self.assertEqual(12, len(WORLDS))
        self.assertEqual(12, len({w.task_id for w in WORLDS}))
        self.assertEqual(12, len({w.error_code for w in WORLDS}))
        self.assertEqual(12, len({w.source_path for w in WORLDS}))

    def test_knowledge_has_rule_but_not_live_values(self):
        for world in WORLDS:
            self.assertIn(world.error_code, world.knowledge)
            self.assertIn(world.root_cause, world.knowledge)
            self.assertNotIn(world.incident.splitlines()[1], world.knowledge)

    def test_placebo_has_no_scaled_identifiers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "placebo"
            build_oakx_repo(root, WORLDS, True)
            corpus = "\n".join(path.read_text() for path in (root / "knowledge").glob("*.md"))
            for world in WORLDS:
                self.assertNotIn(world.error_code, corpus)
                self.assertNotIn(world.root_cause, corpus)

    def test_oakx_search_is_bounded_and_enumeration_blocked(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "ops").mkdir()
            (root / "oakx").mkdir()
            tools = BoundedTools(root / "ops", root / "oakx", 1)
            self.assertIn("error", tools.call("list_files", {"repo": "oakx"}))
            tools.call("search_files", {"repo": "oakx", "query": "missing"})
            self.assertIn("error", tools.call("search_files", {"repo": "oakx", "query": "again"}))


if __name__ == "__main__":
    unittest.main()
