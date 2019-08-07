from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.scatter import Scatter

class Myapp(App):
    def build(self):
        lable=Label(text='hhhhhhhhhhhhhhhhhhhhhhh')
        fd=FloatLayout()
        sf=Scatter()
        
        fd.add_widget(sf)
        sf.add_widget(lable)

        return fd
Myapp().run()
