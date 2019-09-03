from mongoengine import *
from lesson11.models.constants import SALARY_CHOICES

connect("employees")


class Role(EmbeddedDocument):
    name = StringField()
    grade = StringField()
    experience = IntField(min_value=1)


class Salary(Document):
    type = StringField(choices=SALARY_CHOICES)
    amount = IntField(min_value=3200, required=True)
    fee = IntField(required=True)
    comment = StringField(max_length=255)

    @property
    def net_salary(self):
        return self.amount - self.fee

    @property
    def commentary(self):
        return self.comment

    @commentary.setter
    def commentary(self, commentary):
        if isinstance(commentary, str):
            self.comment = commentary
        else:
            raise TypeError('Wrong type')


class Employee(Document):
    name = StringField(max_length=255)
    surname = StringField(max_length=255)
    email = EmailField()
    salary_payments = ListField(ReferenceField(Salary))
    role = EmbeddedDocumentField(Role)


role = Role()
role.name = 'CEO'
role.grade = 'Senior'
role.experience = 10

salary = Salary()
salary.amount = 3500
salary.fee = 100
salary.type = '13'
salary.save()

employee = Employee()
employee.name = 'John'
employee.surname = 'Doe'
employee.role = role
employee.salary_payments = [salary]
employee.save()


