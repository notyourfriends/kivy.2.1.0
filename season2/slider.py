from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

#Design File
Builder.load_file('slider-25.kv')

class MyLayout(Widget):
	def slide_it(self, *args):
		#print(args[1])
		self.slide_text.text = str(int(args[1]))
		self.slide_text.font_size = str(int(args[1]) * 5)

class SliderApp(App):
	def build(self):
		return MyLayout()


if __name__ == "__main__":
	SliderApp().run()