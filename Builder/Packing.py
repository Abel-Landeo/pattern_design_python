from abc import  ABCMeta, abstractmethod

class Packing(metaclass=ABCMeta):
	
	@abstractmethod
	def pack(self): pass