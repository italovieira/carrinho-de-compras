from .util import serialize
from bson.objectid import ObjectId

class DAO:

    def __init__(self, collection):
        self.collection = collection

    def get_all(self):
        items = self.collection.find()
        return [serialize(x) for x in items]

    def get(self, _id):
        item = self.collection.find_one({ '_id': ObjectId(_id) })
        return serialize(item) if item is not None else {}

    def save(self, item: dict):
        result = self.collection.insert_one(item)
        return str(result.inserted_id)

    def delete(self, _id):
        result = self.collection.delete_one({ '_id': ObjectId(_id) })
        return result.deleted_count

    def update(self, _id, item: dict):
        result = self.collection.replace_one({ '_id': ObjectId(_id) }, item)
        return result.modified_count
