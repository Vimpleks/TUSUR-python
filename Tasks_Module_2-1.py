# Задача 1. Среднее
from random import randint
print('Задача 1:')
num_1 = randint(1, 1000)
num_2 = randint(1, 1000)
num_3 = randint(1, 1000)
average = (num_1 + num_2 + num_3) / 3
print(f'Случайные числа: {num_1}, {num_2}, {num_3}')
print(f'Среднее значение случайных чисел: {average}')
print('-------')

# Задача 2. Деление и еще раз деление
print('Задача 2:')
x = randint(1, 1000)
y = randint(1, 1000)
print(f'Случайные числа: {x}, {y}')
print(f'Целочисленное деление x на y: {x // y}')
print(f'Остаток от деления x на y: {x % y}')
print('-------')

# Задача 3. Округление
print('Задача 3:')
x = 14.721
print('{0:.2f}'.format(x))
print('{0:.0f}'.format(x))
print('{0:=011}'.format(x))
print('-------')

# [Junior] Задача 4. Число "наоборот"
print('Задача 4:')
x = 12345
print(f'Целое число: {x}')
str_x = str(x)
if x >= 0:
    print('Число x наоборот:', int(str_x[::-1]))
else:
    print('Число x наоборот:', int(str_x[0] + str_x[:0:-1]))
print('-------')

# [Junior+] Задача 5. Число "наоборот" (усложненное)
print('Задача 5:')
x = -123
int_max = 2 ** 31
int_min = -2 ** 31
print(f'Целое число: {x}')
str_x = str(x)
if x >= 0:
    reversed_x = int(str_x[::-1])
else:
    reversed_x = int(str_x[0] + str_x[:0:-1])
if int_min < reversed_x < int_max:
    print('Число x наоборот:', reversed_x)
else:
    print('Число x наоборот: 0')