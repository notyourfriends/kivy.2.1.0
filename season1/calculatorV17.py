from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window

#Design File
Builder.load_file('calculatorV17.kv')

#Set the app size
Window.size = (500, 700) #Width Height

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text= '0'

	#Create Press Button func
	def button_press(self, button):
		# variabel penampung
		prior = self.ids.calc_input.text

		# determine if 0 is sitting there
		if prior == "0":
			self.ids.calc_input.text = " "
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	# Decimal function
	def dot(self):
		prior = self.ids.calc_input.text
		#Add decimal sign
		if "." in prior:
			pass
		else:
			prior = f'{prior}.'
			self.ids.calc_input.text = prior

	# Remove last character 
	def remove(self):
		prior = self.ids.calc_input.text
		#remove last char
		prior = prior[:-1]
		#output back to the textbox
		self.ids.calc_input.text = prior
		
	#pos/neg
	def pos_neg(self):
		prior= self.ids.calc_input.text
		#see if there's a sign
		if '-' in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'

	def math_sign(self, sign):
		# variable penampung
		prior = self.ids.calc_input.text

		# put + sign
		self.ids.calc_input.text = f'{prior}{sign}'

	#hasil
	def equals(self):
		# variable penampung
		prior = self.ids.calc_input.text

		#Addition
		if "+" in prior:
			num_list = prior.split("+")
			answer = 0

			#loop thru out list
			for number in num_list:
				answer = answer + int(number)
			
			#print the answer in the text box
			self.ids.calc_input.text = str(answer)

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	CalculatorApp().run()