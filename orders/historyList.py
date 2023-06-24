import coreapi


def test():
    # Initialize a client & load the schema document
    username = 'john1'
    password = 'password12345678'
    auth = coreapi.auth.BasicAuthentication(username=username, password=password)
    client = coreapi.Client(auth=auth)
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["orders", "order_history", "list"]
    result = client.action(schema, action)

    try:
        # Perform the API request
        result = client.action(schema, action)

        # JSON response output
        print(f"Listing of closed orders successful. JSON response:\n{result}")
    except Exception as e:
        print(f"Listing of closed orders failed. Error message: {str(e)}")


if __name__ == "__main__":
    # Call the test function
    test()
    input()
