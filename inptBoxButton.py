import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
	#initialize infinite keywords
	def __init__(self, **kwargs):
		#Call Grid layout constructor
	    super(MyGridLayout, self).__init__(**kwargs)

	    #Set Columns
	    self.cols = 2

	    #Add Widgets 1 Name
	    self.add_widget(Label(text="Name: "))

	    #Add input box
	    self.name = TextInput(multiline=False)

	    #multiline = True makes you can type using enter for new line
	    
	    self.add_widget(self.name)

	    #Add Widgets 2 Age
	    self.add_widget(Label(text="Age: "))

	    #Add input box
	    self.age = TextInput(multiline=False)
	    self.add_widget(self.age)

	    #Add Widgets 3 Address
	    self.add_widget(Label(text="Address: "))

	    #Add input box
	    self.address = TextInput(multiline=False)
	    self.add_widget(self.address)

	    #Create Submit Button
	    self.submit = Button(text="Submit", font_size=32)

	    #Bind the button
	    self.submit.bind(on_press=self.press)
	    self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text 
		age = self.age.text
		address = self.address.text

		#print(f'Hello {name}, you"re {age} old years, and you live at {address}')
		self.add_widget(Label(text=f"Hello {name}, you're {age} old years, and you live in {address}"))

		#clear the input boxes
		self.name.text=" "
		self.age.text=" "
		self.address.text=" "


class MyApp(App):
	def build(self):
		return MyGridLayout()


if __name__== '__main__':
	MyApp().run()