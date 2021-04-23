from flask_restful import Resource, reqparse
from tracing import init_tracer
from ..dao.voucher import VoucherDAO

_dao = VoucherDAO()

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True)
parser.add_argument('code', type=str, required=True)
parser.add_argument('amount', type=int, required=True)
parser.add_argument('available', type=bool, required=True)

tracing = init_tracer('voucher route')


class VoucherRoute(Resource):
    @tracing.trace('get voucher')
    def get(self, _id):
        return _dao.get(_id)

    @tracing.trace('put voucher')
    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    @tracing.trace('delete voucher')
    def delete(self, _id):
        return _dao.delete(_id)


class VoucherListRoute(Resource):
    @tracing.trace('get vouchers')
    def get(self):
        return _dao.get_all()

    @tracing.trace('post vouchers')
    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
