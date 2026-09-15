# Architecture

## Purpose

Greeting App generates a greeting based on a person's name
and the hour of the day.

## Current Structure

src/greeting_app/core.py

Coordinates validation, resolves the current hour when needed,
and contains the application's greeting logic.

src/greeting_app/name_validation.py

Validates that greeting names are not empty.

src/greeting_app/hour_validation.py

Validates that hours are within the 24-hour clock range.

tests/test_core.py

Contains automated tests for greeting behavior.

## Data Flow

Caller
  ↓
greet(name, hour)
  ↓
Validate name
  ↓
Read the current hour if hour is omitted or explicitly set to None
  ↓
Validate the resolved hour
  ↓
Determine time period
  ↓
Return greeting string

## Design Principles

Business logic belongs in src/greeting_app/.

Tests verify observable behavior.

The current time is read only when the caller omits hour or explicitly
passes None. When the caller provides an integer hour, including 0, the
current time is not read.

`greet()` preserves the validation order of its original implementation:
the name is validated before reading the current time or validating the
hour. Empty names raise `ValueError("name must not be empty")`, and hours
outside 0 through 23 raise
`ValueError("hour must be between 0 and 23")`.
