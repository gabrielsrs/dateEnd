from flask_restx import Resource, Namespace

from src.utils.response_marshalling.get_date_marshalling import get_models, get_date
from src.utils.response_marshalling.create_date_marshalling import create_models, created_date
from src.utils.response_marshalling.update_date_marshalling import update_models, updated_date
from src.utils.response_marshalling.delete_date_marshalling import delete_models, deleted_date

from ..handlers.get_date_handler import GetDateHandler
from ..handlers.create_date_handler import CreateDateHandler
from ..handlers.update_date_handler import UpdateDateHandler
from ..handlers.delete_date_handler import DeleteDateHandler

from ..utils.validation_parsers.create_parser import CreateParser
from ..utils.validation_parsers.update_parser import UpdateParser
from ..utils.validation_parsers.id_validator import id_validator

from ..utils.payload_expect.date_payload import date_payload_models, date_payload

api = Namespace('Date', description='date routes', ordered=True)

def assign_models(models):
    """
    Add each model marshalling in api

    :param models: List from each marshalling module

    :return: None
    """
    for model in models:
        api.models[model.name] = model

for module_models in [
    get_models,
    create_models,
    update_models,
    delete_models,
    date_payload_models
]:
    assign_models(module_models)

@api.route('/<string:date_id>')
class DateEnd(Resource):
    """
    Resource for managing date.

    Operations:
    - **Read** (`GET /date/{date_id}`) → Retrieve a date by ID.
        :param get_date: The unique identifier of a date
        :return: A json with contain the date object, with specific characteristics from date

    - **Update** (`PUT /date/{date_id}`) → Update an existing date.
        :param get_date: The unique identifier of a date
        :return: A json with contain the date raw object updated

    - **Delete** (`DELETE /date/{date_id}`) → Remove a date.
        :param get_date: The unique identifier of a date
        :return: A message confirming the date deleted
    """
    
    def __init__(self, api=None, *args, **kwargs):
        """Initializes with an API instance, additional parameters and update parser"""
        super().__init__(api, *args, **kwargs)
        self.update_parser = UpdateParser()

    def _update_parser(self):
        """Get parser related with update"""
        return self.update_parser()

    @api.marshal_with(get_date)
    @id_validator
    def get(self, date_id):
        """Get user details by ID."""
        get_handler = GetDateHandler(date_id)
        return get_handler.get_date()

    @api.marshal_with(updated_date)
    @api.expect(date_payload, validate=False)
    @api.expect(_update_parser)
    @id_validator
    def patch(self, date_id):
        """Update an existing date."""
        update_handler = UpdateDateHandler(date_id)
        return update_handler.update_date(self.update_parser)

    @api.marshal_with(deleted_date)
    @id_validator
    def delete(self, date_id):
        """Delete a specific date."""
        delete_handler = DeleteDateHandler(date_id)
        return delete_handler.delete_date()

@api.route('')
class DateEndPost(Resource):
    """
    Resource for managing creation date.

    Operations:
    - **Create** (`POST /date`) → Add a new date.
        :return: A json with contain the date raw object created
    """
    def __init__(self, api=None, *args, **kwargs):
        """Initializes with an API instance, additional parameters and create parser"""
        super().__init__(api, *args, **kwargs)

        self.create_handler = CreateDateHandler()
        self.create_parser = CreateParser()

    def _create_parser(self):
        """Get parser related with create"""
        return self.create_parser()

    @api.marshal_with(created_date)
    @api.expect(date_payload, validate=False)
    @api.expect(_create_parser)
    def post(self):
        """
        Create a new date.
        In addition required fields, any other field are accepted
        """
        return self.create_handler.create_date(self.create_parser)
