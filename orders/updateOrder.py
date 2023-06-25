import coreapi


def send(order_id, name, owner, quantity, cost, status, bid_type):
    # Initialize a client & load the schema document
    username = 'john1'
    password = 'password12345678'
    auth = coreapi.auth.BasicAuthentication(username=username, password=password)
    client = coreapi.Client(auth=auth)
    schema = client.get("http://testsite.light-it.io/docs/")

    # Interact with the API endpoint
    action = ["orders", "orders", "update"]
    params = {
        "id": order_id,
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
    # Define different sets of test data
    test_data = [
        {
            "id": 1,
            "name": "TestProduct1",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": "1",
            "name": "TestProduct2",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": "one",
            "name": "TestProduct3",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": "",
            "name": "TestProduct4",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "Test Product 5",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "Test-Product-6",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "Test_Product_7",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "Test!Product!8",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "9",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": 10,
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "",
            "owner": 1,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct12",
            "owner": "1",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct13",
            "owner": "one",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct14",
            "owner": "",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct15",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct16",
            "owner": 1,
            "quantity": "ten",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct17",
            "owner": 1,
            "quantity": "",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct18",
            "owner": 1,
            "quantity": 10,
            "cost": "100",
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct19",
            "owner": 1,
            "quantity": "10",
            "cost": "hundred",
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct20",
            "owner": 1,
            "quantity": "10",
            "cost": "",
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct21",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 4,
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct22",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": "1",
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct23",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": "one",
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct24",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": "",
            "bid_type": 1,
        },
        {
            "id": 1,
            "name": "TestProduct25",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": 3,
        },
        {
            "id": 1,
            "name": "TestProduct26",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "1",
        },
        {
            "id": 1,
            "name": "TestProduct27",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "one",
        },
        {
            "id": 1,
            "name": "TestProduct28",
            "owner": 1,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "",
        }
    ]

    print("\n <======================= Order Updating Testing ========================>\n")
    for data in test_data:
        print("Testing with data:", data)
        send(
            data["id"],
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
