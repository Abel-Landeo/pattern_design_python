from abc import ABCMeta, abstractmethod

class AbstractLogger(metaclass=ABCMeta):
	INFO = 1
	DEBUG = 2
	ERROR = 3

	def __init__(self):
		self._level = 0
		self._nextLogger = None

	def setNextLogger(self, nextLogger):
		self._nextLogger = nextLogger

	def logMessage(self, level, message):
		if self._level <= level:
			self._write(message)
		if self._nextLogger is not None:
			self._nextLogger.logMessage(level, message)

	@abstractmethod
	def _write(self, message): pass

	