from flask_restful import Resource, reqparse
import bcrypt
from tracing import init_tracer
from ..dao.user import UserDAO

_dao = UserDAO()

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('password', type=str, required=True)

tracing = init_tracer('user route')

class UserRoute(Resource):
    @tracing.trace('get user')
    def get(self, _id):
        return _dao.get(_id)

    @tracing.trace('put user')
    def put(self, _id):
        args = parser.parse_args()
        return _dao.update(_id, args)

    @tracing.trace('delete user')
    def delete(self, _id):
        return _dao.delete(_id)


class UserListRoute(Resource):
    @tracing.trace('get users')
    def get(self):
        return _dao.get_all()

    @tracing.trace('post users')
    def post(self):
        args = parser.parse_args()
        args['password'] = str(bcrypt.hashpw(args['password'].encode('utf-8'), bcrypt.gensalt()))
        return _dao.save(args), 201


class OrderRoute(Resource):
    @tracing.trace('get order')
    def get(self, user_id):
        return _dao.get_orders(user_id)

    @tracing.trace('post order')
    def post(self, user_id):
        args = parser.parse_args()
        return _dao.save_order(user_id), 201
