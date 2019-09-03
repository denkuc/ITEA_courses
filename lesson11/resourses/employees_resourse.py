from flask import request
from flask_restful import Resource
from lesson11.schemas.employee_schema import EmployeeSchema
from lesson11.models.employees import Employee
from marshmallow import ValidationError


class EmployeeAPI(Resource):
    @staticmethod
    def get(id_=None):
        if not id_:
            return EmployeeSchema(many=True).dump(Employee.objects())
        else:
            return EmployeeSchema().dump(
                Employee.objects.get(id=id_))

    @staticmethod
    def post():
        err = EmployeeSchema().validate(request.json)
        if err:
            return err

        employee_obj = Employee(**request.json).save()
        return EmployeeSchema().dump(employee_obj)

    @staticmethod
    def put(id_):
        err = EmployeeSchema().validate(request.json)
        if err:
            raise ValidationError(err)
        employee_obj = Employee.objects.get(id=id_)
        employee_obj.update(**request.json)
        return EmployeeSchema().dump(employee_obj)

    @staticmethod
    def delete(id_):
        Employee.objects.get(id=id_).delete()
