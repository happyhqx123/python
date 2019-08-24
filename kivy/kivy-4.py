from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class MyFloatLayout(FloatLayout):
	pass

class TestApp(App):
	def build(self):
		return MyFloatLayout()

TestApp().run()
