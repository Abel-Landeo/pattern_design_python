
class Item:
	
	def __init__(self, title, price, country):
		self.title = title
		self.price = price
		self.country = country

	def info(self):
		print("title: " + self.title + ", price: " + str(self.price) + ", country: " + self.country)
		