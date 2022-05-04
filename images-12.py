from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

#Design Files
Builder.load_file('images-12.kv')

class MyLayout(Widget):
	pass

class TestApp(App):
	def build(self):
		Window.clearcolor = (240/255, 240/255, 240/255, 1)
		return MyLayout()

if __name__ == "__main__":
	TestApp().run()