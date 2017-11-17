from abc import ABCMeta, abstractmethod

class MediaPlayer(metaclass=ABCMeta):
	
	@abstractmethod
	def play(self, audioType, fileName): pass