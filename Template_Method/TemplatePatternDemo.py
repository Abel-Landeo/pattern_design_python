from Cricket import Cricket
from Football import Football
class TemplatePatternDemo:
	
	@staticmethod
	def main():
		game = Cricket()
		game.play()
		print("")
		game = Football()
		game.play()

TemplatePatternDemo.main()