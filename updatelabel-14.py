from kivy.app import App
from kivy.lang import Builder
#from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

#Design File
Builder.load_file("updatelabel-14.kv")

class MyLayout(Widget):
	def press(self):
		#Create Variable for Widgets
		name = self.ids.name_input.text

		#Update the Label
		self.ids.name_label.text = f"Hello {name}!"

		#Clear input box
		self.ids.name_input.text = " "

class AwesomeApp(App):
	def build(self):
#		Window.clearcolor=(1,1,1,1)
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()