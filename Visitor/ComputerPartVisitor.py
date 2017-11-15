from abc import ABCMeta, abstractmethod

class ComputerPartVisitor(metaclass=ABCMeta):

	@abstractmethod
	def visit(self, part): pass
	