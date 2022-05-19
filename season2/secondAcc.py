from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget

Builder.load_file('secondAcc.kv')

class MyLayout(Widget):
	def press_it(self):
		#Grab the value progress bar
		current = self.ids.my_progress_bar.value
		#Reset the value after value = 100
		if current == 1:
			current = 0
		else:
		#Increment the value
			current += .25
		#set to current progress value
		self.ids.my_progress_bar.value = current

		#update the label
		self.ids.progress_id.text = f'{int(current*100)}% Progress'

	def switch_click(self, siwtchObject, switchValue):
		if (switchValue):
			self.ids.switch_label.text = 'The Switch is ON now'
		else:
			self.ids.switch_label.text = 'The Switch is OFF now'
class SecondApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	SecondApp().run() 