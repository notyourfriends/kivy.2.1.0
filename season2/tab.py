from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel

#Design
Builder.load_file('tab.kv')

class MyLayout(TabbedPanel):
	pass

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()