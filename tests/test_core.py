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