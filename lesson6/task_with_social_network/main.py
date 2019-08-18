from auth import Auth, SignUp


class StartPage:
    def go_to_start_page(self):
        print("Добро пожаловать. У вас уже есть учетная запись? (да/нет)")
        is_signup = input().lower()
        if is_signup == 'да':
            Auth(self)
        elif is_signup == 'нет':
            SignUp(self)
        else:
            print("Выберите из двух вариантов.")
            self.go_to_start_page()


if __name__ == '__main__':
    start_page = StartPage()
    start_page.go_to_start_page()
