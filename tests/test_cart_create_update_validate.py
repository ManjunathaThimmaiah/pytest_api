import pytest
from api.api_requests import add_to_cart,get_a_cart, update_cart



# Test case for creating, updating, and validating a cart
def test_create_update_validate_cart():
    # Define initial payload
    initial_payload = {
        "userId": 3,
        "date": "2020-02-03",
        "products": [
            {"productId": 5, "quantity": 2},
            {"productId": 1, "quantity": 4}
        ]
    }

    # Step 1: Create a new cart
    created_cart_data, create_status_code = add_to_cart(initial_payload)

    # Validate response code
    assert create_status_code == 200, f"Expected status code 201, but got {create_status_code}"

    # Validate creation response
    created_cart_id = created_cart_data["id"]
    assert created_cart_data['userId'] == initial_payload[
        'userId'], f"Expected userId {initial_payload['userId']}, but got {created_cart_data['userId']}"
    assert created_cart_data['date'] == initial_payload[
        'date'], f"Expected date {initial_payload['date']}, but got {created_cart_data['date']}"
    assert len(created_cart_data["products"]) == len(initial_payload[
                                                         "products"]), f"Expected {len(initial_payload['products'])} products, but got {len(created_cart_data['products'])}"

    for i in range(len(initial_payload["products"])):
        assert created_cart_data["products"][i]["productId"] == initial_payload["products"][i][
            "productId"], f"Expected productId {initial_payload['products'][i]['productId']} at index {i}, but got {created_cart_data['products'][i]['productId']}"
        assert created_cart_data["products"][i]["quantity"] == initial_payload["products"][i][
            "quantity"], f"Expected quantity {initial_payload['products'][i]['quantity']} for productId {initial_payload['products'][i]['productId']} at index {i}, but got {created_cart_data['products'][i]['quantity']}"

    # Define update payload
    update_payload = {
        "userId": 3,
        "date": "2024-05-27",
        "products": [
            {"productId": 7, "quantity": 2},
            {"productId": 8, "quantity": 4}
        ]
    }

    # Step 2: Update the created cart
    updated_cart_data, update_status_code = update_cart(created_cart_id, update_payload)

    # Validate response code
    assert update_status_code == 200, f"Expected status code 200, but got {update_status_code}"

    # Validate update response
    assert updated_cart_data['userId'] == update_payload[
        'userId'], f"Expected userId {update_payload['userId']}, but got {updated_cart_data['userId']}"
    assert updated_cart_data['date'] == update_payload[
        'date'], f"Expected date {update_payload['date']}, but got {updated_cart_data['date']}"
    assert len(updated_cart_data["products"]) == len(update_payload[
                                                         "products"]), f"Expected {len(update_payload['products'])} products, but got {len(updated_cart_data['products'])}"

    for i in range(len(update_payload["products"])):
        assert updated_cart_data["products"][i]["productId"] == update_payload["products"][i][
            "productId"], f"Expected productId {update_payload['products'][i]['productId']} at index {i}, but got {updated_cart_data['products'][i]['productId']}"
        assert updated_cart_data["products"][i]["quantity"] == update_payload["products"][i][
            "quantity"], f"Expected quantity {update_payload['products'][i]['quantity']} for productId {update_payload['products'][i]['productId']} at index {i}, but got {updated_cart_data['products'][i]['quantity']}"

    # Step 3: Retrieve and validate the updated cart
    retrieved_cart_data, retrieve_status_code = get_a_cart(created_cart_id)

    # Validate response code
    assert retrieve_status_code == 200, f"Expected status code 200, but got {retrieve_status_code}"

    # Validate retrieved response
    assert retrieved_cart_data, "No data was retrieved for the created cart"

    assert retrieved_cart_data[
               'id'] == created_cart_id, f"Expected cart ID {created_cart_id}, but got {retrieved_cart_data['id']}"
    assert retrieved_cart_data['userId'] == update_payload[
        'userId'], f"Expected userId {update_payload['userId']}, but got {retrieved_cart_data['userId']}"
    assert retrieved_cart_data['date'] == update_payload[
        'date'], f"Expected date {update_payload['date']}, but got {retrieved_cart_data['date']}"
    assert len(retrieved_cart_data["products"]) == len(update_payload[
                                                           "products"]), f"Expected {len(update_payload['products'])} products, but got {len(retrieved_cart_data['products'])}"

    for i in range(len(update_payload["products"])):
        assert retrieved_cart_data["products"][i]["productId"] == update_payload["products"][i][
            "productId"], f"Expected productId {update_payload['products'][i]['productId']} at index {i}, but got {retrieved_cart_data['products'][i]['productId']}"
        assert retrieved_cart_data["products"][i]["quantity"] == update_payload["products"][i][
            "quantity"], f"Expected quantity {update_payload['products'][i]['quantity']} for productId {update_payload['products'][i]['productId']} at index {i}, but got {retrieved_cart_data['products'][i]['quantity']}"


# Main function to run the end-to-end test
if __name__ == "__main__":
    pytest.main()
