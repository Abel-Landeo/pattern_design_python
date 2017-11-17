from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
	
	@staticmethod
	def draw(self): pass