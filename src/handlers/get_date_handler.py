from ..repositories.date_repository import DateRepository
from ..utils.id_parser import IdParser

class GetDateHandler:
    def __init__(self, date_id):

        self.conn = DateRepository()
        self.id = IdParser(date_id)

    def get_date(self):
        query_response = self.conn.find_one(self.id.id_to_object())

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        query_response.pop("_id")
        return  {**self.id.object_to_id(), **query_response}
