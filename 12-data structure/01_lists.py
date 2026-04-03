marks = [54, 23, 64, 93, 32]   # list of numbers (index: 0 to 4)
mixed = [43, "hello", False, 4.2]   # list (index: 0 to 3)

print(marks[2:4])   # [64, 93] → slicing: start=2, end=4 (4 excluded)

print(marks[2])     # 64 → element at index 2

print(mixed[4])     # ❌ Error → IndexError
                    # Reason:
                    # mixed list has only 4 elements
                    # valid index = 0,1,2,3
                    # index 4 does not exist → out of range