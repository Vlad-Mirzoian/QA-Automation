import coreapi


def send(usrname, passwrd):
    # Initialize a client & load the schema document
    auth = coreapi.auth.BasicAuthentication(username=usrname, password=passwrd)
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


def test():
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    print("\n <======================= Order History Testing ========================>\n")
    send(username, password)
    input()


if __name__ == "__main__":
    test()
