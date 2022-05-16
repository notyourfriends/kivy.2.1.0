from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.spelling import Spelling
from kivy.uix.screenmanager import ScreenManager, Screen



#Design different screens 
class FirstWindow(Screen):
	pass

class SecondWindow(Screen):
	pass

class WindowManager(ScreenManager):
	pass

#Design Files
#important, make sure this kv below windowmanager
kv = Builder.load_file('multiwindows.kv')


class MultiWinApp(App):
	def build(self):
		return kv

if __name__ == "__main__":
	MultiWinApp().run()