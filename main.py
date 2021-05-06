from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
import random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior

Builder.load_file('./design.kv')


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = 'sign_up_screen'
    def login(self, u, p):
        with open('./users.json') as file:
            users = json.load(file)
            if u in users and users[u]['password'] == p:
                self.manager.current = 'login_success'
            else:
                self.ids.wrong_login.text = 'Wrong username or password, try again'


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
        self.manager.current = 'sign_up_success'

class SignUpSuccess(Screen):
    def back_to_login(self):
        self.manager.current = 'login_screen'

class LoginSuccess(Screen):
    def logout(self):
        self.manager.current = 'login_screen'

    def get_quote(self, emo):
        emo = emo.lower()
        available_emo = glob.glob('assets/*txt')
        available_emo = [Path(filename).stem for filename in available_emo]

        if emo in available_emo:
            with open(f'assets/{emo}.txt') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = 'Try typing another emotion'

class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    MainApp().run()
