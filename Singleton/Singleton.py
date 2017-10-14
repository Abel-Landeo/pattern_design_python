class Singleton:
	
	__obj = None

	def __init__(self):
		self._instance = None

	@staticmethod
	def getInstance():
		if(Singleton.__obj is None):
			Singleton.__obj = Singleton()
		return Singleton.__obj

	