from Item import Item
from Wrapper import Wrapper
class Burger(Item):
	
	def packing(self): 
		return Wrapper()
	
	