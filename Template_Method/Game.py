from abc import ABCMeta, abstractmethod

class Game(metaclass=ABCMeta):

	@abstractmethod
	def initialize(self): pass

	@abstractmethod
	def startPlay(self): pass

	@abstractmethod
	def endPlay(self): pass

	def play(self):
		self.initialize()
		self.startPlay()
		self.endPlay()
	