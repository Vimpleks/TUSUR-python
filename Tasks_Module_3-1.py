# Задача 1. Последний с четными
import statistics
from statistics import median

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

# [Junior] Задача 4. Медиана
# Альтернативное решение используя готовую функцию:
# elements = [3, 6, 20, 99, 10, 15]
# print(statistics.median(elements))
print('Задача 4:')
elements = [3, 6, 20, 99, 10, 15]
elements_sorted = sorted(elements)
if len(elements_sorted) % 2 == 0:
    elements_median = (elements_sorted[len(elements_sorted) // 2] + elements_sorted[len(elements_sorted) // 2 - 1]) / 2
else:
    elements_median = elements_sorted[len(elements_sorted) // 2]
print(elements_median)
print('-------')

# [Junior+] Задача 5. Полосатые слова
print('Задача 5:')
text = input('Введите текст: ')
vowels = set('A E I O U Y'.replace(' ', ''))
consonants = set('B C D F G H J K L M N P Q R S T V W X Z'.replace(' ', ''))
result = 0
words_text = re.split(r'[.,!?:; ]+', text.upper())
print(words_text)
for word in words_text:
    if len(word) > 1 and word.isalpha():
        if set(word[::2]).issubset(vowels) and set(word[1::2]).issubset(consonants):
            result += 1
        elif set(word[::2]).issubset(consonants) and set(word[1::2]).issubset(vowels):
            result += 1
print(f'"Полосатых" слов: {result}')
print('-------')