from functools import wraps
import re
from werkzeug.exceptions import BadRequest

def id_validator(assign):
    DATE_REGEX = re.compile(r"^[a-fA-F0-9]{24}$")

    @wraps(assign)
    def wrapper(*args, **kwargs):
        date_id = kwargs.get('date_id')
        if not DATE_REGEX.match(date_id):
            raise BadRequest("Invalid date Id")
        return assign(*args, **kwargs)
    return wrapper
