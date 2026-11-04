# Project instructions

## Project map
- taskboard.py contains the task selection logic and CLI.
- tasks.json is demonstration data.
- test_taskboard.py contains standard-library unittest tests.

## Development
- Use Python 3.11 or newer.
- Run tests with: python -m unittest -v
- Run the CLI with: python taskboard.py tasks.json --status open --limit 2

## Change boundaries
- Preserve stored task data and the default ordering of results.
- Use the Python standard library; discuss new dependencies first.
- Keep changes scoped to the requested behavior.
- Preserve unrelated working-tree changes.

## Completion
- Add a regression test when fixing a reproducible bug.
- Report the commands run and any checks that could not run.
- Summarize behavior changes and remaining limitations.
