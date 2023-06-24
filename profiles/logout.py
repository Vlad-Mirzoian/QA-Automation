import coreapi


def test():
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["profiles", "logout", "create"]
    result = client.action(schema, action)

    try:
        # Perform the API request
        result = client.action(schema, action)

        # JSON response output
        result = dict(result)
        print(f"Logout is successful. JSON response:\n{result}")
    except Exception as e:
        print(f"Logout failed. Error message: {str(e)}")


if __name__ == "__main__":
    # Call the test function
    test()
    input()
