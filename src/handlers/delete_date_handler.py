from ..repositories.date_repository import DateRepository
from ..utils.id_parser import IdParser

class DeleteDateHandler:
    def __init__(self, date_id):
        self.conn = DateRepository()
        self.id = IdParser(date_id)

    def delete_date(self):
        query_response = self.conn.delete_one(self.id.id_to_object())

        if not query_response.deleted_count:
            return {"message": "Id not found", "data": {}}

        return self._handle_query_response()

    def _handle_query_response(self):
        return {"deletedId": self.id.object_to_id()["id"]}, 200
