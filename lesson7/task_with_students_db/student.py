class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__faculty = None
        self.__group_number = None
        self.__student_id_card = None
        self.__marks = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id_):
        self.__id = id_

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        self.__faculty = faculty

    @property
    def group_number(self):
        return self.__group_number

    @group_number.setter
    def group_number(self, group_number):
        self.__group_number = group_number

    @property
    def student_id_card(self):
        return self.__student_id_card

    @student_id_card.setter
    def student_id_card(self, student_id_card):
        self.__student_id_card = student_id_card

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        self.__marks = marks

    def __repr__(self):
        return f"\nСтудент: {self.name}\n" \
               f"Факультет: {self.faculty}\n" \
               f"Группа: {self.group_number}\n" \
               f"Студенческий билет: {self.student_id_card}\n" \
               f"Оценки: {self.marks}"


class StudentSerializer:
    __index_id = 0
    __index_name = 1
    __index_faculty = 2
    __index_group_number = 3
    __index_student_id_card = 4
    __index_marks = 5

    def get_serialized_student(self, student: Student):
        return (None,
                student.name,
                student.faculty,
                student.group_number,
                student.student_id_card,
                self.__get_marks_as_string(student.marks))

    @staticmethod
    def __get_marks_as_string(list_with_marks):
        list_with_marks = map(str, list_with_marks)
        return ','.join(list_with_marks)

    def get_deserialized_student(self, student_tuple):
        student = Student()
        student.id = student_tuple[self.__index_id]
        student.name = student_tuple[self.__index_name]
        student.faculty = student_tuple[self.__index_faculty]
        student.group_number = student_tuple[self.__index_group_number]
        student.student_id_card = student_tuple[self.__index_student_id_card]
        student.marks = self.__get_marks_as_list(student_tuple[self.__index_marks])

        return student

    @staticmethod
    def __get_marks_as_list(string_with_marks):
        list_with_marks = string_with_marks.split(',')
        list_with_marks = [int(mark) for mark in list_with_marks]

        return list_with_marks
