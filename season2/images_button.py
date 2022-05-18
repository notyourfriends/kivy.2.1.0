from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Design
Builder.load_file('images_button.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()