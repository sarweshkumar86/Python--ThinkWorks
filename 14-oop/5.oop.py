# Object with Data

class Employee:

    def set_data(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)


# Creating objects
e1 = Employee()
e2 = Employee()

# Setting data
e1.set_data("John", 30000)
e2.set_data("Alice", 40000)

# Display data
e1.display()
e2.display()


print("  ''''''''''''''''''''self Keyword----------------------------- ")



class Student:

    def set_data(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


s1 = Student()
s2 = Student()

s1.set_data("Rahul")
s2.set_data("Aman")

s1.display()
s2.display()