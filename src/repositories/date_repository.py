from ..config.db_connection import create_conn

class DateRepository:
    """Query methods from database"""
    
    def __init__(self):
        """Initiate database connection"""
        self.conn = create_conn()

    def find_one(self, query_filter):
        """
        Get one document from given id

        :param query_filter: Id for filter document

        :return: Document found or None
        """
        query_response = self.conn.find_one(query_filter)

        return query_response

    def insert_one(self, data):
        """
        Insert one document in database

        :param data: Object with dictionary data to insert

        :return: InsertOneResult object with document id created
        """
        query_response = self.conn.insert_one(data)

        return query_response

    def update_one(self, query_filter, data):
        """
        Update one document from a given id

        :param query_filter: Id from document to update
        :param data: Dictionary data to update 

        :return: UpdateResult Object that have updated document information
        """
        query_response = self.conn.update_one(query_filter, {"$set": data})

        return query_response

    def delete_one(self, query_filter):
        """
        Delete one document from a given id

        :param query_filter: Id from document to delete

        :return: DeleteResult Object that have delete information
        """
        query_response = self.conn.delete_one(query_filter)

        return query_response
