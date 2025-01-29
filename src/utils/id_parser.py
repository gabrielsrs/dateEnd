from bson.objectid import ObjectId

class IdParser:
    def __init__(self, date_id):
        self.id = date_id

    def id_to_object(self):
        return {"_id": ObjectId(self.id)}
    
    def object_to_id(self):
        return {"id": str(self.id)}

