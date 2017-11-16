from abc import ABCMeta, abstractmethod

class Container(metaclass=ABCMeta):
	
	@abstractmethod
	def getIterator(self): pass