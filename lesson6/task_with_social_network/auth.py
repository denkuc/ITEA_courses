import re

from social_network import SocialNetwork
from user import User
import shelve

db_name = 'local.db'


class StartPage:
    def __init__(self):
        print("Добро пожаловать. У вас уже есть учетная запись? (да/нет)")
        is_signup = input().lower()
        if is_signup == 'да':
            Auth()
        elif is_signup == 'нет':
            SignUp()
        else:
            print("Выберите из двух вариантов.")
            StartPage()


class RegistrationModule:
    @staticmethod
    def _login_exists(login):
        with shelve.open(db_name) as db:
            user = db['user'].get(login, None)
            if user:
                return user

    @staticmethod
    def _pass_is_valid(password):
        return re.match(r'[A-Za-z0-9@#$%^&+=]{8,16}', password)


class SignUp(RegistrationModule):
    admin_token = "admin112263"

    def __init__(self):
        print("Создадим новый аккаунт.")
        print("Вы администратор? Введите админ-токен для создания профиля "
              "администратора")
        self.user = User()
        admin_token = input()
        if admin_token == self.admin_token:
            print('Ваша учетная запись будет иметь права администратора.')
            self.user.is_admin = True
        else:
            print('Токен не верен. Ваша учетная запись не будет админ-прав.')
            self.user.is_admin = False
        login = self._enter_login()
        self.user.login = login
        password = self._enter_pass()
        self.user.password = password

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
            with shelve.open(db_name) as db:
                new_user = {self.user.login: {'pass': password}}
                db['user'] = {**db['user'], **new_user}
                return self._reenter_pass()

    def _reenter_pass(self):
        print("Повторите пароль:")
        reentered_password = input()
        print(reentered_password)
        with shelve.open(db_name) as db:
            if reentered_password != db['user'][self.user.login]['pass']:
                print("Пароли не совпадают. Повторите снова.")
                self._enter_pass()
            else:
                print("Пароли совпадают. Пара логин-пароль зарегистрирована.")
                return reentered_password


class Auth(RegistrationModule):
    def __init__(self):
        print('Введите логин:')
        login = input()
        if self._login_exists(login):
            with shelve.open(db_name) as db:
                self.user = db['user'][login]
                self._enter_pass()
        else:
            print('Юзер с таким логином не зарегистрирован. '
                  'Возвращаемся на главную страницу.')
            StartPage()

    def _enter_pass(self):
        print('Введите пароль:')
        password = input()
        if password == self.user['pass']:
            print('Добро пожаловать в социальную сеть!')
            SocialNetwork()
        else:
            print('Неправильный пароль. Попробуйте еще раз.')
            self._enter_pass()


if __name__ == '__main__':
    # StartPage()
    with shelve.open(db_name) as db:
        db['user'] = {}
        print(db['user'])
