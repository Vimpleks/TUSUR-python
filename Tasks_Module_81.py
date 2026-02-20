# Задача 1. Друзья

class Friends:
    def __init__(self, connections: list[set[str]]):
        self.connections = list()
        for connection in connections:
            if len(connection) == 2:
                self.connections.append(set(connection))
            else:
                print('Связь должна быть только из двух имен')

    def add(self, connection: set[str]):
        if connection in self.connections:
            return False
        self.connections.append(connection)
        return True

    def remove(self, connection: set[str]):
        if connection not in self.connections:
            return False
        self.connections.remove(connection)
        return True

    def names(self):
        result = set()
        for connection in self.connections:
            result.update(connection)
        return result

    def connected(self, name: str):
        result = set()
        for connection in self.connections:
            if name in connection:
                result.update(connection - {name})
        return result

    def __str__(self):
        return f"Friends({self.connections})"

my_friends = Friends([
    {'sofia', 'nikola'},
    {'nikola', 'ivan'},
    {'anna', 'sofia'}
])
# print(my_friends.add({'nikola', 'sofia'}))
# print(my_friends.add({'nikola', 'alex'}))
# print(my_friends.names())
# print(my_friends.connected('alex'))
# print(my_friends.remove({'nikola', 'anna'}))
# print(my_friends.remove({'nikola', 'alex'}))
# print(my_friends.names())
# print(my_friends.connected('nikola'))
# print(my_friends.connected('alex'))
# print(my_friends.connections)
# print(my_friends)

# Задача 2. Деканат

class Student:
    def __init__(self, student_id: int, name_student: str):
        self.student_id = student_id
        self.name_student = name_student
        self.grade_subject = dict()

    def add_grade(self,subject: str, grade: int):
        self.grade_subject[subject] = grade
        return f'Студенту {self.name_student} добавлена оценка {grade} по предмету {subject}'

    def get_avg_grade_student(self):
        if len(self.grade_subject) == 0:
            return 0
        return round(sum(self.grade_subject.values()) / len(self.grade_subject), 1)

    def __str__(self):
        return f'Студент: {self.name_student}, {self.student_id}, {self.grade_subject}'

class GroupStudy:
    def __init__(self, number_group: str):
        self.number_group = number_group
        self.students = list()

    def add_student(self, student: Student):
        self.students.append(student)
        return f'Студент {student.name_student} добавлен в группу {self.number_group}'

    def remove_student(self, student: Student):
        self.students.remove(student)
        return f'Студент {student.name_student} удален из группы {self.number_group}'

    def get_avg_grade_group(self):
        total_avg_grade_students  = 0
        if len(self.students) == 0:
            return 0
        for student in self.students:
            total_avg_grade_students += student.get_avg_grade_student()
        return round(total_avg_grade_students / len(self.students), 1)

    def get_avg_grade_subject(self, subject: str):
        grade_subject_group = list()
        for student in self.students:
            grade_subject_group.append(student.grade_subject[subject])
        return round(sum(grade_subject_group) / len(grade_subject_group), 1) if self.students else 0

    def __str__(self):
        return f'Группа: {self.number_group}, {[student.name_student for student in self.students]}'

class DeanOffice:
    def __init__(self, name):
        self.name = name
        self.groups = list()

    def add_group(self, group: GroupStudy):
        self.groups.append(group)

    def get_students_for_expulsion(self, min_avg: float = 2.5):
        students = list()
        for group in self.groups:
            for student in group.students:
                if student.get_avg_grade_student() <= min_avg:
                    students.append((student.name_student, student.get_avg_grade_student()))
        return students

    def get_scholarship_students(self, max_avg: float = 4.0):
        students = list()
        for group in self.groups:
            for student in group.students:
                if student.get_avg_grade_student() >= max_avg:
                    students.append((student.name_student, student.get_avg_grade_student()))
        return students

    def get_subject_statistics(self):
        subject_statistics = dict()
        all_subjects = set()
        for group in self.groups:
            for student in group.students:
                for subject in student.grade_subject.keys():
                    all_subjects.add(subject)
            for subject in all_subjects:
                subject_statistics[subject] = group.get_avg_grade_subject(subject)
        return subject_statistics


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

mihailov = Student(4,'Михайлов Михаил Михайлович')
mihailov.add_grade('Мат. анализ', 2)
mihailov.add_grade('Теория вероятности', 2)
mihailov.add_grade('Программирование', 3)

ab520 = GroupStudy('АБ-520')
ab520.add_student(nikolaev)
ab520.add_student(petrov)
ab520.add_student(ivanov)
ab520.add_student(mihailov)

avt_faculty = DeanOffice('Факультет АВТ')
avt_faculty.add_group(ab520)

#print(f'Средняя оценка у студента {mihailov.name_student} = {mihailov.get_avg_grade_student()}')
# print(f'Средняя оценка у студентов группы {ab520.number_group} = {ab520.get_avg_grade_group()}')
# print(f'Средняя оценка по программированию у студентов группы {ab520.number_group}\
#  = {ab520.get_avg_grade_subject('Программирование')}')
#print(f'Студенты на отчисление: {avt_faculty.get_students_for_expulsion()}')
#print(f'Студенты-стипендиаты: {avt_faculty.get_scholarship_students()}')
print(avt_faculty.get_subject_statistics())

