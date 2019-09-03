from mongoengine import *
connect("students")


class Curator(Document):
    full_name = StringField(max_length=100, required=True)


class Faculty(Document):
    name = StringField(max_length=100, required=True)


class Student(Document):
    full_name = StringField(max_length=100, required=True, unique=True)
    group = IntField(max_value=99999)
    marks = ListField(IntField(max_value=100))
    curator = ReferenceField(Curator)
    faculty = ReferenceField(Faculty)


def get_students_by_curator_name(curator_name):
    curator_id = Curator.objects.filter(full_name=curator_name)
    students = Student.objects.filter(curator=curator_id)
    for s in students:
        print(s)


def get_excellent_students_by_faculty(faculty):
    faculty_id = Faculty.objects(name=faculty)
    students = Student.objects(faculty=faculty_id)
    excellent_students = [s for s in students if list(map(lambda mark: mark > 90, s.marks))]
    for s in excellent_students:
        print(s)


# get_students_by_curator_name('Толик')
