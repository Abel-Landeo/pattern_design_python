from SingletonThreadSafe import SingletonThreadSafe
from Singleton import Singleton
class SingletonPatternDemo:
	
	def __init__(self):
		pass

	def demo(self):
		print("Checking singleton class...")
		s1 = Singleton.getInstance()
		s2 = Singleton.getInstance()
		if(s1 == s2):
			print("same ")
		else:
			print("not same")

		print("Checking SingletonThreadSafe...")
		s3 = SingletonThreadSafe.getInstance()
		s4 = SingletonThreadSafe.getInstance()
		if(s3 == s4):
			print("same ")
		else:
			print("not same")

a = SingletonPatternDemo()
a.demo()