# Задача 1. Анализ текста. Популярность.
print('Задача 1:')
#text = input('Введите текст: ')
text = "hello, word of word..."
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


print('-------')