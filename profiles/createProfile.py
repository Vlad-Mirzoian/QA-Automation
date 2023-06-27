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
        {"username": "alan", "email": "example1@mail.com", "password": "password12345678"},
        {"username": "alan1", "email": "example2@mail.com", "password": "password12345678"},
        {"username": "alan_", "email": "example3@mail.com", "password": "password12345678"},
        {"username": "alan-", "email": "example4@mail.com", "password": "password12345678"},
        {"username": "alan!", "email": "example5@mail.com", "password": "password12345678"},
        {"username": "5678", "email": "example6@mail.com", "password": "password12345678"},
        {"username": "5678_", "email": "example7@mail.com", "password": "password12345678"},
        {"username": "5678-", "email": "example8@mail.com", "password": "password12345678"},
        {"username": "5678!", "email": "example9@mail.com", "password": "password12345678"},
        {"username": "", "email": "example10@mail.com", "password": "password12345678"},
        {"username": "alan1", "email": "example@mail", "password": "password12345678"},
        {"username": "alan2", "email": "examplemail.com", "password": "password12345678"},
        {"username": "alan3", "email": "example", "password": "password12345678"},
        {"username": "alan4", "email": "", "password": "password12345678"},
        {"username": "alan5", "email": "example11@mail.com", "password": "password_12345678"},
        {"username": "alan6", "email": "example12@mail.com", "password": "password-12345678"},
        {"username": "alan7", "email": "example13@mail.com", "password": "password12345678!"},
        {"username": "alan8", "email": "example14@mail.com", "password": "password"},
        {"username": "alan9", "email": "example15@mail.com", "password": "12345678"},
        {"username": "alan10", "email": "example16@mail.com", "password": "_12345678"},
        {"username": "alan11", "email": "example17@mail.com", "password": "-12345678"},
        {"username": "alan12", "email": "example18@mail.com", "password": "!12345678"},
        {"username": "alan13", "email": "example19@mail.com", "password": ""},
    ]

    print("\n <======================= Profile Creation Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(data["username"], data["email"], data["password"])
        print()
    input()


if __name__ == "__main__":
    test()
