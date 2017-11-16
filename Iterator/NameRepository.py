from Container import Container
from Iterator import Iterator

class NameRepository(Container):
	
	def __init__(self):
		self.names = ["Robert", "Jhon", "Lora"]

	def getIterator(self):
		return self.NameIterator(self)

	class NameIterator(Iterator):
		
		def __init__(self, outerSelf):
			self.index = 0
			self.outerSelf = outerSelf

		def hasNext(self):
			if self.index < len(self.outerSelf.names):
				return True
			return False

		def next(self):
			if self.hasNext():
				self.index += 1
				return self.outerSelf.names[self.index-1]

			return None

