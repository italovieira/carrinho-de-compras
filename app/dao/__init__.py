from ..db import mongo

class DAO:

    def __init__(self, collection_name):
        self.collection = mongo.db[collection_name]

    def get_all(self):
        return self.collection.find()

    def get(self, id):
        return self.collection.find_one({ '_id': id })

    def save(self, item: dict):
        result = self.collection.insert_one(item)
        return str(result.inserted_id)

    def delete(self, id):
        result = self.collection.delete_one({ '_id': id })
        return result.deleted_count

    def update(self, id, item: dict):
        result = self.collection.update_one({ '_id': id }, item)
        return result.modified_count
