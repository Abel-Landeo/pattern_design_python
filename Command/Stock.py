
class Stock:
	"""Request class"""
	def __init__(self):
		self.__name = "ABC"
		self.__quantity = 10

	def buy(self):
		print("Stock [ Name: " + self.__name + ", Quantity: " + str(self.__quantity) + "] bought")

	def sell(self):
		print("Stock [ Name: "+ self.__name + ", Quantity: " + str(self.__quantity) + " ] sold")
