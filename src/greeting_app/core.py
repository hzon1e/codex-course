from datetime import datetime


def greet(name: str, hour: int | None = None) -> str:
    if name == "":
        raise ValueError("name must not be empty")

    if hour is None:
        hour = datetime.now().hour

    if hour < 0 or hour > 23:
        raise ValueError("hour must be between 0 and 23")

    if hour < 12:
        period = "Good morning"
    elif hour < 18:
        period = "Good afternoon"
    else:
        period = "Good evening"

    return f"{period}, {name}!"
