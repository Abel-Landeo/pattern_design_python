from Observer import Observer

class BinaryObserver(Observer):

	def __init__(self, subject):
		self.__subject = subject
		self.__subject.attach(self)

	def update(self):
		print("Binary String: " + bin(self.__subject.getState()))
	
		