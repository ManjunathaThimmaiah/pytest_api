
### README.md

```markdown
# Cart API Testing

This project is designed to test the Cart API provided by the FakeStore API. It includes methods for creating, updating, retrieving, and deleting carts, as well as sorting carts based on different criteria. The tests are written using the `pytest` framework.

```

# Project structure

```

project_root/
│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── api/
│   ├── __init__.py
│   └── api_requests.py
│
├── tests/
│   ├── __init__.py
│   ├── test_cart_create_and_delete.py
|   ├── test_cart_create_and_validate.py
│   ├── test_cart_create_update_validate.py
│   └── test_cart_fetch_sortOrder_validate.py
│
└── requirements.text


- config: Contains configuration files.
- api: Contains the API request methods encapsulated in a class.
- tests: Contains the test cases for the Cart API.

## Setup

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

```

1. Clone the repository:

```sh
git clone git@github.com:ManjunathaThimmaiah/pytest_api.git
cd pytest_api
```

2. Create and activate a virtual environment:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### Configuration

Ensure that the `config.py` file contains the correct URLs for the API. For this example, the URLs are hardcoded in the `api_requests.py` file.

## Running Tests

You can run the tests using `pytest`. 

### Running Tests from the Console

1. Navigate to the project root directory.

2. Run the following command:

```sh
pytest
```

### Running Tests from an Editor

If you are using an IDE like PyCharm, make sure your IDE is configured to include the project root in the PYTHONPATH.

## API 

The `api_requests.py` provides methods for interacting with the Cart API:

- `add_to_cart(payload)`: Adds a new cart.
- `get_a_cart(cart_id)`: Retrieves a cart by ID.
- `delete_a_cart(cart_id)`: Deletes a cart by ID.
- `update_cart(cart_id, payload)`: Updates a cart by ID.
- `get_cart_order_sort(order='desc')`: Retrieves carts sorted by a specified order.

## Example Test Cases

### `test_create_and_delete.py`

### Scenario 1: Add cart, Get the cart, Delete the cart

1. **Add Cart**
   - Create a new cart with specific user ID, date, and products.
   - Verify the cart creation response status code is `201 Created`.
   - Verify the cart data returned matches the input payload.

2. **Get the Cart**
   - Retrieve the cart using the cart ID from the previous step.
   - Verify the response status code is `200 OK`.
   - Verify the cart data matches the data from the creation step.

3. **Delete the Cart**
   - Delete the cart using the cart ID.
   - Verify the response status code is `200 OK`.

### `test_cart_create_update_validate.py`

### Scenario 1: Add cart, update the cart, Delete the cart

1. **Add Cart**
   - Create a new cart with specific user ID, date, and products.
   - Verify the cart creation response status code is `201 Created`.
   - Verify the cart data returned matches the input payload.

2. **Update the Cart**
   - Update the cart with a new set of products, date, or user ID.
   - Verify the update response status code is `200 OK`.
   - Verify the updated cart data matches the update payload.

3. **Get the Cart to Validate**
   - Retrieve the updated cart using the cart ID.
   - Verify the response status code is `200 OK`.
   - Verify the cart data matches the updated data.

4. **Delete the Cart**
   - Delete the cart using the cart ID.
   - Verify the response status code is `200 OK`.

### `test_cart_fetch_sort_order.py`

1. **Validate the Last in the List**
   - Retrieve the last cart in the sorted list.
   - Verify the cart data matches the expected data.

## Note

**There are failing tests in github action, It is due to the fake server which is not really creating any new data or updating nor deleting records**

## Contributing

If you would like to contribute, please open an issue or submit a pull request.
