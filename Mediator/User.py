from ChatRoom import ChatRoom

class User:
	
	def __init__(self, name):
		self.__name = name

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def sendMessage(self, message):
		ChatRoom.showMessage(self, message)