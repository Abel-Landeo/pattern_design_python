from ShapeDecorator import ShapeDecorator

class RedShapeDecorator(ShapeDecorator):

	def __init__(self, decoratedShape):
		ShapeDecorator.__init__(self, decoratedShape)

	def draw(self):
		self._decoratedShape.draw()
		self.__setRedBorder(self._decoratedShape)

	def __setRedBorder(self, decoratedShape):
		print("Border Color: Red")	
