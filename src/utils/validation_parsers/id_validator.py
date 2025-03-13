from functools import wraps
import re
from werkzeug.exceptions import BadRequest

def id_validator(assign):
    """
    A decorator to validate id

    :return: The wrapper function
    """
    DATE_REGEX = re.compile(r"^[a-fA-F0-9]{24}$")

    @wraps(assign)
    def wrapper(*args, **kwargs):
        """
        Validate date id format

        :param: Expected a date_id in kwargs

        :raise BadRequest: If date_id not match with regex

        :return: All args and kwargs
        """
        date_id = kwargs.get('date_id')
        if not DATE_REGEX.match(date_id):
            raise BadRequest("Invalid date Id")
        return assign(*args, **kwargs)
    
    return wrapper
