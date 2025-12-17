# Задача 1. Анализ текста. Популярность.
print('Задача 1:')
text = input('Введите текст: ')
chars_popularity = {}
words_popularity = {}
for i in text:
    if i.isalpha():
        if i in chars_popularity:
            chars_popularity[i] += 1
        else:
            chars_popularity[i] = 1
words_text = text.split()
for word in words_text:
    word = word.strip('.,!?;:')
    if word.isalpha():
        if word in words_popularity:
            words_popularity[word] += 1
        else:
            words_popularity[word] = 1
print(f'Введенный текст: {text}')
print(f'Популярность букв: {chars_popularity}')
print(f'Популярность слов: {words_popularity}')
print('-------')

# Задача 2. Римские цифры
print('Задача 2:')
number = int(input('Введите число от 1 до 3999: '))
number_new = number
roman_numerals = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
                  'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10,
                  'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
roman_number = ''
if 1 <= number <= 3999:
    for key, value in roman_numerals.items():
        while number_new >= value:
            roman_number += key
            number_new -= value
    print(f'Число {number} по римски будет: {roman_number}')
else:
    print('Введенное число не попадает в диапазон от 1 до 3999')
print('-------')

# Задача 3. Ленивый спекулянт
print('Задача 3:')
rates = {'Sberbank': 55.8, 'VTB24': 53.91}
rates_keys = list(rates.keys())
rates_values = list(rates.values())
rates_min_value_index = rates_values.index(min(rates_values))
print(f'{rates_keys[rates_min_value_index]} -> {rates_values[rates_min_value_index]}')
print('-------')

# Задача 4. Вверх дном
print('Задача 4:')
book = {'Petr': '546810', 'Katya': '241815'}
book_reverse = {value: key for key, value in book.items()}
print(f'Исходный словарь: {book}')
print(f'Перевернутый словарь: {book_reverse}')
print('-------')

# Задача 5. Структурируем данные
print('Задача 5:')
dates = ['2017-03-01', '2017-03-02']
rates = [55.7, 55.2]
dict_result = dict(zip(dates, rates))
print(f'Словарь курсов валют на определенную дату: {dict_result}')
print('-------')

# [Junior+] Задача 6. Судья игры "Крестики-нолики"
print('Задача 6:')
data = [
    "OOX",
    "XXO",
    "OXX"
 ]
winning_combination_x = 'XXX'
winning_combination_O = 'OOO'
result_game = ''
data_diagonal = [data[0][0] + data[1][1] + data[2][2], data[0][2] + data[1][1] + data[2][0]]
data_vertical = []
for i in range(len(data)):
    data_vertical.append(data[0][i] + data[1][i] + data[2][i])
if (winning_combination_O in data or winning_combination_O in data_vertical or
    winning_combination_O in data_diagonal):
    result_game = 'O'
elif (winning_combination_x in data or winning_combination_x in data_vertical or
    winning_combination_x in data_diagonal):
    result_game = 'X'
else:
    result_game = 'D'
print(f'{data} -> {result_game}')
print('-------')