"""Task-list example with corrected filtering and optional priority ordering."""

import argparse
import json
from pathlib import Path


def select_tasks(tasks, status="all", limit=None, sort="input"):
    if limit is not None and limit < 0:
        raise ValueError("limit must be non-negative")
    if sort not in {"input", "priority"}:
        raise ValueError("unsupported sort order")

    selected = [
        task for task in tasks
        if status == "all" or task["status"] == status
    ]

    if sort == "priority":
        selected = sorted(selected, key=lambda task: task["priority"])

    return selected if limit is None else selected[:limit]


def main():
    parser = argparse.ArgumentParser(description="List demonstration tasks.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--status", choices=("all", "open", "done"), default="all")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--sort", choices=("input", "priority"), default="input")
    args = parser.parse_args()
    if args.limit is not None and args.limit < 0:
        parser.error("--limit must be non-negative")
    tasks = json.loads(args.file.read_text(encoding="utf-8"))
    for task in select_tasks(tasks, status=args.status, limit=args.limit, sort=args.sort):
        print(f"{task['id']}\t{task['status']}\t{task['priority']}\t{task['title']}")


if __name__ == "__main__":
    main()
