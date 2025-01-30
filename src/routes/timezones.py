from flask_restx import Resource, Namespace
from ..handlers.timezones_handler import TimezonesHandler

api = Namespace('timezones', description='timezones route')

@api.route('')
class Timezones(Resource):
    def get(self):
        timezones_handler = TimezonesHandler()
        return timezones_handler.timezones()
