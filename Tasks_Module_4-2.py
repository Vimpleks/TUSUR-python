# Задача 1. Случайности не случайны.
print('Задача 1:')

from random import uniform
n = int(input('Введите целое число: '))

def return_list_float_numbers(num: int) -> list:
    list_float_numbers = [uniform(0, num) for i in range(num)]
    return list_float_numbers

print(return_list_float_numbers(n))
print('-------')

# Задача 2. Ленивое объединение
print('Задача 2:')

from itertools import chain
list_one = [1, 2, 5]
list_two = [3, 4]

def join_lists(list_one: list, list_two: list) -> list:
    total_lists = list(chain(list_one, list_two))
    return total_lists

print(join_lists(list_one, list_two))
print('-------')

# Задача 3. Рефакторинг.
print('Задача 3:')

# def responses_creator(item_ids):
#     item_ids = [None] if item_ids is None else item_ids
#
#     responses = []
#     for item_id in item_ids:
#         new_response = dict(item_id=item_id)
#         responses.append(new_response)
#     return responses

def responses_creator(item_ids):
    item_ids = [None] if item_ids is None else item_ids
    return [dict(item_id=item_id) for item_id in item_ids]

print(responses_creator([1, 2, 3]))
print('-------')