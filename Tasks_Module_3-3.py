# Задача 1. Не уникальные элементы.
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
list = [x, y, z]
result = [[x, y, z] for x in list for y in list for z in list if x + y - z > n]
print(result)
print('-------')

# Задача 3. Удвоенные нечетные.
print('Задача 3:')

print('-------')

# [Junior] Задача 4. Дешифратор.
print('Задача 4:')

print('-------')

# [Junior+] Задача 5. Возраст привидений
print('Задача 5:')

print('-------')