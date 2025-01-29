from ..config.db_connection import create_conn

class DateRepository:
    def __init__(self):
        self.conn = create_conn()

    def find_one(self, query_filter):
        query_response = self.conn.find_one(query_filter)

        return query_response

    def insert_one(self, data):
        query_response = self.conn.insert_one(data)

        return query_response

    def update_one(self, query_filter, data):
        query_response = self.conn.update_one(query_filter, {"$set": data})

        return query_response

    def delete_one(self, query_filter):
        query_response = self.conn.delete_one(query_filter)

        return query_response
