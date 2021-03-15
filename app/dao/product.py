from . import DAO

class ProductDAO(DAO):

    def __init__(self, collection_name='products'):
        super().__init__(collection_name)
