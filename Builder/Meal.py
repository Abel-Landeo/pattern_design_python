
class Meal:
	
	def __init__(self):
		self.__items = []
	
	def addItem(self, item):
		self.__items.append(item)

	def getCost(self):
		cost = 0.0
		for item in self.__items:
			cost += item.price()
		return cost

	def showItems(self):
		for item in self.__items:
			print("Item : " + item.name(), end='')
			print(", Packing : " + item.packing().pack(), end='')
			print(", Price : " + str(item.price()))
		
	
