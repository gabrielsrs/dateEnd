from ..repositories.date_repository import DateRepository
from ..utils.id_parser import IdParser
from werkzeug.exceptions import NotFound


class DeleteDateHandler:
    """Manage the delete date"""

    def __init__(self, date_id):
        """Initiate the db connection and id to delete"""

        self.conn = DateRepository()
        self.id = IdParser(date_id)

    def delete_date(self):
        """
        Delete a date based in current class id

        :raise NotFound: Query from given id return nothing
        
        :return: Id from deleted object
        """
        
        query_response = self.conn.delete_one(self.id.id_to_object())

        if not query_response.deleted_count:
            raise NotFound("Id not found")

        return self._handle_query_response()

    def _handle_query_response(self):
        """
        Manipulate ID for str format

        :return: Id from self.id
        """
        
        return {"deletedId": self.id.object_to_id()["id"]}, 200
