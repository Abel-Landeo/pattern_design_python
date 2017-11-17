from Circle import Circle
from Rectangle import Rectangle
from Square import Square

class ShapeMaker:
	"""Facade class"""

	def __init__(self):
		self.__circle = Circle()
		self.__rectangle = Rectangle()
		self.__square = Square()

	def drawCircle(self):
		self.__circle.draw()

	def drawRectangle(self):
		self.__rectangle.draw()

	def drawSquare(self):
		self.__square.draw()
	