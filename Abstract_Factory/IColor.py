from abc import ABCMeta, abstractmethod

class IColor(metaclass=ABCMeta):

	@abstractmethod
	def fill(self):	pass