from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

#Design File
Builder.load_file('calculator-15.kv')

#Set the app size
Window.size = (500, 700) #Width Height

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text= '0'

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	CalculatorApp().run()