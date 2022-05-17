from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

#Design Files
Builder.load_file('Tabs.kv')

class MyLayout(TabbedPanel):
	pass

class TabsApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	TabsApp().run()