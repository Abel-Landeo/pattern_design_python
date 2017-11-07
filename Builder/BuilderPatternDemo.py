from MealBuilder import MealBuilder 
class BuilderPatternDemo:
	
	@staticmethod
	def main():
		mealBuilder = MealBuilder()
		vegMeal = mealBuilder.prepareVegMeal()
		print("Veg Meal")
		vegMeal.showItems()
		print("Total cost: " + str(vegMeal.getCost()))

		nonVegMeal = mealBuilder.prepareNonVegMeal()
		print("\nNon-Veg Meal")
		nonVegMeal.showItems()
		print("Total cost: " + str(nonVegMeal.getCost()))

BuilderPatternDemo.main()