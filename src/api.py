from flask_restx import Api
from .routes.date_route import api as date
from .routes.timezones import api as timezones

api = Api(bundle_errors=True)

api.add_namespace(date, path='/date')
api.add_namespace(timezones, path='/timezones')