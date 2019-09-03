from marshmallow import Schema, fields, validates, ValidationError
from lesson11.models.employees import Role, Employee, Salary


class SalarySchema(Schema):
    class Meta:
        model = Salary
        fields = ('amount', 'fee', 'comment')


# class RoleSchema(Schema):
#     class Meta:
#         model = Role


class EmployeeSchema(Schema):
    class Meta:
        model = Employee
        fields = ('name', 'surname')
