from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


#Design file
Builder.load_file('ImagesBtn.kv')

class MyLayout(Widget):
	pass

class ImBtnApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	ImBtnApp().run()