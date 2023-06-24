import coreapi


def test(username, email, password):
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["profiles", "login", "create"]
    params = {
        "username": username,
        "email": email,
        "password": password,
    }

    try:
        # Perform the API request
        result = client.action(schema, action, params=params)

        # JSON response output
        result = dict(result)
        result['user'] = dict(result['user'])
        print(f"Login is successful. JSON response:\n{result}")
    except coreapi.exceptions.ErrorMessage as e:
        print(f"Login failed. Error message: {str(e)}")


if __name__ == "__main__":
    # Define different sets of test data
    test_data = [
        {"username": "john1", "email": "mail2@example.com", "password": "password12345678"},
        {"username": "john", "email": "mail2@example.com", "password": "password12345678"},
        {"username": "", "email": "mail2@example.com", "password": "password12345678"},
        {"username": "john1", "email": "mail2@example.co", "password": "password12345678"},
        {"username": "john1", "email": "", "password": "password12345678"},
        {"username": "john1", "email": "mail2@example.com", "password": "password1234"},
        {"username": "john1", "email": "mail2@example.com", "password": ""},
    ]

    print("\n <========================== Login Testing ===========================>\n\n")
    for data in test_data:
        print("Testing with data:", data)
        test(data["username"], data["email"], data["password"])
        print()
    input()
