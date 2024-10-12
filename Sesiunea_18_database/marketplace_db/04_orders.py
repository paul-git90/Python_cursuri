"""
Interactiunea cu tabelul orders
"""

# CRUD - ne ajuta sa actualizam, modificam, adaugam, stergem date din DB

import sqlite3
PATH_DB = "marketplace.db"
connection = sqlite3.connect(PATH_DB)
cursor = connection.cursor()

# CREATE ORDER

# # todo pasul 1: crearea comenzii (se poate adauga optional id si valoare id pentru indexare)
# order_query = '''
#     INSERT INTO orders (customer_id, order_date)
#     VALUES (2, "30.02.2024");
# '''
# cursor.execute(order_query)
# connection.commit()
#
# # todo pasul 2: adaugarea produselor in cos
# order_items_query = '''
#     INSERT INTO order_items (order_id, product_id, quantity, total_price)
#     VALUES (?, ?, ?, ?);
# '''
# order_items_list = [(3, 4, 5, 1950), (2, 3, 25, 120.45)]
# cursor.executemany(order_items_query, order_items_list)
# connection.commit()

# todo READ / GET ORDER BY ID
get_order_by_id_and_items_query = '''
    SELECT orders.id, orders.customer_id, orders.order_date, order_items.product_id,
           order_items.quantity, order_items.total_price
    FROM orders
    LEFT JOIN order_items ON orders.id = order_items.order_id
    WHERE orders.id = ?;
'''
print(f"** print pentru a vedea ORDER:")
cursor.execute(get_order_by_id_and_items_query, (3, ))
order_and_items = cursor.fetchall()
print(order_and_items)

# todo READ / GET ALL ORDERS - [tema individuala] - [la fel se poate face pentru *FROM order_items]
print(f"** print pentru a vedea ALL ORDERS:")

cursor.execute('''
    SELECT * FROM orders;
''')
orders = cursor.fetchall()

print(f"** optional print pentru a vedea intreaga lista:\n {orders}\n urmeaza for:")

for order_and_items in orders:
    print(order_and_items)

# # todo UPDATE ORDER
# update_quantity_query = '''
#     UPDATE order_items SET quantity = ?
#     WHERE order_id = ? AND product_id = ?;
# '''
# new_quantity = 6
# order_id = 1
# product_id = 2
# cursor.execute(update_quantity_query, (new_quantity, order_id, product_id))
# connection.commit()
#
# print(f"** print pentru a vedea modificarile:")
# cursor.execute(get_order_by_id_and_items_query, (1,))
# order_and_items = cursor.fetchall()
# print(order_and_items)

# # todo DELETE ORDER
# delete_order_query = '''
#     DELETE FROM orders WHERE id = ?;
# '''
# cursor.execute(delete_order_query, (1, ))
# connection.commit()
