# Задача 1. Градусник.
print('Задача 1:')
temperature_celsius = [39.2, 36.5, 37.3, 37.8]
temperature_fahrenheit = list(map(lambda x: 9 / 5 * x +32, temperature_celsius))
print(temperature_fahrenheit)
print('-------')

# Задача 2. Длинномер.
print('Задача 2:')
elements = ['Tina', 'Raj', 'Tom']
elements_length = list(map(len, elements))
print(elements_length)
print('-------')

# Задача 3. Рефакторинг.
# sentences = ['капитан джек воробей',
#              'капитан дальнего плавания',
#              'ваша лодка готова, капитан']
# cap_count = 0
# for sentence in sentences:
#     cap_count += sentence.count('капитан')
# print(cap_count)
print('Задача 3:')
sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']
cap_count = sum(map(lambda x: x.count('капитан'), sentences))
print(cap_count)
print('-------')

# Задача 4. Возведение в степень.
print('Задача 4:')
x = [2, 3, 4]
y = [10, 11, 12]
exponentiation = list(map(lambda a, b: a ** b, x, y))
print(exponentiation)
print('-------')

# Задача 5. Ленивая функция.
print('Задача 5:')
def generate_elements(n):
    for x in range(n + 1):
        if x == 0:
            yield -10
        elif x % 3:
            yield 45
        elif x % 5:
            yield (x / 5) + 93
        else:
            yield x / 2
print(list(generate_elements(7)))
print('-------')

# Задача 6. Самый большой прямоугольник.
print('Задача 6:')
def largest_histogram(heights: list) -> int:
    stack = []
    max_area = 0
    heights.append(0)
    for i in range(len(heights)):

        while stack and heights[i] <= heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    return max_area
heights = [2, 1, 4, 5, 1, 3, 3]
print(largest_histogram(heights))

print('-------')