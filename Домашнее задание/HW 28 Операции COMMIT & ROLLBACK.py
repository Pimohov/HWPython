# import sqlite3
#
# conn = sqlite3.connect('my.db')
# cursor = conn.cursor()
#
# try:
#     cursor.execute('BEGIN TRANSACTION')
#     cursor.execute('SAVEPOINT my_savepoint1')
#     cursor.execute('UPDATE accounts SET balance = balance - 100 WHERE user_id = 1')
#     cursor.execute('RELEASE my_savepoint1')
#     cursor.execute('SAVEPOINT my_savepoint2')
#     cursor.execute('UPDATE accounts SET balance = balance + 100 WHERE user_id = 2')
#     cursor.execute('RELEASE my_savepoint2')
#
#     conn.execute('COMMIT')
#
# except Exception as e:
#     cursor.execute('ROLLBACK TO my_savepoint2')
#     print(f'Error: {e}')
#
# finally:
#     conn.close()
