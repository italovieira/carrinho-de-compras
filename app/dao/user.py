from . import DAO

class UserDAO(DAO):

    def __init__(self, collection_name='user'):
        super().__init__(collection_name)
