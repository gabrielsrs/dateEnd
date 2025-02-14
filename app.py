from flask import Flask
from src.api import api
from src.utils.error_handler import ErrorHandler

app = Flask(__name__)
api.init_app(app)

app.register_error_handler(Exception, lambda error: ErrorHandler(error)())

if __name__ == '__main__':
    app.run(debug=True)
