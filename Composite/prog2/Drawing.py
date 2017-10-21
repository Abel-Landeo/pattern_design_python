from Shape import IShape

class Drawing(IShape):

	def __init__(self):
		self.shapes = []
	
	def draw(self, color):
		print("Composite Drawing:")
		for shape in self.shapes:
			shape.draw(color)

	def add(self, shape):
		self.shapes.append(shape)

	def remove(self, shape):
		self.shapes.remove(shape)

	def clear(self):
		self.shapes = []
		print("all shapes cleared")

