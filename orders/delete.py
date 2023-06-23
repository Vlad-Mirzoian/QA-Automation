import coreapi


def test(orid):
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["orders", "orders", "delete"]
    params = {
        "id": orid,
    }
    result = client.action(schema, action, params=params)

    # JSON response output
    result = dict(result)
    print(f"JSON response:\n{result}")
    input()


if __name__ == "__main__":
    # Enter the input data
    order_id = input("Order id: ")

    # Call the test function
    test(order_id)
