from MediaPlayer import MediaPlayer
from VlcPlayer import VlcPlayer
from Mp4Player import Mp4Player

class MediaAdapter(MediaPlayer):
	
	def __init__(self, audioType):
		if audioType.lower() == "vlc":
			self.advancedMusicPlayer = VlcPlayer()

		elif audioType.lower() == "mp4":
			self.advancedMusicPlayer = Mp4Player()

	def play(self, audioType, fileName):
		if audioType.lower() == "vlc":
			self.advancedMusicPlayer.playVlc(fileName)
		elif audioType.lower() == "mp4":
			self.advancedMusicPlayer.playMp4(fileName)