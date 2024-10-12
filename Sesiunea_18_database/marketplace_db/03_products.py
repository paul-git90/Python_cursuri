"""
Interactiunea cu tabelul products
"""
# todo CRUD - ne ajuta sa actualizam, modificam, adaugam, stergem date din DB

import sqlite3
PATH_DB = "marketplace.db"
connection = sqlite3.connect(PATH_DB)
cursor = connection.cursor()

# CREATE PRODUCTS

# product_query = '''
#     INSERT INTO products (name, category, price, stock_count, description)
#     VALUES (?, ?, ?, ?, ?);
# '''
# products_list = [
#     ("miere", "apicole", 34.99, 60, "miere poliflora, 1kg"),
#     ("rosii", "legume", 9, 430, "rosii la plasa 1kg, 1kg"),
#     ("nescafe", "cafea", 0.85, 1452, "cafea instant, 15g"),
# ]
# cursor.executemany(product_query, products_list)
# connection.commit()
