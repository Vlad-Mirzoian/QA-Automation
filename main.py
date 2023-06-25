from orders import *
from profiles import *

print("1. Profile Creation test\n2. Login test\n3. Logout test\n4. Order Creation test\n5. Order Updating test\n"
      "6. Order Deletion test\n7. Order History test\n0. Exit")
while True:
    choice = input("Select an operation to perform: ")
    if choice == '1':
        createProfile.test()
    elif choice == '2':
        loginProfile.test()
    elif choice == '3':
        logoutProfile.test()
    elif choice == '4':
        createOrder.test()
    elif choice == '5':
        updateOrder.test()
    elif choice == '6':
        deleteOrder.test()
    elif choice == '7':
        historyOrders.test()
    elif choice == '0':
        break
    else:
        print("There is no such option. Try again!")
