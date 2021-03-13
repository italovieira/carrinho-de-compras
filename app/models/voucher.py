from . import Model

class Voucher(Model):

    def __init__(self, id, type, code, amount, available):
        self.id = id
        self.type = type
        self.code = code
        self.amount = amount
        self.available = available
