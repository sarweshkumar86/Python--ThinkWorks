# Q3. Write a Python program using if-elif-else to check age conditions (>, ==18, ==0, else).


age = int(input("Enter your age: "))

if(age>18):
    print("You can drive")
elif(age == 18):
    print("Lets schedule an interview")
elif(age == 0):
    print("Hey you are just born")
else:
    print("Sorry you cannot drive")