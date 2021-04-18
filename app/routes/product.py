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
    def get(self, _id):
        return _dao.get(_id)

    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    def delete(self, _id):
        return _dao.delete(_id)


class ProductListRoute(Resource):
    @trace(tracer, 'get products')
    def get(self):
        return _dao.get_all()

    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
