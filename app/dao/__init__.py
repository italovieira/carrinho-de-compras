from ..db import mongo

class DAO:

    def __init__(self, collection_name):
        self.collection = mongo.db[collection_name]

    def get_all(self):
        return self.collection.find()

    def get(self, id):
        return self.collection.find_one({ '_id': id })

    def save(self, item: dict):
        self.collection.insert_one(item)

    def delete(self, id):
        self.collection.delete_one({ '_id': id })

    def update(self, id, item: dict):
        self.collection.update_one({ '_id': id }, item)
