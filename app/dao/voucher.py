from . import DAO
from ..db import mongo

class VoucherDAO(DAO):

    def __init__(self, collection_name='vouchers'):
        self.collection = mongo.db[collection_name]
        super().__init__(self.collection)
