from abc import ABCMeta, abstractmethod

class ComputerPart(metaclass=ABCMeta):

	@abstractmethod
	def accept(self, computerPartVisitor): pass
	
