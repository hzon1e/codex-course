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
    with pytest.raises(ValueError):
        greet("", 8)


@pytest.mark.parametrize("hour", [-1, 24])
def test_invalid_hour_raises_value_error(hour: int) -> None:
    with pytest.raises(ValueError):
        greet("Kelvin", hour)


@pytest.mark.parametrize("hour", range(24))
def test_valid_hours_return_expected_greeting(hour: int) -> None:
    if hour < 12:
        period = "Good morning"
    elif hour < 18:
        period = "Good afternoon"
    else:
        period = "Good evening"

    assert greet("Kelvin", hour) == f"{period}, Kelvin!"

def test_intentional_ci_failure() -> None:
    assert 1 == 2