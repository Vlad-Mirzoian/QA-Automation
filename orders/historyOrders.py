import coreapi
import json


def send(client, schema):
    # Interact with the API endpoint
    action = ["orders", "order_history", "list"]

    try:
        # Perform the API request
        result = client.action(schema, action)

        # JSON response output
        result_dict = json.loads(json.dumps(result))
        print(f"Listing of closed orders successful. JSON response:\n{result_dict}")
    except Exception as e:
        print(f"Listing of closed orders failed. Error message: {str(e)}")


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

    print("\n <======================= Order History Testing ========================>\n")
    send(client, schema)
    input()


if __name__ == "__main__":
    test()
