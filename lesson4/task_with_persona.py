from abc import ABC, abstractmethod
from datetime import datetime
from dateutil.relativedelta import relativedelta


class Person(ABC):
    def __init__(self, last_name, birth_date, faculty):
        super().__init__()
        self._last_name = last_name
        self._birth_date = birth_date
        self._faculty = faculty

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self._birth_date = birth_date

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, faculty):
        self._faculty = faculty

    @abstractmethod
    def __repr__(self):
        return f"{self.__class__.__name__} {self.last_name}, " \
               f"Birth Date: {self.birth_date}, Faculty: {self.faculty}"

    def get_age(self):
        birth_datetime = datetime.strptime(self._birth_date, "%d.%m.%Y")
        age = relativedelta(datetime.now(), birth_datetime)
        return age.years


class Applicant(Person):
    def __init__(self, last_name, birth_date, faculty):
        super().__init__(last_name, birth_date, faculty)

    def __repr__(self):
        return super().__repr__()


class Student(Person):
    def __init__(self, last_name, birth_date, faculty, course):
        super().__init__(last_name, birth_date, faculty)
        self.__course = course

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        self.__course = course

    def __repr__(self):
        additional_data = f", Course {self.course}"
        return super().__repr__() + additional_data


class Teacher(Person):
    def __init__(self, last_name, birth_date, faculty, job_title,
                 experience_years):
        super().__init__(last_name, birth_date, faculty)
        self.__job_title = job_title
        self.__experience_years = experience_years

    @property
    def job_title(self):
        return self.__job_title

    @job_title.setter
    def job_title(self, job_title):
        self.__job_title = job_title

    @property
    def experience_years(self):
        return self.__experience_years

    @experience_years.setter
    def experience_years(self, experience_years):
        self.__experience_years = experience_years

    def __repr__(self):
        additional_data = f", Job Title: {self.job_title}, " \
                          f"Experience Years: {self.experience_years}"
        return super().__repr__() + additional_data


list_of_people = [
    Applicant("Каракуц", "24.02.2002", "МЕіМ"),
    Applicant("Данилюк", "12.03.2003", "ФЕтаУ"),
    Applicant("Василюк", "29.07.2002", "ФІСіТ"),
    Applicant("Русанова", "02.12.2001", "МЕіМ"),
    Applicant("Куриец", "09.05.2001", "ФІСіТ"),
    Student("Пашкевич", "17.08.2001", "ФЕтаУ", 1),
    Student("Иванова", "19.08.2001", "МЕіМ", 2),
    Student("Иванов", "12.08.2001", "ФІСіТ", 2),
    Student("Цыбко", "11.08.2001", "ФЕтаУ", 3),
    Student("Головач", "21.08.2001", "МЕіМ", 3),
    Student("Смешко", "08.08.2001", "ФІСіТ", 4),
    Student("Ляшко", "30.08.1997", "ФЕтаУ", 5),
    Student("Зеленский", "01.08.1998", "МЕіМ", 4),
    Teacher("Кошевой", "07.11.2000", "МЕіМ", "Преподаватель экономики", 20),
    Teacher("Фролова", "07.08.1972", "ФІСіТ", "Преподаватель физики", 20),
    Teacher("Тимошенко", "07.02.1952", "ФЕтаУ", "Преподаватель права", 20),
    Teacher("Петров", "07.01.1992", "МЕіМ", "Преподаватель маркетинга", 20),
]


def age_is_in_range(age, above=None, below=None):
    above = 0 if above is None else above
    below = 100 if below is None else below
    return above < age < below


[print(person) for person in list_of_people]

filtered_list_1 = list(filter(lambda x: x.get_age() > 19,
                              list_of_people))
filtered_list_2 = list(filter(lambda x: x.get_age() < 25,
                              list_of_people))
filtered_list_3 = list(filter(lambda x: 22 > x.get_age() > 19,
                              list_of_people))

print('\n')
[print(person) for person in filtered_list_1]
print('\n')
[print(person) for person in filtered_list_2]
print('\n')
[print(person) for person in filtered_list_3]
