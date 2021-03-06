from flask_restful import Api, Resource

from .index import IndexRoute

api = Api()

def configure_routes(app):
    api.add_resource(IndexRoute, '/')

    api.init_app(app)
