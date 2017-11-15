from Observer import Observer

class HexaObserver(Observer):
	
	def __init__(self, subject):
		self.__subject = subject
		self.__subject.attach(self)

	def update(self):
		print("Hex String: " + hex(self.__subject.getState()))
		