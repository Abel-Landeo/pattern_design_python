from DrawAPI import DrawAPI

class RedCircle(DrawAPI):
	
	def drawCircle(self, radius, x, y):
		print("Drawing Circle[color: red, radius: " + str(radius) + ", x: " + str(x) +", y: " + str(y) + "]")
