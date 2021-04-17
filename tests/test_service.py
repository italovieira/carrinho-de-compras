from flask import Flask, json
import pytest
import logging

from app import create_app
app = create_app('test')
c = app.test_client()

def create_user(name,email,password):
    user = {
        'name': name,
        'email': email,
        'password': password
    }
    response = c.post('/users', json=user)
    id_user = response.get_json()

    return id_user

def create_product(name,price,available):
    product = {
        'name': name,
        'price': price,
        'available': available
    }
    response = c.post('/products', json=product)
    id_product = response.get_json()

    return id_product

def create_voucher(type,code,amount,available):
    voucher = {
        'type': type,
        'code': code,
        'amount': amount,
        'available': available
    }
   
    response = c.post('/vouchers', json=voucher)
    id_voucher = response.get_json()

    return id_voucher

def create_order(products,id_voucher,date,id_user):
    order = {
        'products': products,
        'voucher_id': id_voucher,
        'date': date
    }

    response_order = c.post('/users/' + id_user + '/orders', json=order)
    id_order = response_order.get_json()
   
    return id_order

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

    new_product1 = {
        'name': 'Moranguinho',
        'price': 0.4,
        'available': 1
    }

    updated_count = c.put('/products/' + id_product1, json=new_product1).get_json()
    assert updated_count == 1
    updated_product1 = c.get('/products/' + id_product1).get_json()
    assert updated_product1['name'] == 'Moranguinho'



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

    product1 = {
        'name': 'Pineaple',
        'price': 6.3,
        'available': 20
    }

    product2 = {
        'name': 'Watermelon',
        'price': 3.5,
        'available': 20
    }

    response_product1 = c.post('/products', json=product1)
    response_product2 = c.post('/products', json=product2)

    id_product1 = response_product1.get_json()
    id_product2 = response_product2.get_json()

    saved_product1 = c.get('/products/' + id_product1).get_json()
    saved_product2 = c.get('/products/' + id_product2).get_json()

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
        'products': [{ 'product_id': id_product1, 'amount': 5 }, {'product_id': id_product2, 'amount': 9 }],
        'voucher_id': id_voucher,
        'date': '21/03/2021'
    }

    response_order = c.post('/users/' + id_user + '/orders', json=order)

    assert response_order.status_code == 201

    saved_order = c.get('/users/' + id_user + '/orders').get_json()[0]
    first_product = saved_order['products'][0]

    assert first_product['product_id'] == id_product1
    assert saved_order['voucher_id'] == id_voucher
    assert saved_order['date'] == '21/03/2021'

def test_get_checkout():
    id_user = create_user('italo', 'italo@gmail.com', '123123')
    id_product1 = create_product('Orange','5','10')
    id_product2 = create_product('Grape','20','4')
    id_voucher = create_voucher('fixed','#20GRATIS',20,True)
    products = [{'product_id': id_product1, 'amount': 5 }, {'product_id': id_product2, 'amount': 2}]
    date = '17/04/2021'
    id_order = create_order(products,id_voucher,date,id_user)

    response = c.post('/users/' + id_user + '/orders/' + id_order + '/checkout')
    checkout = response.get_json()

    assert response.status_code == 201

    assert checkout['subtotal'] == 65
    assert checkout['discount'] == 20
    assert checkout['shipping'] == 30
    assert checkout['total'] == 75
