# Задача 1. Список из числа.
print('Задача 1:')
def return_digits_reverse(num: int) -> list:
    num_str = str(num)
    num_str_reverse = num_str[::-1]
    list_digits = [int(n) for n in num_str_reverse]
    return list_digits
number = int(input('Введите натуральное число: '))
print(return_digits_reverse(number))
print('-------')

# Задача 2. Палиндром.
print('Задача 2:')
def word_is_palindrome(word: str) -> bool:
    if word == word[::-1]:
        return True
    else:
        return False
word = input('Введите слово, состоящее только из строчных латинских букв: ')
if word.isalpha() and word.islower():
    print(word_is_palindrome(word))
else:
    print('Введенное слово не соответсвует заданным условиям')
print('-------')

# Задача 3. Деканат.
print('Задача 3:')
students = [
            {'surname': 'Иванов', 'name': 'Василий', 'middle name': 'Федорович', 'birth year': 2008, 'course': 2, 'group number': 520,
            'grades' : {'Математический анализ': 4, 'История': 5, 'Философия': 4, 'Линейная алгебра': 5, 'Статистика': 3}},
            {'surname': 'Петров', 'name': 'Дмитрий', 'middle name': 'Алексеевич', 'birth year': 2006, 'course': 3, 'group number': 420,
            'grades' : {'Математический анализ': 5, 'История': 4, 'Философия': 5, 'Линейная алгебра': 4, 'Статистика': 4}},
            {'surname': 'Галкин', 'name': 'Семен', 'middle name': 'Михайлович', 'birth year': 2006, 'course': 2, 'group number': 521,
             'grades' : {'Математический анализ': 3, 'История': 3, 'Философия': 3, 'Линейная алгебра': 5, 'Статистика': 3}},
            {'surname': 'Веселов', 'name': 'Андрей', 'middle name': 'Константинович', 'birth year': 2007, 'course': 2, 'group number': 521,
             'grades' : {'Математический анализ': 5, 'История': 5, 'Философия': 5, 'Линейная алгебра': 5, 'Статистика': 5}},
            {'surname': 'Бондарев', 'name': 'Иван', 'middle name': 'Васильевич', 'birth year': 2005, 'course': 3, 'group number': 421,
             'grades' : {'Математический анализ': 5, 'История': 4, 'Философия': 4, 'Линейная алгебра': 5, 'Статистика': 4}},
            ]
def get_students_by_course(students: list, course: int) -> list:
    """
    Возвращает список студентов по курсу в алфавитном порядке, на вход получает список всех студентов и номер курса.
    """
    students_by_course = [student for student in students if student['course'] == course]
    students_by_course.sort(key=lambda s: (s['surname'], s['name'], s['middle name']))
    return students_by_course

from collections import defaultdict

def get_average_grade_by_group(students: list) -> dict:
    """
    Находит средний балл каждой группы по каждому предмету
    Возвращает словарь, где в качестве ключей номер группы, а в качестве значений словарь с предметами и средним баллом.
    """
    data = defaultdict(lambda: defaultdict(list))
    for student in students:
        group = student['group number']
        for subject, grade in student['grades'].items():
            data[group][subject].append(grade)
    averages = {}
    for group, subjects in data.items():
        averages[group] = {subject: sum(grades) / len(grades) for subject, grades in subjects.items()}
    return averages

def find_youngest_and_oldest(students: list) -> tuple:
    """
    Определяет самого старшего студента и самого младшего студентов.
    """
    youngest_student = max(students, key=lambda element: element['birth year'])
    oldest_student = min(students, key=lambda element: element['birth year'])
    return youngest_student, oldest_student

def best_student_by_group(students: list) -> dict:
    """
    Возвращает словарь, где для каждой группы определен лучшый с точки зрения успеваемости студент
    """
    best_student_by_group = {}
    for student in students:
        avg_grade = sum(student['grades'].values()) / len(student['grades'])
        group = student['group number']
        if group not in best_student_by_group or avg_grade > best_student_by_group[group][0]:
            best_student_by_group[group] = (avg_grade, student['surname'], student['name'], student['middle name'])
    return best_student_by_group

print('Студенты 2 курса:')
for student in get_students_by_course(students, 2):
    print(student['surname'], student['name'], student['middle name'])

print('....................')

for group, average in get_average_grade_by_group(students).items():
    print(f'Группа {group} имеет средние оценки по предметам: ')
    for subject, grades in average.items():
        print(subject, grades, sep = ' -> ')

print('....................')

yuongest_student = find_youngest_and_oldest(students)[0]
oldest_student = find_youngest_and_oldest(students)[1]
print(f'Самый молодой студент: {yuongest_student['surname']} {yuongest_student['name']} {yuongest_student['middle name']}')
print(f'Самый старший студент: {oldest_student['surname']} {oldest_student['name']} {oldest_student['middle name']}')

print('....................')

for group, average in best_student_by_group(students).items():
    print(f'Самый лучший студент группы {group} - {average[1]} {average[2]} {average[3]} со средним баллом {average[0]}')

print('-------')

# [Junior-] Задача 4. Пешки.
print('Задача 4:')

coordinates = {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}

def count_protected_pawns(coordinates: set) -> int:
    coordinates_set = set()
    for coord in coordinates:
        vertical = ord(coord[0]) - ord('a') + 1
        horizontal = int(coord[1])
        coordinates_set.add((vertical, horizontal))
    protected_pawns_count = 0
    for vertical, horizontal in coordinates_set:
        if ((vertical - 1, horizontal - 1) in coordinates_set ) or ((vertical + 1, horizontal - 1) in coordinates_set):
            protected_pawns_count += 1
    return protected_pawns_count
print('Количество защищенных пешек:', count_protected_pawns(coordinates))

print('-------')