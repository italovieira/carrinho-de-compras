from flask_restful import Resource, reqparse

from ..models.product import Product


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('name')
parser.add_argument('price')
parser.add_argument('available')

class ProductRoute(Resource):

    def get(self, id):
        product = Product(1, 'Apple', 10.3, 10)
        return product.to_dict()

    def post(self, cnpj):
        args = parser.parse_args()
        product = Product(**args)
        # save product
        return product.serialize(), 201


class ProductListRoute(Resource):

    def get(self):
        products = [Product(1, 'Apple', 10.3, 10),
                    Product(2, 'Banana', 5.3, 3)]
        return [item.to_dict() for item in products]
