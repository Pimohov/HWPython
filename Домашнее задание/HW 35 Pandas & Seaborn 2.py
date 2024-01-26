# Задание №1
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# tips = sns.load_dataset("tips")
#
# sns.histplot(tips['total_bill'], bins=30, color='blue', alpha=0.5, label='Total Bill')
# sns.histplot(tips['tip'], bins=30, color='orange', alpha=0.5, label='Tip')
#
# plt.title('Совмещенные гистограммы')
# plt.xlabel('Сумма')
# plt.ylabel('Частота')
#
# plt.show()

# Задание №2
# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd
#
# data = {
#     'Февраль': [1, 2, 3, 4],
#     'Март': [5, 6, 7, 8],
#     'Апрель': [9, 10, 11, 12],
#     'Май': [13, 14, 15, 16]
# }
#
# df = pd.DataFrame(data)
#
# sns.heatmap(df, annot=True, cmap='viridis')
#
# plt.title('Корреляция между месяцами и пассажирскими перевозками')
# plt.ylabel('Год')
# plt.xlabel('Месяц')
#
# plt.show()

# Задание №3
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# diamonds = sns.load_dataset("diamonds")
#
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='cut', y='price', data=diamonds, palette='viridis')
#
# plt.title('Ящик с усами')
# plt.xlabel('Качество резки')
# plt.ylabel('Цена')
#
# plt.show()





