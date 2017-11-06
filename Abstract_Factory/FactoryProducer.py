from ShapeFactory import ShapeFactory
from ColorFactory import ColorFactory

class FactoryProducer:
	
	@staticmethod
	def getFactory(choice):
		if (choice == 'shape'):
			return ShapeFactory()

		if(choice == 'color'):
			return ColorFactory()

		return None