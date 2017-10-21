from Circle import Circle
from Triangle import Triangle
from Drawing import Drawing

class Client:

	@staticmethod
	def main():
		print("Composite pattern Shapes..")
		cir1 = Circle()
		cir1.draw("red")
		cir2 = Circle()
		cir2.draw("blue")
		tri1 = Triangle()
		tri1.draw("green")

		drawing = Drawing()
		drawing.add(cir1)
		drawing.add(tri1)
		drawing.draw("yellow")

		drawing.add(cir2)
		drawing.draw("orange")

		drawing.remove(tri1)
		drawing.draw("orange")
	

Client.main()