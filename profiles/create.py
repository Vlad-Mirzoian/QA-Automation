import coreapi


def test(username, email, password):
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
    result = client.action(schema, action, params=params)

    # JSON response output
    result = dict(result)
    result['user'] = dict(result['user'])
    print(f"JSON response:\n{result}")
    input()


if __name__ == "__main__":
    # Enter the input data
    usrname = input("Name: ")
    mail = input("Email: ")
    passwrd = input("Password: ")

    # Call the test function
    test(usrname, mail, passwrd)
