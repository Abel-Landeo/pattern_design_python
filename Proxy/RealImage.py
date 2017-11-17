from Image import Image

class RealImage(Image):
	
	def __init__(self, fileName):
		self.__fileName = fileName
		self.__loadFromDisk(fileName)

	def display(self):
		print("Displaying " + self.__fileName)

	def __loadFromDisk(self, fileName):
		print("Loading " + fileName)
		