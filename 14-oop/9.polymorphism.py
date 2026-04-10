'''
Polymorphism
Definition : Polymorphism means same method name behaves differently.
Same function name
Different classes → different output


'''
print("............................. Example 1 (Basic Polymorphism) ........................")

class Dog:
    def speak(self):
        print("Woof")


class Cat:
    def speak(self):
        print("Meow")


d = Dog()
c = Cat()

d.speak()
c.speak()

print("............................. Example 2 Loop Example ........................")

class Employee:
    def work(self):
        print("Employee is working")


class Developer:
    def work(self):
        print("Developer is coding")


class Designer:
    def work(self):
        print("Designer is designing")


people = [Employee(), Developer(), Designer()]

for p in people:
    p.work()