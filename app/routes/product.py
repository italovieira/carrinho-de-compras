from flask_restful import Resource, reqparse
from tracing import init_tracer
from ..dao.product import ProductDAO

_dao = ProductDAO()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('price', type=float, required=True)
parser.add_argument('available', type=int, required=True)

tracing = init_tracer('product route')

class ProductRoute(Resource):
    @tracing.trace('get product')
    def get(self, _id):
        return _dao.get(_id)

    @tracing.trace('put product')
    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    @tracing.trace('delete product')
    def delete(self, _id):
        return _dao.delete(_id)


class ProductListRoute(Resource):
    @tracing.trace('get products')
    def get(self):
        return _dao.get_all()

    @tracing.trace('post products')
    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
