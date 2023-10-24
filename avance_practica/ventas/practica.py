from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Contenedor_01(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class PracticaApp(App):
    def build(self):
        return Contenedor_01()

if __name__=='__main__':
    PracticaApp().run()

