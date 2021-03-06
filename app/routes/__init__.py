from flask_restful import Api, Resource

from .index import IndexRoute
from .product import ProductRoute
from .product import ProductListRoute
from .voucher import VoucherRoute
from .voucher import VouchersListRoute 

api = Api()

def configure_routes(app):
    api.add_resource(IndexRoute, '/')

    api.add_resource(ProductRoute, '/products/<id>')
    api.add_resource(ProductListRoute, '/products')
    api.add_resource(VoucherRoute, '/vouchers/<id>')
    api.add_resource(VouchersListRoute, '/vouchers')
    api.init_app(app)
