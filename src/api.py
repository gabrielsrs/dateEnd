from flask_restx import Api
from werkzeug.exceptions import HTTPException
from collections import OrderedDict

from .routes.date_route import api as date
from .routes.timezones_route import api as timezones

api = Api(bundle_errors=True)

@api.errorhandler(HTTPException)
def http_exception_error_handler(error):
    if hasattr(error, "data"):
        error.data = OrderedDict([
            ("code", error.code),
            ("message", error.data["message"] or "An unexpected error occurred"),
            ("errors", error.data["errors"]),
        ])

        return {
            "code": error.code,
            "message": error.data["message"] or "An unexpected error occurred",
            "error": error.data["errors"],
        }, error.code

    return {
        "code": error.code,
        "message": error.description or "An unexpected error occurred",
        "error": str(error),
    }, error.code

api.add_namespace(date, path='/date')
api.add_namespace(timezones, path='/timezones')
