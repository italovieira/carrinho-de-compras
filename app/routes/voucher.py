from flask_restful import Resource, reqparse
from ..dao.voucher import VoucherDAO
from tracing import init_tracer
from decorators import trace

_dao = VoucherDAO()

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True)
parser.add_argument('code', type=str, required=True)
parser.add_argument('amount', type=int, required=True)
parser.add_argument('available', type=bool, required=True)

tracer = init_tracer('voucher route')


class VoucherRoute(Resource):
    @trace(tracer, 'get voucher')
    def get(self, _id):
        return _dao.get(_id)

    @trace(tracer, 'put voucher')
    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    @trace(tracer, 'delete voucher')
    def delete(self, _id):
        return _dao.delete(_id)


class VoucherListRoute(Resource):
    @trace(tracer, 'get vouchers')
    def get(self):
        return _dao.get_all()

    @trace(tracer, 'post vouchers')
    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
