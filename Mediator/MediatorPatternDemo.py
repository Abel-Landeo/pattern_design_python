from User import User

class MediatorPatternDemo:
	
	@staticmethod
	def main():
		einstein = User("Albert Einstein")
		bohr = User("Niels Bohr")

		bohr.sendMessage("Probability is part of the nature of mechanic quantic")
		einstein.sendMessage("God does not play dice")

MediatorPatternDemo.main()


		