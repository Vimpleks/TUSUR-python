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

from collections import defaultdict

data = defaultdict(lambda: defaultdict(list))
for student in students:
    group = student['group number']
    for subject, grade in student['grades'].items():
        data[group][subject].append(grade)
averages = {}
for group, subjects in data.items():
    averages[group] = {subject: sum(grades) / len(grades) for subject, grades in subjects.items()}

print(data)
