from Observer import Observer

class OctalObserver(Observer):
	
	def __init__(self, subject):
		self.__subject = subject
		self.__subject.attach(self)

	def update(self):
		print("Octal String: " + oct(self.__subject.getState()))
		