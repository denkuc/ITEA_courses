from marshmallow import Schema, fields
from lesson11.models.employees import Role, Employee


class RoleSchema(Schema):
    class Meta:
        model = Role
        fields = ['name', 'experience']


class EmployeeSchema(Schema):
    payments = fields.List(fields.String())
    role = fields.Nested(RoleSchema)
    id = fields.String(dump_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'role', 'salary_payments']
