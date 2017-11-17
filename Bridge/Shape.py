from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
	
	def __init__(self, drawAPI):
		self._drawAPI = drawAPI

	@abstractmethod
	def draw(self): pass