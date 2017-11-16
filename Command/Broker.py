
class Broker:
	
	def __init__(self):
		self.__orderList = []

	def takeOrder(self, order):
		self.__orderList.append(order)

	def placeOrders(self):
		for order in self.__orderList:
			order.execute()
		self.__orderList = []
