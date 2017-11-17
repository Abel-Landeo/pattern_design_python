from ProxyImage import ProxyImage

class ProxyPatternDemo:
	
	@staticmethod
	def main():
		image = ProxyImage("text_10mb.jpg")
		image.display()
		print("")
		image.display()

ProxyPatternDemo.main()