
class Subject:
	
	def __init__(self):
		self.__observers = []
		self.__state = 0

	def getState(self):
		return self.__state

	def setState(self, state):
		self.__state = state
		self.notifyAllObservers()

	def attach(self, observer):
		self.__observers.append(observer)

	def notifyAllObservers(self):
		for observer in self.__observers:
			observer.update()


