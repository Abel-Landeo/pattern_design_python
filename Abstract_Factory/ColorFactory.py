from AbstractFactory import AbstractFactory
from Red import Red
from Green import Green
from Blue import Blue

class ColorFactory(AbstractFactory):
	def getShape(self, shape):
		return None

	def getColor(self, color):
		if (color is None):
			return None
		
		if(color == 'red'):
			return Red()

		if (color == 'green'):
			return Green()

		if (color == 'blue'):
			return Blue()

		return None

	
		