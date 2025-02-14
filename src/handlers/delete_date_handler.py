from ..repositories.date_repository import DateRepository
from ..utils.id_parser import IdParser
from werkzeug.exceptions import NotFound


class DeleteDateHandler:
    def __init__(self, date_id):
        self.conn = DateRepository()
        self.id = IdParser(date_id)

    def delete_date(self):
        query_response = self.conn.delete_one(self.id.id_to_object())

        if not query_response.deleted_count:
            raise NotFound("Id not found")

        return self._handle_query_response()

    def _handle_query_response(self):
        return {"deletedId": self.id.object_to_id()["id"]}, 200
