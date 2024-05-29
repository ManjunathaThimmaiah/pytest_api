
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

### `test_create_update_validate_cart.py`

Tests the creation, updating, and validation of a cart.

### `test_cart_fetch_sort_order.py`

Tests the fetching and sorting of carts.

## Contributing

If you would like to contribute, please open an issue or submit a pull request.

