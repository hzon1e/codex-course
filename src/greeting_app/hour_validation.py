def validate_hour(hour: int) -> None:
    """Raise ValueError when *hour* is outside the 24-hour clock range."""
    if hour < 0 or hour > 23:
        raise ValueError("hour must be between 0 and 23")
