class Employee:
	
	def __init__(self, name, dept, salary):
		self.name = name
		self.dept = dept
		self.salary = salary
		self.subordinates = []
	
	def add(self, employee):
		self.subordinates.append(employee)

	def info(self):
		print("name: " + self.name +", dept: " + self.dept + ", salary: " + str(self.salary))

