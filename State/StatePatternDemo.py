from Context import Context
from StartState import StartState
from StopState import StopState
class StatePatternDemo:

	@staticmethod
	def main():
		context = Context()
		startState = StartState()
		startState.doAction(context)
		print(context.getState().toString())
		
		stopState = StopState()
		stopState.doAction(context)
		print(context.getState().toString())

StatePatternDemo.main()