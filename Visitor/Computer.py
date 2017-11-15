from ComputerPart import ComputerPart
from Mouse import Mouse
from Keyboard import Keyboard
from Monitor import Monitor

class Computer(ComputerPart):

	def __init__(self):
		self.__parts =[Mouse(), Keyboard(), Monitor()]

	def accept(self, computerPartVisitor):
		for part in self.__parts:
			part.accept(computerPartVisitor)
		computerPartVisitor.visit(self)
	