# import sqlite3

# class SQLiteConnection:
#     def __init__(self, db_name):
#         self.db_name = db_name

#     def __enter__(self):
#         self.conn = sqlite3.connect(self.db_name)
#         self.cursor = self.conn.cursor()
#         return self.cursor

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.conn.commit()
#         self.conn.close()

# # Usage of the context manager to insert data
# create_table_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);"
# insert_query = "INSERT INTO users (name, age) VALUES (?, ?);"

# with SQLiteConnection('example.db') as cursor:
#     cursor.execute(create_table_query)
#     cursor.execute(insert_query, ('Alice', 30))
#     cursor.execute(insert_query, ('Bob', 25))


import sqlite3
from contextlib import contextmanager

@contextmanager
def sqlite_connection(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn
    try:
        yield cursor
        conn.commit()
    finally:
        conn.close()

# Usage of the context manager to insert data
create_table_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);"
insert_query = "INSERT INTO users (name, age) VALUES (?, ?);"

with sqlite_connection('example.db') as cursor:
    cursor.execute(create_table_query)
    cursor.execute(insert_query, ('Ace', 30))
    cursor.execute(insert_query, ('jay', 25))

