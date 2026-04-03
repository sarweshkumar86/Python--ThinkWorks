a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)  
# union → combines all unique elements from both sets
# duplicates automatically removed

print(c)  
# Output: {1, 2, 3, 4, 23, 55}

d = a.intersection(b)  
# intersection → common elements in both sets

print(d)  
# Output: {1, 23}

# union()        → all elements (no duplicates)
# intersection() → common elements only