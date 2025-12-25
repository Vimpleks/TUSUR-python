# Задача 1. Список из числа.
print('Задача 1:')
def return_digits_reverse(num: int) -> list:
    num_str = str(num)
    num_str_reverse = num_str[::-1]
    list_digits = [int(n) for n in num_str_reverse]
    return list_digits
#number = int(input('Введите натуральное число: '))
#print(return_digits_reverse(number))
print('-------')

# Задача 2. Палиндром.
print('Задача 2:')
def word_is_palindrome(word: str) -> bool:
    if word == word[::-1]:
        return True
    else:
        return False
#word = input('Введите слово, состоящее только из строчных латинских букв: ')
word = 'топот'
if word.isalpha() and word.islower():
    print(word_is_palindrome(word))
else:
    print('Введенное слово не соответсвует заданным условиям')
print('-------')

# Задача 3. Деканат.
print('Задача 3:')

print('-------')

# [Junior] Задача 4. Пешки.
print('Задача 4:')

print('-------')

# [Junior+] Задача 5. Min-max.
print('Задача 5:')

print('-------')