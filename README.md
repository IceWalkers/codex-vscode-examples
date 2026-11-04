# Codex in VS Code: practical examples

Companion materials for **Mastering Codex in VS Code: Context, Planning, Debugging, and Code Review**, an [IceWalkers](https://www.icewalkers.com/) guide.

Practice giving a coding agent context, investigating a reproducible bug, writing a regression test, and reviewing a bounded feature change. The example is a small Python task-list CLI with no external dependencies.

## Requirements

- Python 3.11 or newer.
- VS Code with the official Codex extension for the agent exercise.
- Git if you want to keep checkpoints.

The Python examples and tests also run without Codex or VS Code. If your system uses `python3` or `py` instead of `python`, substitute that command below.

## Choose your starting point

| Directory | Purpose |
| --- | --- |
| [examples/original](examples/original) | Starting implementation with a deliberate filtering bug and five baseline tests. |
| [examples/completed](examples/completed) | Corrected implementation, optional priority sorting, and 15 tests. |
| [prompts.md](prompts.md) | Adaptable prompts for investigation, implementation, review, and handoff. |

Each example includes `taskboard.py`, `tasks.json`, `test_taskboard.py`, and an `AGENTS.md` with project instructions.

For the exercise, copy `examples/original` to a separate working folder and open that folder in VS Code. Keep the completed implementation outside the agent's workspace so it can investigate the defect without reading the answer. Start a Git repository in the working copy if you want to practice checkpoints.

## 1. Reproduce the bug

From the original working folder:

```bash
python -m unittest -v
python taskboard.py tasks.json --status open --limit 2
```

The five baseline tests pass, but the CLI prints only task 2:

```text
2	open	2	Fix login error
```

The expected result contains tasks 2 and 3. The implementation applies the limit before filtering, so a completed task consumes one of the two available positions.

Ask Codex to trace the CLI arguments through the selection function before editing. Then add this method to the existing `SelectionTests` class:

```python
def test_filter_happens_before_limit(self):
    result = select_tasks(self.tasks, status="open", limit=2)
    self.assertEqual([task["id"] for task in result], [2, 3])
```

Confirm that the regression fails against the original implementation. Fix the selection order, rerun the tests, and inspect the diff. Preserve input order, the fixture, and the existing output format.

## 2. Add optional priority sorting

Request a `--sort priority` option with these requirements:

- Preserve input order by default.
- When sorting is requested, filter by status, sort by ascending numeric priority, then apply the limit.
- Preserve the relative order of tasks with equal priority.
- Leave the input list unchanged.
- Keep the existing tab-separated output format.

The fixture guarantees a numeric priority on every record. Define additional validation requirements separately if you adapt this tool to arbitrary input.

Use the [prompt collection](prompts.md) and project instructions to keep the task bounded. Review the result against each requirement before accepting it.

## 3. Compare with the completed example

From the repository root:

```bash
cd examples/completed
python -m unittest -v
python taskboard.py tasks.json --status open --limit 2
python taskboard.py tasks.json --status open --sort priority --limit 2
```

The completed suite contains 15 tests. The first CLI command selects:

```text
2	open	2	Fix login error
3	open	1	Review release notes
```

The command with priority sorting selects:

```text
3	open	1	Review release notes
4	open	1	Audit dependencies
```

The tests cover the filtering regression, ordering, stable ties, combined filtering and sorting with a limit, empty results, selection argument validation, and preservation of input data. The fixture and CLI output are small enough to inspect directly.

## What this example assumes

Every task has an integer ID, a title, an `open` or `done` status, and a numeric priority. The code trusts that record structure. It does not implement general JSON schema validation, production file error handling, persistence, or authentication.

The original defect is intentional. A passing baseline illustrates a missing test case. These files are instructional fixtures, not a benchmark of Codex performance or a transcript of a recorded IDE session.

## License

The companion code and documentation are available under the [MIT license](LICENSE). The license covers this repository's files; it does not grant rights to the separate IceWalkers article, OpenAI branding, or third-party material linked by the guide.
