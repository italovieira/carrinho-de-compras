from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from tracing import init_tracer
from ..dao.user import UserDAO
from ..dao.product import ProductDAO
from ..dao.voucher import VoucherDAO

user_dao = UserDAO()
product_dao = ProductDAO()
voucher_dao = VoucherDAO()

parser = reqparse.RequestParser()

tracing = init_tracer('checkout route')

class CheckoutRoute(Resource):
    @tracing.trace('post checkout')
    def post(self, user_id, order_id):
        order_dict = user_dao.get_order(user_id, order_id)

        # Subtotal
        subtotal = 0
        quantity = 0
        for item in order_dict['products']:
            product = product_dao.get(item['product_id'])
            subtotal += product['price'] * item['amount']
            quantity += item['amount']


        # Shipping
        shipping = 0
        if subtotal >= 400:
            shipping = 0
        elif quantity <= 10:
            shipping = 30
        else:
            shipping = 50


        # Voucher
        voucher = voucher_dao.get(order_dict['voucher_id'])

        total = 0
        discount = 0
        if voucher['type'] == 'percentual':
            discount = subtotal * voucher['amount'] / 100
        elif voucher['type'] == 'fixed':
            discount = voucher['amount']
        elif voucher['type'] == 'shipping':
            shipping = 0

        total = subtotal + shipping - discount

        return { 'subtotal': subtotal, 'discount': discount, 'shipping': shipping, 'total': total }, 201
