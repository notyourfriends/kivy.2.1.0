from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

#Design
Builder.load_file('images_button.kv')

class MyLayout(Widget):
	def click_on(self):
		self.ids.my_label.text = 'Press the image'
		self.ids.my_image.source = 'images/after.png'

	def click_off(self):
		#self.ids.my_label.text = 'now long press the image'
		self.ids.my_image.source = 'images/before.png'


class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()