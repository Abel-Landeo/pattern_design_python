from Computer import Computer
from ComputerPartDisplayVisitor import ComputerPartDisplayVisitor

class VisitorPatternDemo:
	
	@staticmethod
	def main():
		computer = Computer()
		computer.accept(ComputerPartDisplayVisitor())

VisitorPatternDemo.main()