import coreapi
import json


def send(username, email, password):
    # Initialize a client & load the schema document
    client = coreapi.Client()
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["profiles", "create"]
    params = {
        "username": username,
        "email": email,
        "password1": password,
        "password2": password,
    }

    try:
        # Perform the API request
        result = client.action(schema, action, params=params)

        # JSON response output
        result_dict = json.loads(json.dumps(result))
        print(f"Profile creation successful. JSON response:\n{result_dict}")
    except Exception as e:
        print(f"Profile creation failed. Error message: {str(e)}")


def test():
    # Define different sets of test data
    test_data = [
        {"username": "alan", "email": "mail@example.com", "password": "password12345678"},
        {"username": "alan1", "email": "mail@example.com", "password": "password12345678"},
        {"username": "alan_", "email": "mail@example.com", "password": "password12345678"},
        {"username": "alan-", "email": "mail@example.com", "password": "password12345678"},
        {"username": "alan!", "email": "mail@example.com", "password": "password12345678"},
        {"username": "5678", "email": "mail@example.com", "password": "password12345678"},
        {"username": "5678_", "email": "mail@example.com", "password": "password12345678"},
        {"username": "5678-", "email": "mail@example.com", "password": "password12345678"},
        {"username": "5678!", "email": "mail@example.com", "password": "password12345678"},
        {"username": "", "email": "mail@example.com", "password": "password12345678"},
        {"username": "alan1", "email": "mail@example", "password": "password12345678"},
        {"username": "alan2", "email": "mailexample.com", "password": "password12345678"},
        {"username": "alan3", "email": "mail", "password": "password12345678"},
        {"username": "alan4", "email": "", "password": "password12345678"},
        {"username": "alan5", "email": "mail@example.com", "password": "password_12345678"},
        {"username": "alan6", "email": "mail@example.com", "password": "password-12345678"},
        {"username": "alan7", "email": "mail@example.com", "password": "password12345678!"},
        {"username": "alan8", "email": "mail@example.com", "password": "password"},
        {"username": "alan9", "email": "mail@example.com", "password": "12345678"},
        {"username": "alan10", "email": "mail@example.com", "password": "_12345678"},
        {"username": "alan11", "email": "mail@example.com", "password": "-12345678"},
        {"username": "alan12", "email": "mail@example.com", "password": "!12345678"},
        {"username": "alan13", "email": "mail@example.com", "password": ""},
    ]

    print("\n <======================= Profile Creation Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(data["username"], data["email"], data["password"])
        print()
    input()


if __name__ == "__main__":
    test()
