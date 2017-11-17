from abc import ABCMeta, abstractmethod

class AdvancedMediaPlayer(metaclass=ABCMeta):
	
	@abstractmethod
	def playVlc(self, fileName): pass	

	@abstractmethod
	def playMp4(self, fileName): pass