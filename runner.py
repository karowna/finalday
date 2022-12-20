# The runner contains the code to Create a User Interface for the Cafe to interact with
# This 'runs' the code and will interact with the Controller directly

print("""
-------- Welcome to QA Cafe --------

What can we help you with?
1) Add Order
2) Read Order By ID
3) Read All Orders
4) Update Order by ID
5) Delete Order by ID
6) Delete All Orders
""")

order = input("Please select a number: ")

if order == "1":
    runAddOrder()
elif order == "2":
    runReadOrderId()
elif order == "3":
    runReadAll()
elif order == "4":
    runUpdateOrderId()
elif order == "5":
    runDeleteOrderId()
elif order == "6":
    runDeleteAllOrders()
else:
    print("That was not a valid number, please try again")


