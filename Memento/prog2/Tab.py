from AuxTab import AuxTab
class Tab:
	
	def __init__(self):
		self.__url = ""

	def setUrl(self, url):
		self.__url = url

	def getUrl(self):
		return self.__url

	def saveUrl(self):
		return AuxTab(self.__url)

	def restoreFromSavedUrl(self, savedUrl):
		self.__url = savedUrl.getUrl()