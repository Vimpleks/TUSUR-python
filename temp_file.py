from Tasks_Module_81 import Student, GroupStudy #CourseStudy

ivanov = Student(1,'Иванов Иван Иванович')
ivanov.add_grade('Мат. анализ', 5)
ivanov.add_grade('Теория вероятности', 4)
ivanov.add_grade('Программирование', 4)

petrov = Student(2,'Петров Петр Петрович')
petrov.add_grade('Мат. анализ', 3)
petrov.add_grade('Теория вероятности', 3)
petrov.add_grade('Программирование', 3)

nikolaev = Student(3,'Николаев Николай Николаевич')
nikolaev.add_grade('Мат. анализ', 5)
nikolaev.add_grade('Теория вероятности', 5)
nikolaev.add_grade('Программирование', 5)

ab520 = GroupStudy('АБ-520')
ab520.add_student(nikolaev)
ab520.add_student(petrov)
ab520.add_student(ivanov)

print(f'Средняя оценка у студента {ivanov.name_student} = {ivanov.get_avg_grade_student()}')
print(f'Средняя оценка у студентов группы {ab520.number_group} = {ab520.get_avg_grade_group()}')
print(f'Средняя оценка по программированию у студентов группы {ab520.number_group}\
 = {ab520.get_avg_grade_subject('Программирование')}')