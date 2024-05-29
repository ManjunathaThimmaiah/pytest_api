import pytest
from api.api_requests import add_to_cart,get_a_cart,delete_a_cart


# Test case for creating and deleting a cart
def test_create_and_delete_cart():
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

    # Validate response code
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

    # Step 2: Delete the created cart
    delete_response_data, delete_status_code = delete_a_cart(created_cart_id)

    # Validate response code
    assert delete_status_code == 200, f"Expected status code 200, but got {delete_status_code}"

    assert delete_response_data, "No data was retrieved for the deleted cart"

    assert delete_response_data['userId'] == payload[
        'userId'], f"Expected userId {payload['userId']}, but got {delete_response_data['userId']}"

    # Validate deletion response
    assert delete_response_data == {}, f"Expected empty response data, but got {delete_response_data}"

    # Step 3: Attempt to retrieve the deleted cart
    retrieved_cart_data, retrieve_status_code = get_a_cart(created_cart_id)

    # Validate response code
    assert retrieve_status_code == 404, f"Expected status code 404 for non-existent cart, but got {retrieve_status_code}"


# Main function to run the end-to-end test
if __name__ == "__main__":
    pytest.main()
