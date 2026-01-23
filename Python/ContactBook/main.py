import sqlite3
import json

# name, address, phone number, email, other
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# create the table if it doesn't exist
query = """
CREATE TABLE IF NOT EXISTS ContactBook (
    id INT AUTO INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    address VARCHAR(150),
    phone VARCHAR(19),
    email VARCHAR(100),
    date DATETIME DEFAULT CURRENT_TIMESTAMP,
    other JSON
);
"""

# create table query
cursor.execute(query)

# basic insert query with some missing fields
insert_query = "INSERT INTO ContactBook (name, email) VALUES ('Joe', 'joe@example.com')"
cursor.execute(insert_query)

# select query
select_query = "SELECT * FROM ContactBook WHERE name = 'Joe'"
cursor.execute(select_query)
result = cursor.fetchone()
print(result)

# select all rows in the database
def select_all():
    query = "SELECT * FROM ContactBook"
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
        
# insert a new person
def insert(name, address, phone, email, other):
    other_json = json.dumps(other)
    insert_query = 'INSERT INTO ContactBook (name, address, phone, email, other) VALUES (?, ?, ?, ?, ?)'
    cursor.execute(insert_query, (name, address, phone, email, other_json))
    

# full insert query
name = 'Matteo'
address = '345 ABC Street'
phone = '123 456 7890'
email = 'matteo@example.com'
other = {
    'favorite_sport': 'soccer'
}
insert(name, address, phone, email, other)

select_query = "SELECT * FROM ContactBook WHERE name = 'Matteo'"
cursor.execute(select_query)
result = cursor.fetchone()
print(result)

update_query = "UPDATE ContactBook SET id = 1 WHERE name = 'Joe'"
cursor.execute(update_query)

update_query = "UPDATE ContactBook SET id = 2 WHERE name = 'Matteo'"
cursor.execute(update_query)
select_all()

# delete_query = "DELETE FROM ContactBook WHERE id = 1"
# cursor.execute(delete_query)
# select_all()


# execute many
people = [
    (3, 'John', '123 abc street', '123 456 7890', 'john@example.com'),
    (4, 'Jacob', '456 def street', '234 567 8901', 'jacob@example.com'),
    (5, 'Jonah', '789 ghi street', '345 678 9012', 'jonah@example.com'),
    (6, 'Jorge', '901 jkl street', '624 145 5145', 'jorge@example.com'),
    (7, 'Jonathon', '234 mno street', '314 134 5461', 'johnathon@example.com')
]
insert_query = "INSERT INTO ContactBook (id, name, address, phone, email) VALUES (?, ?, ?, ?, ?)"
cursor.executemany(insert_query, people)
print()
select_all()

# select with like operator
select_with_like = "SELECT * FROM ContactBook WHERE name LIKE 'J%' AND address LIKE '%abc%'"
cursor.execute(select_with_like)
results = cursor.fetchall()
print("\nSelecting with like operator")
for row in results:
    print(row)
    

# CRUD operations
# - CREATE (INSERT), READ (SELECT), UPDATE, DELETE

# insert operation
# def insert(name, address, phone, email, other):
#     insert_query = """INSERT INTO ContactBook (name, address, phone, email, other) 
#                       VALUES (?, ?, ?, ?, ?);"""
#     cursor.execute(insert_query, (name, address, phone, email, other))
#     conn.commit()

# # select all records
# def select_all():
#     select_all = "SELECT * FROM ContactBook;"
#     cursor.execute(select_all)
#     rows = cursor.fetchall()
#     # get column names
#     columns = [description[0] for description in cursor.description]
#     for row in rows:
#         row_string = ''
#         for i in range(len(row)):
#             column_name = columns[i]
#             row_val = row[i]
#             if i < len(row) - 1:
#                 row_string += f'{column_name}: {row_val}, '
#             else:
#                 row_string += f'{column_name}: {row_val}'
#         print(row_string)

# insert(name, address, phone, email, other)
# select_all()

# conn.close()