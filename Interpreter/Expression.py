from abc import ABCMeta, abstractmethod

class Expression(metaclass=ABCMeta):
	
	@abstractmethod
	def interpret(self, context): pass
		