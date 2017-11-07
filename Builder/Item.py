from abc import ABCMeta, abstractmethod

class Item(metaclass=ABCMeta):
	
	@abstractmethod
	def name(self): pass

	@abstractmethod
	def packing(self): pass

	@abstractmethod
	def price(self): pass
