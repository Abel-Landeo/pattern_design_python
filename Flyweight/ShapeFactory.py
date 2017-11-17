from Circle import Circle

class ShapeFactory:
	
	__circleMap = {}

	@staticmethod
	def getCircle(color):
		circle = ShapeFactory.__circleMap.get(color, None)

		if circle is None:
			circle = Circle(color)
			ShapeFactory.__circleMap[color] = circle
			print("Creating circle of color : " + color)

		return circle