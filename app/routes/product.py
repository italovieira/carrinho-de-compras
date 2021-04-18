from flask_restful import Resource, reqparse
from ..dao.product import ProductDAO
from tracing import init_tracer
from decorators import trace

_dao = ProductDAO()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('price', type=float, required=True)
parser.add_argument('available', type=int, required=True)

tracer = init_tracer('product route')

class ProductRoute(Resource):
    @trace(tracer, 'get product')
    def get(self, _id):
        return _dao.get(_id)

    @trace(tracer, 'put product')
    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    @trace(tracer, 'delete product')
    def delete(self, _id):
        return _dao.delete(_id)


class ProductListRoute(Resource):
    @trace(tracer, 'get products')
    def get(self):
        return _dao.get_all()

    @trace(tracer, 'post products')
    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
