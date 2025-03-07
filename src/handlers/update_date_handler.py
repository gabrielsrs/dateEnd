from ..services.update_date_service import UpdateDateService
from ..repositories.date_repository import DateRepository
from flask import request
from ..utils.id_parser import IdParser

class UpdateDateHandler:
    """Menage the date update"""

    def __init__(self, date_id):
        """Initialize db connection, service that format the data and further id to get date"""

        self.conn = DateRepository()
        self.update_date_service = UpdateDateService()
        self.id = IdParser(date_id)

    def update_date(self, update_parser):
        """
        Update date from current id database.

        :param update_parser: Parser to validate request data

        :return: Formatted object with date object updated
        """

        req_data = request.get_json()
        req_data.update(update_parser().parse_args())

        current_data = self.conn.find_one(self.id.id_to_object())

        to_update_data = self.update_date_service.update_date(req_data, current_data)

        query_response = self.conn.update_one(self.id.id_to_object(), to_update_data)

        return self._handle_query_response(query_response)

    def _handle_query_response(self, query_response):
        """
        Formate the query_response

        :param query_response: Database data from updated date

        :return: Formatted date object response
        """

        updated_date = self.conn.find_one(self.id.id_to_object())
        updated_date.pop("_id")

        return {
            "code": 200,
            "message": "Object successfully updated",
            "matched_count": query_response.matched_count, 
            "modified_count": query_response.modified_count,
            "data": {**self.id.object_to_id(), **updated_date}
        }, 200
