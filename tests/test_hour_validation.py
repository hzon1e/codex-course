import pytest

from greeting_app.hour_validation import validate_hour


@pytest.mark.parametrize("hour", [-1, -24])
def test_hour_below_zero_raises_value_error(hour: int) -> None:
    with pytest.raises(ValueError):
        validate_hour(hour)


@pytest.mark.parametrize("hour", [24, 48])
def test_hour_above_23_raises_value_error(hour: int) -> None:
    with pytest.raises(ValueError):
        validate_hour(hour)


@pytest.mark.parametrize("hour", range(24))
def test_hour_from_zero_through_23_is_valid(hour: int) -> None:
    validate_hour(hour)
