import json
from pathlib import Path
import unittest

from taskboard import select_tasks


class SelectionTests(unittest.TestCase):
    def setUp(self):
        fixture = Path(__file__).with_name("tasks.json")
        self.tasks = json.loads(fixture.read_text(encoding="utf-8"))

    def test_default_preserves_order(self):
        self.assertEqual(select_tasks(self.tasks), self.tasks)

    def test_filter_without_limit(self):
        result = select_tasks(self.tasks, status="open")
        self.assertEqual([task["id"] for task in result], [2, 3, 4])

    def test_limit_without_filter(self):
        result = select_tasks(self.tasks, limit=2)
        self.assertEqual([task["id"] for task in result], [1, 2])

    def test_zero_limit(self):
        self.assertEqual(select_tasks(self.tasks, limit=0), [])

    def test_negative_limit(self):
        with self.assertRaises(ValueError):
            select_tasks(self.tasks, limit=-1)


if __name__ == "__main__":
    unittest.main()
