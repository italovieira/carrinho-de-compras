from ..db import get_db
from ..model import Product

db = get_db()
__collection = 'products'

collection = db[__collection]

def get_all() -> Product:
    return collection.find()

def get(id: int) -> Product:
    return collection.find({ '_id': id })

def save(item: Product):
    collection.insert_one(item.to_dict())

def delete(id: int):
    collection.delete_one({ '_id': id })

def update(id: int, item: Model):
    collection.update_one({ '_id': id }, item)
