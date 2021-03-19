from flask import flask, json

from app.api import configure_api

app = create_app('test')

product1 = {
    "id" = 1,  
    "name" = "Apple",
    "price" = 10.3,
    "available" = 10
    }

product2 = {
    "id" = 2,  
    "name" = "Banana",
    "price" = 5.3,
    "available" = 3
    }
voucher1 = {
    "id" = 1,  
    "type" = "shipping",
    "code" = "#FRETEGRATIS",
    "amount" = 0,
    "available" = true
    }
voucher2 = {
    "id" = 2,  
    "type" = "percentual",
    "code" = "#30OFF"
    "amount" = 30,
    "available" = false
    }
voucher3 = {
    "id" = 3,  
    "name" = "fixed",
    "code" = "#10REAIS"
    "amount" = 10,
    "available" = true
    }        

def test_product_sucess():
    response = c.post('products/', product1)
    json_data = json.get_json()
    
    assert response.status_code == 201
    assert json_data['aceito']

def test_get_product():
    response = c.get('/products/1')

    json_data = response.get_json()

    assert response.status_code == 201

    json_data = response.get_json()

    store_dict = json_data['product']
    assert store_dict == {
        "id" = 1,  
        "name" = "Apple",
        "price" = 10.3,
        "available" = 10
    }
