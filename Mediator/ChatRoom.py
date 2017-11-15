
from datetime import datetime
class ChatRoom:

	@staticmethod
	def showMessage(user, message):
		print('{:%d/%m/%Y %H:%M:%S} '.format(datetime.now()) + "[" + user.getName() + "] " + message)
		