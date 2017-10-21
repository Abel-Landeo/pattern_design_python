import abc

class IShape(metaclass = abc.ABCMeta):

	@abc.abstractmethod
	def draw(self, color):
		pass
	
		