''' 

Concept: Function

👉 Function = block of code that runs when called

👉 Use:
✔ Reuse code
✔ Avoid repetition

🧪 Question

Q. What is a function in Python?

✅ Answer

👉 Function is a block of code that performs a specific task and runs when called.

🧪 1. Simple Function
'''

''' 
 Q. Write a Python program to create and call a function.
'''


def greet():
    print("Hello Student")

greet()   # Hello Student


'''

# 🧪 2. Function with Parameter

# Q. Write a Python program to pass value in function.

def greet(name):
    print("Hello", name)

greet("Rahul")   # Hello Rahul

''' 
# .....................................................

'''

# 🧪 3. Function with Return

# Q. Write a Python program to return value from function.

def add(a, b):
    return a + b

result = add(10, 20)
print(result)   # 30

''' 

'''
# 🧪 4. Function with Multiple Calls

# Q. Write a Python program to call function multiple times.

def show():
    print("Welcome")

show()   # Welcome
show()   # Welcome

''' 

# ......................................................

'''  

# 🧪 5. Function with Default Parameter

# Q. Write a Python program using default parameter.


def greet(name="Student"):
    print("Hello", name)

greet()         # Hello Student
greet("Rahul")  # Hello Rahul

'''


