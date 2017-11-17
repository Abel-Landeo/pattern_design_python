from ShapeMaker import ShapeMaker

class FacadePatternDemo:

	@staticmethod
	def main():
		shapeMaker = ShapeMaker()

		shapeMaker.drawCircle()
		shapeMaker.drawRectangle()
		shapeMaker.drawSquare()

FacadePatternDemo.main()

		
		