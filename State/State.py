from abc import ABCMeta, abstractmethod
class State(metaclass=ABCMeta):
	
	@abstractmethod
	def doAction(self, context): pass