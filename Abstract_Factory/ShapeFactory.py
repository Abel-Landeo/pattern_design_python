from AbstractFactory import AbstractFactory
from Circle import Circle
from Rectangle import Rectangle
from Square import Square

class ShapeFactory(AbstractFactory):
	
	def getShape(self, shape):
		if (shape is None):
			return None

		if (shape == 'circle'):
			return Circle()

		if (shape == 'rectangle'):
			return Rectangle()

		if (shape == 'square'):
			return Square()
		
		return None

	def getColor(self, color):
		return None
		