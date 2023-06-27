import coreapi
import json


def send(client, schema, order_id, name, owner, quantity, cost, status, bid_type):
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
        result_dict = json.loads(json.dumps(result))
        print(f"Order creation successful. JSON response:\n{result_dict}")
    except Exception as e:
        print(f"Order creation failed. Error message: {str(e)}")


def test():
    # Initialize a client & load the schema document
    while True:
        try:
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            auth = coreapi.auth.BasicAuthentication(username=username, password=password)
            client = coreapi.Client(auth=auth)
            schema = client.get("http://testsite.light-it.io/docs/")
            break
        except Exception as e:
            print(print(f"Authorization failed. Error message: {str(e)}"))

    # Define different sets of test data
    test_data = [
        {
            "id": 235,
            "name": "TestProduct1",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": "235",
            "name": "TestProduct2",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": "two hundred thirty five",
            "name": "TestProduct3",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": "",
            "name": "TestProduct4",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "Test Product 5",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "Test-Product-6",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "Test_Product_7",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "Test!Product!8",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "9",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": 10,
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "",
            "owner": 34,
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct12",
            "owner": "34",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct13",
            "owner": "thirty four",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct14",
            "owner": "",
            "quantity": 10,
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct15",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct16",
            "owner": 34,
            "quantity": "ten",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct17",
            "owner": 34,
            "quantity": "",
            "cost": 100,
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct18",
            "owner": 34,
            "quantity": 10,
            "cost": "100",
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct19",
            "owner": 34,
            "quantity": "10",
            "cost": "hundred",
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct20",
            "owner": 34,
            "quantity": "10",
            "cost": "",
            "status": 1,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct21",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": 4,
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct22",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": "1",
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct23",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": "one",
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct24",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": "",
            "bid_type": 1,
        },
        {
            "id": 235,
            "name": "TestProduct25",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": 3,
        },
        {
            "id": 235,
            "name": "TestProduct26",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "1",
        },
        {
            "id": 235,
            "name": "TestProduct27",
            "owner": 34,
            "quantity": "10",
            "cost": 100,
            "status": 1,
            "bid_type": "one",
        },
        {
            "id": 235,
            "name": "TestProduct28",
            "owner": 34,
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
            client,
            schema,
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
