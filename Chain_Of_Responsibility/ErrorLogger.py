from AbstractLogger import AbstractLogger

class ErrorLogger(AbstractLogger):
	
	def __init__(self, level):
		AbstractLogger.__init__(self)
		self._level = level

	def _write(self, message):
		print("Error Console::Logger: " + message)
		