def serialize(item: dict):
    if '_id' in item:
        item['_id'] = str(item['_id'])
    return item
