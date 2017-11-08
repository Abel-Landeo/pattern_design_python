from Originator import Originator
from CareTaker import CareTaker
class MementoPatternDemo:
	
	@staticmethod
	def main():
		originator = Originator()
		careTaker = CareTaker()

		originator.setState("State one")
		originator.setState("State two")
		careTaker.add(originator.saveStateToMemento())

		originator.setState("State three")
		careTaker.add(originator.saveStateToMemento())

		originator.setState("State four")

		print("Current state: " + originator.getState())

		originator.getStateFromMemento(careTaker.get(0))
		print("First saved State: " + originator.getState())
		originator.getStateFromMemento(careTaker.get(1))
		print("Second saved State: " + originator.getState())

MementoPatternDemo.main()