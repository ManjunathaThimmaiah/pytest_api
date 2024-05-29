import pytest
from api.api_requests import get_cart_order_sort


# Test case for sorting carts
def test_sort_cart():
    # Define sort order
    sort_order = 'desc'

    # Step 1: Get sorted carts
    sorted_carts, sort_status_code = get_cart_order_sort(sort_order)

    # Validate response code
    assert sort_status_code == 200, f"Expected status code 200, but got {sort_status_code}"

    # Validate if data is retrieved
    assert sorted_carts, "No data was retrieved for sorted carts"

    # Validate the order of the carts (assuming each cart has an 'id' field)
    cart_ids = [cart['id'] for cart in sorted_carts]
    sorted_cart_ids = sorted(cart_ids, reverse=(sort_order == 'desc'))

    assert cart_ids == sorted_cart_ids, f"Expected cart IDs to be sorted in {sort_order} order, but got {cart_ids}"


# Main function to run the end-to-end test
if __name__ == "__main__":
    pytest.main()
