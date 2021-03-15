from pymongo import MongoClient

class Mongo:

    def __init__(self, app=None):
        self.db = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        client = MongoClient(app.config['MONGO_URI'])
        self.db = client[app.config['MONGO_DATABASE']]
