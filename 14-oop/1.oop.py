''' 

# OOP in Python

1. Class

Definition:
A class is a blueprint used to create objects. It defines variables and functions.



Example:
class Employee:
    pass   # Empty class (just a template)

............................................................    

🔹 2. Members of a Class

👉 Class has 2 types of members:

✔ (A) Variables (Attributes)
1. Class Variable (Common for all objects)


class Employee:
    company = "HP"   # Class variable (same for all objects)    



2. Instance Variable (Different for each object)
self.name = name    # Instance variable (unique for each object)


.........................................................................


✔ (B) Methods (Functions inside class)
👉 Methods = functions defined inside a class

class Employee:

    def greet(self):              # Method
        print("Hello Employee")   # Action

        
        
🔹 3. Object (Instance)
Definition:
An object is a real instance of a class.

e1 = Employee()   # Creating object

👉 e1 = object of Employee class

............................................................................


🔹 4. self Keyword

Definition:
self refers to the current object.

class Employee:

    def show(self):
        print("This is self:", self)   # Shows object address

e1 = Employee()
e1.show()   # self = e1


.............................................................................



🔹 5. Constructor (__init__)

Definition:
A constructor is a special method that runs automatically when an object is created.


class Employee:

    def __init__(self, name):
        self.name = name   # Initialize data

e1 = Employee("John")


...............................................................................


6. Full Example (IMPORTANT 🔥)
class Employee:

    company = "HP"   # Class variable (shared by all objects)

    def __init__(self, name, salary):
        # Constructor runs when object is created
        
        self.name = name        # Instance variable
        self.salary = salary    # Instance variable

    def get_info(self):
        # Method to display employee details
        
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Company: {self.company}")


# Creating object
e1 = Employee("John", 34000)

# Calling method
e1.get_info()



..........................................................


🔹 7. Inheritance

Definition:
Inheritance allows one class to use properties of another class.


class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):       # Inheriting Animal
    def speak(self):
        print("Woof")    # Overriding

d = Dog()
d.speak()



...............................................................................


🔹 8. Polymorphism

Definition:
Same method name behaves differently.


class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")


..............................................................


🔹 9. Encapsulation

Definition:
Binding data and methods together and controlling access.

✅ Example:
class Person:

    def __init__(self, age):
        self._age = age   # Private variable (convention)

    def get_age(self):
        return self._age


        


'''