from Context import Context
from OperationAdd import OperationAdd
from OperationSubstract import OperationSubstract
from OperationMultiply import OperationMultiply

class StrategyPatternDemo:
	@staticmethod
	def main():
		context = Context(OperationAdd())
		print("10 + 5 = " + str(context.executeStrategy(10,5)))

		context = Context(OperationSubstract())
		print("10 - 5 = " + str(context.executeStrategy(10,5)))

		context = Context(OperationMultiply())
		print("10 * 5 = " + str(context.executeStrategy(10,5)))

StrategyPatternDemo.main()