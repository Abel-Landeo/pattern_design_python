from Shape import Shape

class ShapeDecorator(Shape):
	
	def __init__(self, decoratedShape):
		self._decoratedShape = decoratedShape

	def draw(self):
		self._decoratedShape.draw()
