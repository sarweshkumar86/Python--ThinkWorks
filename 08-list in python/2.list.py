# What is List?

#  List = collection of items in order


names = ["Rahul", "Amit", "John"]


names = ["Rahul", "Amit", "John"]
# index →   0        1       2

print(names[0])  # Rahul
print(names[1])  # Amit

print('......................................................')    
# ndex always starts from 0


#display using loop -------------------------------------------------

for name in names:
    print(name)   # name = Rahul, Amit, John

print('......................................................')    

# display using while loop ........................................

names = ["Rahul", "Amit", "John"]

i = 0
while i < len(names):
    print(names[i])   # i = 0,1,2
    i += 1
    

    