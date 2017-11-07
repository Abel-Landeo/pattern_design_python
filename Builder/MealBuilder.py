from Meal import Meal
from VegBurger import VegBurger
from Coke import Coke
from ChickenBurger import ChickenBurger
from Pepsi import Pepsi

class MealBuilder:
	
	def prepareVegMeal(self):
		meal = Meal()
		meal.addItem(VegBurger())
		meal.addItem(Coke())
		return meal
	
	def prepareNonVegMeal(self):
		meal = Meal()
		meal.addItem(ChickenBurger())
		meal.addItem(Pepsi())
		return meal