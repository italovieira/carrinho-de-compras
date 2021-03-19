from . import DAO

class VoucherDAO(DAO):

    def __init__(self, collection_name='vouchers'):
        super().__init__(collection_name)
