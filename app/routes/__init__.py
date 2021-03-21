from flask_restful import Api, Resource

from .index import IndexRoute
from .product import ProductRoute
from .product import ProductListRoute
from .voucher import VoucherRoute
from .voucher import VoucherListRoute
from .user import UserRoute
from .user import UserListRoute

api = Api()

def configure_routes(app):
    api.add_resource(IndexRoute, '/')

    api.add_resource(ProductRoute, '/products/<string:_id>')
    api.add_resource(ProductListRoute, '/products')

    api.add_resource(VoucherRoute, '/vouchers/<string:_id>')
    api.add_resource(VoucherListRoute, '/vouchers')

    api.add_resource(UserRoute, '/users/<string:_id>')
    api.add_resource(UserListRoute, '/users')

    api.init_app(app)
