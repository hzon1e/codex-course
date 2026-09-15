from datetime import datetime
from unittest.mock import patch

import pytest

from greeting_app.core import greet


def test_morning_greeting() -> None:
    result = greet("Kelvin", 8)

    assert result == "Good morning, Kelvin!"


def test_afternoon_greeting() -> None:
    result = greet("Kelvin", 14)

    assert result == "Good afternoon, Kelvin!"


def test_evening_greeting() -> None:
    result = greet("Kelvin", 20)

    assert result == "Good evening, Kelvin!"


def test_empty_name_raises_value_error() -> None:
    with pytest.raises(ValueError) as exc_info:
        greet("", 8)

    assert str(exc_info.value) == "name must not be empty"


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_hour_raises_value_error(hour: int) -> None:
    with pytest.raises(ValueError) as exc_info:
        greet("Kelvin", hour)

    assert str(exc_info.value) == "hour must be between 0 and 23"


def test_empty_name_error_precedes_invalid_hour_error() -> None:
    with pytest.raises(ValueError) as exc_info:
        greet("", 24)

    assert str(exc_info.value) == "name must not be empty"


def test_empty_name_is_validated_before_current_time_is_read() -> None:
    with patch("greeting_app.core.datetime") as mock_datetime:
        with pytest.raises(ValueError) as exc_info:
            greet("")

    assert str(exc_info.value) == "name must not be empty"
    mock_datetime.now.assert_not_called()


def test_omitted_hour_uses_current_morning_hour() -> None:
    with patch("greeting_app.core.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2026, 9, 15, 8)

        result = greet("Kelvin")

    assert result == "Good morning, Kelvin!"


def test_none_hour_uses_current_evening_hour() -> None:
    with patch("greeting_app.core.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2026, 9, 15, 20)

        result = greet("Kelvin", None)

    assert result == "Good evening, Kelvin!"


def test_explicit_zero_hour_does_not_read_current_time() -> None:
    with patch("greeting_app.core.datetime") as mock_datetime:
        result = greet("Kelvin", 0)

    assert result == "Good morning, Kelvin!"
    mock_datetime.now.assert_not_called()


def test_name_whitespace_is_not_trimmed() -> None:
    assert greet(" ", 8) == "Good morning,  !"


@pytest.mark.parametrize("hour", range(24))
def test_valid_hours_return_expected_greeting(hour: int) -> None:
    if hour < 12:
        period = "Good morning"
    elif hour < 18:
        period = "Good afternoon"
    else:
        period = "Good evening"

    assert greet("Kelvin", hour) == f"{period}, Kelvin!"
