from flask_restful import Resource, reqparse
from ..dao.voucher import VoucherDAO

_dao = VoucherDAO()

parser = reqparse.RequestParser()
parser.add_argument('type', type=str, required=True)
parser.add_argument('code', type=str, required=True)
parser.add_argument('amount', type=int, required=True)
parser.add_argument('available', type=bool, required=True)


class VoucherRoute(Resource):
    def get(self, _id):
        return _dao.get(_id)

    def put(self, _id):
        args = parser.parser_args()
        return _dao.update(_id, args)

    def delete(self, _id):
        return _dao.delete(_id)


class VoucherListRoute(Resource):
    def get(self):
        return _dao.get_all()

    def post(self):
        args = parser.parse_args()
        return _dao.save(args), 201
