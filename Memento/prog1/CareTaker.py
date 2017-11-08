
class CareTaker:
	
	def __init__(self):
		self.__mementoList = []

	def add(self, state):
		self.__mementoList.append(state)

	def get(self, index):
		return self.__mementoList[index]
		
		