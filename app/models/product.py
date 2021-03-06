from . import Model

class Product(Model):

    def __init__(self, id, name, price, available):
        self.id = id
        self.name = name
        self.price = price
        self.available = available
