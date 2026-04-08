''' 
 Members of a Class
Definition :  Members of a class are the variables and methods (functions) defined inside a class.

 There are 2 types of members:
  Variables (Attributes)
 1. Class Variable
    .Same for all objects
    .Defined directly inside class

'''



class Employee:
    company = ' HP'    #class variable


e1=Employee()
e2=Employee()

a=e1.company
b=e2.company
print(a)
print(b)



# ............................................................

''' 

2. Instance Variable

 Different for each object
 Defined using self inside methods

 '''
class Salary:
    def set_data(self, name):
        self.name = name   # here only name is parameter only work during function only 
                           # here self.name i.e e3.name mean create variable in object e3 paramenet "| we give any name instead of name self.a= name, self.b=name"              
    def display(self):
        print(self.name)


e3 = Salary()
e4 = Salary()

e3.set_data("Hello")  # pass parameter to name
e4.set_data("Hi")

e3.display()
e4.display()



 