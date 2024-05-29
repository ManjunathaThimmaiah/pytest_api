import requests
from config.config import CART_URL


def add_to_cart(payload):
    response = requests.post(CART_URL, json=payload)
    return response.json(), response.status_code


def get_a_cart(cart_id):
    url = f"{CART_URL}/{cart_id}"
    response = requests.get(url)
    return response.json(), response.status_code


def delete_a_cart(cart_id):
    # Assuming the API has an endpoint /user to create a new user
    response = requests.delete(f"{CART_URL}/{cart_id}")
    return response.json(), response.status_code


def update_cart(cart_id, payload):
    url = f"{CART_URL}/{cart_id}"
    response = requests.put(url, json=payload)
    return response.json(), response.status_code


def get_cart_order_sort(order='desc'):
    response = requests.get(f"{CART_URL}?sort={order}")
    return response.json(), response.status_code
