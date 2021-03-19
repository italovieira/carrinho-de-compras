from flask_restful import Resource, reqparse

from ..models.product import Product
from ..dao.product import ProductDAO

_dao = ProductDAO()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('price', type=float, required=True)
parser.add_argument('available', type=int, required=True)


class ProductRoute(Resource):
    def get(self, _id):
        return _dao.get(_id)

    def put(self, _id):
        args = parser.parser_args()
        return _dao.update(_id, args)

    def delete(self, _id):
        return _dao.delete(_id)


class ProductListRoute(Resource):
    def get(self):
        return _dao.get_all()

    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
