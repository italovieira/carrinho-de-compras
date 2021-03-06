from flask_restful import Resource, reqparse

from ..models.voucher import Voucher


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('type')
parser.add_argument('name')
parser.add_argument('amount')
parser.add_argument('available')

class VoucherRoute(Resource):

    def get(self, id):
        voucher = Voucher(1,'frete', 'freteGratis', 0, True)
        return voucher.to_dict()

    def post(self, cnpj):
        args = parser.parse_args()
        voucher = Voucher(**args)
        # save product
        return voucher.serialize(), 201


class VouchersListRoute(Resource):

    def get(self):
        vouchers = [Voucher(1, 'frete', 'freteGratis', 0, True),
                    Voucher(2, 'percent', '30OFF', 30, True),
                    Voucher(3, 'amount', '10Reais', 10, True)]
        return [item.to_dict() for item in vouchers]
