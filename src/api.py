from flask_restx import Api
from .routes.date_route import api as date

api = Api(bundle_errors=True)

api.add_namespace(date, path='/date')