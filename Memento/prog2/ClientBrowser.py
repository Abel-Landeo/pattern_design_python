from Tab import Tab
from History import History
class ClientBrowser:

	@staticmethod
	def main():
		tab = Tab()
		history = History()

		tab.setUrl("http://tutorialspoint.com")
		history.add(tab.saveUrl())

		tab.setUrl("https://www.python.org/doc/")
		history.add(tab.saveUrl())

		tab.setUrl("http://www.trome.com.pe")

		print("Current web url: " + tab.getUrl())

		print("Back button is clicked.. ")
		tab.restoreFromSavedUrl(history.get(1))
		print("Saved url: " + tab.getUrl())

		print("Back button again.. ")
		tab.restoreFromSavedUrl(history.get(0))
		print("Saved url: " + tab.getUrl())
		
ClientBrowser.main()