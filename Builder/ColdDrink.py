from Item import Item
from Bottle import Bottle
class ColdDrink(Item):
	
	def packing(self):
		return Bottle()
	