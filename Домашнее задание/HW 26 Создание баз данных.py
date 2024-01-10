# Задание №1
# import sqlite3
#
# conn = sqlite3.connect('mydatabase.db')
#
# cursor = conn.cursor()
#
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS Products (
#     ProductID INT PRIMARY KEY,
#     Name TEXT,
#     Price REAL
# );
# '''
#
# insert_data_query = '''
# INSERT INTO Products (ProductID, Name, Price) VALUES
# (1, 'Laptop', 999.99),
# (2, 'Smartphone', 499.99);
# '''
#
# cursor.execute(create_table_query)
# conn.commit()
#
# select_data_query = 'SELECT * FROM Products;'
# cursor.execute(select_data_query)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)


# Задание №2
# import sqlite3
# import csv
#
# conn = sqlite3.connect('mydatabase.db')
#
# cursor = conn.cursor()
#
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS Products (
#     ProductID INT PRIMARY KEY,
#     Name TEXT,
#     Price REAL
# );
# '''
#
# with open('/path/to/datafile.csv', 'r') as csvfile:
#     csvreader = csv.reader(csvfile)
#     next(csvreader)
#     cursor.executemany('INSERT INTO Employees VALUES (?, ?, ?, ?, ?);', csvreader)
#
# conn.commit()
#
# select_data_query = 'SELECT * FROM Products;'
# cursor.execute(select_data_query)
# rows = cursor.fetchall()
# for row in rows:
#     print(row)
#
# conn.close()