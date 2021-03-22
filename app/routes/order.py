from flask_restful import Resource, reqparse
from ..dao.user import UserDAO

_dao = UserDAO()

parser = reqparse.RequestParser()
parser.add_argument('products', type=dict, action='append')
parser.add_argument('voucher_id', type=str, required=True)
parser.add_argument('date', type=str, required=True)

class OrderListRoute(Resource):
    def get(self, user_id):
        return _dao.get_orders(user_id)

    def post(self, user_id):
        args = parser.parse_args()
        return _dao.save_order(user_id, args), 201
