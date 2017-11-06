from abc import ABCMeta, abstractmethod

class AbstractFactory(metaclass=ABCMeta):

	@abstractmethod
	def getColor(self, color): pass

	@abstractmethod
	def getShape(self, shape): pass	