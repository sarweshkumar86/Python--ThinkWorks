# Question:
# Write a program that takes a list of numbers and removes all duplicates using a set.

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]   # list with duplicates

unique_numbers = list(set(numbers))     
# set(numbers) → removes duplicates
# Reason:
# set stores only unique values
# list() → convert set back to list

print("Original list:", numbers)        
# [1, 2, 3, 2, 4, 5, 1, 6, 3]

print("List without duplicates:", unique_numbers)
# Output may be unordered because set is unordered