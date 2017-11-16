from Stock import Stock
from BuyStock import BuyStock
from SellStock import SellStock
from Broker import Broker

class CommandPatternDemo:

	@staticmethod
	def main():
		abcStock = Stock()
		buyStockOrder = BuyStock(abcStock)
		sellStockOrder = SellStock(abcStock)

		broker = Broker()
		broker.takeOrder(buyStockOrder)
		broker.takeOrder(sellStockOrder)

		broker.placeOrders()
	
CommandPatternDemo.main()