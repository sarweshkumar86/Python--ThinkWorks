'''
Inheritance
 Definition : Inheritance allows one class to use properties (variables & methods) of another class.

'''

print('.................... Basic Inheritance ......................')

class Animal:

    def speak(self):
        print("Animal makes sound")


class Dog(Animal):   # Inheriting Animal
    pass


d = Dog()
d.speak()

print('.................... Method Overriding ......................')

class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speaks(self):
        print("Woof")   # Overriding parent method


d = Dog()
d.speak()
d.speaks()

print('.................... Using Parent + Child Together......................')

class Animal:

    def eat(self):
        print("Eating...")


class Dog(Animal):

    def bark(self):
        print("Barking...")


d = Dog()

d.eat()   # from parent
d.bark()  # from child