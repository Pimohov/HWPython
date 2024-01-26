# Задание №1
# import pandas as pd
#
# data = {'Name': ['Иван', 'Мария', 'Алексей', 'Екатерина'],
#         'Age': [20, 22, 21, 23],
#         'Gender': ['М', 'Ж', 'М', 'Ж'],
#         'GPA': [3.5, 4.0, 3.2, 3.8]}
#
# df = pd.DataFrame(data)
# print(df)

# Задание №2
# print(df['Name'])
#
# fem_students = df[df['Gender'] == 'Ж']
# print(fem_students)
#
# gpa_student = df[df['GPA'] == df['GPA'].max()]
# print(gpa_student)

# Задание №3
# df['Age'] = df['Age'] + 1
# print(df)
#
# min_age = df['Age'].idxmin()
# df.at[min_age, 'GPA'] = 4.5
# print(df)

# Задание №4
# new_student = {'Name': 'Анна', 'Age': 20, 'Gender': 'Ж', 'GPA': 3.9}
# df = df._append(new_student, ignore_index=True)
# print(df)

# Задание №5
# df['GPA'] = df['GPA'] + 0.5
# print(df)

# Задание №6
# age_sort = df.sort_values(by='Age', ascending=False)
# print(age_sort)
#
# gpa_sort = df.sort_values(by='GPA')
# print(gpa_sort)

# Задание №7
# df.to_csv('students_data.csv', index=False)
