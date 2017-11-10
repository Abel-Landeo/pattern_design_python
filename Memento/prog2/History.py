
class History:
	
	def __init__(self):
		self.__tabList = []

	def add(self, auxTab):
		self.__tabList.append(auxTab)

	def get(self, index):
		return self.__tabList[index]