from ComputerPart import ComputerPart

class Mouse(ComputerPart):

	def accept(self, computerPartVisitor):
		computerPartVisitor.visit(self)
	