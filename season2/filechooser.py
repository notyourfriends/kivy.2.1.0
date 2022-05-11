from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget

#Design 
Builder.load_file('filechooser-23.kv')

class MyLayout(Widget):
	def selected(self, filename):
		try:
			self.ids.my_image.source = filename[0]
			print(filename[0])
		except:
			pass
class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()