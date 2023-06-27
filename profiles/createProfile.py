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
        {"username": "john", "email": "mail1@example.com", "password": "password12345678"},
        {"username": "john1", "email": "mail2@example.com", "password": "password12345678"},
        {"username": "john_", "email": "mail3@example.com", "password": "password12345678"},
        {"username": "john-", "email": "mail4@example.com", "password": "password12345678"},
        {"username": "john!", "email": "mail5@example.com", "password": "password12345678"},
        {"username": "1234", "email": "mail6@example.com", "password": "password12345678"},
        {"username": "1234_", "email": "mail7@example.com", "password": "password12345678"},
        {"username": "1234-", "email": "mail8@example.com", "password": "password12345678"},
        {"username": "1234!", "email": "mail9@example.com", "password": "password12345678"},
        {"username": "", "email": "mail10@example.com", "password": "password12345678"},
        {"username": "sam1", "email": "mail11@example", "password": "password12345678"},
        {"username": "sam2", "email": "mail12example.com", "password": "password12345678"},
        {"username": "sam3", "email": "mail13", "password": "password12345678"},
        {"username": "sam4", "email": "", "password": "password12345678"},
        {"username": "sam5", "email": "mail15@example.com", "password": "password_12345678"},
        {"username": "sam6", "email": "mail16@example.com", "password": "password-12345678"},
        {"username": "sam7", "email": "mail17@example.com", "password": "password12345678!"},
        {"username": "sam8", "email": "mail18@example.com", "password": "password"},
        {"username": "sam9", "email": "mail19@example.com", "password": "12345678"},
        {"username": "sam10", "email": "mail20@example.com", "password": "_12345678"},
        {"username": "sam11", "email": "mail21@example.com", "password": "-12345678"},
        {"username": "sam12", "email": "mail22@example.com", "password": "!12345678"},
        {"username": "sam13", "email": "mail23@example.com", "password": ""},
    ]

    print("\n <======================= Profile Creation Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(data["username"], data["email"], data["password"])
        print()
    input()


if __name__ == "__main__":
    test()
