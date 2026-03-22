# Задание 5
# Нужно написать программу для управления остатками товаров. Программа должна уметь читать остатки товаров из CSV,
# группировать их, сохранять историю операций и делать «снимки» базы.
# Описание работы:
# 1. Программа считывает файл inventory.csv (поля: название, категория, количество).
# 2. Выводит в лог информацию при считывании очередного товара.
# 3. Выводит в лог предупреждение, если количество товара <=5.
# 4. Группирует товары в словарь вида {категория:список товаров категории}.
# 5. Сохраняет итоговый словарь в бинарный файл.
# 6. При следующем запуске восстанавливает объект из бинарного файла и выполняет дальнейшую работу с учетом восстановленного словаря.

import logging
import csv
import pickle
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
"{asctime} : {name} : {levelname} : {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M"
)

info_warning_handler = logging.FileHandler('inventory.log', encoding='utf-8')
info_warning_handler.setFormatter(formatter)
logger.addHandler(info_warning_handler)

if os.path.exists('pickle_inventory'):
    with open('pickle_inventory', 'rb') as file:
        inventory_category = pickle.load(file)
else:
    inventory_category = {}

with open('inventory.csv', encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        name = row['название']
        category = row['категория']
        logger.info(f"{row}")
        if int(row['количество']) <= 5:
            logger.warning(f'Количество товара {row['название']} <= 5')
        if category not in inventory_category:
            inventory_category[category] = set()
        inventory_category[category].add(name)

with open('pickle_inventory', 'wb+') as file:
    pickle.dump(inventory_category, file)
