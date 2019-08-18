import re
from datetime import datetime
from db import db_name
from social_network import SocialNetwork
from user import User
import shelve


class RegistrationModule:
    @staticmethod
    def _login_exists(login):
        with shelve.open(db_name) as db:
            user = db.get(login, None)
            if user:
                return user

    @staticmethod
    def _pass_is_valid(password):
        return re.match(r'[A-Za-z0-9@#$%^&+=]{8,16}', password)


class SignUp(RegistrationModule):
    admin_token = "admin112263"

    def __init__(self, start_page):
        self.__start_page = start_page
        self.__today = datetime.now().strftime('%d.%m.%Y')
        print("Создадим новый аккаунт.")
        print("Вы администратор? Введите админ-токен для создания профиля "
              "администратора")
        self.user = User()
        admin_token = input()
        if admin_token == self.admin_token:
            print('Ваша учетная запись будет иметь права администратора.')
            self.user.is_admin = True
        else:
            print('Токен не верен. Ваша учетная запись не будет '
                  'иметь админ-прав.')
            self.user.is_admin = False
        login = self._enter_login()
        self.user.login = login
        password = self._enter_pass()
        self.user.password = password
        self.__start_page.go_to_start_page()

    def _enter_login(self):
        print("Введите логин:")
        login = input()
        if self._login_exists(login):
            print("Такой юзер уже зарегистрирован. Введите другой логин.")
            self._enter_login()
        else:
            print(f"Новый пользователь {login} создан.")
            return login

    def _enter_pass(self):
        print("Введите пароль (от 8 до 16 символов, буквы, цифры):")
        password = input()
        if not self._pass_is_valid(password):
            print("Пароль не верный. Повторите.")
            self._enter_pass()
        else:
            return self._save_user_info(password)

    def _save_user_info(self, password):
        with shelve.open(db_name) as db:
            db[self.user.login] = {'login': self.user.login,
                                   'pass': password,
                                   'is_admin': self.user.is_admin,
                                   'registration_date': self.__today,
                                   'posts': []}
            return self._reenter_pass()

    def _reenter_pass(self):
        print("Повторите пароль:")
        reentered_password = input()
        with shelve.open(db_name) as db:
            if reentered_password != db[self.user.login]['pass']:
                print("Пароли не совпадают. Повторите снова.")
                self._enter_pass()
            else:
                print("Пароли совпадают. Пара логин-пароль зарегистрирована. "
                      "Возвращаемся на стартовую страницу.")
                return reentered_password


class Auth(RegistrationModule):
    def __init__(self, start_page):
        self.__start_page = start_page
        print('Введите логин:')
        login = input()
        if self._login_exists(login):
            with shelve.open(db_name) as db:
                self.__user = db[login]
                self._enter_pass()
        else:
            print('Юзер с таким логином не зарегистрирован. '
                  'Возвращаемся на главную страницу.')
            self.__start_page.go_to_start_page()

    def _enter_pass(self):
        print('Введите пароль:')
        password = input()
        if password == self.__user['pass']:
            print('Добро пожаловать в социальную сеть!\n')
            social_network = SocialNetwork(self.__start_page, self.__user)
            social_network.go_to_main_page()
        else:
            print('Неправильный пароль. Попробуйте еще раз.')
            self._enter_pass()
