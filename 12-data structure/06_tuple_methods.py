t = (3, 12, 1, 54, 23, 12)   # tuple

print(t.count(12))   # 2 → counts how many times 12 appears

print(t.index(12))   # 1 → returns index of first occurrence of 12
                     # Reason:
                     # 12 appears at index 1 and 5
                     # index() always returns first position
                     #  count() → total occurrences
                     #   index() → first position only