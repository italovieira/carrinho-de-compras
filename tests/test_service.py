from flask import Flask, json
import pytest
import logging

from app import create_app
app = create_app('test')
c = app.test_client()

def test_get_users():
    user = {
        'name': 'erildo',
        'email': 'erildo@ufrn.edu.br',
        'password': '123456789'
    }

    response = c.post('/users', json=user)

    id_user = response.get_json()

    assert response.status_code == 201

    saved_user = c.get('/users/' + id_user).get_json()

    #Testando se o usuario foi cadastrado corretamente no banco
    assert saved_user['name'] == 'erildo'
    assert saved_user['email'] == 'erildo@ufrn.edu.br'

def test_get_product():
    product1 = {
        'name': 'Apple',
        'price': 10.3,
        'available': 10
    }

    product2 = {
        'name': 'Banana',
        'price': 5.3,
        'available': 20
    }

    response1 = c.post('/products', json=product1)
    response2 = c.post('/products', json=product2)

    id_product1 = response1.get_json()
    id_product2 = response2.get_json()

    assert response1.status_code == 201
    assert response2.status_code == 201

    saved_product1 = c.get('/products/' + id_product1).get_json()
    saved_product2 = c.get('/products/' + id_product2).get_json()
    
    #Testando através da rota se o primeiro produto foi cadastrado corretamente no banco
    assert saved_product1['name'] == 'Apple'
    assert saved_product1['price'] == 10.3
    assert saved_product1['available'] == 10

    #Testando através da rota se o segundo produto foi cadastrado corretamente no banco
    assert saved_product2['name'] == 'Banana'
    assert saved_product2['price'] == 5.3
    assert saved_product2['available'] == 20

def test_get_voucher():
    voucher1 = {
        'type': 'shipping',
        'code': '#FRETEGRATIS',
        'amount': 0,
        'available': True
    }

    voucher2 = {
        'type': 'percentual',
        'code': '#30OFF',
        'amount': 30,
        'available': False
    }
   
    response3 = c.post('/vouchers', json=voucher1)
    response4 = c.post('/vouchers', json=voucher2)

    id_voucher1 = response3.get_json()
    id_voucher2 = response4.get_json()
 
    assert response3.status_code == 201
    assert response4.status_code == 201

    saved_voucher1 = c.get('/vouchers/' + id_voucher1).get_json()
    saved_voucher2 = c.get('/vouchers/' + id_voucher2).get_json()

    #Testando através da rota se o primeiro voucher foi cadastrado corretamente no banco
    assert saved_voucher1['type'] == 'shipping'
    assert saved_voucher1['code'] == '#FRETEGRATIS'
    assert saved_voucher1['amount'] == 0
    assert saved_voucher1['available'] == True

    #Testando através da rota se o segundo voucher foi cadastrado corretamente no banco
    assert saved_voucher2['type'] == 'percentual'
    assert saved_voucher2['code'] == '#30OFF'
    assert saved_voucher2['amount'] == 30
    assert saved_voucher2['available'] == False


def test_get_order():
    user = {
        'name': 'italo',
        'email': 'italo@ufrn.edu.br',
        'password': '123456789'
    }

    response_user = c.post('/users', json=user)

    id_user = response_user.get_json()

    saved_user = c.get('/users/' + id_user).get_json()

    product = {
        'name': 'Pineaple',
        'price': 6.3,
        'available': 20
    }

    response_product = c.post('/products', json=product)

    id_product = response_product.get_json()

    saved_product = c.get('/products/' + id_product).get_json()

    voucher = {
        'type': 'percentual',
        'code': '#30OFF',
        'amount': 30,
        'available': True
    }
   
    response_voucher = c.post('/vouchers', json=voucher)
 
    id_voucher = response_voucher.get_json()

    saved_voucher = c.get('/vouchers/' + id_voucher).get_json()
 
    order = {
        'products': [{ 'product_id': id_product, 'amount': 5 }, {'product_id': id_product, 'amount': 9 }],
        'voucher_id': id_voucher,
        'date': '21/03/2021'
    }

    response_order = c.post('/users/' + id_user + '/orders', json=order)
    app.logger.debug(response_order.get_json())

    assert response_order.status_code == 201

    saved_order = c.get('/users/' + id_user + '/orders').get_json()[0]

    app.logger.debug(saved_order)
    app.logger.debug(saved_order['products'])

    first_product = saved_order['products'][0]

    assert first_product['product_id'] == id_product
    assert saved_order['voucher_id'] == id_voucher
    assert saved_order['date'] == '21/03/2021'
