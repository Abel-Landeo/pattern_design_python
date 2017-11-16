from AbstractLogger import AbstractLogger

class FileLogger(AbstractLogger):
	
	def __init__(self, level):
		AbstractLogger.__init__(self)
		self._level = level

	def _write(self, message):
		print("File::Logger: " + message)
		