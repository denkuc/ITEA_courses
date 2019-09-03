from random import choice
from lesson9.students.students import Student, Curator, Faculty

from mongoengine import connect
connect("students")

CURATORS = ['Толик Толикович', 'Петр Алексеевич', 'Юлия Владимировна',
            'Владимир Александрович', 'Денис Романович']
NAMES = ['Сергей', 'Алексей', 'Роман', 'Ольга', 'Алина', 'Олег', 'Кирилл',
         'Игнат', 'Платон', 'Антон', 'Стас', 'Евгений', 'Юрий', 'Виктор']
FACULTIES = ['МЕіМ', 'КЕФ', 'ОЕФ', 'ФЕФ', 'АПК', 'ЮІ', 'ФІСіТ', 'ФЕтаУ', 'ФМ', 'ФУПТАМ']


def create_students(number):
    for curator_name in CURATORS:
        curator = Curator()
        curator.full_name = curator_name
        curator.save()

    for faculty_name in FACULTIES:
        faculty = Faculty()
        faculty.name = faculty_name
        faculty.save()

    for i in range(number):
        student = Student()
        student.full_name = f'{choice(NAMES)} {choice(NAMES)}ченко'
        student.curator = Curator.objects(full_name=choice(CURATORS))[0]
        student.faculty = Faculty.objects(name=choice(FACULTIES))[0]
        student.group = choice(range(1, 6))*100 + choice(range(10))
        student.marks = [choice(range(86, 101)) for _ in range(5)]
        student.save()


create_students(100)
