from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from datetime import datetime

Builder.load_file('./design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'


class RootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):
    def add_user(self, u, p):
        with open('./users.json') as file:
            users = json.load(file)

        users[u] = {'username': u, 'password': p,
                    'created': datetime.now().strftime('%Y-%m-%d %H-%M-%S')}

        with open('./users.json', 'w') as file:
            json.dump(users, file)
        print(users)


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
