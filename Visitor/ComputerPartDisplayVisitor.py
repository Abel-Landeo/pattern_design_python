from ComputerPartVisitor import ComputerPartVisitor
from Computer import Computer
from Mouse import Mouse
from Keyboard import Keyboard
from Monitor import Monitor
class ComputerPartDisplayVisitor(ComputerPartVisitor):

	def visit(self, part):
		if isinstance(part, Computer):
			print("Displaying computer")
		elif isinstance(part, Mouse):
			print("Displaying mouse")
		elif isinstance(part, Keyboard):
			print("Displaying Keyboard")
		elif isinstance(part, Monitor):
			print("Displaying Monitor")
