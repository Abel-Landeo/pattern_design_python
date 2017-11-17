from Image import Image
from RealImage import RealImage

class ProxyImage(Image):
	
	def __init__(self, fileName):
		self.__fileName = fileName
		self.__realImage = None

	def display(self):
		if self.__realImage == None:
			self.__realImage = RealImage(self.__fileName)

		self.__realImage.display()