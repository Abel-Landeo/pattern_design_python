from TerminalExpression import TerminalExpression
from OrExpression import OrExpression
from AndExpression import AndExpression

class InterpretPatternDemo:

	@staticmethod
	def getMaleExpression():
		robert = TerminalExpression("Robert")
		john = TerminalExpression("John")
		return OrExpression(robert, john)

	@staticmethod
	def getMarriedWomanExpression():
		julie = TerminalExpression("Julie")
		married = TerminalExpression("Married")
		return AndExpression(julie, married)

	@staticmethod
	def main():
		isMale = InterpretPatternDemo.getMaleExpression()
		isMarriedWoman = InterpretPatternDemo.getMarriedWomanExpression()
		print("John is male? " + str(isMale.interpret("John")))
		print("Julie is a married woman? " + str(isMarriedWoman.interpret("Married Julie")))

InterpretPatternDemo.main()