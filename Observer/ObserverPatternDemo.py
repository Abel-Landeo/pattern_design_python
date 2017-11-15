from Subject import Subject
from HexaObserver import HexaObserver
from OctalObserver import OctalObserver
from BinaryObserver import BinaryObserver
class ObserverPatternDemo:
	
	@staticmethod
	def main():
		subject = Subject()

		HexaObserver(subject)
		OctalObserver(subject)
		BinaryObserver(subject)

		print("First state change: 15")
		subject.setState(15)
		print("Second state change: 10")
		subject.setState(10)

ObserverPatternDemo.main()