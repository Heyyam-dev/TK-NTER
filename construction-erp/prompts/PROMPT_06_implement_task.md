# PROMPT 06 — Implement One Approved Task

> **Nə vaxt:** plan təsdiqləndikdən sonra. "Bütün proqramı yaz" əvəzinə hər dəfə yalnız **bir** tapşırıq seçilir.
> **Nümunə:** `RPT-001` (Excel) bitmədən `RPT-002` (Word) hesabatına keçilmir.

---

## Read

- PROJECT.md
- plan.md
- ARCHITECTURE.md
- DATA_MODEL.md
- DATABASE_SCHEMA.md
- SECURITY.md, if available
- The specific task and its dependencies

## Task

Implement only the following approved task:

```text
TASK_ID: [INSERT TASK ID]
```

## Before coding

1. Confirm the task exists in plan.md.
2. Verify that its dependencies are complete.
3. Inspect the existing repository and relevant files.
4. Identify the exact files that need to be created or modified.
5. Check compatibility with the existing architecture.
6. Report blockers before making changes.

## During implementation

- Follow the approved technology stack.
- Keep the change limited to the task scope.
- Preserve existing behaviour unless the task explicitly changes it.
- Keep the UI responsive: no long-running work (data loading, report export) on the GUI thread.
- Keep UI code separate from data and report-generation logic.
- Use parameterised database queries wherever the app touches a database.
- Never hardcode secrets or absolute local paths.
- Handle empty data, missing files and export errors with a clear message, not a crash.
- Make sure Azerbaijani characters (ə, ı, ö, ü, ş, ç, ğ) render correctly in UI and in Excel/Word/PDF output.
- Avoid unrelated refactoring.
- Do not overwrite unrelated files.
- Do not claim that a test passed unless it was actually executed.

## After implementation

1. Run the relevant automated tests.
2. Report the exact commands executed and their results.
3. Explain any failed or unexecuted tests.
4. Review security and data-integrity implications.
5. List all changed files.
6. Compare the implementation against the task's acceptance criteria.
7. Update the task status in plan.md only when completion is supported by evidence.

## Rules

- If a requirement is ambiguous or a dependency is incomplete, **stop and report** the issue rather than inventing a solution.
- **Do not begin the next task** until the current task has been reviewed and approved.
