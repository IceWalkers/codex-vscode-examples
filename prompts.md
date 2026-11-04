# Codex prompts for VS Code

These templates are starting points. Replace file names, behavior, and commands with the facts of your project.

### Understand unfamiliar code

```text
Explain how [operation] flows through this project.
Start from [entry point]. Identify the files and functions involved,
where input is validated, and which state changes.
Separate confirmed behavior from assumptions. Do not edit files.
```

### Investigate a failure

```text
Reproduce [failure] using [command/input].
Inspect the relevant code and tests. Propose the most likely cause
with supporting evidence before implementing a fix.
If reproduction is blocked, report the missing prerequisite.
```

### Implement a bounded change

```text
Implement [behavior] in [area].
Preserve [existing contract] and [unrelated work].
Completion means [observable acceptance criteria].
Add or update relevant tests, run [appropriate checks], and report results.
```

### Review a patch

```text
Review the current diff against [requirements].
Focus on regressions, missing cases, and changes outside scope.
For each finding, identify the location, a triggering input or condition,
and the consequence. Do not edit during this review.
```

### Prepare a handoff

```text
Summarize the goal, settled decisions, changed files, actual verification
results, and remaining work for a fresh chat.
Include relevant paths and commands. Keep proposed checks separate from
completed checks. Exclude secrets and unrelated conversation history.
```
