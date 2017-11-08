from Memento import Memento
class Originator:
	
	def __init__(self):
		self.__state = ""

	def setState(self, state):
		self.__state = state

	def getState(self):
		return self.__state

	def saveStateToMemento(self):
		return Memento(self.__state)

	def getStateFromMemento(self, memento):
		self.__state = memento.getState()