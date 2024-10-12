"""
Interactiunea cu tabelul users
"""

# CRUD - ne ajuta sa actualizam, modificam, adaugam, stergem date din DB

import sqlite3
PATH_DB = "marketplace.db"
connection = sqlite3.connect(PATH_DB)
cursor = connection.cursor()

# CREATE

# todo adauga 1 user metoda 1
# cursor.execute('''
#     INSERT INTO users (username, email, password, first_name, last_name)
#     VALUES ("Dan_Ion.90", "dan@email.com", "pass123", "Ion", "Dan");
# ''')
# connection.commit()

# todo adauga 1 user metoda 2
# user_query = '''
#     INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# '''
# cursor.execute(user_query, ("Daniel_Mihai.92", "mihai_dan92@email.com", "pass922", "Mihai", "Daniel",
#                             "str. Nucilor, nr. 1", "Iasi", "097876", "Romania"))
# connection.commit()

# todo adauga many users
# users_query = '''
#     INSERT INTO users (username, email, password, first_name, last_name, address, city, postal_code, country)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
# '''
# users_to_create_list = [
#     ("Cristian_Bucur", "bucur_cristian@email.com", "qwerty123", "Bucur", "Cristian", "str. Macilor, nr. 23", "Brasov",
#      "092345", "Romania"),
#     ("Artista90", "narcisa_arte@email.com", "54perle", "Artemis", "Narcisa", "str. Nuferilor, nr. 142", "Constanta",
#      "098876", "Romania"),
#     ("Roxi_super_girl", "roxi_mihai95@email.com", "noaptea_mea", "Mihai", "Roxana", "str. Martie, nr. 65", "Tulcea",
#      "097777", "Romania"),
#     ("Bucur_Paul_92", "bucur_eugen@email.com", "marte2", "Bucur", "Paul - Eugen", "str. Septembrie, nr. 78", "Ilfov",
#      "096542", "Romania");
# ]
# cursor.executemany(users_query, users_to_create_list)
# connection.commit()

# todo READ / GET USER BY ID
print(f"** print pentru a vedea BY ID:")

get_by_id_query = '''SELECT * FROM users WHERE id = ?;'''
cursor.execute(get_by_id_query, (1,))
user = cursor.fetchone()
print(user)

# todo READ / GET ALL USERS
print(f"** print pentru a vedea ALL USERS:")

cursor.execute('''
    SELECT * FROM users;
''')
users = cursor.fetchall()

print(f"** optional print pentru a vedea intreaga lista:\n {users}\n urmeaza for:")

for user in users:
    print(user)

# todo READ / GET USER BY USERNAME
print(f"** print pentru a vedea BY USERNAME:")

get_by_username_query = '''SELECT * FROM users WHERE username = ?;'''
cursor.execute(get_by_username_query, ('Roxi_super_girl',))
user = cursor.fetchone()
print(user)

# # todo UPDATE USER by ID (este recomandat by ID)
# print(f"** print pentru a vedea UPDATE USER:")
#
# cursor.execute('''
#     UPDATE users SET username="Popescu_Ion.90"
#     WHERE id = 1;
# ''')
# connection.commit()

# # todo verificare update:
# get_by_id_query = '''SELECT * FROM users WHERE id = ?;'''
# cursor.execute(get_by_id_query, (1,))
# user = cursor.fetchone()
# print(user)

# # todo DELETE USER BY ID (este recomandat by ID)
# print(f"** print pentru a vedea DELETE USER BY ID:")
#
# cursor.execute('''
#     DELETE FROM users
#     WHERE id = 8;
# ''')
# connection.commit()

# # todo verificare delete:
# get_by_id_query = '''SELECT * FROM users WHERE id = ?;'''
# cursor.execute(get_by_id_query, (8,))
# user = cursor.fetchone()
# print(user)

# # CREATE
# # todo adauga din nou un user cu metoda 1 (se va adauga ultimul in lista: next VALUES)
# cursor.execute('''
#     INSERT INTO users (username, email, password, first_name, last_name)
#     VALUES ("Danilov_Ion.90", "dan@email.com", "pass123", "Ion", "Dan");
# ''')
# connection.commit()

# # todo daca doresti sa adaugi un nou user la id:1, unde ai sters inainte alt user(se va adauga in lista fct de VALUES)
# cursor.execute('''
#     INSERT INTO users (id, username, email, password, first_name, last_name)
#     VALUES (1, "Popescu_Ion.90", "ion_pop@email.com", "pass321", "Ion", "Popescu");
# ''')
# connection.commit()
