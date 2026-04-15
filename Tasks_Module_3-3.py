# Задача 1. Не уникальные элементы.
import itertools
from itertools import permutations

print('Задача 1:')
array_numbers = [10, 9, 10, 10, 9, 8]
if array_numbers:
    result = [number for number in array_numbers if array_numbers.count(number) > 1]
    print(result)
else:
    print('Исходный массив пустой')
print('-------')

# Задача 2. Перестановки.
print('Задача 2:')
x = 1
y = 2
z = 4
n = 2
elements = [x, y, z]
result = [[x, y, z] for x in elements for y in elements for z in elements if x + y - z > n]
permutations_elements = itertools.permutations(elements)
print(result)
print(permutations_elements)
print('-------')

# Задача 3. Удвоенные нечетные.
print('Задача 3:')
# n = int(input())
n = 5
numbers = [number * 2 for number in range(n) if number % 2 != 0]
print(numbers)
print('-------')

# [Junior] Задача 4. Дешифратор.
print('Задача 4:')
key = ('....',
   'X..X',
   '.X..',
   '...X')
value = ('xhwc',
   'rsqx',
   'xqzz',
   'fyzr')
password = ''
key_turn = list(key)
for i in range(4):
    password += ''.join(v for k, v in zip(''.join(key_turn), ''.join(value)) if k == 'X')
    key_turn = [''.join(i) for i in zip(*key_turn[::-1])]
print(f'Пароль: {password}')
print('-------')

# [Junior+] Задача 5. Возраст привидений
print('Задача 5:')

print('-------')