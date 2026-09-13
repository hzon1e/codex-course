from datetime import datetime


def greet(name: str, hour: int | None = None) -> str:
    if hour is None:
        hour = datetime.now().hour

    if hour < 12:
        period = "Good morning"
    elif hour < 18:
        period = "Good afternoon"
    else:
        period = "Good evening"

    return f"{period}, {name}!"