# import sqlite3
#
# db_path = 'my.db'
#
# try:
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()
#
#     try:
#         create = '''
#         CREATE TABLE IF NOT EXISTS Users (
#             id INTEGER PRIMARY KEY,
#             username TEXT,
#             email TEXT
#         )
#         '''
#         cursor.execute(create)
#         conn.commit()
#
#         insert_data_query = '''
#         INSERT INTO Users (username, email) VALUES (?, ?)
#         '''
#         user = ('user_name', 'user@gmail.com')
#         cursor.execute(insert_data_query, user)
#         conn.commit()
#
#         select_query = '''
#         SELECT * FROM Users
#         '''
#         cursor.execute(select_query)
#
#         print("Содержимое таблицы Users:")
#         for row in cursor:
#             print(row)
#
#     except sqlite3.Error as e:
#         print("Ошибка при выполнении SQL-запроса:", e)
#
# finally:
#     try:
#         conn.close()
#     except sqlite3.Error as e:
#         print("Ошибка при закрытии соединения:", e)


# Пример с ORM
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# Base = declarative_base()
# class User(Base):
#     __tablename__ = 'Users'
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     email = Column(String)
#
# engine = create_engine('sqlite:///my.db', primary_key=True)
#
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
#
# try:
#     new_user = User(username='user_name', email='user@gmail.com')
#     session.add(new_user)
#     session.commit()
#     users = session.query(User).all()
#     print("Содержимое таблицы Users:")
#     for user in users:
#         print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
#
# except Exception as e:
#     print("Ошибка при взаимодействии с базой данных:", e)
#
# finally:
#     session.close()