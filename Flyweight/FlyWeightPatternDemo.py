from ShapeFactory import ShapeFactory
from random import randint

class FlyweightPatternDemo:
	__colors = ["Red", "Green", "Blue", "White", "Black"]

	@staticmethod
	def main():

		for i in range(0,19):
			circle = ShapeFactory.getCircle(FlyweightPatternDemo.__getRandomColor())
			circle.setX(FlyweightPatternDemo.__getRandomX())
			circle.setY(FlyweightPatternDemo.__getRandomY())
			circle.setRadius(100)
			circle.draw()

	@staticmethod
	def __getRandomColor():
		return FlyweightPatternDemo.__colors[randint(0,4)]

	@staticmethod
	def __getRandomX():
		return randint(1,100)

	@staticmethod
	def __getRandomY():
		return randint(1,100)

FlyweightPatternDemo.main()