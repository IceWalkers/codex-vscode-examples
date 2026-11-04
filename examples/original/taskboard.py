"""Task-list example with a deliberately introduced filter/limit defect."""

import argparse
import json
from pathlib import Path


def select_tasks(tasks, status="all", limit=None):
    if limit is not None and limit < 0:
        raise ValueError("limit must be non-negative")

    candidates = tasks if limit is None else tasks[:limit]

    if status == "all":
        return candidates

    return [task for task in candidates if task["status"] == status]


def main():
    parser = argparse.ArgumentParser(description="List demonstration tasks.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--status", choices=("all", "open", "done"), default="all")
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()
    if args.limit is not None and args.limit < 0:
        parser.error("--limit must be non-negative")
    tasks = json.loads(args.file.read_text(encoding="utf-8"))
    for task in select_tasks(tasks, status=args.status, limit=args.limit):
        print(f"{task['id']}\t{task['status']}\t{task['priority']}\t{task['title']}")


if __name__ == "__main__":
    main()
