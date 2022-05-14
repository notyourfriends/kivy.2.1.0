from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.core.window import Window

#design files
Builder.load_file('floatlayout-13.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (0,1,1,1)
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()
