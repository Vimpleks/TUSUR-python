# Задача 1. Fizz Buzz
print('Задача 1:')
num = int(input())
if num % 3 == 0 and num % 5 == 0:
    print('Fizz Buzz')
elif num % 3 == 0:
    print('Fizz')
elif num % 5 == 0:
    print('Buzz')
else:
    print(str(num))
print('-------')

# Задача 2. Оценка числа
# Во втором задании все условия являются взаимосключающими, то есть у вас не может получиться ситуации,
# когда число пройдёт по условию в нескольких условных операторах. Следовательно, нет смысла после первого
# условия проверять число x на чётность из-за того, что все нечётные числа дальше первого условия не пройдут.
# Первоначальны ответ:
# print('Задача 2:')
# x = int(input())
# if x % 2 != 0:
#     print('Плохо')
# elif 2 <= x <= 5 and x % 2 == 0:
#     print('Неплохо')
# elif 6 <= x <= 20 and x % 2 == 0:
#     print('Так себе')
# elif x > 20 and x % 2 == 0:
#     print('Отлично')
# print('-------')
print('Задача 2:')
x = int(input())
if x % 2 != 0:
    print('Плохо')
elif 2 <= x <= 5:
    print('Неплохо')
elif 6 <= x <= 20:
    print('Так себе')
elif x > 20:
    print('Отлично')
print('-------')


# Задача 3. Последовательность
# В третьем задании число N может принимать значения [1-9], включая границы. Если в вашу функцию отправить
# число 16 - функция вернёт значения от 1 до 16, хотя в таком случае она работать не должна. Будьте внимательнее.
# print('Задача 3:')
# N = int(input())
# for i in range(1, N + 1):
#     print(i, end='')
# print('\n-------')
print('Задача 3:')
N = int(input('Введите число от 1 до 9:'))
if 1 <= N <= 9:
    for i in range(1, N + 1):
        print(i, end='')
else:
    print('Число должно быть от 1 до 9')
print('\n-------')

# Задача 4. Секретное сообщение
print('Задача 4:')
text = input()
word = ''
for i in text:
    if i.isupper():
        word += i
print(word)
print('-------')

# [Junior] Задача 5. Три слова
print('Задача 5:')
text = input()
word = text.split()
count = 0
for i in word:
    if i.isalpha():
        count += 1
        if count == 3:
            break
    else:
        count = 0
if count == 3:
    print(True)
else:
    print(False)
print('-------')

# [Junior+] Задача 6. Мир захватили левши
print('Задача 6:')
list_text = ["left", "right", "left", "stop"]
text = ','.join(list_text)
result = text.replace('right', 'left')
print(result)
print('-------')