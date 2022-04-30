import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('color-7.kv')

class MyGridLayout(Widget):
	
	name = ObjectProperty(None)
	age = ObjectProperty(None)
	address = ObjectProperty(None)

	def press(self):
		name=self.name.text
		age=self.age.text
		address=self.address.text

		print(f"Hello {name} you're {age} years old and live in {address}")
		#clear the input boxes
		self.name.text=""
		self.age.text=""
		self.address.text=""

class Awesome(App):
	def build(self):
		return MyGridLayout()

if __name__ == "__main__":
	Awesome().run()