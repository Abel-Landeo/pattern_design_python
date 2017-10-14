import threading
class SingletonThreadSafe:

	__singleton = None
	lock = threading.RLock()
	
	def __init__(self):
		self._instance = None
		
	@staticmethod
	def getInstance():
		if(SingletonThreadSafe.__singleton is None):
			with SingletonThreadSafe.lock:
				SingletonThreadSafe.__singleton = SingletonThreadSafe()
		return SingletonThreadSafe.__singleton