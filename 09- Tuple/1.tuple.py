# Concept: Tuple

# 👉 Tuple = ordered collection (like list)
# 👉 But immutable (cannot change)

# t = (10, 20, 30)   # tuple
# print(t)


# Write a Python program to create a tuple.

t = (1, 2, 3)

print(t)   # (1, 2, 3)


# 2. Access Elements (Indexing)

# Q. Write a Python program to access elements of a tuple.

t = ("Rahul", "Amit", "John")

print(t[0])   # Rahul
print(t[2])   # John


print('......................end question number 2----------------')

# 🧪 3. Tuple is Immutable

# Q. What happens if we try to change a tuple?

t = (10, 20, 30)

# t[0] = 100   # ❌ Error → tuple does not support item assignment

print('......................end question number 3----------------')

# 🧪 4. Tuple Slicing

# Q. Write a Python program to slice a tuple.

t = (10, 20, 30, 40, 50)

print(t[1:4])   # (20, 30, 40)
print(t[:3])    # (10, 20, 30)
print(t[2:])    # (30, 40, 50)

print('......................end question number 4----------------')

# 🧪 5. Loop through Tuple

# Q. Write a Python program to print tuple elements using loop.

t = ("A", "B", "C")

for i in t:
    print(i)   # A, B, C

print('......................end question number 5----------------')

# 🧪 6. Tuple Length

# Q. Write a Python program to find length of tuple.

t = (1, 2, 3, 4)

print(len(t))   # 4    

print('......................end question number 6----------------')

# 🧪 7. Count Method

# Q. Write a Python program to count occurrences in tuple.

t = (1, 2, 2, 3)

print(t.count(2))   # 2

print('......................end question number 7----------------')

# 🧪 8. Index Method

# Q. Write a Python progra m to find index of element in tuple.

t = (10, 20, 30)

print(t.index(20))   # 1

print('......................end question number 8----------------')