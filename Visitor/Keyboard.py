from ComputerPart import ComputerPart

class Keyboard(ComputerPart):
	
	def accept(self, computerPartVisitor):
		computerPartVisitor.visit(self)