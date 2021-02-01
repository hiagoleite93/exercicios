from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        return Button(text='Hello World')
        return Label(self=Label,**kwargs)

TestApp().run()