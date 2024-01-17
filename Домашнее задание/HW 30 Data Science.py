# Задание №1
# import csv
#
# def filter_csv(csv_file_path):
#     with open(csv_file_path, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             if row['Name'].startswith('A') :
#                 print(row)
#
# csv_file_path = 'data.csv'
#
# filter_csv(csv_file_path)

# Задание №2
# import csv
#
# def filter_csv(csv_file_path):
#     with open(csv_file_path, 'r', newline='') as file:
#         csv_reader = csv.DictReader(file)
#         for row in csv_reader:
#             if row['Book'].startswith('A'):
#                 print(row)
#
# def add_book(csv_file_path, book, author, year):
#     with open(csv_file_path, 'a', newline='') as file:
#         fieldnames = ['Book', 'Author', 'Year']
#         csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
#         csv_writer.writerow({'Book': book, 'Author': author, 'Year': year})
#
# csv_file_path = 'books.csv'
#
# add_book(csv_file_path, '1984', 'Джордж Оруэлл', '1949')
#
# filter_csv(csv_file_path)

