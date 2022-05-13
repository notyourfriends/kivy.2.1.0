from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

#Design File
Builder.load_file('carousel-27.kv')

class MyLayout(Widget):
	pass

class CarouselApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	CarouselApp().run()