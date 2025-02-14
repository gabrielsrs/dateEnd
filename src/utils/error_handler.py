from werkzeug.exceptions import HTTPException

class ErrorHandler:
    def __init__(self, error):
        self.error = error

    def __call__(self, *args, **kwds):
        if isinstance(self.error, HTTPException):
            if self.error.code == 404:
                return {
                    "code": 404, 
                    "message": "Resource not found",
                    "error": str(self.error),
                }, 404

            if self.error.code == 400:
                return {
                    "code": 404, 
                    "message": self.error.description or "Invalid request",
                    "error": str(self.error),
                }, 404

            return {
                "code": self.error.code, 
                "message": self.error.description,
                "error": str(self.error),
            }

        return {
            "message": "An unexpected error occurred",
            "error": str(self.error),
        }, 500
