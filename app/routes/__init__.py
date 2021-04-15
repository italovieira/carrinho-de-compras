from flask_restful import Api, Resource

from .index import IndexRoute
from .product import ProductRoute
from .product import ProductListRoute
from .voucher import VoucherRoute
from .voucher import VoucherListRoute
from .user import UserRoute
from .user import UserListRoute
from .order import OrderListRoute
from .checkout import CheckoutRoute

api = Api()

def configure_routes(app):
    api.add_resource(IndexRoute, '/')

    api.add_resource(ProductRoute, '/products/<_id>')
    api.add_resource(ProductListRoute, '/products')

    api.add_resource(VoucherRoute, '/vouchers/<_id>')
    api.add_resource(VoucherListRoute, '/vouchers')

    api.add_resource(UserRoute, '/users/<_id>')
    api.add_resource(UserListRoute, '/users')

    api.add_resource(OrderListRoute, '/users/<user_id>/orders')

    api.add_resource(CheckoutRoute, '/users/<user_id>/orders/<order_id>/checkout')

    api.init_app(app)
