from ComputerPart import ComputerPart

class Monitor(ComputerPart):
	
	def accept(self, computerPartVisitor):
		computerPartVisitor.visit(self)