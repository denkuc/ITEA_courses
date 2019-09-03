from flask import request
from flask_restful import Resource
from lesson11.schemas.employee_schema import EmployeeSchema
from lesson11.models.employees import Employee


class EmployeeAPI(Resource):
    def get(self, id_=None):
        if not id_:
            return EmployeeSchema(many=True).dump(Employee.objects())

    def post(self):
        pass

    def put(self, id_):
        pass

    def delete(self, id_):
        pass
