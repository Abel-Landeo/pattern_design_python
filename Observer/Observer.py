from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):

	def __init__(self):
		self.__subject = None

	@abstractmethod
	def update(self): pass
	
