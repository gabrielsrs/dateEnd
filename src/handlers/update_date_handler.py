from ..services.update_date_service import UpdateDateService
from ..repositories.date_repository import DateRepository
from flask import request
from ..utils.id_parser import IdParser

class UpdateDateHandler:
    def __init__(self, date_id):
        self.conn = DateRepository()
        self.update_date_service = UpdateDateService()
        self.id = IdParser(date_id)

    def update_date(self, update_parser):
        req_data = request.get_json()
        current_data = self.conn.find_one(self.id.id_to_object())
        to_update_data = self.update_date_service.update_date(update_parser, req_data, current_data)

        if isinstance(to_update_data, tuple):
            return {
                "code": 400,
                **to_update_data[0],
                "data": {}
            }, to_update_data[1]

        query_response = self.conn.update_one(self.id.id_to_object(), to_update_data)

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        updated_date = self.conn.find_one(self.id.id_to_object())
        updated_date.pop("_id")

        return {
            "code": 200,
            "message": "Object successfully updated",
            "matched_count": query_response.matched_count, 
            "modified_count": query_response.modified_count,
            "data": {**self.id.object_to_id(), **updated_date}
        }, 200
