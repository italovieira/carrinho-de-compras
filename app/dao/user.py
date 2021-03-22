from bson.objectid import ObjectId
from . import DAO
from ..db import mongo
from .util import serialize

class UserDAO(DAO):
    def __init__(self, collection_name='user'):
        self.collection = mongo.db[collection_name]
        super().__init__(self.collection)

    def get(self, _id):
        item = self.collection.find_one({ '_id': ObjectId(_id) }, { 'orders': 0 })
        return serialize(item)

    def save_order(self, user_id, order: dict):
        result = self.collection.update( { '_id' : ObjectId(user_id) }, { '$push': { 'orders': order }})

    def get_orders(self, user_id):
        return self.collection.find({ '_id': ObjectId(user_id) }, { 'orders': 1 })
