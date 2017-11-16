from Order import Order

class SellStock(Order):
	
	def __init__(self, abcStock):
		self.__abcStock = abcStock

	def execute(self):
		self.__abcStock.sell()