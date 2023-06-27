import coreapi
import json


def send(client, schema, order_id):
    # Interact with the API endpoint
    action = ["orders", "orders", "delete"]
    params = {
        "id": order_id,
    }

    try:
        # Perform the API request
        result = client.action(schema, action, params=params)

        # JSON response output
        result_dict = json.loads(json.dumps(result))
        print(f"Order deletion successful. JSON response:\n{result_dict}")
    except Exception as e:
        print(f"Order deletion failed. Error message: {str(e)}")


def test():
    # Initialize a client & load the schema document
    while True:
        try:
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            auth = coreapi.auth.BasicAuthentication(username=username, password=password)
            client = coreapi.Client(auth=auth)
            schema = client.get("http://testsite.light-it.io/docs/")
            break
        except Exception as e:
            print(print(f"Authorization failed. Error message: {str(e)}"))

    test_data = [{"id": 0}, {"id": "1"}, {"id": "one"}, {"id": ""}]
    print("\n <======================= Order Deletion Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(client, schema, ["id"])
        print()
    input()


if __name__ == "__main__":
    test()
