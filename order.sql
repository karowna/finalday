DROP TABLE IF EXISTS orders;
CREATE TABLE orders (order_id INTEGER PRIMARY KEY AUTOINCREMENT, item_name VARCHAR(30) NOT NULL, item_quantity INT NOT NULL, item_pickup BOOLEAN NOT NULL);
INSERT INTO orders (item_name, item quanity, item_delivery) VALUES ('testing', 6 )
