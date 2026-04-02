''' 

Dictionary


A Python dictionary is a built-in data structure that stores data in key-value pairs,
allowing for efficient data retrieval using a specific key rather than a numeric index. 


Data stored as:

key : value

student = {"name": "Rahul", "age": 25}

'''   

# Create Dictionary

# Q1 . Write a Python program to create a dictionary.

d = {"A": 1, "B": 2}

print(d)   # {'A': 1, 'B': 2}

# ....................................

# 2. Access Value
# Q. Write a Python program to access value using key.

d = {"name": "Rahul", "age": 25}

print(d["name"])   # Rahul

# .........................................

# 3. Add Value

# Q. Write a Python program to add a new key-value pair.

d = {"A": 1}

d["B"] = 2

print(d)   # {'A': 1, 'B': 2}


# ..............................................

# 4. Update Value

# Q. Write a Python program to update a value in dictionary.

d = {"A": 1}

d["A"] = 100

print(d)   # {'A': 100}


# .................................................


# 5. Delete Value

# Q. Write a Python program to delete a key-value pair.

d = {"A": 1, "B": 2}

d.pop("A")

print(d)   # {'B': 2}


# ...................................................

# 6. Loop in Dictionary

# Q. Write a Python program to print all keys and values.

d = {"A": 1, "B": 2}

for k, v in d.items():
    print(k, v)   # A 1 , B 2

# ...................................................


# 7. Search Key

# Q. Write a Python program to check if key exists.

d = {"A": 1, "B": 2}

print("A" in d)   # True
print("C" in d)   # False
