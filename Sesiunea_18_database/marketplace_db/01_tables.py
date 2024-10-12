"""
In cadrul acestui fisier vom crea tabele pentru baza de date
"""

import sqlite3
PATH_DB = "marketplace.db"
connection = sqlite3.connect(PATH_DB)
cursor = connection.cursor()

# Crearea tabelelor

# todo Tabelul users QUERY
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    address TEXT,
    city TEXT,
    postal_code TEXT,
    country TEXT
    );
''')

# todo Tabelul products
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL,
    stock_count INTEGER DEFAULT 0,
    description TEXT
    );
''')

# todo Tabelul orders
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES users(id)
    );
''')

# todo Tabelul order_items
cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER DEFAULT 1,
    total_price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
    );
''')

# # todo DELETE TABLE
# cursor.execute('''
#     DROP TABLE order_items;
# ''')

connection.commit()
connection.close()
