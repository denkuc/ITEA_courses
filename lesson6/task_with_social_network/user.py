class User:
    def __init__(self):
        self.__login = None
        self.__password = None
        self.__is_admin = None

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        self.__is_admin = is_admin
