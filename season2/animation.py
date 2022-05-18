from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.animation import Animation

#Design
Builder.load_file('animation.kv')

class MyLayout(Widget):
	def animate_it(self, widget, *args):
		self.ids.my_button.text = ''
		#First Animate change the color in 3 second
		animate = Animation(
			background_color = (0,0,1,1),
			duration = 2)
		#Second Animate 
		animate += Animation(size_hint = (1,1),
			duration = 1)
		animate += Animation(size_hint = (1,.5),
			duration = 1)
		animate += Animation(size_hint = (.5,1),
			duration = 1)
		animate += Animation(size_hint = (.5,.5),
			duration = 1)
		animate += Animation(pos_hint ={'center_x':0.1},
			duration = 1)
		animate += Animation(pos_hint ={'center_x':0.9},
			duration = 1)
		animate += Animation(pos_hint ={'center_x':0.5},
			duration = 1)
		
		#turn into transparent and bring it back to normal
		animate += Animation(opacity=0,
			duration = 3)
		animate += Animation(background_color = (1,1,1,1),
			opacity=1)

		# Start the Animation
		animate.start(widget)

		#Create a callback
		animate.bind(on_complete = self.my_callback)

	def my_callback(self, *args):
		self.ids.my_label.text = "Did you see that?"
		self.ids.my_button.text = 'Press Here'

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == "__main__":
	AwesomeApp().run()