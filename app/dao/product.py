from . import DAO
from ..db import mongo

class ProductDAO(DAO):

    def __init__(self, collection_name='products'):
        self.collection = mongo.db[collection_name]
        super().__init__(self.collection)
