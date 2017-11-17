from abc import ABCMeta, abstractmethod

class DrawAPI(metaclass=ABCMeta):
	"""bridge implementer interface"""

	@abstractmethod
	def drawCircle(self, radius, x, y): pass