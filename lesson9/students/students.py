from marshmallow import Schema
from mongoengine import *

connect("students")


class Curator(Document):
    full_name = StringField(max_length=100, required=True)


class Faculty(Document):
    name = StringField(max_length=100, required=True)


class Student(Document):
    full_name = StringField(max_length=100, required=True)
    group = IntField(max_value=99999)
    marks = ListField(IntField(max_value=100))
    curator = ReferenceField(Curator)
    faculty = ReferenceField(Faculty)


class StudentSchema(Schema):
    class Meta:
        model = Student
        fields = ['full_name', 'group', 'marks']


def get_students_by_curator_name(curator_name):
    try:
        curator_id = Curator.objects.filter(full_name=curator_name)[0].id
        students = Student.objects.filter(curator=curator_id)

        return StudentSchema(many=True).dumps(students)
    except IndexError:
        return []


def get_excellent_students_by_faculty(faculty):
    try:
        faculty_id = Faculty.objects(name=faculty)[0].id
        students = Student.objects(faculty=faculty_id)
        excellent_students = [s for s in students
                              if all(mark > 90 for mark in s.marks)]

        return StudentSchema(many=True).dumps(excellent_students)
    except IndexError:
        return []


print(get_students_by_curator_name('Юлия Владимировна'))
print(get_excellent_students_by_faculty('МЕіМ'))
