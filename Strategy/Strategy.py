from abc import ABCMeta, abstractmethod

class Strategy(metaclass=ABCMeta):
	
	@abstractmethod
	def doOperation(self, num1, num2): pass

		