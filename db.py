# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
import sqlite3 as sqlite3
connection = sqlite.connect ("order-db")
cursor = connection.cursor()

def runQuery(query):
    data = cursor.execute(query)
    return data

add_order = f"INSERT INTO orders (order_id, item_name) VALUES ({name}, {quantity}, {pickup})"
read_order_by_id = f"SELECT order_id, item_name, item_quanitity, item_pickup FROM orders WHERE order_id = {order_id_select}"
read_all_orders = f"SELECT * FROM orders"
update_order_by_id = f"UPDATE orders SET item_name = {value} WHERE order_id = {order_id_select}" 
delete_order_by_id = f"DELETE FROM orders WHERE order_id = {order_id_select}"
delete_all_orders = "DELETE * FROM orders"

connection.commit()