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
        
        req_data.update(create_parser().parse_args())
        to_create_data = self.create_date_service.create_date(req_data)

        query_response = self.conn.insert_one(to_create_data)

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        self.id = IdParser(query_response.inserted_id)
        created_date = self.conn.find_one(self.id.id_to_object())
        created_date.pop("_id")

        return {
            "code": 201,
            "message": "Date successfully created",
            "data": {**self.id.object_to_id(), **created_date}
        }, 201
