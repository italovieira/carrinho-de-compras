from flask import current_app, g
from pymongo import MongoClient


def connect_to_database():
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client[current_app.config['MONGO_DATABASE']]
    return db

def get_db():
    if 'db' not in g:
        g.db = connect_to_database()
    return g.db

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        db.close()
