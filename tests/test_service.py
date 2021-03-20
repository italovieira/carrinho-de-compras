from flask import Flask, json
from os.path import dirname, isfile, join
from dotenv import load_dotenv
import pytest

# add to the path .env file
_ENV_FILE = join(dirname(__file__), '.env')
# if .env exists read it
if isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)

@pytest.fixture(autouse=True)
def client():
    from app import create_app

    app = create_app('test')
    c = app.test_client()
    return c

def test_get_product(client):
    c = client

    product1 = {
        '_id': 1,
        'name': 'Apple',
        'price': 10.3,
        'available': 10
    }

    product2 = {
        '_id': 2,
        'name': 'Banana',
        'price': 5.3,
        'available': 20
    }

def test_get_voucher(client):
    c = client

    voucher1 = {
        '_id': 1,
        'type': 'shipping',
        'code': '#FRETEGRATIS',
        'amount': 0,
        'available': True
    }

    voucher2 = {
        '_id': 2,
        'type': 'percentual',
        'code': '#30OFF',
        'amount': 30,
        'available': False
    }

    response1 = c.post('/products', json=product1)
    response2 = c.post('/products', json=product2)
    response3 = c.post('/vouchers', json=product1)
    response4 = c.post('/vouchers', json=product2)

    json_data = response1.get_json()
    json_data = response2.get_json()
    json_data = response3.get_json()
    json_data = response4.get_json()

    assert response1.status_code == 201
    assert response2.status_code == 201
    assert response3.status_code == 201
    assert response4.status_code == 201

    products_dict = json_data['products']

    assert products_dict[0] == {
        '_id': 1,
        'name': 'Apple',
        'price': 10.3,
        'available': 10
    }
    assert products_dict[1] == {
         '_id': 2,
        'name': 'Banana',
        'price': 5.3,
        'available': 20
    }

    vouchers_dict = json_data['vouchers']

    assert vouchers_dict[0] == {
       '_id': 1,
        'type': 'shipping',
        'code': '#FRETEGRATIS',
        'amount': 0,
        'available': True
    }
    assert vouchers_dict[1] == {
        '_id': 2,
        'type': 'percentual',
        'code': '#30OFF',
        'amount': 30,
        'available': False
    }