from . import Model

class Voucher(Model):

    def __init__(self, id, type, name, amount, available):
        self.id = id
        self.type = type
        self.name = name
        self.amount = amount
        self.available = available
        
