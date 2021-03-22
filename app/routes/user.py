from flask_restful import Resource, reqparse
import bcrypt
from ..dao.user import UserDAO

_dao = UserDAO()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)

class UserRoute(Resource):
    def get(self, _id):
        return _dao.get(_id)

    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    def delete(self, _id):
        return _dao.delete(_id)


class UserListRoute(Resource):
    def get(self):
        return _dao.get_all()

    def post(self):
        args = parser.parse_args()
        args['password'] = str(bcrypt.hashpw(args['password'].encode('utf-8'), bcrypt.gensalt()))
        return _dao.save(args), 201


class OrderRoute(Resource):
    def get(self, user_id):
        return _dao.get_orders(user_id)

    def post(self, user_id):
        args = parser.parse_args()
        return _dao.save_order(user_id), 201
