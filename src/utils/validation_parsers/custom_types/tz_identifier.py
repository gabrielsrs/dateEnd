from zoneinfo import available_timezones

def tz_identifier(value):
    """
    Validate if passed value is an available timezone

    :param value: A timezone option

    :raise ValueError: If timezone is not valid

    :return: The value passed
    """
    if value not in available_timezones():
        raise ValueError(f'Invalid tz identifier "{value}"')
    return value

tz_identifier.__schema__ = {"type": "string", "format": "tz identifier"}
