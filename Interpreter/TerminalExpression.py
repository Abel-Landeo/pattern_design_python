from Expression import Expression

class TerminalExpression(Expression):
	
	def __init__(self, data):
		self.__data = data

	def interpret(self, context):
		if self.__data in context:
			return True
		return False
		