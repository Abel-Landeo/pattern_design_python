from State import State
class StartState(State):
	
	def doAction(self, context):
		print("Player is in start state")
		context.setState(self)

	def toString(self):
		return "Start State"