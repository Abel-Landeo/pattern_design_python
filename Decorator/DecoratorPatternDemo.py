from Circle import Circle
from RedShapeDecorator import RedShapeDecorator
from Rectangle import Rectangle

class DecoratorPatternDemo:

	@staticmethod
	def main():
		circle = Circle()
		redCircle = RedShapeDecorator(Circle())
		redRectangle = RedShapeDecorator(Rectangle())

		print("Circle with normal border")
		circle.draw()

		print("Circle of red border")
		redCircle.draw()

		print("Rectangle of red border")
		redRectangle.draw()

DecoratorPatternDemo.main()
	