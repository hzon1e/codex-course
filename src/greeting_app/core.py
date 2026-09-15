from datetime import datetime

from greeting_app.hour_validation import validate_hour
from greeting_app.name_validation import validate_name


def greet(name: str, hour: int | None = None) -> str:
    validate_name(name)

    if hour is None:
        hour = datetime.now().hour

    validate_hour(hour)

    if hour < 12:
        period = "Good morning"
    elif hour < 18:
        period = "Good afternoon"
    else:
        period = "Good evening"

    return f"{period}, {name}!"
