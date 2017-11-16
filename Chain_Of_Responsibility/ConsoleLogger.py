from AbstractLogger import AbstractLogger

class ConsoleLogger(AbstractLogger):
	
	def __init__(self, level):
		AbstractLogger.__init__(self)
		self._level = level

	def _write(self, message):
		print("Standard Console::Logger: " + message)

		