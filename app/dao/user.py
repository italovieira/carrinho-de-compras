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
        order_id = ObjectId()
        order = { '_id': order_id, **order }
        result = self.collection.update_one( { '_id' : ObjectId(user_id) }, { '$push': { 'orders': order }})
        if result:
            return str(order_id)

    def get_orders(self, user_id):
        result = self.collection.find_one({ '_id': ObjectId(user_id) }, { '_id': 0, 'orders': 1 })
        orders = result['orders'] if 'orders' in result else []
        return [serialize(x) for x in orders]

    def get_order(self, user_id, order_id):
        order = list(self.collection.aggregate([
            { '$match': { '_id' : ObjectId(user_id) }},
            { '$project': {
                'orders': { '$filter': {
                    'input': '$orders',
                    'as': 'item',
                    'cond': {'$eq': ['$$item._id', ObjectId(order_id)]}
                    }}
                }
            }
        ]))

        return serialize(order[0]['orders'][0])

    def get_all(self):
        items = self.collection.find({}, { 'orders': 0 })
        return [serialize(x) for x in items]
