from NameRepository import NameRepository

class IteratorPatternDemo:
	
	@staticmethod
	def main():
		namesRepository = NameRepository()

		iter = namesRepository.getIterator()
		while iter.hasNext():
			print("Name: " + iter.next())
		

IteratorPatternDemo.main()