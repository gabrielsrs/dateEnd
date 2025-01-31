from flask import Flask
from src.api import api
from werkzeug.exceptions import NotFound

app = Flask(__name__)
api.init_app(app)

@app.errorhandler(NotFound)
def not_found(error):
    return {"code": 404, "message": "Resource not found"}, 404

if __name__ == '__main__':
    app.run(debug=True)
