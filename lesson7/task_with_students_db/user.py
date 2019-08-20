from lesson7.task_with_students_db.context_manager_mysql import \
    CursorMysqlContextManager
from lesson7.task_with_students_db.student import StudentSerializer


class User:
    __ALL_STUDENTS_QUERY = """SELECT * FROM student"""
    __STUDENT_ID_CARD_QUERY = """SELECT * FROM student WHERE student_id_card = '%s'"""
    __STUDENT_NAME_QUERY = """SELECT * FROM student WHERE name = '%s'"""

    def __init__(self):
        self.__serializer = StudentSerializer()

    def get_all_students(self):
        return self.__get_students_by_query(self.__ALL_STUDENTS_QUERY)

    def get_excellent_students(self):
        students = self.get_all_students()
        excellent_students = list(filter(self.__student_is_excellent,
                                         students))
        return excellent_students

    def get_student_by_student_id_card(self, student_id_card):
        query = self.__STUDENT_ID_CARD_QUERY % student_id_card
        return self.__get_students_by_query(query)

    def get_student_by_name(self, name):
        query = self.__STUDENT_NAME_QUERY % name
        return self.__get_students_by_query(query)

    def __get_students_by_query(self, query):
        with CursorMysqlContextManager() as (connection, cursor):
            cursor.execute(query)
            student_tuples = cursor.fetchall()
            students = [self.__serializer.get_deserialized_student(student)
                        for student in student_tuples]
            return students

    @staticmethod
    def __student_is_excellent(student):
        marks = student.marks
        return all(90 <= mark <= 100 for mark in marks)


user = User()
print(user.get_all_students())
print(user.get_excellent_students())
print(user.get_student_by_student_id_card('КВ19210398'))
print(user.get_student_by_name('Иванова Полина Георгиевна'))
