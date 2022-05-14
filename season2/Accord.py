from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.core.spelling import Spelling

#Design File
Builder.load_file('Accord.kv')

class MyLayout(Widget):
	def selected(self, filename):
		try:
			self.ids.my_image.source=filename[0]
			print(filename[0])
		except:
			pass

	def press(self):
		#Create instance of Spelling
		s = Spelling()

		#Select the language
		s.select_language('en_US')

		#language options
		#print(s.list_languanges())

		#Grab word from the textbox
		word = self.ids.word_input.text
		options = s.suggest(word)
		x = ''
		for item in options:
			x = f'{x} {item}/'

		#update the label
		self.ids.word_label.text = f'{x}'

	def slide_it(self, *args):
		#print(args[1])
		self.slide_text.text = str(int(args[1]))
		self.slide_text.font_size = str(int(args[1]) * 5)

	checks = []
	def checkbox_click(self, instance, value, topping):
		if value == True:
			MyLayout.checks.append(topping)
			tops = ''
			for x in MyLayout.checks:
				tops = f'{tops} {x}'
			self.ids.output_label.text = f'You Selected: {tops}'
		else:
			MyLayout.checks.remove(topping)
			tops = ''
			for x in MyLayout.checks:
				tops = f'{tops} {x}'
			self.ids.output_label.text = f'You Selected: {tops}'



class AccordsApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	AccordsApp().run()