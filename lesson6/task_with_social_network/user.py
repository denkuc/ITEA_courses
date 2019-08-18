import shelve
from db import db_name


class User:
    def __init__(self):
        self.__login = None
        self.__password = None
        self.__is_admin = None
        self.__registration_date = None

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

    @property
    def registration_date(self):
        return self.__registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        self.__registration_date = registration_date


class UsersInfo:
    def __init__(self, social_network):
        self.__social_network = social_network

    def show_all_users(self):
        with shelve.open(db_name) as users:
            print('\n')
            for user_data in users.values():
                [print(f'{key}: {item}') for key, item
                 in user_data.items() if key != 'pass']
                print('\n')

        self.__social_network.go_to_main_page()
