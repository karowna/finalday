# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data

# Not a complete function, but a suggestion of what to do
def read_by_id(id):
    order_data = db.query(id)
    order = order(order_data)

def runAddOrder():
    name = input("please enter the item name: ")
    quantity = input("please enter the quanitity of the item: ")
    delivery = input("please enter whether you want the item delivered or not: ")
    order = db.add_order
    return name, quantity, delivery

def runReadOrderId()
    id = input("what Id do you want to read?: ")
    order = db.read_by_id

def runReadAll()
    order = read_all_orders

def runUpdateOrderId()
    id = input("what Id do you want to update?: ")
    order = update_order_by_id

def 
    
    
runAddOrder()



  