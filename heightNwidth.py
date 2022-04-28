import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
	def __init__(self,**kwargs):
	    super(MyGridLayout, self).__init__(**kwargs)

	    #set column
	    self.cols = 1
	    self.row_force_default =True
	    self.row_default_height = 120
	    self.col_force_default = True
	    self.col_default_width = 300

	    #create a second gridlayout
	    self.topgrid = GridLayout(
	    	row_force_default=True,
	    	row_default_height=40,
	    	col_force_default=True,
	    	col_default_width=100,)
	    self.topgrid.cols = 2

	    #adding widget 1
	    self.topgrid.add_widget(Label(text='Name:'))
	    self.name=TextInput(multiline=True)
	    self.topgrid.add_widget(self.name)
	    #adding widget 2
	    self.topgrid.add_widget(Label(text='Age:'))
	    self.age=TextInput(multiline=False)
	    self.topgrid.add_widget(self.age)
	    #adding widget 1
	    self.topgrid.add_widget(Label(text='City:'))
	    self.city=TextInput(multiline=False)
	    self.topgrid.add_widget(self.city)

	    #adding new top grid
	    self.add_widget(self.topgrid)

	    #create submit button
	    self.submit= Button(text='Submit',
	     font_size=32,
	     size_hint_y = None,
	     height = 50,
	     size_hint_x = None,
	     width = 200)

	    #Bind the Button
	    self.submit.bind(on_press = self.press)
	    self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text
		age = self.age.text
		city = self.city.text

		self.add_widget(Label(text=f"Hello {name} you're {age} old years live in {city} City"))
		
		#clear the input
		self.name.text=" "		
		self.age.text=" "		
		self.city.text=" "		

class MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == "__main__":
	MyApp().run()