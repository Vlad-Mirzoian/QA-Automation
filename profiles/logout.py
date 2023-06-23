import coreapi


def test():
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["profiles", "logout", "create"]
    result = client.action(schema, action)

    # JSON response output
    result = dict(result)
    print(f"JSON response:\n{result}")
    input()


if __name__ == "__main__":
    # Call the test function
    test()
