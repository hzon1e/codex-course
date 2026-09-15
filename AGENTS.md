# Project

This repository is a small Python project used to learn
software engineering and Codex workflows.

# Read First

Before making changes, read:

- README.md
- ARCHITECTURE.md

Read relevant files under docs/ when the task affects
documented product behavior or architecture.

# Project Structure

Production code belongs in:

src/greeting_app/

Tests belong in:

tests/

# Engineering Rules

Keep business logic out of test files.

Do not commit secrets or .env files.

Do not add new dependencies unless they are necessary.

Keep changes focused on the requested task.

Avoid unrelated refactoring.

# Validation

Before reporting a coding task as complete, run:

pytest
ruff check .
mypy src

# Definition of Done

A coding task is complete only when:

- the requested behavior is implemented
- relevant tests exist
- all tests pass
- Ruff passes
- mypy passes
- relevant documentation is updated
- no unrelated files were changed

## Review workflow

本專案提供 review-changes Skill，
位於 .agents/skills/review-changes/SKILL.md。

使用者明確啟用此 Skill 時，依其流程進行唯讀變更審查。
審查與修復是不同任務；未獲批准前，不自行修復審查發現的問題。