# Задание 2
# Сценарий работы:
# 1. Пользователь вводит название файла (обязательно с расширением .csv и разделителем ';').
# 2. Программа выводит названия столбцов, которые были найдены в файле.
# 3. Пользователь выбирает некоторый столбец.
# 4. Программа выводит список уникальных значений из выбранного столбца.
# 5. Пользователь вводит выбранное для фильтрации значение.
# 6. Программа записывает новый файл (в формате .csv) со строками, где выбранный столбец содержит указанное пользователем значение.

import csv
my_delimiter = ','
user_file = input("Укажите название файла с расширением .csv: ")
with open(user_file, encoding="utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=my_delimiter)
    names_column = {}
    print("В файле найдены столбцы:")
    for index, name in enumerate(next(csv_reader), start=1):
        print(f"{index}. {name}")
        names_column[index] = name
user_column = int(input(f"Укажите столбец для фильтрации (введите цифру 1-{len(names_column)}): "))
with open(user_file, encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=my_delimiter)
    unique_column_values = set()
    print(f"Уникальные значения столбца {user_column}:")
    for row in csv_reader:
        unique_column_values.add(row[names_column[user_column]])
    unique_column_values_dict = {}
    for index, element in enumerate(unique_column_values, start=1):
        print(f"{index}. {element}")
        unique_column_values_dict[index] = element
value_filter = int(input(f"Укажите значение для фильтрации (введите цифру 1-{len(unique_column_values_dict)}): "))
with open(user_file, encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=my_delimiter)
    rows_filter = []
    for row in csv_reader:
        if row[names_column[user_column]] == unique_column_values_dict[value_filter]:
            rows_filter.append(row)
filter_file = f"{user_file.rstrip('.csv')}-{names_column[user_column]}-{unique_column_values_dict[value_filter]}.csv"
with open(filter_file, "w", encoding="utf-8", newline='') as csv_file:
    csv_writer = csv.DictWriter(csv_file, delimiter=my_delimiter, fieldnames=(list(names_column.values())))
    csv_writer.writeheader()
    csv_writer.writerows(rows_filter)