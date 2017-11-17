from Shape import Shape

class Circle(Shape):

	def __init__(self, color):
		self.__color = color
		self.__x = None
		self.__y = None
		self.__radius = None

	def setX(self, x):
		self.__x = x

	def setY(self, y):
		self.__y = y

	def setRadius(self, radius):
		self.__radius = radius

	def draw(self):
		print("Circle: draw() [Color: "+self.__color+", x: "+str(self.__x)+", y: "+str(self.__y)+", radius: "+str(self.__radius))  