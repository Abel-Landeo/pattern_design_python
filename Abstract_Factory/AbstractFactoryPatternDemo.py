from FactoryProducer import FactoryProducer

class AbstractFactoryPatternDemo:

	@staticmethod
	def main():
		shapeFactory = FactoryProducer.getFactory('shape')
		
		shape1 = shapeFactory.getShape('circle')
		shape1.draw()

		shape2 = shapeFactory.getShape('rectangle')
		shape2.draw()

		shape3 = shapeFactory.getShape('square')
		shape3.draw()

		colorFactory = FactoryProducer.getFactory('color')
		color1 = colorFactory.getColor('red')
		color1.fill()

		color2 = colorFactory.getColor('green')
		color2.fill()

		color3 = colorFactory.getColor('blue')
		color3.fill()


AbstractFactoryPatternDemo.main()

	