'''
Constructor (__init__)
 Definition : A constructor is a special method that runs automatically when an object is created.
 In Python, constructor = __init__()

'''
# Example 1 (Basic Constructor)
class Student:

    def __init__(self):
        print("Constructor is called")


s1 = Student()


print("................contructor with data ...........................")

# Example 2 (Constructor with Data)
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


s1 = Student("Rahul")
s1.display()

print("................Example 3 (Multiple Objects) ...........................")

class Student:

    def __init__(self, name):
        self.name = name


s1 = Student("Rahul")
s2 = Student("Aman")

print(s1.name)
print(s2.name)

