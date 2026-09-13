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

# Definition of Done

A coding task is complete only when:

- the requested behavior is implemented
- relevant tests exist
- all tests pass
- relevant documentation is updated
- no unrelated files were changed