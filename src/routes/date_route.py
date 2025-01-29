from flask_restx import Resource, Namespace

from ..handlers.get_date_handler import GetDateHandler
from ..handlers.create_date_handler import CreateDateHandler
from ..handlers.update_date_handler import UpdateDateHandler
from ..handlers.delete_date_handler import DeleteDateHandler

from ..utils.validation_parsers.create_parser import CreateParser
from ..utils.validation_parsers.update_parser import UpdateParser
from ..utils.validation_parsers.id_validator import id_validator

api = Namespace('date', description='date routes')

@api.route('/<string:date_id>')
class DateEnd(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)
        self.update_parser = UpdateParser()

    def _update_parser(self):
        return self.update_parser()

    @id_validator
    def get(self, date_id):
        get_handler = GetDateHandler(date_id)
        return get_handler.get_date()

    @api.expect(_update_parser)
    @id_validator
    def patch(self, date_id):
        update_handler = UpdateDateHandler(date_id)
        return update_handler.update_date(self.update_parser)

    @id_validator
    def delete(self, date_id):
        delete_handler = DeleteDateHandler(date_id)
        return delete_handler.delete_date()

@api.route('')
class DateEndPost(Resource):
    def __init__(self, api=None, *args, **kwargs):
        super().__init__(api, *args, **kwargs)

        self.create_handler = CreateDateHandler()
        self.create_parser = CreateParser()

    def _create_parser(self):
        return self.create_parser()

    @api.expect(_create_parser)
    def post(self):
        return self.create_handler.create_date(self.create_parser)
