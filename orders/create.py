import coreapi


def test(name, owner, quantity, cost, status, bid_type):
    # Initialize a client & load the schema document
    client = coreapi.Client()
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
    result = client.action(schema, action, params=params)

    # JSON response output
    result = dict(result)
    print(f"JSON response:\n{result}")
    input()


if __name__ == "__main__":
    # Enter the input data
    order_name = input("Product name: ")
    owner_id = input("User id: ")
    amount = input("Quantity of a product: ")
    order_cost = input("Product price: ")
    order_status = input("Order status; choices: 1 - Opened, 2 - Pending, 3 - Closed: ")
    order_bid_type = input("Bid type; choices: 1 - Selling, 2 - Buying: ")

    # Call the test function
    test(order_name, owner_id, amount, order_cost, order_status, order_bid_type)
