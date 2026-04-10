'''
This example combines:

Class
Object
Constructor
Instance Variable
Method

'''

class Employee:

    company = "HP"   # Class variable

    def __init__(self, name, salary):
        # Constructor (runs automatically)
        self.name = name
        self.salary = salary

    def get_info(self):
        # Method to display data
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("Company:", self.company)


# Creating object
e1 = Employee("John", 34000)

# Calling method
e1.get_info()