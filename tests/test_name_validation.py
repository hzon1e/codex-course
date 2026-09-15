"""Tests for name validation."""

import pytest

from greeting_app.name_validation import validate_name


def test_empty_name_raises_value_error() -> None:
    with pytest.raises(ValueError):
        validate_name("")


@pytest.mark.parametrize("name", ["Ada", " "])
def test_non_empty_name_does_not_raise(name: str) -> None:
    validate_name(name)
