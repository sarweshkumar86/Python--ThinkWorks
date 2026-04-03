''' 
Concept: Set

👉 Set = collection of unique values
👉 No duplicate + no index + unordered


🧪 Question
Q. What is a set in Python?
👉 Set is an unordered collection of unique elements.

Example
s = {1, 2, 3, 3, 4}
print(s)   # {1, 2, 3, 4} → duplicate removed
'''

# 1️⃣ Add Element
# Q. Write a program to add element in set.
s = {1, 2}
s.add(3)
print(s)   # {1, 2, 3}

# .................................................

# 2️⃣ Remove Element
# Q. Write a program to remove element from set.
s = {1, 2, 3}
s.remove(2)
print(s)   # {1, 3}

# ....................................................

# 3️⃣ Union
# Q. Write a program to join two sets.
a = {1, 2}
b = {2, 3}
print(a | b)   # {1, 2, 3}

# .....................................................

# 4️⃣ Intersection
# Q. Write a program to find common elements.
a = {1, 2}
b = {2, 3}
print(a & b)   # {2}

# ...................................................




s = {3, 23, 2, 11}   # set (unordered collection)

print(s, type(s))    
# Output: {2, 3, 11, 23} <class 'set'>
# Reason:
# set does not maintain order → elements can appear in any order

# print(s[3]) ❌ Error
# Reason:
# set has no indexing → you cannot access elements using index