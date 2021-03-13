from flask_restful import Resource, reqparse

from ..models.voucher import Voucher


parser = reqparse.RequestParser()
parser.add_argument('id', required=True)
parser.add_argument('type')
parser.add_argument('code')
parser.add_argument('amount')
parser.add_argument('available')

class VoucherRoute(Resource):

    def get(self, id):
        voucher = Voucher(1, 'shipping', '#FRETEGRATIS', 0, True)
        return voucher.to_dict()

class VouchersListRoute(Resource):

    def get(self):
        vouchers = [Voucher(1, 'shipping', '#FRETEGRATIS', 0, True),
                    Voucher(2, 'percentual', '#30OFF', 30, False),
                    Voucher(3, 'fixed', '#10REAIS', 10, True)]
        return [item.to_dict() for item in vouchers]
