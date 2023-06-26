import coreapi


def send(usrname, passwrd, name, owner, quantity, cost, status, bid_type):
    # Initialize a client & load the schema document
    auth = coreapi.auth.BasicAuthentication(username=usrname, password=passwrd)
    client = coreapi.Client(auth=auth)
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["orders", "orders", "create"]
    params = {
        "name": name,
        "owner": owner,
        "quantity": quantity,
        "cost": cost,
        "status": status,
        "bid_type": bid_type,
    }

    try:
        # Perform the API request
        result = client.action(schema, action, params=params)

        # JSON response output
        result = dict(result)
        print(f"Order creation successful. JSON response:\n{result}")
    except Exception as e:
        print(f"Order creation failed. Error message: {str(e)}")


def test():
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    # Define different sets of test data
    test_data = [
        {
            "name": "TestProduct1",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "Test Product 2",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "Test-Product-3",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "Test_Product_4",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "Test!Product!5",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "6",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": 7,
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct9",
            "owner": "1",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct10",
            "owner": "one",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct11",
            "owner": "",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct12",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct13",
            "owner": 1,
            "quantity": "ten",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct14",
            "owner": 1,
            "quantity": "",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct15",
            "owner": 1,
            "quantity": 10,
            "cost": "100",
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct16",
            "owner": 1,
            "quantity": "10",
            "cost": "hundred",
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct17",
            "owner": 1,
            "quantity": "10",
            "cost": "",
            "status": 1,
            "bid_type": 1,
        },
        {
            "name": "TestProduct18",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 4,
            "bid_type": 1,
        },
        {
            "name": "TestProduct19",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": "1",
            "bid_type": 1,
        },
        {
            "name": "TestProduct20",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": "one",
            "bid_type": 1,
        },
        {
            "name": "TestProduct21",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": "",
            "bid_type": 1,
        },
        {
            "name": "TestProduct22",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": 3,
        },
        {
            "name": "TestProduct23",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "1",
        },
        {
            "name": "TestProduct24",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "one",
        },
        {
            "name": "TestProduct25",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "",
        }
    ]

    print("\n <======================= Order Creation Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(
            username,
            password,
            data["name"],
            data["owner"],
            data["quantity"],
            data["cost"],
            data["status"],
            data["bid_type"],
        )
        print()
    input()


if __name__ == "__main__":
    test()
