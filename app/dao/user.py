from . import DAO
from ..db import mongo

class UserDAO(DAO):
    def __init__(self, collection_name='user'):
        self.collection = mongo.db[collection_name]
        super().__init__(self.collection)
