from MediaPlayer import MediaPlayer
from MediaAdapter import MediaAdapter

class AudioPlayer(MediaPlayer):

	def __init__(self):
		self.mediaAdapter = None
	
	def play(self, audioType, fileName):
		if audioType.lower() == "mp3":
			print("Playing mp3 file. Name: " + fileName)
		elif audioType.lower() == "vlc" or audioType.lower() == "mp4":
			self.mediaAdapter = MediaAdapter(audioType)
			self.mediaAdapter.play(audioType, fileName)
		else:
			print("Invalid media. " + audioType + " format not supported")
