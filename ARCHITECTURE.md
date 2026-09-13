# Architecture

## Purpose

Greeting App generates a greeting based on a person's name
and the hour of the day.

## Current Structure

src/greeting_app/core.py

Contains the application's greeting logic.

tests/test_core.py

Contains automated tests for greeting behavior.

## Data Flow

Caller
  ↓
greet(name, hour)
  ↓
Determine time period
  ↓
Return greeting string

## Design Principles

Business logic belongs in src/greeting_app/.

Tests verify observable behavior.

The current time should only be read when the caller does
not explicitly provide an hour.