from DrawAPI import DrawAPI

class GreenCircle(DrawAPI):
	
	def drawCircle(self, radius, x, y):
		print("Drawing Circle[color: green, radius: " + str(radius) + ", x: " + str(x) +", y: " + str(y) + "]")
		