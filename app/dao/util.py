def serialize(item: dict):
    item['_id'] = str(item['_id'])
    return item
