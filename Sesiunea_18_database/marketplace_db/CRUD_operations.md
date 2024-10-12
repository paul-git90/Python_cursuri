
# CRUD Operations

**CRUD** is an acronym that represents the four fundamental operations that can be performed on data in a database or software application:

## 1. Create
The **create** operation refers to inserting new data into a database or system. In SQL, this is done using the `INSERT` statement. Example: adding a new user to an application.

```sql
INSERT INTO users (username, email) VALUES ('john_doe', 'john@example.com');
```

## 2. Read
The **read** operation refers to retrieving stored data from a database or system. In SQL, this is done using the `SELECT` statement. Example: retrieving information about a product.

```sql
SELECT * FROM users WHERE id = 1;
```

## 3. Update
The **update** operation refers to modifying existing data in a database. In SQL, this is done using the `UPDATE` statement. Example: changing the price of a product.

```sql
UPDATE users SET email = 'newemail@example.com' WHERE id = 1;
```

## 4. Delete
The **delete** operation refers to removing data from a database. In SQL, this is done using the `DELETE` statement. Example: deleting a product that is no longer available.

```sql
DELETE FROM users WHERE id = 1;
```

## Importance of CRUD
CRUD is a fundamental concept in software development and databases as it defines the basic interactions with data. It's an essential part of any application that manipulates information (e.g., web applications, desktop applications, data management systems).

In application development, CRUD is often used to describe the functionality that an application must provide for managing data.

