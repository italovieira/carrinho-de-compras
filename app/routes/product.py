from flask_restful import Resource, reqparse

from ..models.product import Product
from ..dao.product import ProductDAO

_dao = ProductDAO()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('price', type=float, required=True)
parser.add_argument('available', type=int, required=True)


class ProductRoute(Resource):

    def get(self, id):
        return _dao.get(id)


class ProductListRoute(Resource):

    def get(self):
        products = [Product(1, 'Apple', 10.3, 10),
                    Product(2, 'Banana', 5.3, 3)]
        return [item.to_dict() for item in products]

    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
