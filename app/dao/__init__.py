from ..db import mongo
from .util import serialize

class DAO:

    def __init__(self, collection_name):
        self.collection = mongo.db[collection_name]

    def get_all(self):
        items = self.collection.find()
        return [serialize(x) for x in items]

    def get(self, _id):
        item = self.collection.find_one({ '_id': _id })
        return serialize(item)

    def save(self, item: dict):
        result = self.collection.insert_one(item)
        return str(result.inserted_id)

    def delete(self, _id):
        result = self.collection.delete_one({ '_id': _id })
        return result.deleted_count

    def update(self, _id, item: dict):
        result = self.collection.update_one({ '_id': _id }, item)
        return result.modified_count
