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


    def test_filter_happens_before_limit(self):
        result = select_tasks(self.tasks, status="open", limit=2)
        self.assertEqual([task["id"] for task in result], [2, 3])

    def test_priority_order(self):
        result = select_tasks(self.tasks, sort="priority")
        self.assertEqual([task["id"] for task in result], [3, 4, 2, 1])

    def test_filter_sort_then_limit(self):
        result = select_tasks(self.tasks, status="open", limit=2, sort="priority")
        self.assertEqual([task["id"] for task in result], [3, 4])

    def test_equal_priorities_keep_input_order(self):
        result = select_tasks([self.tasks[3], self.tasks[2]], sort="priority")
        self.assertEqual([task["id"] for task in result], [4, 3])

    def test_input_is_unchanged(self):
        before = json.loads(json.dumps(self.tasks))
        select_tasks(self.tasks, status="open", sort="priority", limit=2)
        self.assertEqual(self.tasks, before)

    def test_large_limit_returns_all_matches(self):
        result = select_tasks(self.tasks, status="open", limit=100)
        self.assertEqual([task["id"] for task in result], [2, 3, 4])

    def test_empty_input(self):
        self.assertEqual(select_tasks([], status="open", sort="priority"), [])

    def test_unknown_sort_is_rejected(self):
        with self.assertRaises(ValueError):
            select_tasks(self.tasks, sort="unknown")

    def test_zero_limit_with_filter_and_sort(self):
        self.assertEqual(select_tasks(self.tasks, status="open", sort="priority", limit=0), [])

    def test_no_matching_records(self):
        self.assertEqual(select_tasks([self.tasks[0]], status="open"), [])


if __name__ == "__main__":
    unittest.main()
