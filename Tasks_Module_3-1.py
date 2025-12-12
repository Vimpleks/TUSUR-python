# Задача 1. Последний с четными
print('Задача 1:')
elements = [1, 3, 5]
if elements:
    result = sum(elements[::2]) * elements[-1]
else:
    result = 0
print(result)
print('-------')

# Задача 2. Max-min
print('Задача 2:')
elements = [10.2, -2.2, 0, 1.1, 0.5]
if elements:
    result = round(max(elements) - min(elements), 3)
else:
    result = 0
print(result)
print('-------')

# Задача 3. Max-min
print('Задача 3:')
elements = (-20, -5, 10, 15)
elements_sorted = sorted(elements, key=abs)
print(elements_sorted)
print('-------')