from ShapeFactory import ShapeFactory
class FactoryPatternDemo:
	
	@staticmethod
	def demo():
		rectangle = ShapeFactory.getShape("rectangle")
		rectangle.draw()
		circle = ShapeFactory.getShape("circle")
		circle.draw()
		square = ShapeFactory.getShape("square")
		square.draw()


FactoryPatternDemo.demo()