from RedCircle import RedCircle
from GreenCircle import GreenCircle
from Circle import Circle

class BridgePatternDemo:
	@staticmethod
	def main():
		redCircle = Circle(100, 100, 10, RedCircle())
		greenCircle = Circle(100, 100, 10, GreenCircle())
		redCircle.draw()
		greenCircle.draw()

BridgePatternDemo.main()