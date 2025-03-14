from flask_restx import Resource, Namespace
from ..handlers.timezones_handler import TimezonesHandler
from src.utils.response_marshalling.timezones_marchalling import timezones_models, timezones

api = Namespace('Timezones', description='timezones route')

def assign_models(model):
    api.models[model.name] = model

for models in timezones_models:
    assign_models(models)

@api.route('')
class Timezones(Resource):
    """
        Resource for managing timezones.

        Operations:
        - **Read** (`GET /timezones`) → Retrieve timezones.
            :return: A json with contain the timezones, with offset and identifiers
    """
    @api.marshal_with(timezones)
    def get(self):
        """Get all available timezones."""
        timezones_handler = TimezonesHandler()
        return timezones_handler.timezones()
