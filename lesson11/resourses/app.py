from flask import Flask
from flask_restful import Api

from lesson11.resourses.employees_resourse import EmployeeAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeeAPI, "/employee", "/employee/<int:id>")


if __name__ == '__main__':
    app.run(debug=True)
