"""Utilities for validating names."""


def validate_name(name: str) -> None:
    """Raise ``ValueError`` when *name* is empty."""
    if name == "":
        raise ValueError("name must not be empty")
