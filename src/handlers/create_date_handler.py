from ..services.create_date_service import CreateDateService
from ..repositories.date_repository import DateRepository
from flask import request

from ..utils.id_parser import IdParser

class CreateDateHandler:
    def __init__(self):
        self.conn = DateRepository()
        self.create_date_service = CreateDateService()

        self.id = None

    def create_date(self, create_parser):
        req_data = request.get_json()
        to_create_data = self.create_date_service.create_date(req_data, create_parser)

        query_response = self.conn.insert_one(to_create_data)

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        self.id = IdParser(query_response.inserted_id)
        created_date = self.conn.find_one(self.id.id_to_object())
        created_date.pop("_id")

        return {**self.id.object_to_id(), **created_date}
