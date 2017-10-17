from Employee import Employee
class Main:
	
	def __init__(self):
		pass

	@staticmethod
	def show():
		print("Composite pattern")
		ceo = Employee('abel', 'CEO', 15000)
		headSales = Employee("Robert","Head Sales", 20000)
		headMarketing = Employee("Michel","Head Marketing",20000)
		clerk1 = Employee("Laura","Marketing", 10000)
		clerk2 = Employee("Bob","Marketing", 10000)
		salesExecutive1 = Employee("Richard", "Sales", 10000)
		salesExecutive2 = Employee("Rob", "Sales", 10000)

		ceo.add(headSales)
		ceo.add(headMarketing)

		headSales.add(salesExecutive1)
		headSales.add(salesExecutive2)

		headMarketing.add(clerk1)
		headMarketing.add(clerk2)

		ceo.info()
		for headSubordinate in ceo.subordinates:
			headSubordinate.info()
			for subordinate in headSubordinate.subordinates:
				subordinate.info()

Main.show()
