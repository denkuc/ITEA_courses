from lesson7.task_with_students_db.context_manager_mysql import \
    CursorMysqlContextManager
from lesson7.task_with_students_db.student import StudentSerializer, Student


class Admin:
    __ADD_STUDENT_QUERY = """INSERT INTO student VALUES ({}, {}, {}, {}, {}, {})"""
    __UPDATE_NAME_QUERY = """UPDATE student SET name = '{}' WHERE student_id_card = '{}'"""
    __UPDATE_GROUP_QUERY = """UPDATE student SET group_number = {} WHERE student_id_card = '{}'"""

    def __init__(self):
        self.__serializer = StudentSerializer()

    def add_student(self, student):
        student_tuple = self.__serializer.get_serialized_student(student)
        query = self.__ADD_STUDENT_QUERY.format(*student_tuple)
        self.__make_changes_in_db(query)

    def update_student_name_by_student_card_id(self, new_name, student_card_id):
        query = self.__UPDATE_NAME_QUERY.format(new_name, student_card_id)
        self.__make_changes_in_db(query)

    def update_student_group_by_student_card_id(self, new_group, student_card_id):
        query = self.__UPDATE_GROUP_QUERY.format(new_group, student_card_id)
        self.__make_changes_in_db(query)

    @staticmethod
    def __make_changes_in_db(query):
        with CursorMysqlContextManager() as (cursor, connection):
            cursor.execute(query)
            connection.commit()


admin = Admin()
new_student = Student()
new_student.name = 'Китов Алексей Олегович'
new_student.faculty = 'ФУПтаМ'
new_student.group_number = 404
new_student.student_id_card = 'КС120390231'
new_student.marks = [100, 100, 100, 99, 100]

# admin.add_student(new_student)
admin.update_student_name_by_student_card_id('Китов Александр Олегович',
                                             'КС120390231')
admin.update_student_group_by_student_card_id(101, 'КС120390231')
