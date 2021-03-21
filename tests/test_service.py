from flask import Flask, json
from os.path import dirname, isfile, join
from dotenv import load_dotenv
import pytest

# add to the path .env file
_ENV_FILE = join(dirname(__file__), '.env')
# if .env exists read it
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

from app import create_app
app = create_app('test')
c = app.test_client()

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
    
    #Testando o primeiro produto
    assert saved_product1['name'] == 'Apple'
    assert saved_product1['price'] == 10.3
    assert saved_product1['available'] == 10

    #Testando o segundo produto
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

    #Testando o primeiro voucher
    assert saved_voucher1['type'] == 'shipping'
    assert saved_voucher1['code'] == '#FRETEGRATIS'
    assert saved_voucher1['amount'] == 0
    assert saved_voucher1['available'] == True

    #Testando o segundo voucher
    assert saved_voucher2['type'] == 'percentual'
    assert saved_voucher2['code'] == '#30OFF'
    assert saved_voucher2['amount'] == 30
    assert saved_voucher2['available'] == False

