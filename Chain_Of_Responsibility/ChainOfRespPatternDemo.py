from AbstractLogger import AbstractLogger
from ErrorLogger import ErrorLogger
from ConsoleLogger import ConsoleLogger
from FileLogger import FileLogger

class ChainOfRespPatternDemo:

	@staticmethod
	def __getChainOfLoggers():
		errorLogger = ErrorLogger(AbstractLogger.ERROR)
		fileLogger = FileLogger(AbstractLogger.DEBUG)
		consoleLogger = ConsoleLogger(AbstractLogger.INFO)

		errorLogger.setNextLogger(fileLogger)
		fileLogger.setNextLogger(consoleLogger)

		return errorLogger

	@staticmethod
	def main():
		loggerChain = ChainOfRespPatternDemo.__getChainOfLoggers()
		loggerChain.logMessage(AbstractLogger.INFO, "This is an information")
		loggerChain.logMessage(AbstractLogger.DEBUG, "This is a DEBUG level information")
		loggerChain.logMessage(AbstractLogger.ERROR, "This is an ERROR level information")
	
ChainOfRespPatternDemo.main()
