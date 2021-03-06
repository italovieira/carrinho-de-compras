from flask_restful import Api, Resource

from .index import IndexRoute
from .product import ProductRoute
from .product import ProductListRoute

api = Api()

def configure_routes(app):
    api.add_resource(IndexRoute, '/')

    api.add_resource(ProductRoute, '/products/<id>')
    api.add_resource(ProductListRoute, '/products')

    api.init_app(app)
