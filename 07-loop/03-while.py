# While Loop

# Q1. Print 0 to 4
i = 0
while i < 5:
    print(i)   # i = 0,1,2,3,4
    i += 1


print(" .............................end .............................. ")


# Q2. Print 1 to 5
i = 1
while i <= 5:
    print(i)   # i = 1,2,3,4,5
    i += 1

print(" .............................end .............................. ")


# Q3. Print even numbers (0 to 10)
i = 0
while i <= 10:
    print(i)   # i = 0,2,4,6,8,10
    i += 2

print(" .............................end .............................. ")


# Q4. Print reverse numbers (5 to 1)
i = 5
while i > 0:
    print(i)   # i = 5,4,3,2,1
    i -= 1        

print(" .............................end .............................. ")


# Q5. Print sum of numbers 1 to 5

i = 1
sum = 0
while i <= 5:
    sum += i   # i = 1,2,3,4,5
    i += 1

print(sum)     # 15    


print(" .............................end .............................. ")




# Q. Write a Python program to print the multiplication table of a given number using loop.

num = 5

for i in range(1, 11):
    print(num * i)   # i = 1 to 10


print(" .............................end .............................. ")

# While Loop
    
num = 5
i = 1

while i <= 10:
    print(num * i)   # i = 1 to 10
    i += 1