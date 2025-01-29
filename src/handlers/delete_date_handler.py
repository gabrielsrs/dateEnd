from ..repositories.date_repository import DateRepository
from ..utils.id_parser import IdParser

class DeleteDateHandler:
    def __init__(self, date_id):
        self.conn = DateRepository()
        self.id = IdParser(date_id)

    def delete_date(self):
        query_response = self.conn.delete_one(self.id.id_to_object())

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        return {
            "deleted_count": query_response.deleted_count, 
            "deletedId": self.id.object_to_id()
        }
