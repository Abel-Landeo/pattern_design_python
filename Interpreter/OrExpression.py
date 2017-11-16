from Expression import Expression

class OrExpression(Expression):
	
	def __init__(self, expr1, expr2):
		self.__expr1 = expr1
		self.__expr2 = expr2

	def interpret(self, context):
		return self.__expr1.interpret(context) or self.__expr2.interpret(context)
		