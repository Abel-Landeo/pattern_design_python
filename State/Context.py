
class Context:
	
	def __init__(self):
		self.__state = None

	def setState(self, state):
		self.__state = state

	def getState(self):
		return self.__state