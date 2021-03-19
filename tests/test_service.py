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

voucher1 = {
    '_id': 1,
    'type': "shipping",
    'code': "#FRETEGRATIS",
    'amount': 0,
    'available': True
}

def test_get_product(client):
    c = client

    product1 = {
        'id': 1,
        'name': "Apple",
        'price': 10.3,
        'available': 10
    }

    product2 = {
        'id': 1,
        'name': "Banana",
        'price': 10.3,
        'available': 10
    }

    response1 = c.post('/products', json=product1)
    response2 = c.post('/products', json=product2)

    json_data = response1.get_json()

    assert response1.status_code == 201
