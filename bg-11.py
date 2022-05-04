import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('bg-11.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (0,0,1,1) #background color behind button
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()