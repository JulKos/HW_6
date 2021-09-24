class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.len = []


    def rate_lecturers(self, lecturer, course, grade):
        """Оценивание лекторов студентами"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.lector_grades:
                lecturer.lector_grades[course].append(grade)
            else:
                    lecturer.lector_grades[course] = [grade]
        else:
            return 'Ошибка!'
        return f'{lecturer.lector_grades[course]}'

    def avg_grade(self):
        """Средняя оценка для студентов"""
        grades_list = []
        for value in self.grades.values():
            grades_list += value
        return sum(grades_list)/len(grades_list)

    def __str__(self):
        """Магический метод __str__"""
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.avg_grade()} \nКурсы в процессе изучения: {self.courses_in_progress} \n Завершенные курсы: {self.finished_courses}'

    def get_grade(self, course):
        return self.grades[course]

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        """Оценивание студентов экспертами"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        """Магический метод __str__"""
        return f'Имя: {self.name} \nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname, *course):
        super().__init__(name=name, surname=surname)
        self.course = course
        self.courses_attached = []
        self.lector_grades = {}

    def __str__(self):
        """Магический метод __str__"""
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lector_grades}'

    def avg_grade(self):
        """Средняя оценка за лекции"""
        grades_list = []
        for value in self.lector_grades.values():
            grades_list += value
        return sum(grades_list) / len(grades_list)

    def get_grade(self, course):
        return self.lector_grades[course]

    def get(self, value):
        return [inst for inst in self.instances if inst.value == value]

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade()

    def __ne__(self, other):
        return self.avg_grade() != other.avg_grade()


some_student_1 = Student('Alisa', 'Ala', 'w')
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Git']
some_student_1.finished_courses += ['Java']


some_student_2 = Student('Ivan', 'Ivi', 'm')
some_student_2.courses_in_progress += ['Python']
some_student_2.courses_in_progress += ['Git']
some_student_2.finished_courses += ['Java']

cool_student = Student('Some', 'Buddy', 'your_gender')
cool_student.courses_in_progress += ['Python']

students_list = [some_student_1, some_student_2]


some_reviewer_1 = Reviewer('Vitaliy', 'Vit')
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Git']

some_reviewer_2 = Reviewer('Sergey', 'Ser')
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Git']
some_reviewer_2.courses_attached += ['Java']

some_reviewer_1.rate_hw(some_student_1, 'Python', 9)
some_reviewer_1.rate_hw(some_student_2, 'Python', 10)
some_reviewer_2.rate_hw(some_student_1, 'Git', 10)
some_reviewer_2.rate_hw(some_student_2, 'Java', 9)
some_reviewer_2.rate_hw(some_student_2, 'Git', 7)
some_reviewer_2.rate_hw(some_student_2, 'Python', 9)


def avg_grade_all_student(students_list, course):
    """Средняя оценка за домашние задания по всем студентам в рамках конкретного курса"""
    grades_list = []
    for student in students_list:
        grades_list += student.get_grade(course)
    return sum(grades_list)/len(grades_list)


some_lecturer_1 = Lecturer('Michail', 'Mich', ' ')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_1.courses_attached += ['Git']
some_lecturer_1.courses_attached += ['Java']

some_lecturer_2 = Lecturer('Vitaliy', 'Vit', ' ')
some_lecturer_2.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['Git']

lecturer_list = [some_lecturer_1, some_lecturer_2]

some_student_1.rate_lecturers(some_lecturer_1, 'Python', 10)
some_student_1.rate_lecturers(some_lecturer_1, 'Git', 9)
some_student_2.rate_lecturers(some_lecturer_1, 'Java', 10)
some_student_2.rate_lecturers(some_lecturer_2, 'Python', 13)
some_student_2.rate_lecturers(some_lecturer_2, 'Python', 9)
some_student_2.rate_lecturers(some_lecturer_1, 'Python', 8)


def avg_grade_all_lecturers(lecturer_list, course):
    """подсчет средней оценки за лекции всех лекторов в рамках курса"""
    grades_list = []
    for lecturer in lecturer_list:
        grades_list += lecturer.get_grade(course)
    return sum(grades_list)/len(grades_list)


# print(avg_grade_all_lecturers(lecturer_list, 'Python'))
#
# print(some_student_2.grades)
#
# print(some_student_2.avg_grade())
#
# print(avg_grade_all_student(students_list, 'Python'))
#
# print(some_lecturer_1.lector_grades)
#
# print(some_reviewer_2)
#
# print(some_lecturer_1)
#
# print(some_student_2)
#
# print(some_lecturer_1 < some_lecturer_2)
#
# print(some_student_1 == some_student_2)


