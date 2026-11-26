# Skills Rules

This file holds the rules for skills in this project. The overall plan is in `plan.md` (sections 1, 5 and 6). This file is the detailed, corrected version of those rules.

---

## 1. General Principles

- **Single purpose**: Each skill does one job (e.g. "read README", "Qwen fine-tune"). A skill does not combine reading, deploying and data preparation.
- **Clear name**: Skill names are lowercase with hyphens (e.g. `readme-oxu`, `qwen-finetune`). The name alone should make clear what the skill does.
- **One-sentence description**: The `description` field of each skill states in one sentence when it should run. It is written in English.
- **Routine work**: Build, test, deploy and data preparation are routine operations and get their own skills.
- **Dangerous operations**: Deletion, `force push` and database changes run only with explicit permission from the user. A skill never starts them on its own initiative.
- **Log**: Every change (date + content) is recorded in the log section at the end of this file.

## 2. File Structure

- Each skill lives in its own folder: `.claude/skills/<skill-name>/SKILL.md`.
- The top of `SKILL.md` has two fields:
  - `name` — the skill name (same as the folder name).
  - `description` — when and why the skill runs (one sentence, in English). Keywords go at the end of this line, e.g. `Keywords: README, oxu`.
- The body of the skill is a step-by-step guide: what is read, which command runs, what is checked, and how the result is presented.

## 3. Keywords

- Each skill has a keyword list (1–3 words, specific). Keywords are written at the end of the `description` field (see section 2).
- When a keyword appears in the user's request, the matching skill runs.
- The same keyword never belongs to two different skills.
- When keywords change, the change is recorded in the log section.

## 4. Security

- Deletion (`rm -rf`, `Remove-Item -Recurse`), `git reset --hard`, `git push --force`, `git clean` and database changes run only with explicit permission.
- Secret files (`.env`, `credentials.json`, `.claude/settings.local.json`) are not printed by a skill and are never committed.
- Git commit and push run only with permission. Direct changes on the `main` branch first require opening a new branch.
- When a skill is unsure, it stops and asks the user; it does not guess and take risks.

## 5. Skill List

There are no skills in the project yet. The planned skills are below (not created yet):

| Skill name | Purpose | Keywords | Status |
|---|---|---|---|
| `readme-oxu` | Read the README of the `readme_reader/` project | README, oxu | Planned |
| `qwen-finetune` | Start the Qwen-VL fine-tuning process | Qwen, fine-tune | Planned |
| `build` | Run the project build | build | Planned |
| `test` | Run tests and report the result | test | Planned |
| `deploy` | Run the deploy process (only with explicit permission) | deploy | Planned |

## 6. Checklist (when creating a new skill)

- [ ] The skill serves a single purpose.
- [ ] The name is lowercase with hyphens, and the purpose is clear from the name.
- [ ] `description` is one English sentence, states when the skill runs, and ends with `Keywords: ...`.
- [ ] Keywords are 1–3 words and do not overlap with another skill.
- [ ] If the skill has a dangerous operation, the permission requirement is written down.
- [ ] Secret files are outside the skill's scope.
- [ ] The skill is added to the list in section 5 and recorded in the log.

---

## 7. Log

| Date | Change |
|---|---|
| 2026-11-26 | File created. The skills rules from `plan.md` were rewritten in detail: file structure, keywords, security, planned skill list and checklist. |
| 2026-11-26 | Review and fix: defined where keywords go in `SKILL.md` (end of the `description` line); added the rule that `description` is written in the file's language; updated the checklist to match. The earlier log line "Istifadəçi → istifadəçi" was wrong (that text is in `plan.md`, not in this file), so it was corrected. |
| 2026-11-26 | Translated the whole file to English. The `description` field rule is now English (previously Azerbaijani). `plan.md` section 6 was updated to match. |
