from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.spelling import Spelling

#Design File
Builder.load_file('spellchecker-24.kv')

class MyLayout(Widget):
	def press(self):
		#Create instance of Spelling
		s = Spelling()

		#Select the languiage
		s.select_language('en_US')

		# See the language option
		# print(s.list_languages())

		#Grab word from the textbox
		word = self.ids.word_input.text

		options = s.suggest(word)

		x = ''
		for item in options:
			x = f'{x} {item}'

		#update the label 
		self.ids.word_label.text = f'{x}'

class SpellChecker(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	SpellChecker().run()