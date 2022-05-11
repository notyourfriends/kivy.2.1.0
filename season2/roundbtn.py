from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window


#Design File
Builder.load_file('roundbtn-22.kv')

class MyLayout(Widget):
	pass

class AwesomeApp(App):
	def build(self):
		Window.clearcolor = (1,1,1,1)
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()