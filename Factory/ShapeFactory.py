from RectangleShape import RectangleShape
from CircleShape import CircleShape
from SquareShape import SquareShape
class ShapeFactory:
	
	@staticmethod
	def getShape(formShape):
		if(formShape == "rectangle"):
			return RectangleShape()
		elif(formShape == "circle"):
			return CircleShape()
		elif(formShape == "square"):
			return SquareShape()
		else:
			return None
		
		