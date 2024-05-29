import pytest
from api.api_requests import add_to_cart,get_a_cart


# test
def test_create_and_validate_cart():
    # Define payload
    payload = {
        "userId": 3,
        "date": "2020-02-03",
        "products": [
            {"productId": 5, "quantity": 2},
            {"productId": 1, "quantity": 4}
        ]
    }

    # Step 1: Create a new cart
    created_cart_data, create_status_code = add_to_cart(payload)
    assert create_status_code == 200, f"Expected status code 201, but got {create_status_code}"


    # Validate creation response
    created_cart_id = created_cart_data["id"]
    assert created_cart_data['userId'] == payload[
        'userId'], f"Expected userId {payload['userId']}, but got {created_cart_data['userId']}"
    assert created_cart_data['date'] == payload[
        'date'], f"Expected date {payload['date']}, but got {created_cart_data['date']}"
    assert len(created_cart_data["products"]) == len(payload[
                                                         "products"]), f"Expected {len(payload['products'])} products, but got {len(created_cart_data['products'])}"

    for i in range(len(payload["products"])):
        assert created_cart_data["products"][i]["productId"] == payload["products"][i][
            "productId"], f"Expected productId {payload['products'][i]['productId']} at index {i}, but got {created_cart_data['products'][i]['productId']}"
        assert created_cart_data["products"][i]["quantity"] == payload["products"][i][
            "quantity"], f"Expected quantity {payload['products'][i]['quantity']} for productId {payload['products'][i]['productId']} at index {i}, but got {created_cart_data['products'][i]['quantity']}"

    # Step 2: Retrieve and validate the created cart
    retrieved_cart_data, create_status_code  = get_a_cart(created_cart_id)

    # Since data is not created in real time below test steps will fail
    # Validate retrieved response
    assert create_status_code == 200, f"Expected status code 200, but got {create_status_code}"

    assert retrieved_cart_data, "No data was retrieved for the created cart"
    assert retrieved_cart_data[
               'id'] == created_cart_id, f"Expected cart ID {created_cart_id}, but got {retrieved_cart_data['id']}"
    assert retrieved_cart_data['userId'] == payload[
        'userId'], f"Expected userId {payload['userId']}, but got {retrieved_cart_data['userId']}"
    assert retrieved_cart_data['date'] == payload[
        'date'], f"Expected date {payload['date']}, but got {retrieved_cart_data['date']}"
    assert len(retrieved_cart_data["products"]) == len(payload[
                                                           "products"]), f"Expected {len(payload['products'])} products, but got {len(retrieved_cart_data['products'])}"

    for i in range(len(payload["products"])):
        assert retrieved_cart_data["products"][i]["productId"] == payload["products"][i][
            "productId"], f"Expected productId {payload['products'][i]['productId']} at index {i}, but got {retrieved_cart_data['products'][i]['productId']}"
        assert retrieved_cart_data["products"][i]["quantity"] == payload["products"][i][
            "quantity"], f"Expected quantity {payload['products'][i]['quantity']} for productId {payload['products'][i]['productId']} at index {i}, but got {retrieved_cart_data['products'][i]['quantity']}"


# Main function to run the end-to-end test
if __name__ == "__main__":
    pytest.main()
