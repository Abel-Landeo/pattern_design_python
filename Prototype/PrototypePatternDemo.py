from Item import Item
import copy
class PrototypePatternDemo:
	
	@staticmethod
	def demo():
		print("Create an original Item:")
		item = Item("Sugar", 15.12, "Peru")
		item.info()

		print("Making a shallow copy of the original Item:")
		copyOfItem = copy.copy(item)
		copyOfItem.info()

		print("Making a deepcopy of the original Item:")
		deepCopyOfItem = copy.deepcopy(item)
		deepCopyOfItem.info()
		
PrototypePatternDemo.demo()