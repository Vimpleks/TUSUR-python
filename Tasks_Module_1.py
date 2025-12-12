# Задача 1. Welcome to Python
name = 'Evgeniya'
surname = 'Naumova'
print('Задача 1:')
print(f'Hello {name} {surname}! You just delved into Python. Great start!')
print('-------')

# Задача 2. Python art
thickness = 5
c = 'H'
print('Задача 2:')
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2) + (c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness) + c + (c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
print('-------')

# Задача 3. Заголовок
text = 'hello world'
print('Задача 3:')
print(text.title())
print('-------')

# Задача 4. Форматированный вывод денежной суммы
# написать программу, которая распечатает число в принятом денежном формате XXX,XXX.XX.
amount = 100500.157
print('Задача 4:')
print('{0:,.2f}'.format(amount))
print('-------')

# [Junior+] Задача 6. Произведение цифр
print('Задача 6:')
exemple_list = [123405, 999, 1000, 1111]
for value in exemple_list:
    value_str = str(value)
    result = 1
    for i in value_str:
        if i == '0':
            continue
        result *= int(i)
    print(f'Число: {value}, произведение цифр: {result}')