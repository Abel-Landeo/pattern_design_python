from State import State
class StopState(State):
	
	def doAction(self, context):
		print("Player is in stop State")
		context.setState(self)

	def toString(self):
		return "Stop State"