''' 
1. Types of Arguments
🧪 Q1. Positional Arguments

Q. Write a Python program using positional arguments.
'''
def add(a, b):
    print(a + b)

add(10, 20)   # 30 (order matters)



''' 
🧪 Q2. Keyword Arguments

Q. Write a Python program using keyword arguments.
'''

def add(a, b):
    # print(a + b)
      print(a)

add(b=20, a=10)   
# add(100,200)


''' 
🧪 Q3. Default Arguments

Q. Write a Python program using default arguments.

'''

def greet(name="Student"):
    print("Hello", name)

greet()         # Hello Student
greet("Rahul")  # Hello Rahul


'''  

🧪 Q4. Variable Arguments (*args)

Q. Write a Python program using *args.
'''

def total(*nums):
    print(sum(nums))

total(10, 20, 30)   # 60

''' 
🧪 Q5. Keyword Variable Arguments (**kwargs)

Q. Write a Python program using **kwargs.

'''

def show(**data):
    print(data)

show(name="Rahul", age=25)   # {'name': 'Rahul', 'age': 25}

''' 

🧠 2. Lambda Function

👉 Small anonymous function (one line)

🧪 Q6. Write a lambda function to add two numbers.
'''


add = lambda a, b: a + b

print(add(10, 20))   # 30


'''  

🧪 Q7. Write a lambda to square a number.
square = lambda x: x * x

print(square(5))   # 25

'''


# 🧠 3. Recursion (Advanced 🔥)

# 👉 Function calling itself

# 🧪 Q8. Write a Python program to print numbers 1 to 5 using recursion.
def show(n):
    if n > 5:
        return
    print(n)
    show(n + 1)

show(1)   # 1 2 3 4 5


