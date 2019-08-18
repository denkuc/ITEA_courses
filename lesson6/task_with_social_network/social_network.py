from post import NewPost
from user import UsersInfo


class SocialNetwork:
    __POST_COMMAND = "--new_post"
    __LOGOUT_COMMAND = "--logout"
    __SHOW_USERS_COMMAND = "--users"
    __USER_OPTIONS = f"Чтобы разместить пост, введите команду {__POST_COMMAND}"\
        f"\nЧтобы выйти из аккаунта, введите команду {__LOGOUT_COMMAND}"
    __ADMIN_OPTIONS = f"\nЧтобы посмотреть информацию о пользователях, " \
                      f"введите команду {__SHOW_USERS_COMMAND}"

    def __init__(self, start_page, user):
        self.__start_page = start_page
        self.__user = user

    def go_to_main_page(self):
        if not self.__user['is_admin']:
            print(self.__USER_OPTIONS)
        else:
            print(self.__USER_OPTIONS + self.__ADMIN_OPTIONS)

        command = input()
        if command == self.__LOGOUT_COMMAND:
            print('Вы вышли из аккаунта.')
            self.__start_page.go_to_start_page()
        elif command == self.__POST_COMMAND:
            new_post = NewPost(self, self.__user)
            new_post.make_new_post()
        elif command == self.__SHOW_USERS_COMMAND and self.__user['is_admin']:
            users_info = UsersInfo(self)
            users_info.show_all_users()
        else:
            print('Команда не правильная. Повторите.')
            self.go_to_main_page()
