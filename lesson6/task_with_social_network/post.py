import shelve
from datetime import datetime

from db import db_name


class NewPost:
    def __init__(self, social_network, user):
        self.__social_network = social_network
        self.__user = user

    def make_new_post(self):
        print('Введите, что вы хотите запостить:')
        post_text = input()
        if len(post_text) > 140:
            print("Длина поста не должна превышать 140 смиволов.")
            self.make_new_post()
        else:
            print("Пост опубликован.")
            self.__save_post_to_user(post_text)
            self.__social_network.go_to_main_page()

    def __save_post_to_user(self, post_text):
        post_datetime = datetime.now().strftime('%d.%m.%Y %H:%M:%S')

        with shelve.open(db_name) as users:
            user_posts = self.__user['posts']
            user_posts.append({post_datetime: post_text})
            self.__user['posts'] = user_posts
            users[self.__user['login']] = self.__user
