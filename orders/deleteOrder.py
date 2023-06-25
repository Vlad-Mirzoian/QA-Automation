import coreapi


def send(order_id):
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["orders", "orders", "delete"]
    params = {
        "id": order_id,
    }

    try:
        # Perform the API request
        result = client.action(schema, action, params=params)

        # JSON response output
        result = dict(result)
        print(f"Order deletion successful. JSON response:\n{result}")
    except Exception as e:
        print(f"Order deletion failed. Error message: {str(e)}")


def test():
    test_data = [{"id": 1}, {"id": "1"}, {"id": "one"}, {"id": ""}]
    print("\n <======================= Order Deletion Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(data["id"])
        print()
    input()


if __name__ == "__main__":
    test()
