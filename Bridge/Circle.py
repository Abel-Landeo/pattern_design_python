from Shape import Shape

class Circle(Shape):
	
	def __init__(self, x, y, radius, drawAPI):
		Shape.__init__(self, drawAPI)
		self.__x = x
		self.__y = y
		self.__radius = radius

	def draw(self):
		self._drawAPI.drawCircle(self.__radius, self.__x, self.__y)
		