import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
	def __init__(self, **kwargs):
	    super(MyGridLayout, self).__init__(**kwargs)

	    #set column
	    self.cols = 1

	    #create a second gridlayout
	    self.top_grid = GridLayout()
	    self.top_grid.cols = 2

	    #add widget 1 Name
	    self.top_grid.add_widget(Label(text='Name: '))
	    #add input box
	    self.name = TextInput(multiline=False)
	    self.top_grid.add_widget(self.name)


	    #add widget 2 Age
	    self.top_grid.add_widget(Label(text='Age: '))
	    #add input box
	    self.age = TextInput(multiline=False)
	    self.top_grid.add_widget(self.age)

	    #add widget 3 Place born
	    self.top_grid.add_widget(Label(text='Born Place: '))
	    #add input box
	    self.born = TextInput(multiline=False)
	    self.top_grid.add_widget(self.born)

	    #add the new top grid
	    self.add_widget(self.top_grid)

	    #create Submit button
	    self.submit = Button(text='Submit', font_size=32)
	    #Bind Button
	    self.submit.bind(on_press = self.press)
	    self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text
		age = self.age.text
		born = self.born.text

		self.add_widget(Label(text=f"Hello {name}, you're {age} years old and born in {born}"))

		#clear input on boxes
		self.name.text=""
		self.age.text=""
		self.born.text=""



class MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == "__main__":
	MyApp().run()
